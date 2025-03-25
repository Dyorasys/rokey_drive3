# 2025-02-20
# gui 눌러야 시작
# 일단 최종본

# -------- 해야 할 것 --------
# 원위치 복귀

#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from aruco_msgs.msg import MarkerArray, Marker
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Pose, PoseArray
from turtlebot_cosmo_interface.srv import MoveitControl
from srv_call_test import TurtlebotArmClient
import time
import ast
import json

class IntegratedProcess(Node):
    def __init__(self):
        super().__init__('integrated_process')
        print('---start---')

        # Aruco Marker Listener 설정
        self.aruco_sub = self.create_subscription(
            MarkerArray,
            'detected_markers',
            self.aruco_listener_callback,
            10)
        
        # Yolo Detection Listener 설정
        self.yolo_sub = self.create_subscription(
            String,
            '/yolo/detected_info',
            self.yolo_listener_callback,
            10)

        # 사용자 gui
        self.gui_sub = self.create_subscription(
            String,
            'gui/command',
            self.gui_listener_callback,
            10)        
        
        # 컨베이어 연결
        self.conv_pub = self.create_publisher(
            String, 'conveyor/control', 10
        )

        
        self.cmd_vel_publisher = self.create_publisher(Twist, '/cmd_vel', 2)
        
        # 상태 변수
        self.aruco_marker_found = False
        self.task_completed = False
        self.yolofind = False
        self.armrun = False
        self.yolo_x = 0
        self.yolo_y = 0
        self.marker_id = None
        self.state = 'START'  
        # self.state = 'PURPLE'  

        self.count = 0
        self.aruco_pose = None  # Aruco marker의 pose 정보를 저장할 변수

        

    def gui_listener_callback(self, msg):
        print('-----------')
        data = json.loads(msg.data)
        self.red = data['red']
        self.blue = data['blue']
        
        self.goal = data['goal']
        self.num = data['red'] + data['blue']
        self.create_timer(1.0, self.run_tasks)


    def aruco_listener_callback(self, msg):
        
        if self.state not in ('ARUCO', 'BACKWARD', 'CHECK'):
            return

        target_marker_id = 4 # 초기에는 4번 마커를 찾음
        
        for marker in msg.markers:
            if marker.id == target_marker_id:
                self.marker_id = marker.id
                self.aruco_pose = marker.pose.pose  # Aruco의 위치 저장
                print('------aruco position-------')
                self.get_logger().info(f'Marker ID: {marker.id}, PositionZ: {self.aruco_pose.position.z}, PostionX : {self.aruco_pose.position.x}')
                self.aruco_marker_found = True
                if self.state ==  'ARUCO':
                    self.execute_forward_task(self.aruco_pose.position.z, self.aruco_pose.position.x)  # 전진 작업 실행
                elif self.state == 'BACKWARD':
                    # 컨베이어에 명령
                    s = String()

                    dist = 630
                    cmd = {"control": "go", "mode": "distance", "distance.mm": dist}


                    s.data = json.dumps(cmd)
                    self.conv_pub.publish(s)
                    self.get_logger().info(f"Publish: {s.data}") 
                    self.execute_backward_task(self.aruco_pose.position.z)

            # 마지막 바구니 놓을 때, marker_id 받아오는걸로 수정 필요!!!!
            if self.state == 'CHECK':
                print(marker.id)
                marker_id = marker.id
                x_position = marker.pose.pose.position.x
                if marker_id == self.goal and abs(x_position) <= 0.04:  # marker3을 가까이서 감지하면 정지
                    print("find")
                    self.publish_cmd_vel(0.0)
                    self.final_task()
                else:  # 어떤 marker든 감지되면 전진
                    print("keep run")
                    self.publish_cmd_vel(0.03)
                        
    def yolo_listener_callback(self, msg):
        if self.state not in ('YOLO', 'PURPLE'):
            return

        if not self.armrun:  # 로봇 암이 동작 중이 아니면
            data = msg.data
            try:
                data_list = ast.literal_eval(data)
                if len(data_list) > 0:
                   
                    if self.state == 'YOLO':
                        new_list = []
                        blue = []
                        red = []
                        for i in range(len(data_list)):
                            if data_list[i][0] == 0:
                                red.append(i)
                            elif data_list[i][0] == 1:
                                blue.append(i)

                        for i in range(self.red):
                            new_list.append(data_list[red[i]])
                        for i in range(self.blue):
                            new_list.append(data_list[blue[i]])
                        for i in range(len(new_list)):
                            print('--------new------')
                            print(new_list[i][0])
                            self.yolo_x = new_list[i][1]
                            self.yolo_y = new_list[i][2]
                            if self.yolo_x > 0 and self.yolo_y > 0:   # right low
                                self.yolo_x += 0.01       # width
                                self.yolo_y += 0.025      # hight

                                print("right low")
                            elif self.yolo_x > 0 and self.yolo_y < 0:  # right high
                                self.yolo_x += 0.01
                                self.yolo_y += 0.005

                                print("right high")
                            elif self.yolo_x < 0 and self.yolo_y > 0:  # left low
                                self.yolo_x -= 0.005       # width
                                self.yolo_y += 0.01      # hight

                                print("left low")
                            elif self.yolo_x < 0 and self.yolo_y < 0:  # left high
                                self.yolo_x -= 0.000 # width  += 오른쪽 -= 왼쪽
                                self.yolo_y += 0.005    # hight -= 위쪽 += 아래쪽

                                print("left high")

                            
                            print(f"Detected coordinates: {self.yolo_x}, {self.yolo_y}")
                            print("done")
                            if not self.yolofind:
                                self.yolofind = True
                                self.yolo_arm_controll()
                                
                                if self.count == self.num:
                                    self.home2_arm_controll()
                                    self.state = 'BACKWARD'
                        
                    elif self.state == 'PURPLE':
                        print('----------purple position-------------')
                        print(data_list)
                        for i in range(len(data_list)):
                            print(data_list[i])
                            if data_list[i][0] == 3:
                                self.yolo_x = data_list[i][1]
                                self.yolo_y = data_list[i][2]
                                break
                        print(f'purple x : {self.yolo_x}, y : {self.yolo_y}')
                        # self.yolofind = False
                        if not self.yolofind:
                            self.yolofind = True
                            self.purple_arm_control()                        
                            
            except Exception as e:
                self.get_logger().error(f"Error processing the data: {e}")

    def execute_aruco_task(self):
        self.state =  'ARUCO'
        

    def execute_forward_task(self, current_z_position, current_x_position):
        
        # 전진 작업: 30cm까지 전진 후 멈추고, 작업을 진행
        if self.aruco_marker_found and self.aruco_pose:
            self.get_logger().info("Executing forward task...")
            # 목표 z축 위치를 30cm로 설정
            # !1
            if current_z_position > 0.3:
                self.publish_cmd_vel(0.05)
            elif current_z_position > 0.162:
                x = 0.0
                # # aruco 위치
                # marking_x = 1.0
                # if current_x_position > marking_x * (0.162/current_z_position):
                #     x = 0.01
                # else:
                #     x = -0.01
                self.publish_cmd_vel(0.025, angular_z = x)
            else:
                self.publish_cmd_vel(0.0)
                self.get_logger().info("Target reached")
                self.camera_arm_controll()
                self.state = 'YOLO'

                
    def execute_backward_task(self, current_z_position):
        # 후진 작업: 1m만큼 후진하고 다시 Aruco marker를 확인
        if self.aruco_marker_found and self.aruco_pose:
            self.get_logger().info("Executing backward task...")
            # 목표 z축 위치를 30cm로 설정
            # !3
            if current_z_position < 0.715:
                self.publish_cmd_vel(-0.05)
            else:
                self.publish_cmd_vel(0.0)
                self.get_logger().info("Target reached")
                self.box_home_arm_controll()
                # time.sleep(3)
                self.state = 'PURPLE'
                # self.yolofind = False

                
    def camera_arm_controll(self):
        arm_client = TurtlebotArmClient()
        response = arm_client.send_request(1, "camera_home")
        arm_client.get_logger().info(f'Response: {response.response}')
        time.sleep(3)        

    def home2_arm_controll(self):
        arm_client = TurtlebotArmClient()
        response = arm_client.send_request(1, "home2")
        arm_client.get_logger().info(f'Response: {response.response}')
        time.sleep(3)      

    def box_home_arm_controll(self):
        arm_client = TurtlebotArmClient()
        response = arm_client.send_request(1, "box_home_01")
        arm_client.get_logger().info(f'Response: {response.response}')
        time.sleep(3)            
    
    def append_pose_init(self, x,y,z):
        pose_array = PoseArray()
        pose = Pose()

        pose.position.x = x
        pose.position.y =  y
        pose.position.z =  z

        pose_array.poses.append(pose)

        return pose_array

    def yolo_arm_controll(self):
        arm_client = TurtlebotArmClient()

        print ("task start!")
        print(f"Get coordinates: {self.yolo_x}, {self.yolo_y}")

        if self.yolofind:
            self.armrun = True

            response = arm_client.send_request(2, "open")
            arm_client.get_logger().info(f'Response: {response.response}')
            time.sleep(1)

            # 박스 위치 조정
            # !2
            pose_array = self.append_pose_init(0.137496 - self.yolo_y + 0.05,0.00 - self.yolo_x ,0.122354 )

            response = arm_client.send_request(0, "", pose_array)
            arm_client.get_logger().info(f'Response: {response.response}')

            pose_array = self.append_pose_init(0.137496 - self.yolo_y + 0.05,0.00 - self.yolo_x ,0.095  )

            response = arm_client.send_request(0, "", pose_array)
            arm_client.get_logger().info(f'Response: {response.response}')     

            response = arm_client.send_request(2, "close")
            arm_client.get_logger().info(f'Response: {response.response}')
   
            response = arm_client.send_request(1, "home2")
            arm_client.get_logger().info(f'Response: {response.response}')
            time.sleep(1)

            print ("conveyor task start")

            response = arm_client.send_request(1, "conveyor_up")
            arm_client.get_logger().info(f'Response: {response.response}')

            response = arm_client.send_request(1, "test_conveyor")
            arm_client.get_logger().info(f'Response: {response.response}')

            response = arm_client.send_request(2, "open")
            arm_client.get_logger().info(f'Response: {response.response}')

            print("throw ")
            
            response = arm_client.send_request(1, "conveyor_up")
            arm_client.get_logger().info(f'Response: {response.response}')

            response = arm_client.send_request(1, "camera_home")
            arm_client.get_logger().info(f'Response: {response.response}')   

            # 컨베이어에 명령
            conv_cmd = String()

            dist = 300
            cmd = {"control": "go", "mode": "distance", "distance.mm": dist}


            conv_cmd.data = json.dumps(cmd)
            self.conv_pub.publish(conv_cmd)
            self.get_logger().info(f"Publish: {conv_cmd.data}") 

            time.sleep(2)

            print("jobs_done")

            self.armrun = False
            self.yolofind = False  # 작업 완료 후 초기화
            
            self.count += 1
        
    def purple_arm_control(self):
        if self.state == 'PURPLE':
            arm_client = TurtlebotArmClient()

            # # 컨베이어 정지

            conv_cmd = String()
            
            cmd = {"control": "stop"}
            conv_cmd.data = json.dumps(cmd)
            self.conv_pub.publish(conv_cmd)


            print ("task start!")
            
            print(f"Get coordinates: {self.yolo_x}, {self.yolo_y}")

            if self.yolofind:
                self.armrun = True

                response = arm_client.send_request(2, "open")
                arm_client.get_logger().info(f'Response: {response.response}')
                time.sleep(1)

                # pose_array = self.append_pose_init(self.yolo_x ,-0.2800000  ,   self.yolo_y + 0.06 )
                pose_array = self.append_pose_init(0.0103589 ,-0.2700000  ,0.205779  - self.yolo_y + 0.08)

                print('-----바구니 위치 -----')
                print(f'x : {self.yolo_x}, y : {self.yolo_y}')
                response = arm_client.send_request(3, "", pose_array)
                arm_client.get_logger().info(f'Response: {response.response}')
                print(pose_array)

                time.sleep(2)

                print('-----이동  -----')

                response = arm_client.send_request(9, "")
                arm_client.get_logger().info(f'Response: {response.response}')

                # 바구니 잡기
                # !4
                print('-----바구니 위치 -----')
                pose_array = self.append_pose_init(0.0103589,-0.3000000   ,0.205779  - self.yolo_y + 0.08 )

                response = arm_client.send_request(3, "", pose_array)
                arm_client.get_logger().info(f'Response: {response.response}')     

                response = arm_client.send_request(9, "")
                arm_client.get_logger().info(f'Response: {response.response}')

                response = arm_client.send_request(2, "close")
                arm_client.get_logger().info(f'Response: {response.response}')
                time.sleep(1)

                response = arm_client.send_request(1, "box_up_01")
                arm_client.get_logger().info(f'Response: {response.response}')    
                time.sleep(1)

                response = arm_client.send_request(1, "box_up_02")
                arm_client.get_logger().info(f'Response: {response.response}')    
                time.sleep(1)

                response = arm_client.send_request(1, "box_up_03")
                arm_client.get_logger().info(f'Response: {response.response}')    
                time.sleep(1)

                response = arm_client.send_request(1, "box_back_01")
                arm_client.get_logger().info(f'Response: {response.response}')   

                time.sleep(1)


                print("jobs_done")

                self.armrun = False
                self.yolofind = False  # 작업 완료 후 초기화
                
                self.state = 'CHECK'
            
    def final_task(self):
        arm_client = TurtlebotArmClient()
        response = arm_client.send_request(1, "box_back_put")
        arm_client.get_logger().info(f'Response: {response.response}') 
        time.sleep(1)
        response = arm_client.send_request(2, "open")
        arm_client.get_logger().info(f'Response: {response.response}')       
        self.state = "FINISH"

    def finish_task(self):
        # 모든 작업이 완료되었을 때
        if self.state == 'FINISH':
            self.get_logger().info("All tasks are complete!")
            arm_client = TurtlebotArmClient()
            response = arm_client.send_request(1, "box_up_03")
            arm_client.get_logger().info(f'Response: {response.response}')    
            time.sleep(1)

            response = arm_client.send_request(1, "home2")
            arm_client.get_logger().info(f'Response: {response.response}')   
            self.destroy_node()
            rclpy.shutdown()

    def publish_cmd_vel(self, linear_x, angular_z=0.0):
        twist = Twist()
        twist.linear.x = linear_x
        twist.angular.z = angular_z
        self.cmd_vel_publisher.publish(twist)

    def run_tasks(self):
        # 상태에 따라 각 작업을 순차적으로 실행
        if self.state == 'START':
            self.execute_aruco_task()
        elif self.state == 'FINISH':
            self.finish_task()

def main(args=None):
    rclpy.init(args=args)
    node = IntegratedProcess()
    
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

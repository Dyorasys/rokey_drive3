#This program runs on Window due to WSL's limitation on integrating USB Camera

import cv2
import os
#import time

save_directory = "img_capture"  #save direectory is set to be under the current directory

def capture_image():

    os.makedirs(save_directory, exist_ok=True)

    # del_img = input("Do you want to delete the previous images: (y/n) ")
    # if del_img == 'y':
    #     file_name = f'{save_directory}\*.*'
    #     os.remove(file_name)
    #     print(f"{file_name} has been deleted.")

    file_prefix = input("Enter a file prefix to use : ")
    file_prefix = f'{file_prefix}_'
    print(file_prefix)
    
    image_count = 0
    # OpenCV 비디오 캡처 객체 생성 (카메라 0번 장치 사용)
    cap = cv2.VideoCapture(2, cv2.CAP_V4L2)
    # self.cap = cv2.VideoCapture(2)
    # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    cap.set(cv2.CAP_PROP_FPS, 25)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, frame = cap.read()
        
        cv2.imshow("Webcam", frame)

        key = cv2.waitKey(1)
        if key == ord('c'):

            # change the filename when multiple people are capturing images
            # ex: obj1_img_{image_count}.jpg
            # then all images and txt files generated can be combined for execution of step 3
            file_name = f'{save_directory}/{file_prefix}img_{image_count}.jpg'  
            
            cv2.imwrite(file_name, frame)
            print(f"Image saved. name:{file_name}")
            image_count += 1
        
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    capture_image()

if __name__ == "__main__":
    main()


import cv2
import os
# 저장할 폴더 지정
save_dir = "capture_images"
os.makedirs(save_dir, exist_ok=True)  # 폴더가 없으면 생성
# 카메라 설정 (USB 카메라 인덱스: 0)
cap = cv2.VideoCapture(2)
# 해상도 설정 (1280x720)
cap.set(3, 1280)  # 가로 해상도
cap.set(4, 720)   # 세로 해상도
count = 0  # 이미지 파일명 번호
print("카메라가 실행되었습니다. 's' 키를 눌러 사진을 저장하세요. 'q'를 누르면 종료됩니다.")
while True:
    ret, frame = cap.read()  # 프레임 캡처
    if not ret:
        print("카메라에서 영상을 가져올 수 없습니다.")
        break
    cv2.imshow("Camera", frame)  # 화면에 영상 출력
    key = cv2.waitKey(1) & 0xFF  # 키 입력 대기
    # 's' 키를 누르면 이미지 저장
    if key == ord('s'):
        filename = os.path.join(save_dir, f"capture_{count:04d}.jpg")  # 예: capture_0001.jpg
        cv2.imwrite(filename, frame)
        print(f"이미지 저장됨: {filename}")
        count += 1  # 파일 번호 증가
    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        print("종료합니다.")
        break
# 카메라 및 창 닫기
cap.release()
cv2.destroyAllWindows()







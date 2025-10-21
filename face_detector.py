import cv2
import mediapipe as mp

# MediaPipe 초기화
mp_face_mesh = mp.solutions.face_mesh

# 주요 랜드마크 인덱스 (눈, 코, 입, 귀)
LANDMARK_IDS = {
    "left_eye": 468,
    "right_eye": 473,
    "nose_tip": 1,
    "upper_lip": 13,
    "lower_lip": 14,
    "left_ear": 234,
    "right_ear": 454
}

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture("face.mp4")
if not cap.isOpened():
    print("⚠️ 동영상 파일을 열 수 없습니다.")
    exit()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = image.shape

            # 모든 랜드마크 좌표 리스트 얻기
            landmark_points = [(int(lm.x * w), int(lm.y * h)) for lm in face_landmarks.landmark]

            # 바운딩 박스 계산 (x, y, w, h)
            x_vals = [p[0] for p in landmark_points]
            y_vals = [p[1] for p in landmark_points]
            x_min, x_max = min(x_vals), max(x_vals)
            y_min, y_max = min(y_vals), max(y_vals)

            # 얼굴 바운딩 박스 그리기 (흰색)
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 255, 255), 2)

            # 주요 포인트 빨간 점 찍기
            for idx in LANDMARK_IDS.values():
                x, y = landmark_points[idx]
                cv2.circle(image, (x, y), 4, (0, 0, 255), -1)

    cv2.imshow("👤 얼굴 사각형 + 주요 특징점", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

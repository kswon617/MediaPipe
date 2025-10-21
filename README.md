# Mediapipe 카메라 테스트 프로젝트

이 프로젝트는 **Mediapipe 라이브러리**를 활용한 카메라 및 동영상 기반 테스트 코드들을 포함하고 있습니다.  
손 감지, 얼굴 감지, 셀피 세그멘테이션 기능을 실시간 또는 동영상으로 확인할 수 있습니다.

---

## 폴더 구조 및 주요 파일

---

## 주요 기능 설명

### 1. 손 감지 (`hand_detector.py`)
- Mediapipe Hands 모듈 사용
- 실시간 카메라 또는 동영상에서 손과 손가락 랜드마크 감지 및 시각화

### 2. 유튜브 영상 손 감지 (`hand_detector_youtube.py`)
- 유튜브 영상 스트림 URL을 입력받아 손 감지 수행
- 실시간처럼 유튜브 영상에서 손과 손가락 랜드마크 감지 및 표시

### 3. 얼굴 감지 (`face_detector.py`)
- Mediapipe Face Mesh 모듈 사용
- 얼굴 주요 부위(눈, 코, 입, 귀 등) 랜드마크 감지 및 빨간 점 표시
- 얼굴 바운딩 박스 표시
- 동영상 또는 실시간 카메라 지원

### 4. 셀피 세그멘테이션 (`selfie_segmentation.py`)
- Mediapipe Selfie Segmentation 사용
- 배경과 인물을 분리하여 배경 효과 적용 가능
- 실시간 영상 지원

---

## 동영상 및 가상환경 파일

- `face.mp4`, `hand.mp4`는 테스트용 동영상 파일로, `.gitignore`에 포함되어 **버전 관리에서 제외**됩니다.
- `.venv/` 폴더(가상환경) 역시 `.gitignore`에 포함되어 커밋 대상에서 제외됩니다.
- 동영상 파일이 없을 경우 기본 카메라 입력으로 테스트할 수 있습니다.

---

## 실행 방법

1. 의존 라이브러리 설치

```bash
pip install opencv-python mediapipe



python hand_detector.py
python hand_detector_youtube.py
python face_detector.py
python selfie_segmentation.py

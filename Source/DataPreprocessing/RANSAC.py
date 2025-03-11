import cv2
import numpy as np

# 가짜 낮 이미지와 원본 밤 이미지 로드
fake_day_image = cv2.imread("/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/light_processing_test/1686934858.664962_fake_B.png")
original_night_image = cv2.imread("/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/light_processing_test/1686934858.664962.png")

# 특징점 검출 및 매칭
detector = cv2.SIFT_create()
matcher = cv2.BFMatcher()

fake_keypoints, fake_descriptors = detector.detectAndCompute(fake_day_image, None)
original_keypoints, original_descriptors = detector.detectAndCompute(original_night_image, None)

matches = matcher.knnMatch(fake_descriptors, original_descriptors, k=2)

# RANSAC 적용하여 정확한 대응점 쌍 식별
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

# RANSAC을 위한 대응점 좌표 변환
fake_points = np.float32([fake_keypoints[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
original_points = np.float32([original_keypoints[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# RANSAC을 사용한 변환 행렬 추정
M, mask = cv2.findHomography(fake_points, original_points, cv2.RANSAC, 5.0)

# 이미지 정합
aligned_image = cv2.warpPerspective(fake_day_image, M, (original_night_image.shape[1], original_night_image.shape[0]))

# 결과 출력
cv2.imshow("Aligned Image", aligned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

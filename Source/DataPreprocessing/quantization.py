import cv2
import numpy as np

# 가짜 낮 이미지 로드
fake_day_image = cv2.imread("/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/light_processing_test/1686934858.664962_fake_B.png")

# 색상 공간 변환 (예: RGB에서 LAB로 변환)
lab_image = cv2.cvtColor(fake_day_image, cv2.COLOR_BGR2LAB)

# 양자화를 위한 파라미터 설정
quantization_level = 8  # 원하는 양자화된 색상 수를 설정합니다.

# 양자화된 이미지 생성
quantized_image = lab_image.copy()
quantized_image[:, :, 1] = np.floor(quantized_image[:, :, 1] / quantization_level) * quantization_level
quantized_image[:, :, 2] = np.floor(quantized_image[:, :, 2] / quantization_level) * quantization_level

# 색상 공간 변환 (예: LAB에서 RGB로 변환)
quantized_image = cv2.cvtColor(quantized_image, cv2.COLOR_LAB2BGR)

# 결과 출력
cv2.imshow("Quantized Image", quantized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

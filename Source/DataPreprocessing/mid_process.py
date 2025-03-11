from PIL import Image
import numpy as np

# 이미지 로드
image = Image.open("/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/results/sample4_0609/test_latest/images/1639975470.825183_mid_A.png")

# 이미지를 NumPy 배열로 변환
pixel_array = np.array(image)

# 이미지의 픽셀 값을 출력
print(pixel_array)
# 넘파이 어레이 값을 CSV 파일로 저장
np.savetxt("/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/results/sample4_0609/test_latest/mid_process/pixel_values.csv", pixel_array.reshape(-1, 3), fmt="%d", delimiter=",")

# 변경된 이미지 저장
# image.save("/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/results/sample4_0609/test_latest/mid_process/1639975470.825183_mid_A.png")

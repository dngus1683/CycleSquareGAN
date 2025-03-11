import cv2
import os

def adjust_lighting(image, brightness_factor):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    value = hsv[:,:,2]
    
    # 밝기가 높은 픽셀만 선택하여 밝기 조절
    bright_pixels = value > 200  # 임계값을 조절하여 밝은 픽셀 선택
    # value[bright_pixels] = value[bright_pixels] * brightness_factor
    value[bright_pixels] = 138
    hsv[:,:,2] = value
    adjusted_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return adjusted_image

# 입력 폴더 경로와 출력 폴더 경로를 설정합니다.
input_folder = '/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/0618/test_org/'
output_folder = '/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/0618/testA/'

# 밝기를 조절할 비율을 결정합니다.
brightness_factor = 0.5  # 밝기를 절반으로 조절하기 위해 0.5를 사용했습니다. 원하는 비율로 조절해주세요.

i = 1
# 입력 폴더 내의 파일들을 순회하면서 처리합니다.
for filename in os.listdir(input_folder):
    # 파일의 전체 경로를 생성합니다.
    input_path = os.path.join(input_folder, filename)
    
    # 이미지를 불러옵니다.
    image = cv2.imread(input_path)
    
    # 이미지의 밝기를 조절합니다.
    adjusted_image = adjust_lighting(image, brightness_factor)
    
    # 출력 파일의 경로를 생성합니다.
    output_path = os.path.join(output_folder, filename)
    
    # 결과 이미지를 저장합니다.
    cv2.imwrite(output_path, adjusted_image)
    print(i)
    i += 1
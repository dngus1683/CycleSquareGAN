from PIL import Image

# 원본 이미지 로드
image = Image.open('/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/light_processing_test/bbb.png')  # 이미지 파일 경로를 적절히 수정하세요.

# 크기 변경
resized_image = image.resize((640, 480))

# 변경된 이미지 저장
resized_image.save('/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/light_processing_test/bbb_re.png')  # 저장할 이미지 파일 경로를 적절히 수정하세요.

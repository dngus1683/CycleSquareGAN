import os
from PIL import Image

def save_images_with_interval(source_folder, target_folder, interval):
    # 타겟 폴더가 없으면 생성
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    file_list = os.listdir(source_folder)
    image_files = [f for f in file_list if os.path.isfile(os.path.join(source_folder, f))]
    image_files.sort()  # 파일명을 정렬하여 순서대로 처리
    
    skipped_images = []  # 건너뛴 이미지 파일명을 저장할 배열
    
    for i, image_file in enumerate(image_files):
        if (i + 1) % interval == 1:  # n 간격으로 이미지 저장
            image_path = os.path.join(source_folder, image_file)
            
            try:
                image = Image.open(image_path)
                new_file_name = os.path.splitext(image_file)[0] + '_new' + os.path.splitext(image_file)[1]  # 새 파일명 생성
                new_file_path = os.path.join(target_folder, new_file_name)
                image.save(new_file_path)
                print(i ,' / ',len(image_files))
                print(f'Saved: {new_file_path}')
            except (OSError, IOError, ValueError, AttributeError):
                skipped_images.append(image_file)  # 오류가 발생한 경우 건너뛴 이미지 파일명을 배열에 저장
                print(f'Skipped: {image_file}')
    
    print('Skipped images:', skipped_images)

# 사용 예시
source_folder = '/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/image4/Day'
target_folder = '/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/image4/trainB'
interval = 4  # n 값 설정

save_images_with_interval(source_folder, target_folder, interval)

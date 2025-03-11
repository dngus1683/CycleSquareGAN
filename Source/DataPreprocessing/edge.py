import cv2
import os

# 이미지가 저장된 폴더 경로
img_folder = './night2day_pix/B/val'

# 새로운 이미지를 저장할 폴더 경로
output_folder = './night2day_pix/A/val'

# 폴더가 없으면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 폴더 내 이미지 파일들에 대해 처리
for img_name in os.listdir(img_folder):
    # 이미지 경로
    img_path = os.path.join(img_folder, img_name)
    # 이미지 읽기
    img = cv2.imread(img_path)
    # Canny 알고리즘을 이용하여 윤곽선 검출
    edges = cv2.Canny(img, 150, 170)
    # 검출된 윤곽선 정보를 이용하여 새로운 이미지 생성
    img_with_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    output_path = os.path.join(output_folder, 'edges_' + img_name)
    # 새로운 이미지 저장
    cv2.imwrite(output_path, img_with_edges)
    
    

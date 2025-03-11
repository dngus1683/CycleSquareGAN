import torch
from torchvision import transforms
from torchvision.utils import save_image
from PIL import Image, ImageFilter, ImageOps
import numpy as np
from scipy.ndimage import sobel
import os

# Path to your data folder
data_folder1 = "/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/day2night_aug0531/image2/day2"
result_folder1 = "/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/day2night_aug0531/image2/day2_aug"
data_folder2 = "/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/day2night_aug0531/image2/Day"
result_folder2 = "/home/rail/catkin_ws/src/pytorch-CycleGAN-and-pix2pix/datasets/day2night_aug0531/image2/Day_aug"


def enhance_edges(image, threshold, alpha):
    # Convert the image to grayscale
    gray_image = image.convert('L')

    # Apply the Sobel filter
    edges = sobel(np.array(gray_image))

    # Apply threshold to enhance the edges
    edges = np.where(edges > threshold, 255, 0).astype(np.uint8)

    # Convert the edges array back to PIL Image
    edges_image = Image.fromarray(edges)

    # Combine the original image and the enhanced edges
    result = Image.blend(image, edges_image, alpha=alpha)

    return result

# Create a transform with desired augmentation options
transform = transforms.Compose([
    transforms.RandomAffine(degrees=0, shear=(0.2, 0.2), scale=(0.8, 1.2)),
    transforms.RandomHorizontalFlip(p=1),
    # transforms.Lambda(lambda x: enhance_edges(x, threshold=50, alpha=0.5)),
    transforms.ToTensor()
])

# Check if GPU is available and use it for acceleration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Loop through each file in the data folder
def aug(data_folder, result_folder):
    for file_name in os.listdir(data_folder):
        # Check if the file is an image (you can modify this condition based on your file types)
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(data_folder, file_name)
            # Load the image
            image = Image.open(file_path).convert("RGB")
            # Apply the augmentation transform
            augmented_images = []
            for _ in range(1):  # Generate 5 augmented images per original image
                augmented_image = transform(image).unsqueeze(0).to(device)
                augmented_images.append(augmented_image)
            # Save the augmented images to the result folder
            for i, augmented_image in enumerate(augmented_images):
                save_image(augmented_image, os.path.join(result_folder, f"aug_{i+1}_{file_name}"))

aug(data_folder1, result_folder1)
# aug(data_folder2, result_folder2)

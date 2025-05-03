import os
import cv2
import numpy as np
from utils import load_image, save_image


def preprocess_image(
    image_path: str, output_path: str, resize_dim: tuple = (640, 640)
) -> None:
    """Preprocess an image by resizing and normalizing."""
    image = load_image(image_path)
    resized_image = cv2.resize(image, resize_dim)
    normalized_image = resized_image / 255.0  # Normalize to [0, 1]
    save_image((normalized_image * 255).astype(np.uint8), output_path)


def preprocess_dataset(
    input_dir: str, output_dir: str, resize_dim: tuple = (640, 640)
) -> None:
    """Preprocess all images in a dataset directory."""
    os.makedirs(output_dir, exist_ok=True)
    for image_file in os.listdir(input_dir):
        input_path = os.path.join(input_dir, image_file)
        output_path = os.path.join(output_dir, image_file)
        preprocess_image(input_path, output_path, resize_dim)


if __name__ == "__main__":
    # Example usage
    preprocess_dataset("data/train/images", "data/train/preprocessed_images")

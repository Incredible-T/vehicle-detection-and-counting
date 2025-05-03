import os
import logging
import yaml
import cv2
import numpy as np
from typing import List, Tuple, Dict


def setup_logging(log_file: str = "logs/project.log") -> None:
    """Set up logging configuration."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def load_yaml_config(file_path: str) -> Dict:
    """Load a YAML configuration file."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def load_image(image_path: str) -> np.ndarray:
    """Load an image from a file path."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def save_image(image: np.ndarray, save_path: str) -> None:
    """Save an image to a file path."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cv2.imwrite(save_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))


def visualize_bounding_boxes(
    image: np.ndarray, boxes: List[Tuple[int, int, int, int]], labels: List[str] = None
) -> np.ndarray:
    """Draw bounding boxes on an image."""
    for i, (x_min, y_min, x_max, y_max) in enumerate(boxes):
        color = (255, 0, 0)  # Red color for bounding boxes
        cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)
        if labels and i < len(labels):
            cv2.putText(
                image,
                labels[i],
                (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                2,
            )
    return image


def split_dataset(data_dir: str, train_ratio: float = 0.8) -> None:
    """Split dataset into training and validation sets."""
    images_dir = os.path.join(data_dir, "images")
    labels_dir = os.path.join(data_dir, "labels")

    images = sorted(os.listdir(images_dir))
    labels = sorted(os.listdir(labels_dir))

    split_index = int(len(images) * train_ratio)
    train_images, valid_images = images[:split_index], images[split_index:]
    train_labels, valid_labels = labels[:split_index], labels[split_index:]

    for subset, subset_images, subset_labels in zip(
        ["train", "valid"], [train_images, valid_images], [train_labels, valid_labels]
    ):
        subset_images_dir = os.path.join(data_dir, subset, "images")
        subset_labels_dir = os.path.join(data_dir, subset, "labels")
        os.makedirs(subset_images_dir, exist_ok=True)
        os.makedirs(subset_labels_dir, exist_ok=True)

        for image, label in zip(subset_images, subset_labels):
            os.rename(
                os.path.join(images_dir, image), os.path.join(subset_images_dir, image)
            )
            os.rename(
                os.path.join(labels_dir, label), os.path.join(subset_labels_dir, label)
            )

import os
import torch
from ultralytics import YOLO
from utils import setup_logging


def train_yolo_model(data_path, model_name, epochs, device):
    """Train a YOLO model with the given parameters."""
    model = YOLO(model_name)  # Load a YOLO model (e.g., 'yolov5s.pt')

    # Train the model
    model.train(
        data=data_path,  # Path to data.yaml
        epochs=epochs,
        device=device,  # '0' for GPU, 'cpu' for CPU
        imgsz=640,  # Image size
        batch=16,  # Batch size
    )

    # Save the trained model
    model.save(os.path.join("models", "yolo_trained_model.pt"))


if __name__ == "__main__":
    setup_logging()

    data_path = "data.yaml"  # Path to the dataset configuration
    model_name = "yolov5s.pt"  # Pretrained YOLO model
    epochs = 10
    device = "cuda" if torch.cuda.is_available() else "cpu"

    train_yolo_model(data_path, model_name, epochs, device)

import logging
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from utils import setup_logging


def evaluate_model(model, data_loader, device):
    """Evaluate a model on a dataset."""
    model.to(device)
    model.eval()
    total = 0
    correct = 0

    with torch.no_grad():
        for images, labels in data_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    logging.info(f"Accuracy: {accuracy:.2f}%")
    return accuracy


if __name__ == "__main__":
    setup_logging()

    # Example dataset and model setup
    transform = transforms.Compose(
        [transforms.Resize((640, 640)), transforms.ToTensor()]
    )

    test_dataset = datasets.ImageFolder("data/valid/images", transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False)

    model = torch.load("models/best_model.pth")  # Load a saved model

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    evaluate_model(model, test_loader, device)

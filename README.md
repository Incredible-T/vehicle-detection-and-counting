# 🚗 Vehicle Detection and Counting

A real-time system for detecting and counting vehicles using **YOLO** and **OpenCV**. This project is designed for applications such as traffic monitoring, smart city infrastructure, and transportation analytics.

## 🔑 Features

- **Real-Time Detection:** Utilizes YOLO for efficient and accurate vehicle detection.
- **Vehicle Counting:** Tracks and counts unique vehicles crossing a defined line.
- **Multi-Class Support:** Identifies various vehicle types, including cars, trucks, buses, and motorcycles.
- **Video & Live Feed Compatibility:** Processes pre-recorded videos and live camera streams.
- **Optimized Performance:** Suitable for deployment on edge devices and cloud platforms.

## 🛠️ Tech Stack

- **YOLOv5/YOLOv8:** Object detection models.
- **OpenCV:** Library for image processing and computer vision tasks.
- **Python:** Core programming language.

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/vehicle-detection-counting.git
   cd vehicle-detection-counting
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Prepare Your Video Source:**

   - For a video file, ensure it's in the project directory or provide the full path.
   - For a live camera feed, ensure the camera is connected and accessible.

2. **Run the Detection Script:**

   ```bash
   python detect_and_count.py --source path_to_video.mp4
   ```

   Replace `path_to_video.mp4` with your video file path or use `0` for the default camera.

3. **View Results:**

   - The script will display the video with detected vehicles and count annotations.
   - Processed videos can be saved by specifying the `--output` parameter.

### Configuration

- **Detection Line:** Customize the position of the counting line in the `config.json` file.
- **Detection Thresholds:** Adjust confidence thresholds in the `config.json` file.

## 📊 Use Cases

- **Traffic Flow Analysis:** Monitor and analyze vehicle movement patterns.
- **Smart City Traffic Management:** Assist in optimizing traffic signals and reducing congestion.
- **Toll Booth Monitoring:** Count vehicles for toll collection purposes.
- **Parking Management:** Monitor vehicle entry and exit in parking facilities.

## 🤝 Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📷 Screenshots

![Detection Example](screenshots/detection_example.png)

*Real-time vehicle detection and counting in action.*

## 📚 Acknowledgements

- [YOLO (You Only Look Once)](https://pjreddie.com/darknet/yolo/)
- [OpenCV](https://opencv.org/)

---

*Note: This project is for educational and research purposes. Ensure compliance with local laws and regulations when deploying surveillance systems.*

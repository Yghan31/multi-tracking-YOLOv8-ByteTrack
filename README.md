# Multi-Tracking YOLOv8 with ByteTrack 🚀

![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-brightgreen)
![ByteTrack](https://img.shields.io/badge/ByteTrack-Multi%20Object%20Tracking-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellowgreen)

Welcome to the **Multi-Tracking YOLOv8 with ByteTrack** repository! This project demonstrates real-time object detection and tracking using the powerful YOLOv8 model and ByteTrack algorithm. It is designed to track multiple objects in video streams, making it ideal for various applications, including animal tracking and security monitoring.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Introduction

In the age of AI and computer vision, tracking objects in real-time is a critical task. This demo software leverages the latest advancements in deep learning to provide efficient and accurate tracking solutions. By combining YOLOv8 for detection and ByteTrack for tracking, this tool can process video streams effectively, whether on a CPU or GPU.

## Features

- **Real-Time Detection:** Utilize YOLOv8 for fast and accurate object detection.
- **Multi-Object Tracking:** Track multiple objects simultaneously using ByteTrack.
- **Flexible Hardware Support:** Run on both CPU and GPU, allowing for versatility in deployment.
- **Easy to Use:** Simple setup and straightforward usage make it accessible for everyone.
- **OpenCV Integration:** Use OpenCV for video handling and display.

## Installation

To get started, follow these steps to install the necessary dependencies:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Yghan31/multi-tracking-YOLOv8-ByteTrack.git
   cd multi-tracking-YOLOv8-ByteTrack
   ```

2. **Install Required Packages:**

   Make sure you have Python 3.8 or higher installed. Then, install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment:**

   If you plan to run the software on a GPU, ensure you have the appropriate CUDA drivers installed. You can check your GPU compatibility on the [NVIDIA website](https://developer.nvidia.com/cuda-downloads).

## Usage

To use the software, follow these steps:

1. **Prepare Your Video Stream:**

   You can use a local video file or a live camera feed. Ensure that your video source is accessible.

2. **Run the Application:**

   Execute the following command in your terminal:

   ```bash
   python main.py --source <your_video_source>
   ```

   Replace `<your_video_source>` with the path to your video file or the camera index (e.g., `0` for the first camera).

3. **View Results:**

   The application will open a window displaying the video stream with detected and tracked objects. Press `q` to exit.

## Examples

Here are some examples of how the software performs in different scenarios:

### Animal Tracking

This software is perfect for tracking animals in various environments. You can set it up to monitor wildlife or pets in real-time.

![Animal Tracking](https://example.com/animal_tracking_image.png)

### Security Monitoring

Use the tool for security purposes, tracking individuals or vehicles in a designated area.

![Security Monitoring](https://example.com/security_monitoring_image.png)

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to fork the repository and submit a pull request. You can also open an issue if you encounter any bugs or have questions.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to me via GitHub or email.

## Releases

You can find the latest releases of the software [here](https://github.com/Yghan31/multi-tracking-YOLOv8-ByteTrack/releases). Download the latest version and execute it to experience the capabilities of this tool.

Feel free to check the "Releases" section for updates and new features.

---

Thank you for exploring the **Multi-Tracking YOLOv8 with ByteTrack** project! I hope you find it useful for your applications.
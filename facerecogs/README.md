## Installation and Setup

This project requires Python and several libraries. Follow these steps to set up your environment:

### Prerequisites

1. Ensure you have Python 3.6 or newer installed on your system.
2. Install CMake:
   - Download from [cmake.org](https://cmake.org/download/)
   - Add CMake to your system PATH during installation

3. Install Visual Studio Build Tools:
   - Download from [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
   - Ensure you select the "Desktop development with C++" workload during installation

### Installing Required Packages

Run the following commands to install the necessary Python libraries:

```bash
pip install opencv-python
pip install numpy
pip install dlib
pip install face_recognition
```

Troubleshooting dlib Installation
If you encounter issues installing dlib, follow these steps:

Ensure Visual Studio Build Tools are correctly installed with "Desktop development with C++" workload.
Verify CMake is installed and added to your system PATH.
Restart your command prompt or PowerShell after installations.
Try installing dlib again:
bashCopypip install dlib


If issues persist, you can try using a pre-built wheel:

Download a pre-built dlib wheel from this repository.
Install the downloaded wheel:
bashCopypip install path\to\dlib_wheel_file.whl

After successfully installing dlib, proceed with installing face_recognition:
bashCopypip install face_recognition
Setting Up Face Recognition
For efficient face recognition:

Create an images folder in your project directory.
Add clear, front-facing photos of individuals you want to recognize to this folder.
Name each image file with the person's name (e.g., john_doe.jpg).

Ensure that the images are of good quality and well-lit for optimal recognition performance.

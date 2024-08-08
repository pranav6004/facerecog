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

Set up Google Cloud Project:
- Go to the [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project
- Enable the Google Drive API and Google Sheets API for your project

 Create Service Account Credentials:
- In the Google Cloud Console, go to "APIs & Services" > "Credentials"
- Click "Create Credentials" > "Service Account"
- Fill in the details and create the account
- Once created, go to the service account details
- Under "Keys", add a new key and select JSON
- Download the JSON file and rename it to `credentials.json`
- Place `credentials.json` in the project root directory

 Set up Google Sheet:
- Create a new Google Sheet
- Share the sheet with the email address in your `credentials.json` (client_email)
- Copy the Sheet ID from the URL (it's the long string in the middle of the URL)

 Update the code:
- Open `main.py`
- Replace `'YOUR_SHEET_ID_HERE'` with your actual Google Sheet ID

 Prepare face images:
- Create an `image` folder in the project directory
- Add clear, front-facing photos of individuals to recognize
- Name each image file with the person's name (e.g., `john_doe.jpg`)


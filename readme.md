# **Face Detection with Python**

This project demonstrates how to detect faces in an image using the `face_recognition` and `Pillow` (PIL) libraries in Python. It loads an image, detects all faces in the image, and draws rectangles around each detected face. The result is displayed and saved as a new image.

## Features
- Detects faces in a given image using `face_recognition`.
- Draws green rectangles around detected faces using `Pillow`.
- Saves the modified image with rectangles highlighting faces.

## Installation

To run this project, you need to install the required Python libraries. You can install them via `pip`:

```bash
pip install face_recognition pillow
```

## Prerequisites

- **Python 3.x**
- **CMake** (for compiling `face_recognition`)
- **dlib** (used by `face_recognition`)

## Usage

1. Clone or download this repository.
2. Place your image file (e.g., `image.jpeg`) in the project directory.
3. Run the script to detect faces and save the output image:

    ```bash
    python face_detection.py
    ```
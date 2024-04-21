# Flask admin dashboard

This repository contains a Flask-based server for object detection and classification of Dendritic Spines using deep learning models. The server utilizes the YOLO (You Only Look Once) model for object detection and a custom-made Convolutional Neural Network (CNN) classifier inspired by VGG-16 for classifying the detected Dendritic Spines into four categories: Mushroom, Stubby, Thin, and Filopodia.

## Features
- Object Detection: The server uses the YOLO model to detect Dendritic Spines in the input images.
- Spine Classification: The detected Dendritic Spines are classified into four categories (Mushroom, Stubby, Thin, and Filopodia) using a custom-made CNN classifier inspired by VGG-16.

## Prerequisites

- Python 3.7 or later

## Getting Started

1. Clone the repository:
- `git clone https://github.com/flash6083/spineDetectionClassification.git`
- `cd SpineDetectionAndClassification`

2. Create a virtual environment and activate it:
- `python -m venv myenv`
- `source myenv/bin/activate`  # On Windows, use `myenv\Scripts\activate` for cmd or `myenv\Scripts\Activate.ps1` for Windows PowerShell

3. Install the required dependencies:
`pip install -r requirements.txt`

4. Run the Flask server:
`python app.py`

The server will start running at `http://localhost:8080`.

## Commit Message Standardization

When contributing to this project, please follow the commit message standardization guidelines:

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Changes that do not affect the meaning of the code (formatting, white-space, etc.)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `test`: Adding or modifying tests
- `chore`: Changes to build processes or auxiliary tools/libraries

For example:
- `git commit -m "feat: add support for user authentication"`
- `git commit -m "fix: resolve issue with database connection"`
- `git commit -m "refactor: improve code organization"`

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b my-new-feature`
3. Make your changes and commit them: `git commit -m 'feat: add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request
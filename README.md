# webcam-detector
Simple qt interface for detecting objects using your webcam

- Detect a face from front

![Image Loaded](docs/detectFace.png?raw=true "loaded face")

- Detect a face from profile

![Image Loaded](docs/detectFaceProfile.png?raw=true "loaded face profile")

- Detect a smile

![Image Loaded](docs/detectHumanSmile.png?raw=true "loaded smile")

## Installation

Recommended way is to create a virtual environment before.

- `cd PATH_TO_PROJECT_FOLDER`
- `pip install .`


## Usage

To launch the interface after installation simply write in terminal:

- `cd PARENT_PATH/webcamDetector`
- `python detector/qtapp.py`

The usage should be pretty straightforward.

Choose the type of the object you'd like to detect from the box and start the feed.
Stop the feed whenever you want. You can capture the feed if you want as well.

Here is a list of shortcuts:

- `ctrl+w`: closes the application
- `ctrl+a`: starts the web cam feed
- `ctrl+e`: stops the web cam feed
- `ctrl+f`: saves the web cam image


## Roadmap

- Custom models for facial key points
- Custom models for other objects

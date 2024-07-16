# Video Player with Recording Functionality

This is a simple video player application built using Python, OpenCV, and tkinter. The application allows you to play video from a camera or video file, and provides functionalities to record, pause, stop, and save the video.

## Features

- **Play Video**: Play video from a camera or a video file.
- **Record Video**: Record the video and save it to a specified location.
- **Pause Video**: Pause the video playback.
- **Stop Recording**: Stop the video recording and finalize the output file.
- **Select Save Location**: Choose where to save the recorded video.

## Requirements

- Python 3.x
- OpenCV
- Pillow
- tkinter

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/video-player-with-recording.git
    cd video-player-with-recording
    ```

2. **Install the required dependencies:**

    ```sh
    pip install opencv-python Pillow
    ```

## Usage

1. **Run the script:**

    ```sh
    python video_player_with_recording.py
    ```

2. **Controls:**
    - **Record**: Click the `Record` button to start recording the video. You need to select a save location if not already selected.
    - **Pause**: Click the `Pause` button to pause the video playback.
    - **Stop**: Click the `Stop` button to stop the recording and save the video file.
    - **Save**: Click the `Save` button to save the recorded video (placeholder for saving functionality).
    - **Select Location**: Click the `Select Location` button to choose where to save the recorded video.

## Code Overview

### `VideoPlayer` Class

- **`__init__(self, window, video_source=0)`**: Initializes the video player with the given video source (default is the camera).
- **`update(self)`**: Updates the video frames on the canvas and handles recording if active.
- **`record(self)`**: Starts the recording by creating a `VideoWriter` object.
- **`pause(self)`**: Pauses the video playback.
- **`stop(self)`**: Stops the recording and finalizes the output file.
- **`save(self)`**: Placeholder method for saving functionality.
- **`select_location(self)`**: Opens a file dialog to select the save location.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Developed by [Malitha Visada](mailto:malithavisada@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Malitha%20Visada-blue)](https://linkedin.com/in/malithavisada)
[![GitHub](https://img.shields.io/badge/GitHub-Malitha--Gunathilaka-green)](https://github.com/Malitha-Gunathilaka)

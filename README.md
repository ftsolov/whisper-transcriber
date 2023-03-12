# Whisper Transcriber
Whisper Transcriber is a command-line interface (CLI) tool that allows users to transcribe audio using the Whisper Model on their local machine.

## Installation
Before running Whisper Transcriber, you must install ffmpeg. You can do this on macOS using Homebrew:

    brew install ffmpeg

To install Whisper Transcriber, clone the repository or download it as a ZIP file. Once downloaded, navigate to the root directory of the project and create a virtual environment:

    python3 -m venv env

Activate the virtual environment:

    source env/bin/activate

Then, install the required dependencies:

    pip install -r requirements.txt

## Usage
To transcribe audio, simply place your audio files in the /audio folder. Then, run the program with the following command:

    python3 transcribe.py

Follow the instructions provided by the program to transcribe your audio.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

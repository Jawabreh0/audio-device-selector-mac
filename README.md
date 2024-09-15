# Audio Device Selector

A lightweight utility for interactive audio device selection on macOS. This tool allows users to choose their preferred input and output audio devices, making it ideal for integration into applications that require custom audio routing or device management.

## Features

- Lists available audio input and output devices
- Provides an intuitive interface for device selection using arrow keys
- Changes both sounddevice library defaults and system-wide audio device settings on macOS
- Easily integrable into larger applications

## Prerequisites

- Python 3.6+ (i'm usign python 3.11.9)
- macOS (due to the use of `switchaudio-osx`)
- `switchaudio-osx` installed via Homebrew

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/jawabreh0/audio-device-selector-mac.git
   cd audio-device-selector-mac
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Install `switchaudio-osx` using Homebrew:
   ```
   brew install switchaudio-osx
   ```

## Usage

Run the script from the command line:

```
python audio_device_selector.py
```

Use the arrow keys to navigate through the list of devices, and press Enter to select a device.


## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/jawabreh0/audio-device-selector/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
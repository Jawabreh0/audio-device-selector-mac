import sounddevice as sd
import curses
import subprocess

def list_audio_devices():
    """
    Returns lists of input and output audio devices.
    """
    devices = sd.query_devices()
    input_devices = [device for device in devices if device['max_input_channels'] > 0]
    output_devices = [device for device in devices if device['max_output_channels'] > 0]
    return input_devices, output_devices

def select_device(stdscr, title, devices):
    """
    Allows the user to navigate and select a device using arrow keys.
    """
    current_row = 0
    curses.curs_set(0)
    
    while True:
        stdscr.clear()
        stdscr.addstr(2, 0, title)

        for idx, device in enumerate(devices):
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(idx + 3, 0, f"> {device['name']}")
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(idx + 3, 0, f"  {device['name']}")

        stdscr.refresh()
        
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(devices) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return current_row

def choose_audio_devices():
    """
    Run the curses interface to choose input and output devices.
    """
    def run(stdscr):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        
        input_devices, output_devices = list_audio_devices()
        selected_input_idx = select_device(stdscr, "Select an input device:", input_devices)
        selected_output_idx = select_device(stdscr, "Select an output device:", output_devices)
        
        return input_devices[selected_input_idx], output_devices[selected_output_idx]

    selected_input_device, selected_output_device = curses.wrapper(run)
    return selected_input_device, selected_output_device

def change_macos_audio_device(device_name, device_type):
    """
    Change macOS audio device using switchaudio-osx.
    """
    try:
        subprocess.run(["SwitchAudioSource", "-s", device_name, "-t", device_type], check=True)
        print(f"Changed {device_type} device to: {device_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to change {device_type} device. Make sure switchaudio-osx is installed.")

def change_audio_devices():
    """
    Choose audio devices and change the system's default devices.
    """
    input_device, output_device = choose_audio_devices()
    
    # Change the default devices for sounddevice
    sd.default.device = (input_device['index'], output_device['index'])
    
    # Change system-wide audio devices
    change_macos_audio_device(input_device['name'], "input")
    change_macos_audio_device(output_device['name'], "output")
    
    # Verify the changes
    current_devices = sd.default.device
    print(f"\nCurrent default input device index: {current_devices[0]}")
    print(f"Current default output device index: {current_devices[1]}")

if __name__ == "__main__":
    change_audio_devices()
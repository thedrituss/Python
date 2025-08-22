# mouse_event2.py

from evdev import InputDevice
import select

# 🔧 Hardcoded device path
DEVICE_PATH = "/dev/input/event2"


def main():
    try:
        # Open the specific device
        device = InputDevice(DEVICE_PATH)
    except FileNotFoundError:
        print(f"❌ Device not found: {DEVICE_PATH}")
        print(
            "💡 Run `ls /dev/input/event*` and `sudo evtest` to check available devices."
        )
        exit(1)
    except PermissionError:
        print("❌ Permission denied. Is your user in the 'input' group?")
        print("💡 Run: sudo usermod -aG input $USER   and then log out/in.")
        exit(1)

    print(f"🎧 Listening to: {device.name} ({DEVICE_PATH})")
    print("🖱️  Move, click, or scroll the mouse. Press Ctrl+C to stop.\n")

    # Use select to poll for events (non-blocking)
    while True:
        try:
            r, w, x = select.select([device], [], [], 1)
            if r:
                for event in device.read():
                    if event.type == 2:  # EV_REL (relative movement)
                        if event.code == 0:  # REL_X
                            print(f"➡️  Mouse moved X: {event.value}")
                        elif event.code == 1:  # REL_Y
                            print(f"⬇️  Mouse moved Y: {event.value}")
                        elif event.code == 8:  # REL_WHEEL
                            direction = "Up" if event.value < 0 else "Down"
                            print(f"🪄 Scrolled: {direction}")

                    elif event.type == 1:  # EV_KEY (button events)
                        # Map common mouse buttons
                        if event.code == 272:  # BTN_LEFT
                            action = "Pressed" if event.value == 1 else "Released"
                            print(f"🔴 Left Button: {action}")
                        elif event.code == 273:  # BTN_RIGHT
                            action = "Pressed" if event.value == 1 else "Released"
                            print(f"🔵 Right Button: {action}")
                        elif event.code == 274:  # BTN_MIDDLE
                            action = "Pressed" if event.value == 1 else "Released"
                            print(f"🟢 Middle Button: {action}")

        except KeyboardInterrupt:
            print("\n👋 Stopped listening to mouse events.")
            break
        except Exception as e:
            print(f"⚠️  Error reading device: {e}")
            break


if __name__ == "__main__":
    main()

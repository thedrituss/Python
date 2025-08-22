# mouse_tracker.py

from evdev import InputDevice, ecodes
import select

# 🔧 Configuration
DEVICE_PATH = "/dev/input/event2"  # Change if needed
SCREEN_WIDTH = 1920  # Adjust to your screen
SCREEN_HEIGHT = 1080
MOUSE_SPEED = 1.0  # Sensitivity multiplier (tweak as needed)


def main():
    try:
        device = InputDevice(DEVICE_PATH)
    except FileNotFoundError:
        print(f"❌ Device {DEVICE_PATH} not found.")
        print("💡 Run: ls /dev/input/event*  to check available devices.")
        exit(1)
    except PermissionError:
        print("❌ Permission denied. Run: sudo usermod -aG input $USER")
        exit(1)

    print(f"🎧 Listening to: {device.name} ({DEVICE_PATH})")
    print(
        f"📍 Starting virtual mouse at center: ({SCREEN_WIDTH // 2}, {SCREEN_HEIGHT // 2})"
    )
    print("🖱️  Move your mouse. Press Ctrl+C to stop.\n")

    # Initial position (center of screen)
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    while True:
        try:
            # Wait for events (non-blocking)
            r, w, xsel = select.select([device], [], [], 1)
            if r:
                for event in device.read():
                    if event.type == ecodes.EV_REL:
                        if event.code == ecodes.REL_X:
                            x += int(event.value * MOUSE_SPEED)
                            x = max(0, min(SCREEN_WIDTH, x))  # Clamp
                        elif event.code == ecodes.REL_Y:
                            y += int(event.value * MOUSE_SPEED)
                            y = max(0, min(SCREEN_HEIGHT, y))

                        # Print updated position
                        print(f"📍 Mouse at: ({x}, {y})")

        except KeyboardInterrupt:
            print("\n👋 Stopped mouse tracker.")
            break
        except Exception as e:
            print(f"⚠️  Error: {e}")
            break


if __name__ == "__main__":
    main()

import pyautogui
import time
import os

print("--- MOUSE COORDINATE FINDER ---")
print("Move your mouse to the spot you want the AI to watch.")
print("Ideally: Slightly in front of the Dino, near the ground.")
print("Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        # Get the color of the pixel under the mouse
        try:
            color = pyautogui.pixel(x, y)
        except:  # noqa: E722
            # Multi-monitor setups sometimes cause pixel() to fail on edges
            color = "???"

        # Clear screen for clean output
        os.system("cls" if os.name == "nt" else "clear")

        print(f"X: {x} | Y: {y}")
        print(f"Color: {color}")
        print("\n(Ctrl+C to Quit)")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nCaptured!")

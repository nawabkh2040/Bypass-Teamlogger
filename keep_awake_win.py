"""
anti_idle_win.py
Keep a Windows PC awake by faking small user input.
Requires: pip install pynput
"""

import time
import random
from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController, Key

mouse = MouseController()
keyboard = KeyboardController()

def simulate_activity():
    """
    Move the mouse a tiny random amount and press/release Shift.
    """
    x, y = mouse.position
    # Move a few pixels to ensure Windows registers activity
    dx = random.randint(5, 20)
    dy = random.randint(5, 20)
    mouse.position = (x + dx, y + dy)
    time.sleep(0.2)
    mouse.position = (x, y)

    # Harmless key tap
    keyboard.press(Key.shift)
    keyboard.release(Key.shift)

    print(f"Simulated input at {time.strftime('%H:%M:%S')}")

def prevent_idle(interval=30):
    """
    Repeatedly simulate user activity every `interval` seconds.
    """
    print("Anti-idle script running. Press Ctrl+C in this window to stop.")
    try:
        while True:
            simulate_activity()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    # Give you a moment to focus the window or desktop you want active
    print("Starting in 5 seconds… switch to the desired desktop/app.")
    time.sleep(5)
    prevent_idle(interval=30)  # change 30 to a different number of seconds if desired

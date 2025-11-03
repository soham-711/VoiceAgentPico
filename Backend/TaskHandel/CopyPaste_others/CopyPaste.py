import pyautogui
import pyperclip
import time
from Head.Mouth import speak

def _wait():
    time.sleep(0.3)

# ---- Clipboard Utilities ---- #
def get_clipboard_text():
    """Get current clipboard content"""
    return pyperclip.paste()

import pyautogui
import time

def paste_from_clipboard(section):
    """
    Open Windows clipboard history (Win+V) and paste a specific section.
    section: 1 = first item, 2 = second item, etc.
    """
    section = int(section)
    # Open clipboard history
    pyautogui.hotkey("win", "v")
    time.sleep(0.5)  # Wait for it to open

    # Navigate to the required section
    # Default: first item is already selected
    if section > 1:
        for _ in range(section - 1):
            pyautogui.press("down")  # Move down
            time.sleep(0.1)

    # Paste selected item
    pyautogui.press("enter")
    speak(f"Pasted item {section} from clipboard history")

    _wait()

# ---- Keyboard Shortcuts ---- #
def copy_text():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    speak("Text copied sir")
    _wait()

def paste_text():
    pyautogui.hotkey("ctrl", "v")
    speak("Text pasted sir")
    _wait()

def select_all():
    pyautogui.hotkey("ctrl", "a")
    speak("Select all sir")
    _wait()

def save():
    pyautogui.hotkey("ctrl", "s")
    speak("Saved sir")
    _wait()

def backspace():
    pyautogui.press("backspace")
    speak("Deleted sir")
    _wait()
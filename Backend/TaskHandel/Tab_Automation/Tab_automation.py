import pyautogui
import time

def open_new_tab():
    pyautogui.hotkey('ctrl', 't')
    return "New tab is opened sir"

def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    return "New tab is closed sir"

def open_browser_menu():
    pyautogui.hotkey('alt', 'f')
    return "opened browser menu sir"

def zoom_in():
    pyautogui.hotkey('ctrl', '+')
    return "Zoom in sir"

def zoom_out():
    pyautogui.hotkey('ctrl', '-')
    return "Zoom out sir"

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')
    return "Page refreshed sir"

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')
    return "Switched to new tab sir"

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    return "Switched to previous tab sir"

def open_history():
    pyautogui.hotkey('ctrl', 'h')
    return "opened history sir"

def open_bookmarks():
    pyautogui.hotkey('ctrl', 'b')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def open_dev_tools():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def toggle_full_screen():
    pyautogui.hotkey('f11')

def open_private_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')


def minimize_tab():
    """Minimize current window."""
    pyautogui.hotkey("win", "d")
    time.sleep(0.2)
    return("Window minimized.")

def maximize_tab():
    """Maximize or restore current window."""
    pyautogui.hotkey("win", "d")
    time.sleep(0.2)
    return("Window maximized.")

def separate_tab():
    """
    Split current app window to left or right half of the screen.
    side = 'left' or 'right'
    """
    
    pyautogui.hotkey("win", "left")
    print("Window snapped to the left.")
    time.sleep(
        2)
    pyautogui.hotkey('enter')
    print("Window snapped to the right.")
    return "Separated sir"
    
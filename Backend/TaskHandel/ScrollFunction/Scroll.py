import pyautogui

def scroll_up():
    print("hnndhn")
    # Scroll up by pressing the Up arrow key five times
    pyautogui.press('up', presses=10)
    return "Scroll up sir"

def scroll_down():
    # Scroll down by pressing the Down arrow key five times
    pyautogui.press('down', presses=10)
    return "Scroll down sir"

def scroll_to_top():
    # Scroll to the top of the page
    pyautogui.hotkey('home')
    return "Scroll to top sir"

def scroll_to_bottom():
    # Scroll to the bottom of the page
    pyautogui.hotkey('end')
    return "Scroll to end sir"
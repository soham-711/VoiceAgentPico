import os
import pyautogui
import time
import pyperclip

def open_calculator():
    """Open Windows Calculator"""
    os.system("start calc")
    time.sleep(1.5)  # Wait for calculator to open
    print("✅ Calculator opened")

def slow_type(text: str, delay: float = 0.3):
    """Type characters one by one slowly"""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)

def calculate(expression: str):
    """
    Type a math expression into Calculator slowly
    and print the result.
    Example: '5 plus 7'
    """
    # Convert speech to math symbols
    expression = expression.lower()
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("multiply", "*")
    expression = expression.replace("times", "*")
    expression = expression.replace("divide", "/")
    expression = expression.replace("into", "*")

    # Open Calculator
    open_calculator()

    # Slowly type the expression
    slow_type(expression, delay=0.4)
    pyautogui.press("enter")
    time.sleep(1)

    # Copy result (Ctrl+C)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    # Get from clipboard
    result = pyperclip.paste()

    return(f"Your calculation result is {result}")
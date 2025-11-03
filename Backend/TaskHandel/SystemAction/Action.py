# import subprocess
# import os
# import ctypes, sys, subprocess
# import pyautogui
# import time
# def run_as_admin():
#     if not ctypes.windll.shell32.IsUserAnAdmin():
#         print("Re-launching as admin...")
#         # Relaunch the script with admin rights
#         ctypes.windll.shell32.ShellExecuteW(
#             None, "runas", sys.executable, " ".join(sys.argv), None, 1
#         )
#         sys.exit()

# def wifi_on():
#     run_as_admin()  # Ensure admin rights
#     subprocess.run('netsh interface set interface "Wi-Fi" admin=enable', shell=True)
#     print("Wi-Fi enabled")

# def wifi_off():
#     run_as_admin()
    
#     subprocess.run('netsh interface set interface "Wi-Fi" admin=disable', shell=True)
#     time.sleep(2) 
#     pyautogui.hotkey("shift","4")
#     time.sleep(0.5)
#     pyautogui.press("enter")
#     print("Wi-Fi disabled")

# def connect_known_wifi():
#     # Lists available networks
#     os.system('cmd /c "netsh wlan show networks"')
#     ssid = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
#     # Tries to connect to previously connected network profile
#     os.system(f'cmd /c "netsh wlan connect name={ssid}"')
#     print("Attempted to connect to SSID:", ssid)


# def main():
#     wifi_on()

# # Conditional execution
# if _name_ == "_main_":
#     main()
# # Example usage:
# # wifi_on()
# # wifi_off()
# # connect_known_wifi()
import ctypes
import os
import sys
import subprocess
import time
import pyautogui

def run_as_admin():
    """ Relaunch the script with admin rights if not already elevated """
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Re-launching as admin...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()

def wifi_on():
    run_as_admin()  # Ensure admin rights
    subprocess.run('netsh interface set interface "Wi-Fi" admin=enable', shell=True)
    print("Wi-Fi enabled")

def wifi_off(): 
    run_as_admin() 
    subprocess.run('netsh interface set interface "Wi-Fi" admin=disable', shell=True)
    time.sleep(2)
    pyautogui.press("left")
     # Types "$" on US layout
    time.sleep(0.5)
    pyautogui.press("enter")
    print("Wi-Fi disabled")
# def shut_down():
#     """Put Windows laptop into Sleep mode"""
#     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
# def turn_off_display():
#     """Turn off the laptop/PC screen (monitor goes off until user input)"""
#     ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
# def turn_off_display():
#     """Turn off screen until user moves mouse/keyboard"""
#     WM_SYSCOMMAND = 0x0112
#     SC_MONITORPOWER = 0xF170
#     # -1 = On, 1 = Low Power, 2 = Off
#     ctypes.windll.user32.SendMessageW(0xFFFF, WM_SYSCOMMAND, SC_MONITORPOWER, 2)

# # Example usage
# print("Turning off display in 5 seconds...")
# time.sleep(5)

def lock_screen():
    """Lock the computer (same as Win + L)"""
    ctypes.windll.user32.LockWorkStation()
def sleep():
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    pyautogui.hotkey("Alt", "F4")
    time.sleep(1)
    pyautogui.press("up")  # Arrow Up
    time.sleep(0.5)
    pyautogui.press("enter")
def shut_down():
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    pyautogui.hotkey("Alt", "F4")
    time.sleep(1)
    pyautogui.press("enter")
def restart():
    pyautogui.hotkey("win", "d")
    time.sleep(1)
    pyautogui.hotkey("Alt", "F4")
    time.sleep(1)
    pyautogui.press("down")  # Arrow Up
    time.sleep(0.5)
    pyautogui.press("enter")


# if _name_ == "_main_":
#     run_as_admin()   # ✅ Check elevation once at start
#     wifi_off()
#     time.sleep(5)
#     wifi_on()
#     shut_down()
#     print("Turning off screen in 5s...")
#     time.sleep(5)
#     turn_off_display()
#     lock_screen()
#     turn_off_display()
#     restart()
# if intent_name == "sleep_moode":
#     sleep()
# elif intent_name == "shut_down":
#     shut_down()
# elif intent_name == "restart":
#     restart()
# elif intent_name == "lock_screen":
#     lock_screen()
# elif intent_name == "wifi_on":
#     wifi_on()   
# elif intent_name == "wifi_off":
#     wifi_off()
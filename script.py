import time
import pyautogui


def change_volume(time_interval) -> None:
    pyautogui.press('volumedown')
    time.sleep(time_interval)
    pyautogui.press('volumeup')
    time.sleep(time_interval)

def avoid_screen_lock(time_interval) -> None:
    while True:
        change_volume(time_interval)

time_interval = 10

if __name__ == '__main__':
    print('Avoid lock screen script started...')
    avoid_screen_lock(time_interval)
    
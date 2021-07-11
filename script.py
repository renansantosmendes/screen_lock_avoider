import time
import pyautogui


def change_volume(time_interval: int) -> None:
    '''
    Increase and decrease the system volume after a given time interval
    
    Parameter:
    - time_interval (int): integer value representing time between volume up and down
    '''
    pyautogui.press('volumedown')
    time.sleep(time_interval)
    pyautogui.press('volumeup')
    time.sleep(time_interval)

def avoid_screen_lock(time_interval: int) -> None:
    '''
    Avoids screen lock executing a change in volume after a given time interval
    
    Parameter:
    - time_interval (int): integer value representing time between volume up and down
    '''
    while True:
        change_volume(time_interval)

time_interval = 10

if __name__ == '__main__':
    print('Avoid lock screen script started...')
    avoid_screen_lock(time_interval)
    
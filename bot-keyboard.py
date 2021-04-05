import time
import keyboard

keyboard.wait('shift')
for j in range (10):
    keyboard.write("NOVASENHA")
    time.sleep(0.3)
    keyboard.press_and_release('enter')
    time.sleep(5)
    for i in range(6):
        keyboard.press_and_release('tab')
        time.sleep(0.3)
    keyboard.press_and_release('enter')
    time.sleep(0.3)
    keyboard.press('ctrl')
    time.sleep(1)
    keyboard.press_and_release('left')
    time.sleep(1)
    keyboard.press_and_release('left')
    time.sleep(1)
    keyboard.press_and_release('delete')
    time.sleep(1)
    keyboard.press_and_release('delete')
    time.sleep(0.5)
    keyboard.release('ctrl')
    time.sleep(0.5)
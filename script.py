from pynput.keyboard import Key, Controller
import time
from datetime import datetime

keyboard = Controller()

time.sleep(2)



def walk_to_evolve():
    steps = 0
    start_time = datetime.now()
    while steps <= 38400:
        # keyboard.press(Key.shift)
        keyboard.press('d')
        time.sleep(0.3)
        keyboard.release('d')
        # steps += 16
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        difference = now - start_time
        print(current_time, difference)
        keyboard.press('a')
        time.sleep(0.3)
        keyboard.release('a')
        # keyboard.release(Key.shift)
        # steps += 16
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        difference = now - start_time
        print(current_time, difference)
    now = datetime.now()
    difference = now - start_time
    print(difference)

# keyboard.press(Key.shift)
# keyboard.press('a')
# time.sleep(1.5)
# keyboard.release('a')
# keyboard.press('d')
# time.sleep(1.5)
# keyboard.release('d')
# keyboard.release(Key.shift)
walk_to_evolve()
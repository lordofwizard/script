#/usr/bin/env python3
from pynput.keyboard import Key, Controller

import time

keyboard = Controller()
while True:
        time.sleep(1)
        keyboard.type("FUCK")
#        keyboard.press(Key.enter)
#       keyboard.release(Key.enter)

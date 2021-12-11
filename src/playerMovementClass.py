import random as rand
import json
import pyautogui
import pydirectinput

class playerMovement():

    def __init__(self) -> None:
        with open(r"configs\keysConfig.json", 'r') as j:
            config = json.load(j)
            self.keyUp = config['up']
            self.keyDown = config['down']
            self.keyLeft = config['left']
            self.keyRight = config['right']
        self.sleep_delay = 0.1

    def up(self):
        print('Up')
        pydirectinput.press(self.keyUp)
        pyautogui.sleep(self.sleep_delay)
        pydirectinput.press(self.keyUp)
        return -2

    def down(self):
        print('Down')
        pydirectinput.press(self.keyDown)
        pyautogui.sleep(self.sleep_delay)
        pydirectinput.press(self.keyDown)
        return 2

    def left(self):
        print('Left')
        pydirectinput.press(self.keyLeft)
        pyautogui.sleep(self.sleep_delay)
        pydirectinput.press(self.keyLeft)
        return -1

    def right(self):
        print('Right')
        pydirectinput.press(self.keyRight)
        pyautogui.sleep(self.sleep_delay)
        pydirectinput.press(self.keyRight)
        return 1

    def rand_mv_square(self):
        self.up()
        pos = 1
        while True:
            if pos == 1:
                pos = pos + rand.choice([self.down, self.right])()
            elif pos == 2:
                pos = pos + rand.choice([self.down, self.left])()
            elif pos == 3:
                pos = pos + rand.choice([self.up, self.right])()
            elif pos == 4:
                pos = pos + rand.choice([self.up, self.left])()
            pyautogui.sleep(0.1)

pmv = playerMovement()

pmv.rand_mv_square()


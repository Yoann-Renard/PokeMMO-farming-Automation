from PIL import Image
import pyautogui
import pytesseract
import json

class screenMonitor():
    """[summary]
    """

    def __init__(self, target = None) -> None:
        self.target = target
        with open("configs\dependenciesConfig.json",'r' ) as j:
            config = json.load(j)
            tesseract_loc = config['tesseract']['location']
        pytesseract.pytesseract.tesseract_cmd = tesseract_loc

    def isOnScreen(self) -> bool:
        try:
            with Image.open(self.target) as f:
                img = f
            if pyautogui.locateOnScreen(img) != None:
                return True
            else:
                return False
        except FileNotFoundError or FileExistsError:
            text_to_search = self.target
            im = pyautogui.screenshot()
            str_on_screen = str(pytesseract.image_to_string(im)).lower()
            if str_on_screen.find(text_to_search) != -1:
                return True
            else:
                return False


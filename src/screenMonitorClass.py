from PIL import Image
import pyautogui
import pytesseract
import json
import asyncio

class screenMonitor():
    """[summary]
    """

    def __init__(self) -> None:
        with open(r"configs\dependenciesConfig.json",'r' ) as j:
            config = json.load(j)
            tesseract_loc = config['tesseract']['location']
        pytesseract.pytesseract.tesseract_cmd = tesseract_loc

    def isOnScreen(self, target: str) -> bool:
        try:
            with Image.open(target) as f:
                img = f
            if pyautogui.locateOnScreen(img) != None:
                return True
            else:
                return False
        except FileNotFoundError or FileExistsError:
            text_to_search = target
            im = pyautogui.screenshot()
            str_on_screen = str(pytesseract.image_to_string(im)).lower()
            if str_on_screen.find(text_to_search) != -1:
                return True
            else:
                return False

    async def _monitor(self, target: str) -> bool:
        self.running_state = True
        try:
            with Image.open(target) as f:
                img = f
            if pyautogui.locateOnScreen(img) != None:
                return True
            else:
                return False
        except FileNotFoundError or FileExistsError:
            text_to_search = target.lower()
            while self.running_state:
                im = pyautogui.screenshot()
                str_on_screen = str(pytesseract.image_to_string(im)).lower()
                if str_on_screen.find(text_to_search) != -1:
                    print(f"{target} found on screen !")
                print(f"Monitoring {text_to_search}...")
                await asyncio.sleep(2)
            else:
                print(f'Monitoring of {text_to_search} canceled')

    async def run(self,target: str):
        await asyncio.gather(
            self._monitor(target)
        )

    async def stop(self) -> bool:
        self.running_state = False

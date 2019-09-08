import settings
import pyautogui
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class AutoQueue:
    """Automatic queue WOW!"""

    def open_wow(self):
        """open wow"""
        pass

    def move_mouse(self, x, y, t):
        """move mouose to"""

        try:
            pyautogui.moveTo(x,y,t)
        except Exception:
            logger.exception(f"Error occured while exec move_mouse on {x}, {y}, {t}")
            raise

    def click_mouse(self, n):
        """click mouse"""

        assert n <= 2 and n >= 1, "n only accept 1 or 2 in click_mouse()"

        if n == 1:
            pyautogui.click()
        else:
            pyautogui.doubleClick()

    def type(self):
        """type keyboard"""
        pass

    def get_mouse_pos(self):
        """get the current location of the mouse"""

        try:
            pos = pyautogui.position()
        except Exception:
            logger.exception(f"Error occured while exec get_mouse_pos")
            raise
        return pos


    def start_queue(self):

        self.move_mouse(settings.WOW_ICON_X, settings.WOW_ICON_Y, 3)
        self.click_mouse(n=2)
        time.sleep(settings.WAIT_TIME_BTW)

        self.move_mouse(settings.RUNGAME_X, settings.RUNGAME_Y, 3)
        self.click_mouse(n=1)
        time.sleep(settings.WAIT_TIME_BTW)
        self.move_mouse(settings.SERVER_X, settings.SERVER_Y, 3)
        self.click_mouse(n=2)


if __name__ == '__main__':

    obj = AutoQueue()
    try:
        obj.start_queue()
    except KeyboardInterrupt:
        raise




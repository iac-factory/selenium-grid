import os
import sys
import time
import pprint
import typing

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

Union = typing.Union
List = typing.List

class Login:
    """
    ...
    """

    def __init__(self):
        self.screenshots = []

        self.driver = webdriver.Remote("http://localhost:4444")

        self.driver.get("https://localhost/sign-in")

        self.screenshot("Sign-In.1")

        self.inputUsername()

        self.screenshot("Sign-In.2")

        self.inputPassword()

        self.screenshot("Sign-In.3")

        time.sleep(2.5)

        self.screenshot("Sign-In.4")

        self.cookies = lambda: self.driver.get_cookies()

        try:
            self.driver.close()
            self.driver.quit()
        finally:
            print("Screenshots" + ":")
            for screenshot in self.screenshots:
                print(" - {0}".format(screenshot))

            sys.exit(0)

    def screenshot(self, name: str) -> None:
        """
        Take a screenshot of the current point in time, and append the full-system path
        to the class instance's `self.screenshots` array attribute.

        Args:
            name: (str) - the name of the screenshot, relative. There is not need to
            append .png nor set the name to the full system path.

        Returns: None
        """

        name = name + ".png" if not name.endswith(".png") else name

        binary = self.driver.get_screenshot_as_png()

        screenshot = open(name, "wb+")
        screenshot.write(binary)
        screenshot.close()

        self.screenshots.append(os.path.abspath(os.path.dirname(__name__)) + os.sep + name)

    def locate(self, id: str) -> Union[WebElement, List]:
        """
        Args:
            id: str - Creates a wait conditional while searching for
                an HTML element via unique ID.

        Returns:
            Union[WebElement, list]
        """

        waiter = None

        try:
            waiter = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, id))
            )
        except Exception: raise Exception
        finally:
            if waiter != self.driver.find_element(By.ID, value = id):
                print("[Warning]", "Locator & Element found mismatched Element(s)")

            return waiter

    def username(self, id: str):
        return self.locate(id)

    def password(self, id: str):
        return self.locate(id)

    def submit(self, id: str):
        return self.locate(id)

    def inputUsername(self, id: str, username: str):
        field = self.username(id)

        try:
            field.send_keys(username)

            time.sleep(1.0)

            field.send_keys(Keys.RETURN)

            time.sleep(1.0)
        except Exception:
            raise Exception
        finally:
            try:
                self.submit.click()
            except Exception:
                raise Exception
            finally:
                time.sleep(2.5)

    def inputPassword(self, id: str, password: str):
        field = self.password(id)

        try:
            field.send_keys(password)

            time.sleep(1.0)

            field.send_keys(Keys.RETURN)

            time.sleep(1.0)
        except Exception:
            raise Exception
        finally:
            time.sleep(2.5)

    def send(self):
        self.submit.click()

def main():
    Login()

if __name__ == "__main__":
    main()

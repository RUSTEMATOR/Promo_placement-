import os
import time

import pytest
import subprocess
from datetime import datetime
from Data.account_info import credentials
from Data.config import urlEN, urlAU, browser_config
from Locators.locators import Locators


class Screenshot:

    def __init__(self, page):
        self.page = page

    def capture_screenshot(self, locale, account_group, screenshot_name):
        # Adjusted base directory to include 'Promo_placement'
        base_dir = "Screenshots"
        # Adjusted date format to 'DD.MM.YYYY'
        date_str = datetime.now().strftime("%d.%m.%Y")
        # Adjusted directory path to include 'locale' and 'screenshot_name' for promo placement
        dir_path = os.path.join(base_dir, date_str, locale, account_group, screenshot_name)

        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        counter = 1

        # Construct the screenshot path with a generic filename or a specific naming convention
        screenshot_path = os.path.join(dir_path, f"screenshot({counter}).png")

        # Check if the screenshot file already exists and increment the counter until a unique filename is found
        while os.path.exists(screenshot_path):
            counter += 1
            screenshot_path = os.path.join(dir_path, f"screenshot({counter}).png")

        self.page.screenshot(path=screenshot_path, full_page=False)


class ScreenshotFull:
    def __init__(self, page):
        self.page = page

    def capture_screenshot_full(self, locale, account_group, screenshot_name):
        # Adjusted base directory to include 'Promo_placement'
        base_dir = "Screenshots"
        # Adjusted date format to 'DD.MM.YYYY'
        date_str = datetime.now().strftime("%d.%m.%Y")
        # Adjusted directory path to include 'locale' and 'screenshot_name' for promo placement
        dir_path = os.path.join(base_dir, date_str, locale, account_group, screenshot_name)

        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        counter = 1

        # Construct the screenshot path with a generic filename or a specific naming convention
        screenshot_path = os.path.join(dir_path, f"screenshot({counter}).png")

        # Check if the screenshot file already exists and increment the counter until a unique filename is found
        while os.path.exists(screenshot_path):
            counter += 1
            screenshot_path = os.path.join(dir_path, f"screenshot({counter}).png")

        self.page.screenshot(path=screenshot_path, full_page=True)


class Login(Locators):
    @pytest.mark.parametrize("group, email,password",
                             [(key, val['username'], val['password']) for key, val in credentials.items()])
    def base_login(self, email, password):
        locators = Locators(self.page)
        self.page.set_viewport_size(browser_config["viewport"])
        self.page.goto(urlEN)
        locators.login_button.click()
        locators.email_input.fill(email)
        locators.password_input.fill(password)
        locators.sign_in_button.click()

    @pytest.mark.parametrize("group, email,password",
                             [(key, val['username'], val['password']) for key, val in credentials.items()])
    def base_login_au(self, email, password):
        locators = Locators(self.page)
        self.page.set_viewport_size(browser_config["viewport"])
        self.page.goto(urlAU)
        locators.login_button.click()
        locators.email_input.fill(email)
        locators.password_input.fill(password)
        locators.sign_in_button.click()
        time.sleep(20)

class VpnChange:
    def connect_vpn(self, location_id):
        # Check if VPN is off
        subprocess.run(["expresso", "disconnect"], check=True)

        # Connect to a new location
        subprocess.run(["expresso", "connect", location_id], check=True)

        # Check if VPN is on
        subprocess.run(["expresso", "status"], check=True)




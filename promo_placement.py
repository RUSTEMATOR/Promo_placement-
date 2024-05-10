import time
import pytest
from playwright.sync_api import Page
from Data.account_info import credentials
from Locators.locators import Locators
from Fucntions.functions import Screenshot, Login, ScreenshotFull

# Promo placement test for the master domain


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_main_slider(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = Screenshot(page)
    login = Login(page)
    login.base_login(email, password)
    locators.lang_dropdown.click()
    locators.en_lang.click()
    time.sleep(5)
    screenshot.capture_screenshot("EN", group, "Main slider")
    if locators.scrolling_arrow.is_visible():
        for _ in range(6):
            locators.scrolling_arrow.click()
            time.sleep(1)
            screenshot.capture_screenshot("EN", group, "Main slider")
    else:
        screenshot.capture_screenshot("EN", group, "Main slider")


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_lobby_promo_slider(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = Screenshot(page)
    login = Login(page)
    login.base_login(email, password)
    locators.lobby_promo_slider.scroll_into_view_if_needed()
    screenshot.capture_screenshot("EN", group, "Lobby slider")
    time.sleep(5)
    locators.lobbypromo_scroll_arrow.click()
    screenshot.capture_screenshot("EN", group, "Lobby slider")


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_promo_page(page: Page, group, email, password):
    screenshot = ScreenshotFull(page)
    login = Login(page)
    login.base_login(email, password)
    time.sleep(5)
    page.goto("https://kingbillycasino.com/promotions")
    time.sleep(5)
    screenshot.capture_screenshot_full("EN", group, "Promo page")


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_promo_page_vip(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = ScreenshotFull(page)
    login = Login(page)
    login.base_login(email, password)
    time.sleep(5)
    page.goto("https://www.kingbillycasino.com/promotions")
    locators.vip_promo_tab.click()
    time.sleep(5)
    screenshot.capture_screenshot_full("EN", group, "Promo page VIP")


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_promo_tournaments(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = ScreenshotFull(page)
    login = Login(page)
    login.base_login(email, password)
    time.sleep(5)
    page.goto("https://kingbillycasino.com/tournaments")
    time.sleep(3)
    screenshot.capture_screenshot_full("EN", group, "Tournaments")
    locators.tournament_promo_scroll_arrow.click()
    screenshot.capture_screenshot_full("EN", group, "Tournaments")


#_____________________________________________________________________________________________________________

@pytest.mark.au
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_main_slider_au(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = Screenshot(page)
    login = Login(page)
    page.set_default_timeout(90000)  # Sets the timeout to 60 seconds
    login.base_login_au(email, password)
    time.sleep(20)
    screenshot.capture_screenshot("AU", group, "Main slider")
    if locators.scrolling_arrow.is_visible():
        for _ in range(6):
            locators.scrolling_arrow.click()
            time.sleep(1)
            screenshot.capture_screenshot("AU", group, "Main slider")
    else:
        screenshot.capture_screenshot("AU", group, "Main slider")


@pytest.mark.au
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_lobby_promo_slider_au(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = Screenshot(page)
    login = Login(page)
    login.base_login_au(email, password)
    page.set_default_timeout(90000)  # Sets the timeout to 60 seconds
    locators.lobby_promo_slider.scroll_into_view_if_needed()
    screenshot.capture_screenshot("AU", group, "Lobby slider")
    time.sleep(20)
    locators.lobbypromo_scroll_arrow.click()
    screenshot.capture_screenshot("AU", group, "Lobby slider")

@pytest.mark.au
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_promo_page_au(page: Page, group, email, password):
    screenshot = ScreenshotFull(page)
    login = Login(page)
    login.base_login_au(email, password)
    page.set_default_timeout(90000)  # Sets the timeout to 60 seconds
    page.goto("https://www.kingbillywin16.com/promotions")
    time.sleep(20)
    screenshot.capture_screenshot_full("AU", group, "Promo page")


@pytest.mark.au
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_promo_page_vip(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = ScreenshotFull(page)
    login = Login(page)
    login.base_login(email, password)
    time.sleep(5)
    page.goto("https://www.kingbillycasino.com/promotions")
    locators.vip_promo_tab.click()
    time.sleep(5)
    screenshot.capture_screenshot_full("AU", group, "Promo page VIP")


@pytest.mark.au
@pytest.mark.parametrize("group, email,password", [(key, val['username'], val['password']) for key, val in credentials.items()])
def test_master_domain_promo_tournaments_au(page: Page, group, email, password):
    locators = Locators(page)
    screenshot = ScreenshotFull(page)
    login = Login(page)
    login.base_login_au(email, password)
    page.set_default_timeout(90000)  # Sets the timeout to 60 seconds
    page.goto("https://www.kingbillywin16.com/tournaments")
    time.sleep(20)
    screenshot.capture_screenshot_full("AU", group, "Tournaments")
    locators.tournament_promo_scroll_arrow.click()
    screenshot.capture_screenshot_full("AU", group, "Tournaments")


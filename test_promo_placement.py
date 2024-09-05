import time
import pytest
from playwright.sync_api import Page
from Data.account_info import credentials
from Locators.locators import Locators
from Fucntions.functions import Screenshot, Login, ScreenshotFull
from Data.config import urlEN, urlAU
# Promo placement test for the master domain


@pytest.mark.ie
@pytest.mark.parametrize("group, email, password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
def test_master_domain_main_slider(page: Page, group, email, password, is_anonymous):
    locators = Locators(page)
    screenshot = Screenshot(page)
    if not is_anonymous:
        login = Login(page)
        login.base_login(email, password)
        locators.lang_dropdown.click()
        locators.en_lang.click()
        time.sleep(10)
    else:
        page.goto("https://www.kingbillycasino.com")
        pass
    screenshot.capture_screenshot("EN", group, "Main slider")
    if locators.scrolling_arrow.is_visible():
        for _ in range(6):
            locators.scrolling_arrow.click()
            time.sleep(3)
            screenshot.capture_screenshot("EN", group, "Main slider")
    else:
        screenshot.capture_screenshot("EN", group, "Main slider")


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
def test_master_domain_lobby_promo_slider(page: Page, group, email, password, is_anonymous):
    locators = Locators(page)
    screenshot = Screenshot(page)
    if not is_anonymous:
        login = Login(page)
        login.base_login(email, password)
        time.sleep(10)
    else:
        page.goto("https://www.kingbillycasino.com")
        pass
    locators.lobby_promo_slider.scroll_into_view_if_needed()
    screenshot.capture_screenshot("EN", group, "Lobby slider")
    time.sleep(3)
    if locators.lobbypromo_scroll_arrow is None:
        pass
    else:
        while locators.lobbypromo_scroll_arrow.is_enabled():
            locators.lobbypromo_scroll_arrow.click()
            time.sleep(1)
            locators.lobbypromo_scroll_arrow.click()
            time.sleep(1)
            if page.locator('button.slick-disabled.slick-arrow.text-btn').first.is_visible():
                screenshot.capture_screenshot("EN", group, "Lobby slider")
                break

            screenshot.capture_screenshot("EN", group, "Lobby slider")

@pytest.mark.ie
@pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
def test_master_domain_promo_page(page: Page, group, email, password, is_anonymous):
    screenshot = ScreenshotFull(page)
    if not is_anonymous:
        login = Login(page)
        login.base_login(email, password)
        time.sleep(10)
    else:
        pass
    page.goto("https://kingbillycasino.com/promotions")
    time.sleep(10)
    screenshot.capture_screenshot_full("EN", group, "Promo page")


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
def test_master_domain_promo_page_vip(page: Page, group, email, password, is_anonymous):
    locators = Locators(page)
    screenshot = ScreenshotFull(page)
    if not is_anonymous:
        login = Login(page)
        login.base_login(email, password)
        time.sleep(10)
    else:
        pass
    page.goto("https://www.kingbillycasino.com/promotions")
    locators.vip_promo_tab.click()
    time.sleep(10)
    screenshot.capture_screenshot_full("EN", group, "Promo page VIP")


@pytest.mark.ie
@pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
def test_master_domain_promo_tournaments(page: Page, group, email, password, is_anonymous):
    locators = Locators(page)
    screenshot = ScreenshotFull(page)
    if not is_anonymous:
        login = Login(page)
        login.base_login(email, password)
        time.sleep(20)
    else:
        pass
    page.goto("https://kingbillycasino.com/tournaments")
    time.sleep(20)
    screenshot.capture_screenshot_full("EN", group, "Tournaments")
    if locators.lobbypromo_scroll_arrow is None:
        pass
    else:
        while locators.lobbypromo_scroll_arrow.is_enabled():
            locators.lobbypromo_scroll_arrow.click()
            time.sleep(1)
            locators.lobbypromo_scroll_arrow.click()
            time.sleep(1)
            if page.locator('button.slick-disabled.slick-arrow.text-btn').first.is_visible():
                screenshot.capture_screenshot_full("EN", group, "Tournaments")
                break
            screenshot.capture_screenshot_full("EN", group, "Tournaments")

@pytest.mark.ie
@pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
def test_master_domain_deposit(page: Page, group, email, password, is_anonymous):
    locators = Locators(page)
    screenshot = Screenshot(page)
    login = Login(page)
    login.base_login(email, password)
    time.sleep(20)
    locators.deposit_button.click()
    locators.deposit_promo_button.scroll_into_view_if_needed()
    time.sleep(20)
    screenshot.capture_screenshot("EN", group, "Deposit")



@pytest.mark.ie
@pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
def test_promo_profile(page: Page, group, email, password, is_anonymous):
    locators = Locators(page)
    screenshot = ScreenshotFull(page)
    login = Login(page)
    login.base_login(email, password)
    time.sleep(20)
    page.goto('https://www.kingbillycasino.com/profile/promo/casino')
    time.sleep(10)
    screenshot.capture_screenshot_full("EN", group, "Promo profile")

# _____________________________________________________________________________________________________________

# @pytest.mark.au
# @pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
# def test_master_domain_main_slider_au(page: Page, group, email, password, is_anonymous):
#     locators = Locators(page)
#     screenshot = Screenshot(page)
#     if not is_anonymous:
#         login = Login(page)
#         page.set_default_timeout(90000)  # Sets the timeout to 60 seconds
#         login.base_login_au(email, password)
#         time.sleep(80)
#     else:
#         page.goto(urlAU)
#         pass
#     screenshot.capture_screenshot("AU", group, "Main slider")
#     if locators.scrolling_arrow.is_visible():
#         for _ in range(6):
#             locators.scrolling_arrow.click()
#             time.sleep(1)
#             screenshot.capture_screenshot("AU", group, "Main slider")
#     else:
#         screenshot.capture_screenshot("AU", group, "Main slider")


# @pytest.mark.au
# @pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
# def test_master_domain_lobby_promo_slider_au(page: Page, group, email, password, is_anonymous):
#     locators = Locators(page)
#     screenshot = Screenshot(page)
#     if not is_anonymous:
#         login = Login(page)
#         login.base_login_au(email, password)
#         time.sleep(20)
#     else:
#         page.goto(urlAU)
#         pass
#     page.set_default_timeout(90000)  # Sets the timeout to 60 seconds
#     locators.lobby_promo_slider.scroll_into_view_if_needed()
#     if locators.lobbypromo_scroll_arrow is None:
#         pass
#     else:
#         while locators.lobbypromo_scroll_arrow.is_enabled():
#             locators.lobbypromo_scroll_arrow.click()
#             time.sleep(7)
#             locators.lobbypromo_scroll_arrow.click()
#             time.sleep(7)
#             if page.locator('button.slick-disabled.slick-arrow.text-btn').first.is_visible():
#                 screenshot.capture_screenshot("AU", group, "Lobby slider")
#                 break
#             screenshot.capture_screenshot("AU", group, "Lobby slider")

# @pytest.mark.au
# @pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
# def test_master_domain_promo_page_au(page: Page, group, email, password, is_anonymous):
#     screenshot = ScreenshotFull(page)
#     if not is_anonymous:
#         login = Login(page)
#         login.base_login_au(email, password)
#         time.sleep(80)
#     else:
#         pass
#     page.goto(f'{urlAU}/promotions')
#     time.sleep(80)
#     screenshot.capture_screenshot_full("AU", group, "Promo page")


# @pytest.mark.au
# @pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
# def test_master_domain_promo_page_vip(page: Page, group, email, password, is_anonymous):
#     locators = Locators(page)
#     screenshot = ScreenshotFull(page)
#     if not is_anonymous:
#         login = Login(page)
#         login.base_login(email, password)
#         time.sleep(80)
#     else:
#         pass
#     page.goto(f'{urlAU}/promotions')
#     locators.vip_promo_tab.click()
#     time.sleep(80)
#     screenshot.capture_screenshot_full("AU", group, "Promo page VIP")


# @pytest.mark.au
# @pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
# def test_master_domain_promo_tournaments_au(page: Page, group, email, password, is_anonymous):
#     locators = Locators(page)
#     screenshot = ScreenshotFull(page)
#     if not is_anonymous:
#         login = Login(page)
#         login.base_login_au(email, password)
#         page.set_default_timeout(90000)  # Sets the timeout to 60 seconds
#     else:
#         pass
#     page.goto(f'{urlAU}/tournaments')
#     time.sleep(80)
#     screenshot.capture_screenshot_full("AU", group, "Tournaments")
#     if locators.lobbypromo_scroll_arrow is None:
#         pass
#     else:
#         while locators.lobbypromo_scroll_arrow.is_enabled():
#             locators.lobbypromo_scroll_arrow.click()
#             time.sleep(7)
#             locators.lobbypromo_scroll_arrow.click()
#             time.sleep(7)
#             if page.locator('button.slick-disabled.slick-arrow.text-btn').first.is_visible():
#                 screenshot.capture_screenshot_full("AU", group, "Tournaments")
#                 break
#             screenshot.capture_screenshot_full("AU", group, "Tournaments")


# @pytest.mark.au
# @pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
# def test_master_domain_deposit(page: Page, group, email, password, is_anonymous):
#     locators = Locators(page)
#     screenshot = Screenshot(page)
#     login = Login(page)
#     login.base_login_au(email, password)
#     time.sleep(20)
#     locators.deposit_button.click()
#     locators.deposit_promo_button.scroll_into_view_if_needed()
#     time.sleep(80)
#     screenshot.capture_screenshot("AU", group, "Deposit")


# @pytest.mark.au
# @pytest.mark.parametrize("group, email,password, is_anonymous", [(key, val['username'], val['password'], False) for key, val in credentials.items()] + [("anonymous", None, None, True)])
# def test_promo_profile(page: Page, group, email, password, is_anonymous):
#     locators = Locators(page)
#     screenshot = ScreenshotFull(page)
#     login = Login(page)
#     login.base_login(email, password)
#     time.sleep(30)
#     page.goto(f'{urlAU}/profile/promo/casino')
#     time.sleep(80)
#     screenshot.capture_screenshot_full("AU", group, "Promo profile")
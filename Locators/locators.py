class Locators:
    def __init__(self, page):
        self.page = page

    @property
    def accept_cookies(self):
        return self.page.get_by_role("button", name="accept")

    @property
    def login_button(self):
        return self.page.get_by_role("link", name="sign in")

    @property
    def email_input(self):
        return self.page.get_by_placeholder("your e-mail address")

    @property
    def password_input(self):
        return self.page.get_by_placeholder("your password")

    @property
    def sign_in_button(self):
        return self.page.get_by_role("button", name="sign in")

    @property
    def banking_methods(self):
        return self.page.get_by_role("link", name="See all banks")

    @property
    def scrolling_arrow(self):
        return self.page.locator("xpath=/html/body/div[1]/div[2]/main/div/div[1]/div/div/div/button[2]")

    @property
    def lobby_promo_slider(self):
        return self.page.locator(".promos-slider > .slick-slider")

    @property
    def lobbypromo_scroll_arrow(self):
        return self. page.locator("xpath=/html/body/div[1]/div[2]/main/div/div[7]/div/div[2]/button[2]")

    @property
    def burger_menu(self):
        return self.page.get_by_role("banner").get_by_role("button").first

    @property
    def promo_tab(self):
        return self.page.locator("#bar").get_by_role("link", name="Promotions")

    @property
    def tournaments_tab(self):
        return self.page.locator("#bar").get_by_role("link", name="Tournaments")

    @property
    def tournament_promo_block(self):
        return self.page.locator(".slick-slider")

    @property
    def tournament_promo_scroll_arrow(self):
        return self.page.locator("xpath=/html/body/div[1]/div[2]/main/div/div[2]/div/div[2]/div/div[2]/button[2]")


    @property
    def vip_promo_tab(self):
        return self.page.locator("xpath=//a[contains(@class, 'promotions-container__link link')][1]")


    @property
    def lang_dropdown(self):
        return self.page.locator("xpath=//div[contains(@class,"
                                 " 'select-language-icons-with-code__button') and @aria-autocomplete='list'][1]").first

    @property
    def en_lang(self):
        return self.page.get_by_role("option", name="en en")


    @property
    def cookie_accept(self):
        return self.page.get_by_role("button", name="accept")




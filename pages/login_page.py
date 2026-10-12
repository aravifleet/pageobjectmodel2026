from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://test-icsample1657400753.pantheonsite.io/"
        self.login_icon = "//a[@title='Log in']"
        self.user_name_input = "#edit-name"
        self.password_input = "#edit-pass"
        self.submit_button = "#edit-submit"
        
    def navigate_to_app(self):
        self.page.goto(self.url)
        
    def login(self, username, password):
        self.click_element(self.login_icon)
        self.fill_element(self.user_name_input,username)
        self.fill_element(self.password_input,password)
        self.click_element(self.submit_button)
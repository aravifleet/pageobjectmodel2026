class BasePage:
    def __init__(self, page):
        self.page = page
        
    def click_element(self, locator):
        self.page.click(locator)
        
    def fill_element(self,locator,value):
        self.page.fill(locator, value)
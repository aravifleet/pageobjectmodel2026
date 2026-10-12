from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.book_link = "//span[text()='Books']"
        self.addtocart = "//a[text()='Add to Cart'][1]"
        self.cart_button = "//a[@title='Cart']"
        self.checkout = "//button[text()='Checkout']"
        self.firstname = "#edit-shipping-information-shipping-profile-address-0-address-given-name"
        self.lastname = "#edit-shipping-information-shipping-profile-address-0-address-family-name"
        self.address = "#edit-shipping-information-shipping-profile-address-0-address-address-line1"
        self.city = "#edit-shipping-information-shipping-profile-address-0-address-locality"
        self.shippingmethod = "#edit-shipping-information-shipping-profile-address-0-address-administrative-area"
        self.paymentmethod = "#edit-shipping-information-shipping-profile-address-0-address-postal-code"
        self.continue_to_review = "//label[text()='UPS Ground: $10.00 ']"
        self.next_action = "//label[text()='Credit card']"
        self.iframeselector = "//input[@value='Continue to review']"
        self.cardnum = "#cardNum"
        self.expiry = "#expiryDate"
        self.cvv = "#cvv"
        self.pay = "#payBtn"
        
        
    def add_to_cart(self):
        self.click_element(self.book_link)
        self.click_element(self.addtocart)
        self.click_element(self.cart_button)
        self.click_element(self.checkout)
        
    def filling_details(self,data):
        self.fill_element(self.firstname, data["first_name"])
        self.fill_element(self.lastname, data["last_name"])
        self.fill_element(self.address, data["address"])
        self.fill_element(self.city, data["city"])
        self.fill_element(self.cardnum, data["cardnum"])
        self.fill_element(self.expiry, data["expiry"])
        self.fill_element(self.cvv, data["cvv"])
        
        
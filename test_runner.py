import os
from sys import exception
from numpy import full
from playwright.sync_api import sync_playwright
from data_loader import load_data
from pages import login_page
from pages import checkout_page
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


def run_tests():
    test_records = load_data("test_data.csv")
    os.makedirs("screenshots",exist_ok=True)
    
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        login_page = LoginPage(page)
        checkout_page = CheckoutPage(page)
        
        for index, row in enumerate(test_records, start=1):
            print("The reading of csv data has been started")
            
            try:
                login_page.navigate_to_app()
                login_page.login(row["username"], row["password"])
                checkout_page.add_to_cart()
                checkout_page.filling_details(row)
                
                screenshotpath = "completed1.png"
                page.screenshot(path=screenshotpath,full_page=True)
                
            except Exception as e:
                failscreens = "failedscreen1.png"
                page.screenshot(path=failscreens, full_page=True)
                
                continue
            
        browser.close()
        
if __name__ == "__main__":
    run_tests()
            

        
        
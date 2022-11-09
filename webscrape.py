from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import *
from selenium.webdriver.chrome.options import Options



# url = 'https://www.amazon.ae/dp/B09SWSX7FW?ref=MarsFS_ERDR_cav'
# # Amazon xpath
# xpath = '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[1]'



def webscrape(url, xpath, website):
    
    
    s = Service('/chromedriver.exe')
    
    # Make Browser Headless
    op = webdriver.ChromeOptions()
    op.add_argument(argument='headless')
    
    # Start Browser
    browser = webdriver.Chrome(service=s, options=op)
    # browser.maximize_window()
    browser.get(url)
    
    
    
    
    # Locate Price Element
    price = browser.find_element(by = By.XPATH, value = xpath).get_attribute(name='innerHTML')
    return price
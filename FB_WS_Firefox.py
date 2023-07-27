from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
import pandas as pd

try:
    #credentials
    user = "YOUR USERNAME HERE"
    pword = "YOUR PASSWORD HERE"
    
    #selenium setup
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument("--headless")
    driver = webdriver.Firefox(options=fireFoxOptions)
    driver.get("https://www.facebook.com")
    
    #log in
    username = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    submit = driver.find_element(By.NAME, "login")
    username.send_keys(user)
    password.send_keys(pword)
    submit.click()
    
    #scrape data (portrait thumbnail URL)
    element = driver.find_element(By.XPATH, "//*[local-name()='svg' and @class='x3ajldb']/*[local-name()='g']/*[local-name()='image']")
    data = element.get_attribute("xlink:href")
finally:
    try:
        driver.close()
    except:
        pass
    else:
        #Save data to excel sheet
        data = {'FB Portrait Thumbnail URL': [data]}
        df = pd.DataFrame(data)
        df.to_excel('output.xlsx', index=False)
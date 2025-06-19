
import time                   
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
driver = webdriver.Firefox()
# getting in to amazon 
driver.get('https://www.amazon.in')
time.sleep(3)
# for window extention
driver.maximize_window()
# input xpath of the searchbox to click
searchbox = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
searchbox.click()
searchbox.send_keys("laptop")
searchbox.send_keys(Keys.RETURN)
time.sleep(3)
# to scroll the display automatically
driver.execute_script("window.scrollBy(0,500);")
time.sleep(3)
# clicks the random product and add that product in cart
laptop=driver.find_elements(By.XPATH, '//*[@id="a-autoid-2-announce"]')
 # if the product is defined it clicks a random product
if laptop:                                      
    laptop1=random.choice(laptop)
    laptop1.click()
else:
    print("product not found")                 

time.sleep(5)
#to get into cart
gotocart=driver.find_element(By.XPATH,'//*[@id="nav-cart"]')
gotocart.click()
time.sleep(3)
#click proceed to buy button
proceedtobuy=driver.find_element(By.CSS_SELECTOR, '#sc-buy-box-ptc-button > span:nth-child(1) > input:nth-child(1)')
proceedtobuy.click()
time.sleep(3)
# enter mobile number or email to login your account
enternumber=driver.find_element(By.XPATH,'//*[@id="ap_email_login"]')
enternumber.click()
enternumber.send_keys("xxxxxxxxxx")
enternumber.send_keys(Keys.RETURN)
time.sleep(5)
# enter password
password=driver.find_element(By.XPATH,'//*[@id="ap_password"]')
password.click()
password.send_keys("********")
password.send_keys(Keys.RETURN)
time.sleep(5)
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
options = Options()
options.add_extension('extension_3_5_0_0.crx')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.maximize_window()
driver.get("https://footlocker.com")
time.sleep(2)
cod = pyautogui.locateCenterOnScreen('d.PNG')
pyautogui.click(cod)
time.sleep(4)
locIframe = driver.find_element_by_xpath('/html/body/div[29]/iframe')
driver.switch_to.frame(locIframe)
time.sleep(2)
password = driver.find_element_by_xpath("/html/body/app-root/div/div/app-signin/div[1]/form/div[1]/input[2]")
password.send_keys("@alisher965" )
name = driver.find_element_by_xpath("/html/body/app-root/div/div/app-signin/div[1]/form/div[1]/input[1]")
name.send_keys("@alisher965" )
time.sleep(2)
signin = driver.find_element_by_xpath("/html/body/app-root/div/div/app-signin/div[2]/ctabutton/button")
signin.click()
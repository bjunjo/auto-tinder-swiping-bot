from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# TODO: Using Selenium and Python Navigate to the Tinder website (https://tinder.com/) and click on LOG IN then LOGIN WITH FACEBOOK.
chrome_driver_path = "/Users/ByoungjunJo/Desktop/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")

# Login to Tinder with Facebook
sleep(5)
tinder_login = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
sleep(5)
fb_login = driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
fb_login.click()

fb_id = os.getenv("ID")
fb_pwd = os.getenv("PWD")
sleep(5)

# Move to the 2nd window with the Facebook login
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

id_input = driver.find_element_by_id("email").send_keys(fb_id)
pwd_input = driver.find_element_by_id("pass").send_keys(fb_pwd)
submit_fb_login = driver.find_element_by_name("login")
submit_fb_login.click()

# Revert back to the first window
driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

# Compliance "agree"
share_location = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[1]').click()

privacy_agreement = driver.find_element_by_xpath('//*[@id="c-174738105"]/div/div[2]/div/div/div[1]/button').click()

sleep(2)
notificaiton = driver.find_element_by_xpath('//*[@id="c-1903119181"]/div/div/div/div/div[3]/button[2]').click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add 2 seconds delay between likes.
    sleep(2)

    try:
        print("swiped")
        like_button = driver.find_element_by_xpath(
            '//*[@id="c-174738105"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)



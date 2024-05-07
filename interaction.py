from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# result = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(result.text)
# content_portal_link = driver.find_element(by=By.LINK_TEXT, value="Content portals")
# content_portal_link.click()
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)
# driver.quit()

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
last_name = driver.find_element(by=By.NAME, value="lName")
email = driver.find_element(by=By.NAME, value="email")
submit_button = driver.find_element(by=By.CLASS_NAME, value="btn")
first_name.send_keys("Hitman")
last_name.send_keys("47")
email.send_keys("hitman@47gmail.com")
submit_button.click()

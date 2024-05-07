from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

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

# signup form
# driver.get(url="https://secure-retreat-92358.herokuapp.com/")
#
# first_name = driver.find_element(by=By.NAME, value="fName")
# last_name = driver.find_element(by=By.NAME, value="lName")
# email = driver.find_element(by=By.NAME, value="email")
# submit_button = driver.find_element(by=By.CLASS_NAME, value="btn")
# first_name.send_keys("Hitman")
# last_name.send_keys("47")
# email.send_keys("hitman@47gmail.com")
# submit_button.click()


# cookie clicker game
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID, value="cookie")


def get_money():
    money = driver.find_element(by=By.ID, value="money").text
    return money


def get_store_items():
    all_items = {}
    store = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

    for item in store:
        item_formatted = item.text.replace(" ", "").split("-")
        try:
            all_items[item_formatted[0]] = item_formatted[1]
        except IndexError:
            pass
    return all_items


def buy_item(item):
    item_to_buy = driver.find_element(by=By.ID, value=f"buy{item}")
    item_to_buy.click()


buy_time = time.time() + 5
five_mins = time.time() + 5 * 60

# *****************My Logic***************
while time.time() < five_mins:
    cookie.click()
    curr_money = int(get_money().replace(',', ''))
    if time.time() > buy_time:
        all_store_items = get_store_items()
        max_value = 0
        max_key = ''
        for key, value in all_store_items.items():
            curr_value = int(value.replace(',', ''))
            if curr_money > curr_value:
                if curr_value > max_value:
                    max_value = curr_value
                    max_key = key
        if max_key:
            buy_item(max_key)
        buy_time = time.time() + 5
click_rate = driver.find_element(by=By.ID, value="cps").text
print(click_rate)

# **************Another Approach************
# def check_and_buy():
#     upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store>div:not(.grayed)")
#     upgrades[-1].click()
#
#
#
# while time.time() < five_mins:
#     cookie.click()
#     if time.time() > buy_time:
#         all_store_items = get_store_items()
#         check_and_buy()
#         buy_time = time.time() + 5
# click_rate = driver.find_element(by=By.ID, value="cps").text
# print(click_rate)

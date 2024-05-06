from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Electric-Multi-Cooker-Pressure/dp/B0B4PQDFCL/ref=sr_1_1_sspa?crid=2YPCTK2W1NLQA&dib=eyJ2IjoiMSJ9.g1Lrz7oNcd8sVDvjEfcK43hdjIMppvRQyEWPpo05tT_k-YZ_pifVShNGsxsQK47WIVE57dn92fpxJ2JdGtXOKb4dnhBYMKPNHLRyjuF9tZQ-RyGcANZNana2UFSxIn4dG7-Rt1VUCxfaqTgaTm7QW6SOY-V84uoC5zmL0kZAaWRZZbZA7imAxeE5PnuHOLR7sCUKVG9o2xZSs5Jh0l09V1BJxkV5dxUzlpOgCOaGxrE.FfNUUFeFTZGOhDqzdqugNH1YyzyGcO_0tq4bC3Brf8E&dib_tag=se&keywords=instant+pot&qid=1714839750&sprefix=insta%2Caps%2C1015&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
# price_pounds = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# price_penny = driver.find_element(by=By.CLASS_NAME, value="a-price-fraction")
# print(f"The price of the item is {price_pounds.text}.{price_penny.text}")

driver.get("https://docs.python.org/3/")
search_bar = driver.find_element(by=By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
print(search_bar.tag_name)
documentation_link = driver.find_element(by=By.XPATH, value='//*[@id="cpython-language-and-version"]/a')
print(documentation_link.text)
by_css_selector = driver.find_element(by=By.CSS_SELECTOR, value="table.contentstable a.biglink")
print(by_css_selector.text)
driver.quit()

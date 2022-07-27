from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():

    driver = "/home/tcotts/chromedriver"
    brave_path = "/usr/bin/brave-browser"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path

    url = 'https://www.livechat.com/typing-speed-test/#/'
    browser = webdriver.Chrome(executable_path=driver, chrome_options=option)
    browser.get(url)

    while True:
        word = browser.find_element(
            by=By.XPATH, value="//span[@data-reactid='.0.1.1.0.0.$=11.0.$=10.1.1.$0']").text

        element = browser.find_element(
            by=By.XPATH, value="//div[@data-reactid='.0.1.1.0.0.$=11.0.$=10.1.0.0.1']")

        element.send_keys(word)
        element.send_keys(Keys.SPACE)


main()

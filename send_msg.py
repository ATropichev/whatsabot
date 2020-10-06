# Simple test sending messages through web.whatsapp.com via selenium
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def read_config_file(config_filename):
    try:
        with open(config_filename, 'r') as f:
            conf = json.load(f)
    except FileNotFoundError:
        conf = {
            'executable_path': input("Enter executable_path: "),
            'firefox_binary': input("Enter firefox_binary: ")
            }
        with open(config_filename, 'w') as f:
            json.dump(conf, f)
    return conf


config = read_config_file('config.json')
browser = webdriver.Firefox(
    executable_path=config['executable_path'],
    firefox_binary=config['firefox_binary']
)
browser.get("https://web.whatsapp.com")
print("Scan QR Code, And then press Enter")
input()

contact = input('Enter name of chat You want to send a message: ')
try:
    # Search for existing chat
    inp_xpath = '//span[@title="{}"]'.format(contact)
    chat = browser.find_element_by_xpath(inp_xpath)
    chat.click()

    message_box = browser.find_element_by_xpath(
        '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(input('Enter Your message: ') + Keys.ENTER)
except NoSuchElementException:
    print(f'\n Chat with {contact} not found!')

browser.quit()

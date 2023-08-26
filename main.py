import requests
import warnings
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():
    # Print introductory information
    print("Copyright (c) 1998-2023")
    print("Brian Oost")
    print("All rights reserved.")
    print("https://brianoost.com/\n")
    
    # Proxy server options
    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxyproxy.com",
        3: "https://www.croxyproxy.rocks",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    # User selects proxy server
    print("Please select a proxy server (1-7). 1 is recommended:")
    proxy_choice = int(input("> "))
    proxy_url = proxy_servers.get(proxy_choice)

    # User inputs Twitch channel name and number of viewers to create
    twitch_username = input("Enter your channel name (e.g., Asmongold): ")
    proxy_count = int(input("Amount of viewers to create: "))
    
    os.system("cls")  # Clear the console screen

    print("Creating virtual viewers now... Please wait.")
  
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    driver_path = 'chromedriver.exe'

    # Set Chrome options for the webdriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)  # Open the selected proxy server in Chrome

    counter = 0  # Counter variable to keep track of the number of viewers created

    for i in range(proxy_count):
        try:
            # Open a new tab in Chrome with the selected proxy server
            driver.execute_script("window.open('" + proxy_url + "')")
            driver.switch_to.window(driver.window_handles[-1])  # Switch to the newly opened tab
            driver.get(proxy_url)  # Load the selected proxy server in the new tab

            text_box = driver.find_element(By.ID, 'url')  # Find the URL input box on the proxy server page
            text_box.send_keys(f'www.twitch.tv/{twitch_username}')  # Enter the Twitch channel URL in the input box
            text_box.send_keys(Keys.RETURN)  # Press Enter to submit the URL

            element_xpath = "//div[@data-a-target='player-overlay-click-handler']"
            element = driver.find_element(By.XPATH, element_xpath)
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            time.sleep(15)

            settings_button = driver.find_element(By.XPATH, "//button[@aria-label='Settings']")
            settings_button.click()

            wait = WebDriverWait(driver, 10)
            quality_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Quality']")))
            quality_option.click()
            time.sleep(15)

            resolution_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), '160p')]")))
            resolution_option.click()

            counter += 1  # Increment the counter for each viewer created
            print(f"Virtual viewer {counter}/{proxy_count} spawned.")  # Print the counter and total count

        except WebDriverException as e:
            print("An error occurred while spawning a virtual viewer (Chrome driver):")
            print(e)
            break

    input('All viewers have been created, press <CTRL+C> to exit this application when done streaming.\n')
    driver.quit()  # Close the Chrome webdriver

if __name__ == '__main__':
    main()

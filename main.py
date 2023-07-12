import requests
import warnings
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

warnings.filterwarnings("ignore", category=DeprecationWarning)

def main():

    print("Copyright (c) 1998-2023")
    print("Brian Oost")
    print("All rights reserved.")
    print("https://brianoost.com/")
    
    print('')

    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxyproxy.com",
        3: "https://www.croxyproxy.rocks",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    print("Please select a proxy server (1-7). 1 is recommended:")  # Selecting proxy server
    
    proxy_choice = int(input("> "))  # User selects a proxy server by entering a number
    proxy_url = proxy_servers.get(proxy_choice)  # Retrieve the URL of the selected proxy server

    twitch_username = input("Enter your channel name (e.g., Asmongold): ")  # User enters their Twitch channel name
    proxy_count = int(input("Amount of viewers to create: "))  # User specifies the number of proxy sites to open
    
    os.system("cls")  # Clear the console screen

    print("Creating virtual viewers now... Please wait.")
  
    chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()  # Set Chrome options for the webdriver
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Exclude certain switches from Chrome
    chrome_options.add_argument('--disable-logging')  # Disable logging
    chrome_options.add_argument('--log-level=3')  # Set log level to 3 (only fatal errors)
    chrome_options.add_argument('--disable-extensions')  # Disable Chrome extensions
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without a graphical interface)
    chrome_options.add_argument("--mute-audio")  # Mute audio
    chrome_options.add_argument('--disable-dev-shm-usage')  # Disable shared memory usage
    chrome_options.binary_location = chrome_path  # Set the Chrome binary location
    driver = webdriver.Chrome(options=chrome_options)  # Create a new Chrome webdriver

    driver.get(proxy_url)  # Open the selected proxy server in Chrome

    counter = 0  # Counter variable to keep track of the number of drivers created

    for i in range(proxy_count):
        try:
            driver.execute_script("window.open('" + proxy_url + "')")  # Open a new tab in Chrome with the selected proxy server
            driver.switch_to.window(driver.window_handles[-1])  # Switch to the newly opened tab
            driver.get(proxy_url)  # Load the selected proxy server in the new tab

            text_box = driver.find_element(By.ID, 'url')  # Find the URL input box on the proxy server page
            text_box.send_keys(f'www.twitch.tv/{twitch_username}')  # Enter the Twitch channel URL in the input box
            text_box.send_keys(Keys.RETURN)  # Press Enter to submit the URL

            counter += 1  # Increment the counter for each driver created
            print(f"Virtual viewer {counter}/{proxy_count} spawned.")  # Print the counter and total count

        except WebDriverException as e:
            print("An error occurred while spawning a virtual viewer (Chrome driver):")
            print(e)
            break  # Exit the loop if an exception occurs

    input('All viewers have been created, press <CTRL+C> to exit this application when done streaming.\n')
    
    driver.quit()  # Close the Chrome webdriver

if __name__ == '__main__':
    main()

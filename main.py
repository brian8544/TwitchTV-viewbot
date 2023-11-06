import requests
import warnings
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import random

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Function to select a random proxy server from the provided dictionary
def selectRandom(proxy_servers):
    return random.choice(list(proxy_servers.values()))

# Main function
def main():
    print("Copyright (c) 1998-2023")
    print("Brian Oost")
    print("All rights reserved.")
    print("https://brianoost.com/")

    print('')

    # Dictionary containing proxy server options
    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxyproxy.com",
        3: "https://www.croxyproxy.rocks",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    # Prompting the user to select a proxy server
    print("Please select a proxy server (1-7). 1 is recommended:")
    proxy_choice = int(input("> "))  # User selects a proxy server by entering a number
    proxy_url = proxy_servers.get(proxy_choice)  # Retrieve the URL of the selected proxy server

    twitch_username = input("Enter your channel name (e.g., Asmongold): ")  # User enters their Twitch channel name
    proxy_count = int(input("Amount of viewers to create: "))  # User specifies the number of proxy sites to open

    os.system("clear")  # Limpar a tela em outros sistemas

    print("Creating virtual viewers now... Please wait.")

    # Configurando o geckodriver (Firefox)
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = True
    firefox_options.log.level = "error"
    firefox_options.add_argument("--mute-audio")
    firefox_options.add_argument('--disable-dev-shm-usage')

    # Caminho para o geckodriver
    geckodriver_path = '/usr/local/bin/geckodriver'

    # Inicialização do driver Firefox
    driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)

    driver.get(proxy_url)  # Abre o servidor proxy selecionado no navegador Firefox

    counter = 0  # Variável contador para acompanhar o número de drivers criados

    # Loop para criar visualizadores virtuais usando diferentes servidores proxy
    for i in range(proxy_count):
        try:
            random_proxy_url = selectRandom(proxy_servers)  # Seleciona um servidor proxy aleatório para esta guia
            driver.execute_script("window.open('" + random_proxy_url + "')")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(random_proxy_url)

            text_box = driver.find_element(By.ID, 'url')
            text_box.send_keys(f'www.twitch.tv/{twitch_username}')
            text_box.send_keys(Keys.RETURN)

            # Aguarda a presença do elemento antes de prosseguir
            element_xpath = "//div[@data-a-target='player-overlay-click-handler']"
            wait = WebDriverWait(driver, 30)  # Ajuste o tempo limite conforme necessário
            element = wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))

            # Continue com suas ações no elemento
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()

            time.sleep(15)  # Se você precisar esperar após interagir com o elemento

            counter += 1  # Incrementa o contador para cada driver criado
            print(f"Virtual viewer {counter}/{proxy_count} spawned.")  # Imprime o contador e o total

        except WebDriverException as e:
            print("An error occurred while spawning a virtual viewer (Firefox driver):")
            print(e)
            break

    input('All viewers have been created, press <CTRL+C> to exit this application when done streaming.\n')

    driver.quit()  # Fecha o driver do Firefox

if __name__ == '__main__':
    main()

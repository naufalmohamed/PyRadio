# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import song_check


def create_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(
        chrome_type=ChromeType.BRAVE).install()), chrome_options=chrome_options)
    return driver


def driver_cunc(driver):
    driver.get(
        "file:///C:/Users/Naufal/Documents/Python Scripts/PyRadio/radio.html")
    video_player = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "video"))
    )
    video_player.click()
    # time.sleep(10)
    # google = driver.find_element(By.ID, "changeVideoButton")
    # google.click()
    # time.sleep(10)


def switch_station(driver):
    print('Switchong Station')
    change_btn = driver.find_element(By.ID, "changeVideoButton")
    change_btn.click()
    video_player = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "video"))
    )
    video_player.click()


driver = create_driver()
driver_cunc(driver)
time.sleep(2)

while True:
    song = song_check.song_validate()
    if  not song:
        switch_station(driver)
        time.sleep(5)
    else:
        print(song)
        pass

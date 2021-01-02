#!/usr/bin/env python3

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import schedule


def botiomack():
    for x in range( 1000):

        print("Opening Browser...")

        driver = webdriver.Chrome("/Users/User/Downloads/chromedriver/chromedriver.exe")

        print("Requesting BR's page...")

        driver.get("https://audiomack.com/highboya/song/blown")

        print("Trying to play song..")

        try:
            btn1 = driver.find_element_by_xpath(
                '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/ul/li/button[1]')

            driver.execute_script("arguments[0].click();", btn1)

            try:
                paused = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.CLASS_NAME, "play-button--paused"))
                )

                if paused:
                    driver.find_element_by_xpath(
                        '//*[@id="react-view"]/div[7]/div/div[1]/button[2]').click()
            except:
                pass

            playing = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "play-button--playing"))
            )

            print("Playing  song...")

            sleep(2)

            print("Done with ", format(x+1))
        except:
            print("Couldn't play song")
        driver.quit()
    print("Done ✅")


botiomack()

# schedule.every().day.do(botiomack)

# while True:
#     schedule.botiomackrun_pending()
#     sleep(1)

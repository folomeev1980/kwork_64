from datetime import datetime
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver


def point(s):
    return s.replace(".", ",")


while True:
    try:

        url = "https://yandex.ru/internet/"

        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x935")
        driver = webdriver.Chrome("chromedriver.exe", options=options)
        driver.get(url)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div/button").click()
        time.sleep(60)
        response = driver.page_source
        soup = BeautifulSoup(response, "lxml")
        soup = soup.findAll("div", class_="speed-progress-bar__value")
        upload = soup[0].text.strip().split("=")[0].strip().split(" ")
        download = soup[1].text.strip().split("=")[0].strip().split(
            " ")
        tm = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        driver.close()
        #print(upload, download)

        with open('speed_test_home_new.csv', mode='a') as speed_test:
            speed_test = csv.writer(speed_test, delimiter=';', lineterminator='\n')
            row = (tm, point(upload[0]), point(upload[1]), "   ", point(download[0]), point(download[1]))
            print(row)
            speed_test.writerow(row)
    except Exception as e:
        with open('speed_test_home_new.csv', mode='a') as speed_test:
            speed_test = csv.writer(speed_test, delimiter=';', lineterminator='\n')
            row = (tm, str(e))
            print(row)
            speed_test.writerow(row)
        driver.close()
    finally:
        time.sleep(300)

from dataclasses import replace
from tkinter import Variable
from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.by import By
from datetime import date, datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

todaydate = datetime.strftime(datetime.now() - timedelta(2), "%Y%m%d")
carnumbers = [["77-EJ-469"], ["99-MU-917"]]
chrome2 = webdriver.Chrome(
    executable_path=os.environ.get("CHROMEDRIVER PATH"), chrome_options=chrome_options
)

url_gps = "https://hosting.wialon.com/"
chrome2.get(url_gps)
time.sleep(3)
chrome2.find_element_by_id("user").send_keys("Abdulali")
chrome2.find_element_by_id("passw").send_keys("mosa22")
chrome2.find_element_by_id("submit").click()
time.sleep(30)
currentYear = str(datetime.strftime(datetime.now() - timedelta(1), "%Y"))
currentMonth = str(datetime.strftime(datetime.now() - timedelta(1), "%m"))
currentDay = str(datetime.strftime(datetime.now() - timedelta(2), "%d"))

if currentMonth == "01":
    currentMonth = "January"
elif currentMonth == "02":
    currentMonth = "February"
elif currentMonth == "03":
    currentMonth = "March"
elif currentMonth == "04":
    currentMonth = "April"
elif currentMonth == "05":
    currentMonth = "May"
elif currentMonth == "06":
    currentMonth = "June"
elif currentMonth == "07":
    currentMonth = "July"
elif currentMonth == "08":
    currentMonth = "August"
elif currentMonth == "09":
    currentMonth = "September"
elif currentMonth == "10":
    currentMonth = "October"
elif currentMonth == "11":
    currentMonth = "November"
elif currentMonth == "12":
    currentMonth = "December"

zerozero = "00:00"
twentrythree59 = "23:59"

data_gps_1 = currentDay + " " + currentMonth + " " + currentYear + " " + zerozero
data_gps_2 = currentDay + " " + currentMonth + " " + currentYear + " " + twentrythree59
f2 = open("/Users/User/Desktop/vibepark/" + todaydate + "-gps" + ".txt", "w")
chrome2.find_element_by_id("time_from_routes_add_filter_time").clear()
time.sleep(1)
chrome2.find_element_by_id("time_from_routes_add_filter_time").send_keys(data_gps_1)
time.sleep(1)
chrome2.find_element_by_id("time_to_routes_add_filter_time").clear()
time.sleep(1)
chrome2.find_element_by_id("time_to_routes_add_filter_time").send_keys(data_gps_2)

# chrome2.find_element_by_xpath("/html/body/div[11]/div/div/div[2]/div[3]").click()
for a in carnumbers:
    time.sleep(2)
    chrome2.find_element_by_id("routes_add_unit").click()
    time.sleep(1)
    chrome2.find_element_by_id("routes_add_unit").send_keys(a)
    time.sleep(1)
    chrome2.find_element(By.CSS_SELECTOR, ".vtblist ul li").click()
    time.sleep(1)
    chrome2.find_element_by_id("routes_add_btn").click()
    time.sleep(4)

    try:
        getkm = chrome2.find_element(
            By.XPATH,
            "/html/body/div[12]/div/div/div[7]/div/div[2]/div/div[2]/div/div[3]/div[2]",
        ).text
        getkm = getkm.replace(" km", "")
        f2.write(a[0])
        f2.write(":")
        f2.write(getkm)
        f2.write(",")
        chrome2.find_element(
            By.XPATH,
            "/html/body/div[12]/div/div/div[7]/div/div[2]/div/div[1]/div[4]/button",
        ).click()
        time.sleep(3)
    except NoSuchElementException:
        f2.write(a[0])
        f2.write(":")
        f2.write("0")
        f2.write(",")
        time.sleep(3)
f2.close()
chrome2.delete_all_cookies()
chrome2.quit()

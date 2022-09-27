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

f2.close()
chrome2.delete_all_cookies()
chrome2.quit()

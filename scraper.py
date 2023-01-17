import time
from dateutil.tz import tzlocal
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller


PATH = r"C:\Users\Austin\OneDrive\chromedriver_win32\chromedriver.exe"
WINDOW_SIZE ="1920,1080"

options = webdriver.ChromeOptions()

chromedriver_autoinstaller.install()
options.add_argument("--headless")
# options.add_argument("--window-size=%s" % WINDOW_SIZE)


driver = webdriver.Chrome(service = Service(PATH))

url = "https://jobs.lever.co/vannevarlabs-2"

driver.get(url)

# Vannevar_Labs_Job_Add_Path = "/html/body/div[2]/div/div/div/div[2]/div[3]/div[4]/a/h5"
# link = driver.find_element("xpath", Vannevar_Labs_Job_Add_Path)
# print(link.text)

def scrapeJobs():
    while(True):
        today = date.today()
        now = datetime.now()
        tz = datetime.now(tzlocal()).tzname()
        
        print("")
        current_date = today.strftime("%B %d, %Y")
        current_time = now.strftime("%H:%M:%S")
        print(f"Job Listings Found On: {current_date} At: {current_time} {tz}")
        print("")


        titles = driver.find_elements(By.CSS_SELECTOR, "h5")
        for x in titles:
            print(x.text)
        return False
scrapeJobs()








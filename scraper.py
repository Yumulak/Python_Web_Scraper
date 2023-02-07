import time
from dateutil.tz import tzlocal
from datetime import datetime, date
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import pandas as pd




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

titles = []
basicInfo = []
categories = []
subCategories = []


# def scrapeJobs():
#     while(True):
today = date.today()
now = datetime.now()
tz = datetime.now(tzlocal()).tzname()

print("")
current_date = today.strftime("%B %d, %Y")
current_time = now.strftime("%H:%M:%S")
print(f"Job Listings Found On: {current_date} At: {current_time} {tz}")
print("")

# postings = driver.find_elements(By.CLASS_NAME, "postings-wrapper")
# titles = driver.find_elements(By.CSS_SELECTOR, "h5")
soup = BeautifulSoup(driver.page_source, "html.parser")
for postings in soup.findAll("div", href = True, attrs = {"class": "posting-wrapper"}):
    title = postings.find("h5")
    info = postings.find("div", attrs = {"class": "posting-categories"})
    category = postings.find("div", attrs = {"class": "large-category-header"})
    subCategory = postings.find("div", attrs = {"class": "posting-category-title large-category-label"})

    titles.append(title.text)
    basicInfo.append(info.text)
    categories.append(category.text)
    subCategories.append(subCategory.text)

df = pd.DataFrame({"Title": titles, "Basic Info": basicInfo, "Category": categories, "Sub-Category": subCategories})
df.to_csv("Vannevar_Labs_Job_Listings.csv", index = False, encoding = "utf-8")

        # for x in postings:
        #     print(x.text)
#         return Falseftt
# scrapeJobs()








import requests
from bs4 import BeautifulSoup
import pandas as pd
import smtplib

r = requests.get("https://jobs.lever.co/vannevarlabs-2")

soup = BeautifulSoup(r.content, "html.parser")

s = soup.find("div", class_="postings-wrapper")

content = s.find_all("h5")

titles = []
links = []

for c in content:
    titles.append(c.text)
    # print(c.text)

for link in s.find_all("a"):
    links.append(link.get("href"))
    # print(link.get("href"))

for listings in zip(titles, links):
    print(listings)

d = {"Title": titles, "Link": links}
df = pd.DataFrame.from_dict(d, orient = "index")
df = df.transpose()
df.to_csv("Vannevar_Labs_Job_Listings.csv", index = False, encoding = "utf-8")

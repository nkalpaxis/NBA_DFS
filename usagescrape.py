from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import csv

# scraping is done with FireFox

# set webdriver.FireFox to driver variable
# set executable path to geckodriver.eve location ex; C:/...

driver = webdriver.Firefox(executable_path="")

driver.get("https://www.nba.com/stats/players/usage/?sort=USG_PCT&dir=-1")

time.sleep(3)

select_button = driver.find_element_by_xpath(
    "/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select"
)
select_button.click()

list_all = driver.find_element_by_xpath(
    "/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]"
)
list_all.click()

table = driver.find_element_by_xpath(
    "/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody"
)

players = []
usage = []

for name in table.find_elements_by_class_name("first"):
    players.append(name.text)

for v in table.find_elements_by_class_name("sorted"):
    usage.append(v.text)

usages = {"Player": players, "Usage": usage}

usage_df = pd.DataFrame(usages, columns=["Player", "Usage"])

usage_df["Player"] = usage_df["Player"].str.replace("'", "")
usage_df["Player"] = usage_df["Player"].str.replace(".", "")


usage_df.to_csv("usage.csv", index=False)

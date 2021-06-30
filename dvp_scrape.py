from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import csv

# scraping is done with FireFox

# set webdriver.FireFox to driver variable
# set executable path to geckodriver.eve location ex; C:/...

driver = webdriver.Firefox(executable_path="")

driver.get(
    "https://www.fantasypros.com/daily-fantasy/nba/fanduel-defense-vs-position.php"
)

select_button = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/nav/nav/div[2]/div[2]/div/select"
)
select_button.click()
# last_15 = driver.find_element_by_xpath(
#     "/html/body/div[2]/div[5]/div/nav/nav/div[2]/div[2]/div/select/option[3]"
# )
# last_15.click()

last_7 = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/nav/nav/div[2]/div[2]/div/select/option[2]"
)
last_7.click()

pg = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/div/div/div[4]/div[1]/ul/li[2]/a"
)
pg.click()

table = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/div/div/div[6]/table/tbody"
)


# l = len(table.find_elements_by_xpath(".//tr"))
# print(l)

trs = []
for tr in table.find_elements_by_xpath(".//tr"):
    if tr.get_attribute("style") == "display: none;":
        continue
    trs.append(tr)

point_guards = []
for tr in trs:
    tds = tr.find_elements_by_xpath(".//td")
    point_guard = {
        "team_name": tds[0].find_element_by_xpath(".//span").text,
        "fd_points": tds[-1].find_element_by_xpath(".//b").text,
    }
    point_guards.append(point_guard)

# print("filtered len", len(trs))
# print(point_guards)


sg = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/div/div/div[4]/div[1]/ul/li[3]/a"
)
sg.click()

trs = []
for tr in table.find_elements_by_xpath(".//tr"):
    if tr.get_attribute("style") == "display: none;":
        continue
    trs.append(tr)

shooting_guards = []
for tr in trs:
    tds = tr.find_elements_by_xpath(".//td")
    shooting_guard = {
        "team_name": tds[0].find_element_by_xpath(".//span").text,
        "fd_points": tds[-1].find_element_by_xpath(".//b").text,
    }
    shooting_guards.append(shooting_guard)

# print(shooting_guards)

sf = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/div/div/div[4]/div[1]/ul/li[4]/a"
)
sf.click()

trs = []
for tr in table.find_elements_by_xpath(".//tr"):
    if tr.get_attribute("style") == "display: none;":
        continue
    trs.append(tr)

small_forwards = []
for tr in trs:
    tds = tr.find_elements_by_xpath(".//td")
    small_forward = {
        "team_name": tds[0].find_element_by_xpath(".//span").text,
        "fd_points": tds[-1].find_element_by_xpath(".//b").text,
    }
    small_forwards.append(small_forward)

# print(small_forwards)

pf = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/div/div/div[4]/div[1]/ul/li[5]/a"
)
pf.click()

trs = []
for tr in table.find_elements_by_xpath(".//tr"):
    if tr.get_attribute("style") == "display: none;":
        continue
    trs.append(tr)

power_forwards = []
for tr in trs:
    tds = tr.find_elements_by_xpath(".//td")
    power_forward = {
        "team_name": tds[0].find_element_by_xpath(".//span").text,
        "fd_points": tds[-1].find_element_by_xpath(".//b").text,
    }
    power_forwards.append(power_forward)

# print(power_forwards)

c = driver.find_element_by_xpath(
    "/html/body/div[2]/div[5]/div/div/div/div[4]/div[1]/ul/li[6]/a"
)
c.click()

trs = []
for tr in table.find_elements_by_xpath(".//tr"):
    if tr.get_attribute("style") == "display: none;":
        continue
    trs.append(tr)

centers = []
for tr in trs:
    tds = tr.find_elements_by_xpath(".//td")
    center = {
        "team_name": tds[0].find_element_by_xpath(".//span").text,
        "fd_points": tds[-1].find_element_by_xpath(".//b").text,
    }
    centers.append(center)

# print(centers)

pg_df = (
    pd.DataFrame(point_guards)
    .rename(columns={"fd_points": "PG"})
    .set_index("team_name")
)
sg_df = (
    pd.DataFrame(shooting_guards)
    .rename(columns={"fd_points": "SG"})
    .set_index("team_name")
)
sf_df = (
    pd.DataFrame(small_forwards)
    .rename(columns={"fd_points": "SF"})
    .set_index("team_name")
)
pf_df = (
    pd.DataFrame(power_forwards)
    .rename(columns={"fd_points": "PF"})
    .set_index("team_name")
)
c_df = pd.DataFrame(centers).rename(columns={"fd_points": "C"}).set_index("team_name")

master_df = pg_df.join(sg_df).join(sf_df).join(pf_df).join(c_df)

master_df.to_csv("dvp.csv", index=True)

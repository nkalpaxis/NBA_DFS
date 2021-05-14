from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd 
import csv 

# scraping is done with FireFox

# set webdriver.FireFox to driver variable
# set executable path to geckodriver.exe location ex; C:/../..
  
driver = webdriver.Firefox(executable_path="")

# use driver.get to open webpage, link below will connect to numberfire nba projections for the night

driver.get("https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections")

# we need to set selenium to sleep for 4 seconds to give numberfire time to prompt us to login
# without time.sleep() code editor will tell us it cannot locate the login element

time.sleep(4)

# numberfire will prompt you to login in order to see projections
# various login options avaiable such as numberfire account, gmail, fanduel

# the first pop up will be to sign up, we want selenium to first select the Click here to login
# link below the sign up options
login1 = driver.find_element_by_xpath(
    "/html/body/main/div[2]/div[4]/div/span[2]/a/strong"
)
login1.click()

# the following code will be logging in through fanduel if you wish to use another option right click the option 
# inspect the element, in the inspection tool right click the element and copy its xpath

# locate fanduel login button through xpath
fd_login = driver.find_element_by_xpath("/html/body/div[4]/div/ul/li[1]/a")

# use .click() function to have selenium click on the login button
fd_login.click()


# locate email field through xpath 
email_field = driver.find_element_by_xpath('//*[@id="forms.login.email"]')
email_field.click()

# next use .send_keys to have selenium enter your login information
email_field.send_keys('replace this string with your email@whatever.com')
email_field.send_keys(Keys.RETURN) # this mimics the enter key

# next locate password field through xpath
password_ = driver.find_element_by_xpath('//*[@id="forms.login.password"]')
password_.click()

# next use .send_keys to have selenium enter your password
password_.send_keys('replace this string with your password')
password_.send_keys(Keys.RETURN)

# after selenium enters your login/password it will redirect your browsers back to numberfire

# we have to have selenium sleep again so we can locate the correct elements
# 3 to 4 seconds should suffice 
time.sleep(3)

# locate main table on numberfire projections page 
table = driver.find_element_by_xpath(
    "/html/body/main/div[2]/div[2]/section/div[4]/div[2]/table"
)

# we just want players names and their projections from the website
# create two empty lists; players & proj

players = []
proj = []

# loop through the table and locate players names which are stored in class='full' by using table.find_elements_by_class_name
# make sure to use find_elements not find_element since there is multiple players
# when appending to the players list make sure to use .text after your iterator 

for player in table.find_elements_by_class_name("full"):
    players.append(player.text)

# next we loop through the table again but for projections this time which are stored in class = 'fp.active'
# make sure to use find_elements not find_element since there is multiple players
# when appending to the proj list make sure to use .text after your iterator 

for projections in table.find_elements_by_class_name("fp.active"):
    proj.append(projections.text)

# next we'll create a dictionary named numfire which stores players list to Player and proj list to Proj

numfire = {"Player": players, "Proj": proj} 

# lastly we will convert numfire dictionary to a pandas DataFrame and then write the DataFrame to a csv file which we can
# import to google sheets or excel 

# make sure the columns=[] matches dictionary Keys in spelling or it will raise errors 
df = pd.DataFrame(numfire, columns=["Player", "Proj"])

# you can replace "projections.csv" with whatever you want to call your projections csv file 

df.to_csv("projections.csv", index=False)


# the following extra code is included if you wish to take periods and apostrophes out of players names
# some websites spell players names differently and I prefer not to have them included
# code below will change names such as C.J. and De'Aron to
# CJ, DeAron

# read back in our newely created csv
num_proj = pd.read_csv("projections.csv")

# make sure the column name "Player" is spelled the same as it is in your csv file
num_proj["Player"] = num_proj["Player"].str.replace("'", "")
num_proj["Player"] = num_proj["Player"].str.replace(".", "")

# re-write csv with cleaned names
num_proj.to_csv("projections.csv", index=False)
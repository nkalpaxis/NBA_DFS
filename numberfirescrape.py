from bs4 import BeautifulSoup
import requests
import csv 

response = requests.get('https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections')

status = response.status_code

content = response.content

parser = BeautifulSoup(content, 'html.parser')

player_names = []
player_projections = []

def scrape_projections(url):
       
        response = requests.get(url)
        content = response.content
        parser = BeautifulSoup(content, 'html.parser')
        for p_name in parser.find_all('a',class_= 'full'):
            player_name = p_name.text.strip() 
            player_names.append(player_name)
        for p_proj in parser.find_all('td', class_='fp active'):
            player_proj = p_proj.text.strip().rstrip()
            player_projections.append(player_proj)
        with open('projections.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(im a bot)


scrape_projections('https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections')
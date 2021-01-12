from bs4 import BeautifulSoup

import requests

import csv 



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

            player_proj = p_proj.text.strip()

            player_projections.append(player_proj)

        if len(player_names) != len(player_projections):

            print(f'number of player names ({len(player_names)}) does not equal ' +

                  f'number of player projections ({len(player_projections)})')

            return

        with open('projections.csv', 'w', newline='') as csv_file:

            writer = csv.writer(csv_file)

            for i in range(len(player_names)):

                writer.writerow([player_names[i], player_projections[i]])



scrape_projections('https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections')
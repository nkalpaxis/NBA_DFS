from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd 


def scrape_stats(url):

    response = requests.get(url)
    
    content = response.content
    
    parser = BeautifulSoup(content, 'html.parser')
    
    parser.find_all('tr', limit=2)
    
    headers = [th.getText() for th in parser.find_all('tr', limit=2)[0].find_all('th')]
    
    headers = headers[1:]
    
    rows = parser.find_all('tr')[1:]
    
    player_stats = [[td.getText() for td in rows[v].find_all('td')]
                    for v in range(len(rows))]
    
    stats = pd.DataFrame(player_stats, columns = headers)
    
    stats.to_csv('bballreference.csv')

scrape_stats('https://www.basketball-reference.com/leagues/NBA_2021_totals.html')


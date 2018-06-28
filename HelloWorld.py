import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.imdb.com/chart/top?ref_=nv_mv_250_6')
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('tr')
results = results[1:-2]
records = []

for result in results:
    movie = result.find('td', attrs={'class': 'titleColumn'}).contents[1].text
    rating = result.find('td', attrs={'class': 'ratingColumn imdbRating'}).contents[1].text
    records.append((movie,rating))

df = pd.DataFrame(records, columns=['Movie', 'Title'])
df.to_csv('IMDBTopMovie.csv', index=True, encoding='utf-8')

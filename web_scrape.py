import requests

from bs4 import BeautifulSoup

with open("aita.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

tag_visible = ['p', 'li']

title = soup.find_all('shreddit-title')[0]['title'].split(":")[0].strip()

post = soup.find_all('div', id=lambda x: x and 'post' in x)[0].find_all('p')

pars = []
for par in post:
    pars.append(par.text)

fullPost = '\n'.join(pars)
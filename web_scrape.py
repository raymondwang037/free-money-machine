import requests

from bs4 import BeautifulSoup

with open("aita.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

tag_visible = ['p', 'li']

post = soup.find_all('div', id=lambda x: x and 'post' in x)[0].find_all('p')

pars = []
for par in post:
    pars.append(par.text)

print('\n'.join(pars))
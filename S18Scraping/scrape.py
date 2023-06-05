import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')

subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

all_links = links + links2
all_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse= True)

def create_custom_hn(links, subtext):
	hn = []
	for i, item in enumerate(links):
		title = links[i].getText()
		href = links[i].get('href', None)
		vote = subtext[i].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(all_links, all_subtext))

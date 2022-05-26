# Bandcamp Webscraper v1.2

import requests
from bs4 import BeautifulSoup

# send request for webpage HTML
wisdomteeth_response = requests.get('https://wisdomteethuk.bandcamp.com/')
wisdomteeth = wisdomteeth_response.content

# convert HTML to BeautifulSoup object
wisdomteeth_soup = BeautifulSoup(wisdomteeth, "html.parser")

# Find all elements with class=title and add to a list
title_list = []
artist_list = []
for release in wisdomteeth_soup.find_all(attrs={'class':'title'}):
    # Split up elements into a list
    release_text = release.get_text('|').split('|')
    # Sometimes only has a track title so specify no artist
    # Add to title and artist lists
    if len(release_text) > 1:
        title_list.append(release_text[0])
        artist_list.append(release_text[1])
    else:
        title_list.append((release_text[0]))
        artist_list.append("none")

#print(title_list)
#print(artist_list)

#while("" in title_list):
#    title_list.remove("")
#while ("" in artist _list):
#    artist_list.remove("")

# Use strip to remove spaces and add to new list
strip_title_list = []
for el in title_list:
    strip_title_list.append(el.strip())
strip_artist_list = []
for ele in artist_list:
    strip_artist_list.append(ele.strip())

# Remove unwanted data at end of list
strip_title_list = strip_title_list[:-4]
strip_artist_list = strip_artist_list[:-4]

# Find links to release pages and add to list
links = []
for link in wisdomteeth_soup.findAll('a'):
    links.append(link.get('href'))

# Remove unwanted data at end of list
links = links[42:-25]

print(strip_title_list)
print(strip_artist_list)
print(links)

print(len(strip_title_list))
print(len(strip_artist_list))
print(len(links))




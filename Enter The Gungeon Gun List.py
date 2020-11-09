#Testing Web Scraping the ETG wiki to get a list of guns and some information about them
#Made by Killer Kat 11/NOV/2020
#End goal would be our own table with at least names, special and synergies.

import requests
from bs4 import BeautifulSoup

#This sends a GET request and stores it 
page_html = requests.get("https://enterthegungeon.gamepedia.com/Guns").text
#This parses the HTML
page_soup = BeautifulSoup(page_html, "lxml")

My_table = page_soup.find('table') #This works because there is only one table but it would not scale.
#print(My_table)
links = My_table.findAll("a") #finding all the hyperlinks so we can extract the names of the guns.

Guns = []

for link in links:
    Guns.append(link.get("title"))

Guns = list(filter(None, Guns)) #Removes NULL values from our list of guns.
#Because this particular table is full of links to non gun pages we need to filter our results
#There should be 243 Guns in the list as there are currrently 243 guns in game.
while 'Jammed' in Guns: Guns.remove('Jammed')
while 'Secret Rooms' in Guns: Guns.remove('Secret Rooms')
while "N/A" in Guns: Guns.remove("N/A")
while 'Quality' in Guns: Guns.remove('Quality')
while 'Curse' in Guns: Guns.remove('Curse')
while 'Coolness' in Guns: Guns.remove('Coolness')
while 'Blanks' in Guns: Guns.remove('Blanks')
Guns.remove("Beadie")
Guns.remove("Shotgun Kin")
#Filter out the Heros
Guns.remove('The Hunter')
Guns.remove('The Marine')
Guns.remove('The Pilot')
Guns.remove('The Convict')
Guns.remove('The Cultist')
Guns.remove('The Robot')
Guns.remove('The Gunslinger')
Guns.remove('The Bullet')
#Filter out status effects
while 'Stun' in Guns: Guns.remove('Stun')
while 'Charm' in Guns: Guns.remove('Charm')
while 'Burn' in Guns: Guns.remove('Burn')
while 'Poison' in Guns: Guns.remove('Poison')
while 'Slow' in Guns: Guns.remove('Slow')
while 'Freeze' in Guns: Guns.remove('Freeze')
while 'Fear' in Guns: Guns.remove('Fear')

print(Guns)
print(len(Guns))


input("end?")
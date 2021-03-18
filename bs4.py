# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:54:28 2021

@author: Palmtree
"""


import requests 
from bs4 import BeautifulSoup
import json


#URL = "https://www.armadarealestate.com/inventory.aspx"
URL = "https://buildout.com/plugins/3e0f3893dc334368bb1ee6274ad5fd7b546414e9/www.armadarealestate.com/inventory/?pluginId=0&iframe=true&embedded=true&cacheSearch=true&=undefined"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, "html.parser") 
#print(soup.prettify()) 
table = soup.find_all(class_='col-md-9 col-sm-8')
print(table)
lists=[]
print(len(table))
for line in table:
    #print(line)
    print("\n")


for row in table.findAll('div', attrs = {'class':'row list-item border-bottom hidden-xs clickable'}): 
    listing = {} 
    listing['image'] = row.div.div.img['src'] 
    lists.append(listing) 

'''
data= {}

filename = 'test.json'
with open(filename, 'w', newline='') as f: 
    json.dump(table,f) 
'''  









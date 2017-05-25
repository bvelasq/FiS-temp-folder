# -*- coding: utf-8 -*-
"""
Created on Thu May 25 12:13:24 2017

@author: Brett Velasquez
"""
booka = {}
booka['Tomfoolery'] = {
    'name': 'Tomfoolery',
    'address': '1 red street, NY',
    'phone': 98989898
}
booka['Merasmus'] = {
    'name': 'Merasmus',
    'address': '1800 Wizard Street, SC',
    'phone': 98995888
}
# so this code will create a file with the title booka if one does not exist
# at the time
import json
json.dumps(booka)
with open('C:\\Users\\Brett\\Desktop\\booka.txt','w') as f: # including the 'w' at the end makes it write to a file
    f.write(s)
    
f = open('C:\\Users\\Brett\\Desktop\\booka.txt','r')# the 'r' means reading the file
s = f.read() # the file will be read into the variable s
import json 
booka = json.loads(s)
print(booka['Merasmus']) 
# so interestingly enough the booka file
# was originally written with the names 'bob' and 'tom' on the computer I am
# using. I then wrote different names in the code which creates the file but 
# the code running here never overwrites the old code, so the file 
# booka only ever returns for the names bob and tom
print(booka['Tomfoolery']['address'])
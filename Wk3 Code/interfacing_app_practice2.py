import json

linestring = open('interface_practice','r').read()
							#print linestring
formated = json.loads(linestring)
							#formated is, in fact, a list
joined = ''.join(map(str, formated))
							#now it's all a string
							#now we get rid of the numbers and the brackets and the commas and the u
import re
import string

trans = string.maketrans(',]', '<>') # creating a transformation table to replace
ooza = joined# joining the thing so I can do translations
j_edit1 = ooza.translate(trans)
j_edit2 = j_edit1.translate(None,"[")
j_edit3 = j_edit2.translate(None, 'u')
j_edit4 = j_edit3.replace("'", " ")
zulu = j_edit4.translate(trans)
f_joined = re.sub('<[^>]+>', '', zulu)

list_ensemble = f_joined.split() #list of ensemble IDs we want
s = ",".join(list_ensemble).replace(",", " ") # getting rid of commas to use with ID finder

tip = open('Gene stable ID Transcript stable ID HGNC symbol EntrezGene transcript name ID.txt', 'r').read()
#getting the entrez IDs out of file and creating a proper lsit with them
ntip = tip.split()


zed = [i for i, x in enumerate(ntip) if x in list_ensemble]
new_zed = [x + 2 for x in zed] #retrieveing the positinos of every hgnc ID we 
#want

hgnc_list = list( ntip[i] for i in new_zed)
hgnc_nc = list(set(hgnc_list)) # the list of said HGNC IDs

# now I just need the lines from the transformation table that house the IDs 
#from the list
mylist = []
with open('HI-II-14.tsv') as f:
        for line in f:
            if any(x in line for x in hgnc_nc):
                mylist.append(line)
thefile = open('reactions_export.txt', 'w')
for item in mylist:
    thefile.write("%s\n" % item)

#with open('HI-II-14.tsv', 'r'):
 #   for line in file:
  #      result =  any(s in file for s in hgnc_nc)
   #     print result

import json

with open("docked_head_pdx_test.txt") as f:
	gene_name = zip(*[line.split(".") for line in f])[0]
	

list_g = gene_name
#print list_g
list_n = [i.split('\t', 1)[0] for i in list_g]
#list_n is a list containing all the genes that are present within the PDX 
#and in the offical format ID to boot(the one with letters that works witht the
#interaction DB)
print list_n

mylist = []
with open('HI-II-14.tsv') as f:
	for line in f:
		if any(x in line for x in list_n):
			mylist.append(line)
thefile = open('reactions_export2.txt', 'w')
for item in mylist:
	thefile.write("%s\n" % item)

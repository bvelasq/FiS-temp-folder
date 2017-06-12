#SO
#This little bit of code is going to read through the genenameDB.txt I got from 
#The HGNC gene name list DB and is going to delete every line that has the
#word 'withdrawn' or 'Withdrawn' in it so I don't have to deal with that shit 
#when reading through it with my other code.


with open('genenamesDB.txt') as f, open('genenamesDB_rip.txt', "w") as f2:
	for x in f:
		if 'withdrawn' not in x:
			f2.write(x)


# all credit to 
#'https://stackoverflow.com/questions/11963728/how-do-i-delete-a-line-that-contains-a-certain-string'



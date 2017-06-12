import json
#so the goal here is to use one of the lists that I downloaded from 
#ICGC, extract what genes were present and how many of them appeared 
#at one time, and then print out the names of those that are present 
#beneath a certain threshold so that I only find 'rare' or 
#'significantly mutated' genes from the NCBI database[can i even make 
#requests of this kind to the NCBI database? will find out later]

#so import the file for reading

file_object = open("06a9c4ce-55a4-4dd7-967c-d72e8da7a89c.htseq.counts","r")

#NOW read out the shit in that file
with open("06a9c4ce-55a4-4dd7-967c-d72e8da7a89c.htseq.counts") as f:
	for line in f:
		numbers_str = line.split()
		#print numbers_str

#so the last 4 lines of the list have data that may mess with code
#that simply wants to edit strings of certain format that come before it
#so we have to get rid of those last 4 lines
#del numbers_str[-1]
#so doing^ will delete the number after the last string value, not the last line as a whole
#HMMMM
#I still haven't gotten rid of those lines yet
#this may be an issue
#FOR LATER, THAT IS
#hhhhhhHHHHHHHHHHHHHHAAAAAAAAAAAAAAAAA


with open("06a9c4ce-55a4-4dd7-967c-d72e8da7a89c.htseq.counts") as f:
	#also going to split off the parts of the gene name past the "."(the decimal bits)
	#atleast until I know what they're for
	gene_name = zip(*[line.split(".") for line in f])[0]
	gene_name = list(gene_name)

with open("06a9c4ce-55a4-4dd7-967c-d72e8da7a89c.htseq.counts") as f:
	num_appearances = zip(*[line.split() for line in f])[1]
	num_appearances = list(num_appearances)

num_appearances = map(int, num_appearances)

#great so I have my two lists now
#NOW I should remove the lines that have appearance values of either 0 or above
#some arbitrary number
#sssaaaaaayyyy... 200
#yup so if a gene appears either 0 or more than 200 times it will be deleted
#SO for the sake of practicing with a small data set I'm limiting the increment to be
# 175 to 200
#Yossi wanted 'most accurate' so I've decided that means 'largest amount of appearances', cuz if there's
#a hug amount of them then it has to be accurate info on the gene, riiiiiiiiiiight?
unfiltered = zip(gene_name, num_appearances)

high_filtered = [(x,y) for x, y in unfiltered if y <= 50000]

#hmmm zero's ain't disppearin'....

#total_filtered = [(x, y) for x, y in high_filtered if y != 0]
total_filtered = [(x, y) for x, y in high_filtered if y >= 10000]
#PRAISE BE, I am simply retarded
#and hey waddya know the filtering got rid of the last 4 lines for me
#HMMMMMMMmm
#NOW THEN to query libraries for the gene info

#so uh, gonna write the list I made to a new file
with open("interface_practice","w") as out_f:
	json.dump(total_filtered, out_f)

#so now I have a file with a list of names and ID's and whatnot 
#so just uh, search the file for every gene name I have that's within the range I want
#and bam
#genes
#oooooooh boooooooooooooy

#read the lists gene_names section, search text file for the name, read the line that the name was found in and find the name of the protein and make a list of those
#	"interface_practice"(the list) >>> DB >>> interactome DB 

#did I really need to make an output document for this?
#probably not
#but why not right?
#ooooh but how would I have cut out the 0's? Probs coulda done that w/o it
#probs right
#let's do this in another code

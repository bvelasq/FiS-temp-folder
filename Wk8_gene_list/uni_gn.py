#need to do the thing of combining lists and making it so no repeating things 
#are in a list more than once

list1 = open('Common_Genes.txt', 'r').read().splitlines()
list2 = open('Driver-Genes.txt', 'r').read().splitlines()
list3 = open('Unique_Genes.txt', 'r').read().splitlines() 
list4 = open('Gene_TCGA.txt', 'r').read().splitlines()
list5 = open('leukDB_rev.txt', 'r').read().splitlines()
list1.extend(list2)
list1.extend(list3)
list1.extend(list4)
list1.extend(list5)

# list_r = compiled list of all genes, includes repeats of genes
list_r = list1
unique_list = []
for i in list_r:
	if i not in unique_list:
		unique_list.append(i)
# unique_list, a list of genes that are not repeated taken from list_r

output = open('testing_Gene_list.txt', 'w')
for item in unique_list:
	output.write("%s\n" % item)


Descriptor of the files and their purpose within the Wk3 Code folder

'06a9c4ce-55a4-4dd7-967c-d72e8da7a89c.htseq.counts'
- The original list of genes taken from the ICGC databse. Used as an input for 'interfacing_app_practice1.py'.
https://dcc.icgc.org/

'Gene stable ID Transcript stable ID HGNC symbol EntrezGene transcript name ID.txt'
- List of ENSG, ENST and HGNC IDs. We had to use HDNC IDs (which DO correctly correlate to data in interactome DB) as the Biomart
tool which gave the other IDs did not/ could not provide the correlating Entrez IDs

'HI-II-14.tsv'
-List of gene interactions used, downloaded from the interactome database.
http://interactome.dfci.harvard.edu/H_sapiens/index.php?page=search

'interface_practice'
-Unclassified file which houses all the ensemble gene IDs we filtered from the original 
gene list using 'interfacing_app_practice1.py'

'interfacing_app_practice1.py'
-First portion of code product/start of the process. Used to import list of genes from 
'06a9c4ce-55a4-4dd7-967c-d72e8da7a89c.htseq.counts' file and provides a list of genes from
'06a9c4ce-55a4-4dd7-967c-d72e8da7a89c.htseq.counts' using parameters specified within the code into the file 'interface_practice'.

'interfacing_app_practice2.py'
-Second and final portion of code product. Using a list ofthe genes names from 'interface_practice' and a list of the provided 
ensemble to HGNC IDs and the interaction database 'HI-II-14.tsv', this code will provide a list of interactions based on the 
genes provided within the list of genes given. 

'mart_export.txt'
-Original file export from the Biomart tool. This file was kept so that the header could be referred to as the file
we did use ('Gene stable ID Transcript stable ID HGNC symbol EntrezGene transcript name ID.txt') had to have the header docked to
be usable.

'reactions_export.txt'
-Exported file from 'interfacing_app_practice2.py' which has the list of reactions correlating to the list of provided genes.

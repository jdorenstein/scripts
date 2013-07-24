import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this program scans the ensembl.proteomes.full for files, then, for each file, it sorts out the patch and the non-patch fasta entries. it then saves two files of patch and non-patch entries to their respective folders

###IOin###
#there are no explicit files to input, but the list that contains the filenames is created here (file_names_list)
file_names_list = []
for fileName in os.listdir('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/ensembl.proteomes.full/'):
	#if the fileName does not start with '.', append it to file_names_list
	if fileName[0] != '.':
		file_names_list.append(fileName)

###IOout###
#nothing to output


###MAIN LOOP###
for file_name in file_names_list:
	###IOin###
	file_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/ensembl.proteomes.full/' + file_name #define the file path to the current proteome
	
	###parse 1###
	
	##create a list of all non-patch and patch fasta entries
	for seq_record in SeqIO.parse(file_path, "fasta"): #parse each fasta entry using biopython. for each entry, create a sequence object named 'seq_record'
		#grab the header for each fasta entry. search for '_PATCH:' in the entry. if it is found, add the sequence object to the 
		header = seq_record.description
		if '_PATCH:' in header:
			
			
		
	
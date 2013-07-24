import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this program scans the ensembl.proteomes.full for files, then, for each file, it sorts out the patch and the non-patch fasta entries. it then saves two files of patch and non-patch entries to their respective folders

###IOin###
#there are no explicit files to input, but the list that contains the filenames is created here (file_names_list)
file_names_list = []
for fileName in os.listdir('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/ensembl.proteomes.full/'):
	file_names_list.append(fileName)

print file_names_list
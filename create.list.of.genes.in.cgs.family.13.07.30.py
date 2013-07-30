import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this script reads in the candidate.genesets.fa fasta and creates a list of the id's (for the human genes) (candidate.genesets.id.list). THIS IS VERSION 2: IT USES THE GENEID INSTEAD OF THE PROTEIN ID
###IOin###
which_dir = raw_input('Enter the ionchannel name:')
cgs_in_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.fa'


###IOout###

list_id_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.genesets.gene.list'
list_id_out = open(list_id_path, 'a')

#for each fasta entry, save the header to the output file

for seq_record in SeqIO.parse(cgs_in_path, "fasta"):
	header = seq_record.description
	lineSplit = header.split(' ')
	#if the header starts with 'h', then save the id in lineSplit[1] to the output file
	if lineSplit[0][0] == 'h':
		list_id_out.write(lineSplit[4][5:] + '\n')
	#else:
	#	list_id_out.write(lineSplit[0] + '\n')
	#	print lineSplit[0] + '\n'
		
		
list_id_out.close()
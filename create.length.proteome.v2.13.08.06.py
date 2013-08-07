import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this script reads in all of the proteomes used in the 13 proteomes fasta. for each proteome, it creates a file that contains the proteinID, and the length
output = ''
#create a list of all the names of the desired files
FileName_list = []
for FileName in os.listdir('/Users/ionchannel/13.PROTEOMES.PATH/000.origional.docs/'):
	if FileName[0:9] == 'proteome.':
		FileName_list.append(FileName)
#main loop. for each file name, create a file that contains the length and the proteinID
for filename in FileName_list:
	###IOin###
	#paths
	candidate_path = '/Users/ionchannel/13.PROTEOMES.PATH/000.origional.docs/' + filename
	###IOout###
	lengths_out_path = '/Users/ionchannel/13.PROTEOMES.PATH/000.origional.docs/proteomes.lengths.13.08.07/' + filename[:-2] + 'lengths'
	lengths_out = open(lengths_out_path, 'a')
	#split the proteome into seq_record objects. for each, format the output as (id) (len). then output to file
	for seq_record in SeqIO.parse(candidate_path, "fasta"):
		protein_id = seq_record.id
		seq_length = str(len(seq_record))
		output = protein_id + '\t' + seq_length + '\n'
		lengths_out.write(output)
	

	output = output + '(' + filename[:-2] + 'lengths) '
	lengths_out.close()
	
	
print output
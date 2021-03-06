from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import os

#this program is designed to parse a fasta file (ensembl), and remove all peptides, except for the longest, that are created from the same gene
for fileName in os.listdir('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/ensembl.proteomes.full/'): #list the ionchannel folders that the user can enter
	print fileName
input_name = raw_input('Enter the name of the file you want to format')
#output_name = raw_input('Enter the name of the output file')
output_name = input_name[:-2] + 'longest.peptide.fa'
input_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/ensembl.proteomes.full/' + input_name
output_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/' + output_name
###IOin###
#nothing to import
###IOout###
output_fasta = open(output_path,'a')


#declare variables

seq_dict = {} #format: [key-(gene locus)] : {[seq_record object], [seq length]}
geneID_id = ''

###parse 1###
#create a dictionary that contains the sequences that should be kept

from Bio import SeqIO
for seq_record in SeqIO.parse(input_path, "fasta"): #parses each fasta entry
	#for each entry, check to see if the gene id has already been found. if so, check to see if the current gene is longer than the recorded gene (use a dictionary)
	geneID_line = seq_record.description
	geneID_list = geneID_line.split(' ')
	sequence_length = len(seq_record)
	for item in geneID_list:
		if item[0:5] == 'gene:':
			
			geneID_id = item
			
			#print geneID_id
	if geneID_id in seq_dict.keys():
		#if the length of the new peptide is longer, replace the sequence. otherwise, proceed
		if sequence_length > seq_dict[geneID_id][1]:
			seq_dict[geneID_id] = [seq_record,sequence_length]
	else:
		#create a formatted entry in the seq_dict
		seq_dict[geneID_id] = [seq_record,sequence_length]
	#geneID_id = ''
print 'created dictionary'


			
###parse 2###
#write the dictionary to a file

for key in seq_dict:
	output = seq_dict[key][0].format('fasta')
	output_fasta.write(output)
	
	
output_fasta.close()

   
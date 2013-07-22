from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this program is designed to parse a fasta file (ensembl), and remove all peptides, except for the longest, that are created from the same gene
#declare variables

seq_dict = {} #format: [key-(gene locus)] : {[seq_record object], [seq length]}


from Bio import SeqIO
for seq_record in SeqIO.parse("/Users/ionchannel/candidate.geneset.mapped.fa", "fasta"): #parses each fasta entry
	#for each entry, check to see if the gene id has already been found. if so, check to see if the current gene is longer than the recorded gene (use a dictionary)
	geneID_line = seq_record.description
	geneID_list = geneID_line.split(' ')
	sequence_length = len(seq_record)
	if geneID_list[4] in seq_dict.keys():
		#if the length of the new peptide is longer, replace the sequence. otherwise, proceed
		if sequence_length > seq_dict[geneID_list[4]][1]:
			#seq_dict[geneID_list[4]][0] = seq_record.description  #replace the header
			#seq_dict[geneID_list[4]][1] = seq_record.format('fasta') #replace the sequence
			#seq_dict[geneID_list[4]][2] = sequence_length
			seq_dict[geneID_list[4]] = [seq_record,sequence_length]
	else:
		#create a formatted entry in the seq_dict
		#seq_dict[geneID_list[4]] = [seq_record.description,seq_record.format('fasta'),sequence_length] 
		seq_dict[geneID_list[4]] = [seq_record,sequence_length]
print 'created dictionary'

for key in seq_dict:
	print seq_dict[key][0].format('fasta')
			
   
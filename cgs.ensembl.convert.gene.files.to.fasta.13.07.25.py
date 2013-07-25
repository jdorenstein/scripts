import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def get_gene(seq_record):
	geneID_line = seq_record.description
	geneID_list = geneID_line.split(' ')
	for item in geneID_list:
		if item[0:5] == 'gene:':
			geneID_id = item[5:]
			break
	return geneID_id
#this script reads in a list of genes (Ensembl) and converts them to a fasta containing the longest peptide for that gene

###IOin###

##ask the user for the location of the desired fasta cgs input file

#get the path to the candidate geneset
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
	print fileName
which_dir = raw_input('Enter the name of the folder the list of geneIDs are located in:')

#set the path to the new.cgs.headers.txt


candidate_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/new.cgs.headers.txt'

print 'This script uses the hsa primary longest peptide fasta. To use a different fasta file, please modify the code.' + '\n'

gene_names_in = open(candidate_path, 'r')



hsa_proteome_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteome.homo.sapiens.primary.longest.peptide.fa'


###IOout###
cgs_out_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.fa'
errors_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/errors.candidate.geneset.fa'
cgs_out = open(cgs_out_path, 'a')
errors_out = open(errors_path, 'a')

###Parse 1###

##use biopython to create a dictionary entry containing each entry in the human proteome (longest peptide)

hsa_proteome_dict = SeqIO.to_dict(SeqIO.parse(hsa_proteome_path, "fasta"), key_function = get_gene)

###Parse 2###

##parse the list of gene names. for each gene, see if it is in the hsa_proteome_dict.keys(). if it is, write the sequence object to the new candidate.geneset.fa. if it is not, print ERROR: (genename)

for line in gene_names_in:
	line_in_proteome = False
	if line[:-1] in hsa_proteome_dict.keys():
		sequence_record = hsa_proteome_dict[line[:-1]]
		output = sequence_record.format('fasta')
		cgs_out.write(output)
		line_in_proteome = True
	if line in hsa_proteome_dict.keys():
		sequence_record = hsa_proteome_dict[line]
		output = sequence_record.format('fasta')
		cgs_out.write(output)
		line_in_proteome = True
	if line_in_proteome == False:
		output = line
		errors_out.write(line)
errors_out.close()



log_out = open('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/000.command.txt', 'a')
log_entry = '\n' + '\n' + '\n' + '==================13.07.25===' + '\n' + '\n' + '\n' + 'RUN cgs.ensembl.convert.gene.files.to.fasta.13.07.25.py TO CONVERT (new.cgs.headers.txt) TO (candidate.geneset.fa)'		
log_out.write(log_entry)

log_out.close()


gene_names_in.close()
cgs_out.close()
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this program takes a fasta file as an input and creates two files (cgs.in.proteome.fa) and (cgs.not.in.proteome.fa). This program is a new version of map.uniprot.to.ensembl.v2.13.07.24.py that converts each uniprotID to a gene, then converts the gene to a peptide

###IOin###

##ask the user for the location of the desired fasta cgs input file

#get the path to the candidate geneset
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
	print fileName
which_dir = raw_input('Enter the name of the folder the candidate geneset is located in:')
print '\n' + '\n'
print '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'
print '\n'
#list the contents of the chosen ion channel geneset folder
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'):
	print fileName
tempvar1 = raw_input('Enter the name of the candidate geneset:')

candidate_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + tempvar1

print 'This script uses the hsa longest peptide fasta. To use a different fasta file, please modify the code.' + '\n'

##input the cgs (frmt: sp|Q13563|PKD2_HUMAN)

#cgs_in = open(candidate_path, 'r')
mapping_db_in = open('/Users/ionchannel/research/tools/db/mapping/HUMAN_9606_idmapping_selected.tab','r')
longest_peptide_in = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteome.homo.sapiens.longest.peptide.fa', 'r')
###IOout###

output_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/cgs.in.proteome.003.fa'
errors_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/cgs.not.in.proteome.003.fa'

cgs_out = open(output_path, 'a')
errors_out = open(errors_path, 'a')



###Parse 1###

##read the cgs headers into a list (formatted so that only the id is left over)

#declare variables

cgs_headers_list = [] #frmt: Q13563

for seq_record in SeqIO.parse(candidate_path, "fasta"):
	header = seq_record.id
	if header[0:2] != 'ci':
		#split the header along the pipes
		headerSplit = header.split('|')
		UniProtID = headerSplit[1]
		#print UniProtID
		cgs_headers_list.append(UniProtID)
	if header[0:2] == 'ci':
		UniProtID = header
		#print UniProtID
		cgs_headers_list.append(UniProtID)
		
###Parse 2###

##create a dictionary 'longest_peptide_dict' that uses the geneid as the key and the peptide id as the stored entry
#declare variables
longest_peptide_dict = {}   #frmt: [key = geneID_id], [entry = proteinid (header_edited)]


#parse the fasta file for each header. remove the 'homo-' prefix. append to longest_peptide_list
for seq_record in SeqIO.parse('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteome.homo.sapiens.longest.peptide.fa', 'fasta'):
	header = seq_record.id
	header_edited = header[5:]
	#create geneID_list (contains each item in the header). this is used to find the gene id.
	geneID_line = seq_record.description
	geneID_list = geneID_line.split(' ')
	for item in geneID_list:
		if item[0:5] == 'gene:':
			geneID_id = item[5:]
	#create an entry in longest_peptide_dict. use the geneid_id as the key and the header_edited as the entry
	longest_peptide_dict[geneID_id] = [header_edited]
	
	
###Parse 3###

##create a dictionary of the mappping database UniProtID as the key, and the ensembl info as the entry. In addition, the script uses the longest peptide list to sort pick the protein id that is the longest
#declare variables
mapping_dict = {}

for line in mapping_db_in:
	#split the line on tabs. frmt: 0[UniprotID] ... 19[Ensembl gene id's] . note: when there are multiple ensembl id's, they are seperated by ';' and a space
	lineSplit = line.split('\t')
	#set mapping_gene_id to the geneID, then use it as the key to convert...
	
	
###Parse 4###

##search the database for each header id. for each id, record each resulting Ensembl id (location 21)
for item in cgs_headers_list:
	if item in mapping_dict.keys():
		if mapping_dict[item][0]:
			output = item + ' -> '
			for result_id in mapping_dict[item]:
				output = output + result_id
			cgs_out.write(output + '\n')
		else:
			errors_out.write(item + '\n')
		
	else:
		errors_out.write(item + '\n')



mapping_db_in.close()

cgs_out.close()
errors_out.close()


















































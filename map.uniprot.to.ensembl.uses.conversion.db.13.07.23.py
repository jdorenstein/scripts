import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this program takes a fasta file as an input and creates two files (cgs.in.proteome.fa) and (cgs.not.in.proteome.fa)

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


##input the cgs (frmt: sp|Q13563|PKD2_HUMAN)

#cgs_in = open(candidate_path, 'r')
mapping_db_in = open('/Users/ionchannel/research/tools/db/mapping/HUMAN_9606_idmapping_selected.tab','r')

###IOout###

output_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/cgs.in.proteome.fa'
errors_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/cgs.not.in.proteome.fa'

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

##create a database that uses the UniProtID as the key, and the ensembl info as the entry
#declare variables
mapping_dict = {}

for line in mapping_db_in:
	lineSplit = line.split('\t')
	mapping_dict[lineSplit[0]] = [lineSplit[21]]

	
	
###Parse 3###

##search the database for each header id. for each id, record each resulting Ensembl id (location 21)
for item in cgs_headers_list:
	if item in mapping_dict.keys():
		if mapping_dict[item][0]:
			output = item + ' -> '
			for result_id in mapping_dict[item]:
				output = output + result_id + ', '
			cgs_out.write(output + '\n')
		else:
			errors_out.write(item + '\n')
		
	else:
		errors_out.write(item + '\n')



mapping_db_in.close()

cgs_out.close()
errors_out.close()


















































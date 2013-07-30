import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this program takes a fasta file as an input and creates two files (cgs.in.proteome.fa) and (cgs.not.in.proteome.fa). This program is a new version of map.uniprot.to.ensembl.uses.conversion.db.13.07.23.py that creates a dictionary (using the .longest.peptide) of each uniprot id to the longest protein (for the gene)

###IOin###

##ask the user for the location of the desired fasta cgs input file





mapping_db_in = open('/Users/ionchannel/research/tools/db/mapping/DROME_7227_idmapping_selected.tab','r')
longest_peptide_in = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/old.databases/130723/longest.peptide.fastas/proteome.drosophila.melanogaster.longest.peptide.fa', 'r')




###Parse 2###

##create a list 'longest_peptide_list' that contains the ensembl id of each entry in the longest peptide fasta
#declare variables
longest_peptide_list = []
#parse the fasta file for each header. remove the 'drosophila-' prefix. append to longest_peptide_list
for seq_record in SeqIO.parse('/Users/ionchannel/research/tools/db/blast/13.proteomes/old.databases/130723/longest.peptide.fastas/proteome.drosophila.melanogaster.longest.peptide.fa', 'fasta'):
	header = seq_record.id
	header_edited = header[11:]
	longest_peptide_list.append(header_edited)
###Parse 3###

##create a dictionary of the mappping database UniProtID as the key, and the ensembl info as the entry. In addition, the script uses the longest peptide list to sort pick the protein id that is the longest
#declare variables
mapping_dict = {}
print longest_peptide_list
for line in mapping_db_in:
	#split the line on tabs. frmt: 0[UniprotID] ... 21[Ensembl id's] . note: when there are multiple ensembl id's, they are seperated by ';' and a space
	lineSplit = line.split('\t')
	#test to see if ';' is in lineSplit[21]
	if ';' in lineSplit[21]:
		longest_match = ''
		#split the line on ';'. then, for each entry, check to see if it is in the longest peptide fasta list. 
		list_of_matches = lineSplit[21].split('; ')
		match_count = 0
		for item in list_of_matches:
			#if the item is in the longest_peptide_list, then append it to longest_match and add one to match_count
			if item in longest_peptide_list:
				match_count = match_count + 1
				longest_match = longest_match + item + ' '
		mapping_dict[lineSplit[0]] = [longest_match, match_count]
		match_count = 0
		#if longest_match == '':
		#	print lineSplit[0]
	else:

		mapping_dict[lineSplit[0]] = [lineSplit[21], 1]
	
#for key in mapping_dict.keys():
#	 if mapping_dict[key][1] > 1:
#	 	print mapping_dict[key]
#print '-----------'
#for key in mapping_dict.keys():
#	 if mapping_dict[key][1] == 1:
#	 	print mapping_dict[key]


mapping_db_in.close()




















































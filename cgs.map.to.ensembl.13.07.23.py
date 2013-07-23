#!/usr/bin/python
import sys,os,csv
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


#this script asks for the name of the candidate geneset, the proteome that contains the desired headers, and uses the info to find the location of the mapped cgs. then, the script maps the sequences to create new headers



###ask for input##

#declare variables
which_dir = ''
candidate_path = ''
octopus_or_13 = ''
proteome_path = ''
output_path = ''

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

#get the path to the proteome
#ask if the user wants to use the octopus proteome or the 13.proteomes fasta
octopus_or_13 = raw_input('Do you want to use the octopus or the 13.proteomes fasta to retrieve the proper headers? <oct> <13>')
if octopus_or_13 == '13':
	proteome_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/ensembl.archive.full/proteome.homo.sapiens.fa'
if octopus_or_13 == 'oct':
	proteome_path = '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/octProteome.fa'
#use location of candidate geneset to get location of output


print 'This program will create an output file named candidate.geneset.mapped.fa in the same directory as the origional cgs.'
output_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/cgs.in.proteome.fa'
errors_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/cgs.not.in.proteome.fa'



###IOin##


#proteome_in = open(proteome_path, 'r')


###IOout##

#cgs_out = open(output_path, 'a')
#errors_out = open(errors_path, 'a')

###parse 1###

#creates a list that contains each sequence (keys for dictionary). also, creates a dictionary entry using the sequence as the key (stores the seq_record object)
#declare variables
cgs_keys = []
cgs_dict = {}
for seq_record in SeqIO.parse(candidate_path, "fasta"):
	cgs_keys.append(str(seq_record.seq))
	cgs_dict[str(seq_record.seq)] = [seq_record]
#print cgs_keys
###parse 2###
#for each entry in the human proteome, search the cgs list for a hit. if the script finds a hit, append the entry from the proteome onto hits_list.
#declare variables
hits_list = []
for seq_record in SeqIO.parse(proteome_path, "fasta"): #parses each fasta entry
	#if the sequence is found in the cgs_list, append the entry to hits_list
	if str(seq_record.seq) in cgs_keys:
		print 'yay    ' + str(seq_record.seq)
	
print 'created dictionary'










###parse 2###

##create a list of the peptide sequences in the candidate geneset and a dictionary that acts like proteome_dict (but stores the info for the cgs


#declare variables



##see if the peptide is located in the proteome. if it is, create an output that contains the proteome header and the peptide. if it is not, use the origional header


#see if the peptide in the cgs is in the proteome. if it is, create an output that contains the proteome header and the peptide. if it is not, use the origional header
#for item in cgs_list:
#	if item in proteome_list:
#		output = proteome_dict[item][0] + '\n' + item + '\n'
#		cgs_out.write(output)
#	if item not in proteome_list:
#		errors_out.write( cgs_dict[item][0] + '\n' + item + '\n' )
#		output = cgs_dict[item][0] + ': candidate_gene_did_not_map_to_proteome' + '\n' + item + '\n'
#		cgs_out.write(output)












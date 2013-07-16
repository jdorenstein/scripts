#!/usr/bin/python
import sys,os,csv


#this script asks for the name of the candidate geneset, the proteome that contains the desired headers, and uses the info to find the location of the mapped cgs. then, the script maps the sequences to create new headers
###define functions##

##this function processes the header and the peptide into a dictionary entry
#      returns (peptide (key)), (header)
def fasta_processor( header, peptide ):
	peptide_formatted = ''
	for line in peptide:
		peptide_formatted = peptide_formatted + line[:-1]
	header_formatted = header[:-1]
	return (header_formatted, peptide_formatted)


###ask for input##

#declare variables
which_dir = ''
candidate_path = ''
octopus_or_12 = ''
proteome_path = ''
output_path = ''

#get the path to the candidate geneset
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
	print fileName
which_dir = raw_input('Enter the name of the folder the candidate geneset is located in:')
print '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'):
	print fileName
tempvar1 = raw_input('Enter the name of the candidate geneset')
candidate_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + tempvar1

#get the path to the proteome
#ask if the user wants to use the octopus proteome or the 12.proteomes fasta
octopus_or_12 = raw_input('Do you want to use the octopus or the 12.proteomes fasta to retrieve the proper headers? <octopus> <12.proteomes>')
if octopus_or_12 == '12.proteomes':
	proteome_path = '/Users/ionchannel/research/tools/db/blast/12.proteomes/000.origional.docs/12.proteomes.fa'
if octopus_or_12 == 'octopus':
	proteome_path = '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/octProteome.fa'

#use location of candidate geneset to get location of output
print 'This program will create an output file named candidate.geneset.mapped.fa in the same directory as the origional cgs.'
output_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.mapped.fa'




###IOin##

cgs_in = open(candidate_path, 'r')
proteome_in = open(proteome_path, 'r')


###IOout##

cgs_out = open(output_path, 'a')

###parse 1###

##using the inputted proteome, create a dictionary that uses the peptide sequence as the key for the header. 

#declare variables

header = ''
peptide = ''
first_entry = True
proteome_dict = {}

#scan in each line. identify the peptides and the headers and match each header to its peptide. when the script detects a new header, it saves the previous header/peptide as a dictionary entry
for line in proteome_in:
	#if the script detects a header, it puts the line into the 'header' variable, in addition, if first_entry == False, it creates a dictionary entry using the header and the peptide
	if line[0] == '>':
		if first_entry == False:
			proteome_dict[peptide] = [header]
			peptide = ''
			header = line[:-1]
		if first_entry == True:
			header = line[:-1]
			first_entry = False
	#if the script detects a peptide, it adds it to the peptide list
	if line[0] != '>':
		peptide = peptide + line[:-1]

print str(proteome_dict)
	
	









cgs_in.close()
cgs_out.close()
proteome_in.close()

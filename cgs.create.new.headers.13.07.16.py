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
print '\n' + '\n'
print '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'
print '\n'
#list the contents of the chosen ion channel geneset folder
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'):
	print fileName
tempvar1 = raw_input('Enter the name of the candidate geneset:')
candidate_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + tempvar1

#get the path to the proteome
#ask if the user wants to use the octopus proteome or the 12.proteomes fasta
octopus_or_12 = raw_input('Do you want to use the octopus or the 12.proteomes fasta to retrieve the proper headers? <oct> <12>')
if octopus_or_12 == '12':
	proteome_path = '/Users/ionchannel/research/tools/db/blast/12.proteomes/000.origional.docs/12.proteomes.fa'
if octopus_or_12 == 'oct':
	proteome_path = '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/octProteome.fa'
#use location of candidate geneset to get location of output

if tempvar1 == 'candidate.genset.fa':
	print 'This program will create an output file named candidate.geneset.mapped.fa in the same directory as the origional cgs.'
	output_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.mapped.fa'
	errors_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.mapped.errors.fa'
if tempvar1 == 'candidate.geneset.full.unsafe.fa':
	print 'This program will create an output file named candidate.geneset.mapped.fa in the same directory as the origional cgs.'
	output_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.mapped.full.unsafe.fa'
	errors_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.mapped.errors.full.unsafe.fa'


###IOin##

cgs_in = open(candidate_path, 'r')
proteome_in = open(proteome_path, 'r')


###IOout##

cgs_out = open(output_path, 'a')
errors_out = open(errors_path, 'a')

###parse 1###

##using the inputted proteome, create a dictionary that uses the peptide sequence as the key for the header. 

#declare variables

header = ''
peptide = ''
first_entry = True
proteome_dict = {}
proteome_list = []

#scan in each line. identify the peptides and the headers and match each header to its peptide. when the script detects a new header, it saves the previous header/peptide as a dictionary entry
for line in proteome_in:
	#if the script detects a header, it puts the line into the 'header' variable, in addition, if first_entry == False, it creates a dictionary entry using the header and the peptide
	if line[0] == '>':
		if first_entry == False:
			proteome_dict[peptide] = [header]
			proteome_list.append(peptide)
			peptide = ''
			header = line[:-1]
		if first_entry == True:
			header = line[:-1]
			first_entry = False
	#if the script detects a peptide, it adds it to the peptide list
	if line[0] != '>':
		peptide = peptide + line[:-1]

###parse 2###

##create a list of the peptide sequences in the candidate geneset and a dictionary that acts like proteome_dict (but stores the info for the cgs


#declare variables

header = ''
peptide = ''
first_entry = True
cgs_dict = {}
cgs_list = []

#scan in each line. identify the peptides and the headers and match each header to its peptide. when the script detects a new header, it saves the previous header/peptide as a dictionary entry
for line in cgs_in:
	#if the script detects a header, it puts the line into the 'header' variable, in addition, if first_entry == False, it creates a dictionary entry using the header and the peptide
	if line[0] == '>':
		if first_entry == False:
			cgs_dict[peptide] = [header]
			cgs_list.append(peptide)
			peptide = ''
		header = line[:-1]
		if first_entry == True: #this allows the program to skip the first header, as this would cause it to produce a false error
			header = line[:-1]
			first_entry = False
	#if the script detects a peptide, it adds it to the peptide list
	if line[0] != '>':
		peptide = peptide + line[:-1]
	
###parse 3###

##see if the peptide is located in the proteome. if it is, create an output that contains the proteome header and the peptide. if it is not, use the origional header


#see if the peptide in the cgs is in the proteome. if it is, create an output that contains the proteome header and the peptide. if it is not, use the origional header
for item in cgs_list:
	if item in proteome_list:
		output = proteome_dict[item][0] + '\n' + item + '\n'
		cgs_out.write(output)
	if item not in proteome_list:
		errors_out.write( cgs_dict[item][0] + '\n' + item + '\n' )
		output = cgs_dict[item][0] + ': candidate_gene_did_not_map_to_proteome' + '\n' + item + '\n'
		cgs_out.write(output)










cgs_in.close()
cgs_out.close()
proteome_in.close()

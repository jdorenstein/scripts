#!/usr/bin/python
import sys,os,csv

#NOTE: This script is a version of fam.fasta.creator.13.07.12.py that is intended for use with -outfmt 7
#this script will create a file that contains a list of sequence id's from a blast report, use the file to create a fasta file, then blast the fasta against a specified database
#      this script is to be used to create a fasta file of the fished octopus proteome genes, then blast it against the hsa proteome database. once the blast is completed, the script will then take the top ten hits for each gene from the blast and test to see if each hit's id matches one from the human candidate geneset

#find the user dependent filepaths
#get the path and name of the blast report and input the blast report


#declare variables
in_path = ''
out_path = ''
use_a_ionchannels = ''
name_out = ''
log_path = ''

#ask for the location of the file
print 'This script will format the results of a blast report into a fasta file, then blast the fasta file against the database specified by the user, then print a formatted entry for the command log into the output file' + '\n'
#ask the user if they want to use a blast output that is located in the ionchannels folder. if yes, then ask which folder they want to enter, and then the name of the blast output
use_a_ionchannels = raw_input('Do you want to use a blast report located inside of the ionchannels project folder? Enter <y> or <n>:')
#if the user marks y, then the script will find out the output that they want to use
if use_a_ionchannels == 'y':
	print 'Which folder do you want to enter? (if you make a mistake, please restart the script)'
	for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
		print fileName
	print '\n'
	which_dir = raw_input(':')
	print 'This script will only accept blast reports located in the geneset folder'
	for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'):
		print fileName
	print '\n'
	which_file = raw_input('Which blast report do you want to use:')
	in_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + which_file
#if the user does not mark y, then the script asks the user to restart the script
else:
	#in_path = raw_input('Please enter the COMPLETE FILEPATH (includes the name of the output file):')
	print 'please restart the script'
	temp_var = raw_input(':') #this is only to stop the script until the user restarts it
#ask the user for the name out the file to put the fasta into
name_out = raw_input('Enter the name of the fasta output file (located in the same folder as the input blast report):')
out_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_out
log_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/000.command.txt'
#-------



###IOin##

blast_in = open(in_path, 'r')
octFasta_in = open( '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/oct_v2_fasta.txt', 'r' )

###IOout##

#NOTE: FOR NOW, THIS SCRIPT WILL ALWAYS OUTPUT THE COMMAND LOG TO A TEMPORARY FILE
#fasta_out frmt: >[pacID] [Hsa-top hit] \n [sequence]
#log_out frmt(pt1): 'RUN SCRIPT TO FORMAT [blast output] INTO [fasta output]
#log_out frmt(pt2): [fasta input files] \n [blast database] \n [command for blast] 

log_out = open(log_path, 'a')
fasta_out = open(out_path, 'a')

#-------

###parse 1###

##this parse finds the filepath of the blast database to be used for the blast


#declare variables
stay_in_loop = True
filepath = ''
filename = ''

#the first loop begins the sequence that asks for the database
while stay_in_loop == True:
	print 'Do you want to use the octopus proteome database, the 12.proteomes database, or a different database?' + '\n'
	print '	If you want to use the octopus database, type in <octopus>.' + '\n' 
	print '	If you want to use the 12.proteomes database, type in <12.proteomes>.' + '\n'
	which_database = raw_input('	If you want to use a different database, type in <other>.')
	#if the user enters octopus, the filepath is set to octProteomeDB
	if which_database == 'octopus':
		stay_in_loop = False
		filepath = '/Users/ionchannel/research/tools/db/blast/oct.proteome/octProteomeDB'
		break
	#if the user enters 12.proteomes, the filepath is set to 12.proteomes
	if which_database == '12.proteomes':
		stay_in_loop = False
		filepath = '/Users/ionchannel/research/tools/db/blast/12.proteomes/12.proteomes.blast.db'
		break
	#if the user enters other, they must enter the full filepath starting at /Users/
	if which_database == 'other':
		filepath = raw_input('Please enter the full filepath: /Users/')
		stay_in_loop = False
		break
		
		#use_a_ionchannels = ''
		#use_a_ionchannels = raw_input('Do you want to use an database located inside of the ionchannels project folder? Enter <y> or <n>:')
		#if use_a_ionchannels == 'y':
			#print 'Which folder do you want to enter? (if you make a mistake, please restart the script)'
			#for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
			#	print fileName
			#print '\n'
			#which_dir = raw_input(':')
			#which_file = raw_input('Which file 
			#filepath = raw_input('Pleae enter the COMPLETE FILEPATH (includes the name of the database):')
			#break
	if which_database != 'octopus' and which_database != '12.proteomes' and which_database != 'other':
		print 'I am sorry, but you did not enter one of the three options. Please recheck your input again.' + '\n'




###parse 2###

###using the blast report entered, create a formatted fasta file that contains each hit (the script asks if the user wants to remove repeats or to keep them)

##create an array that contains the information in the octFasta_in file
#declare variables

octFasta = {}

#create a dictionary from the CSV file that uses the pacID as the key
for line in octFasta_in:
	lineSplit = line.split('\t')
	bhh = lineSplit [12]
	peptide = lineSplit[14]
	
	if bhh:
		bhh_mod = 'Hsa-' + bhh + ': '
		octFasta[lineSplit[0]] = [lineSplit[0] , bhh_mod , peptide ]
	if not bhh:
		octFasta[lineSplit[0]] = [lineSplit[0] , 'No best human hit identified in Excel file: ' , peptide ] 

##create a list out of all of the hits found in the blast report (uses the lcl| format for the top hits)
#declare variables

top_hits = []

#parse file for lcl| then input the pacID
for line in blast_in: #split the blast report up on the lines
	lineSplit = line.split(' ')
	#if the line is a result, then the result's id is appended onto blast_list
	if lineSplit[0][0:4] == 'lcl|':
		top_hits.append(lineSplit[0][4:])
		
#ask the user if they want to make the list unique. if the user answers yes, then remove duplicate entries in the list

rem_duplicates = raw_input('Do you want to remove duplicate entries in the fasta file? <y> or <n>')
if rem_duplicates == 'y':
	top_hits = list(set(top_hits))
	print 'Duplicates removed'
##create the fasta file by using each entry in the list as a key for use in the octFasta dictionary, which is then formatted into a usable fasta output

num = 0
#for each item in top_hits, find the corresponding octopus proteome gene, then format the entry into the fasta file 
for item in top_hits:	
	output = '>' + octFasta[item][0] + ' ' + octFasta[item][1] + '\n' + octFasta[item][2] 
	fasta_out.write(output)
	num = num + 1 
print 'Fasta created'

###parse 3###

###ask if the user wants the blast to be run, then create a formatted command line output (if the user answers no, then only create log of the script being created. if the user marks yes, then log both the script and the blast). 

##ask the user if they want the blast to be run
#declare variables

run_blast = 'y'
command_line_output = ''

#use raw_input to determine if the user wants to run the blast

run_blast = raw_input('Do you want to BLAST the fasta against the specified database? <y> or <n>')

#if the user marks yes, then ask for the name of the blast report and error log, generate a command to run the blast, and run the blast (if the user does not mark yes, then the script will skip this step
if run_blast == 'y':
	name_blast_report_out = raw_input('Enter the name for your blast report:')
	name_blast_error_out = raw_input('Enter the name for the error log of the blast report:')
	options_blosum = raw_input('Enter the blosum setting: <45> or <62>')
	options_evalue = raw_input('Enter the evalue setting (just the number):')
	#options_results_both = raw_input('Enter the number of results to record:')
	options_outfmt = raw_input('Enter the output format: <0> or <7>
	command_line_output = 'blastp -db ' + filepath + ' -query ' + out_path + ' -out ' + '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_blast_report_out + ' 2> /Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_blast_error_out + ' -evalue ' + options_evalue + ' -matrix BLOSUM' + options_blosum + ' -outfmt ' + options_outfmt + ' -num_threads 2 &'	
	os.system(command_line_output)

#generate the formatted command log

log_out.write('\n' + '\n' + '\n' + '--------------------' + '\n' + '\n' + '\n' + 'RUN fam.fasta.creator.13.07.12 TO FORMAT (' + which_file + ') INTO (' + name_out + ')' + '\n' + '\n' + '\n' + '--------------------' + '\n' + '\n' + '\n' + 'BLAST ' + name_out + ' AGAINST ' + which_database + ', BLOSUM' + options_blosum + ', E=' + options_evalue + ' (' + name_blast_report_out + ')' + '\n' + '\n' + 'fasta file' + '\n' + '      ./' + which_dir + '/' + name_out + '\n' + 'Database' + '\n' + '      ' + filepath + '\n' + '\n' + 'command:' + '\n' + '      ' + command_line_output )






blast_in.close()
log_out.close()
fasta_out.close()
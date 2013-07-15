#!/usr/bin/python
import sys,os,csv

#this script will create a fasta file out of the results of the inputted blast report and inputted CSV source file (it will be interactive), then blast the fasta against a specified database


#find the user dependent filepaths
#get the path and name of the blast report and input the blast report


#declare variables
in_path = ''
out_path = ''
use_a_ionchannels = ''
name_out = ''

#ask for the location of the file
print 'This script will format the results of a blast report into a fasta file, then blast the fasta file against the database specified by the user, then print a formatted entry for the command log into the output file' + '\n'
#ask the user if they want to use a blast output that is located in the ionchannels folder. if yes, then ask which folder they want to enter, and then the name of the blast output
use_a_ionchannels = raw_input('Do you want to use an database located inside of the ionchannels project folder? Enter <y> or <n>:')
#if the user marks y, then the script will find out the output that they want to use
if use_a_ionchannels == 'y':
	print 'Which folder do you want to enter? (if you make a mistake, please restart the script)'
	for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
		print fileName
	print '\n'
	which_dir = raw_input(':')
	print 'This script will only accept outputs located in the geneset folder'
	which_file = raw_input('Which file do you want to use:')
	in_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + which_file
#if the user does not mark y, then the script asks them to enter a complete filepath
else:
	in_path = raw_input('Please enter the COMPLETE FILEPATH (includes the name of the output file):')
	
#ask the user for the name out the file to put the fasta into
name_out = raw_input('Enter the name of the fasta output file (located in the same folder as the input blast report):')
out_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_out
#-------



###IOin##

blast_in = open(in_path, 'r')
octFasta_in = open( '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/oct_v2_fasta.txt', 'r' )

###IOout##

#NOTE: FOR NOW, THIS SCRIPT WILL ALWAYS OUTPUT THE COMMAND LOG TO A TEMPORARY FILE
#fasta_out frmt: >[pacID] [Hsa-top hit] \n [sequence]
#log_out frmt(pt1): 'RUN SCRIPT TO FORMAT [blast output] INTO [fasta output]
#log_out frmt(pt2): [fasta input files] \n [blast database] \n [command for blast] 
log_out = open('/Users/ionchannel/research/projects/temp.command.out', 'a')
fasta_out = open(out_path, 'a')



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

#using the blast report entered, create a formatted fasta file that contains each hit (the script asks if the user wants to remove repeats or to keep them)

#create an array that contains the information in the octFasta_in file
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

#create a list out of all of the hits found in the blast report (uses the lcl| format for the top hits)
#declare variables

top_hits = []

#parse file for lcl| then input the pacID
for line in blast_in #split the blast report up on the lines
	lineSplit = line.split(' ')
	#if the line is a result, then the result's id is appended onto blast_list
	if lineSplit[0][0:4] == 'lcl|':
		top_hits.append(lineSplit[0][4:])
		
#ask the user if they want to make the list unique. if the user answers yes, then remove duplicate entries in the list

rem_duplicates = raw_input('Do you want to remove duplicate entries in the fasta file? <y> or <n>')
if rem_duplicates == 'y':
	






blast_in.close()
log_out.close()
fasta_out.close()
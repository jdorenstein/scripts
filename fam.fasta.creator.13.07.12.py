#!/usr/bin/python
import sys,os,csv

#this script will create a fasta file out of the results of the inputted blast report and inputted CSV source file (it will be interactive) 


###IOin
#get the path and name of the fasta input file (ask the user for which fasta file or to enter the location of a custom fasta file

#declare variables
stay_in_loop = True
filepath = ''
filename = ''

#mainloop
while stay_in_loop == True:
	print 'Do you want to use the octopus proteome fasta file, the 12.proteomes fasta file, or a different fasta file?' + '\n'
	print '	If you want to use the octopus fasta, type in <octopus>.' + '\n' 
	print '	If you want to use the 12.proteomes fasta, type in <12.proteomes>.' + '\n'
	which_database = raw_input('	If you want to use a different fasta, type in <other>.')
	if which_database == 'octopus':
		stay_in_loop = False
		filepath = '/Users/ionchannel/research/tools/db/blast/oct.proteome/octProteomeDB'
		break
	if which_database == '12.proteomes':
		stay_in_loop = False
		filepath = '/Users/ionchannel/research/tools/db/blast/12.proteomes/12.proteomes.blast.db'
		break
	if which_database == 'other':
		stay_in_loop = False
		use_a_ionchannels = ''
		use_a_ionchannels = raw_input('Do you want to use an fasta located inside of the ionchannels project folder? Enter <y> or <n>:')
		if use_a_ionchannels == 'y':
			print 'Which folder do you want to enter? (if you make a mistake, please restart the script)'
			for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
				print fileName
			print '\n'
			which_dir = raw_input(':')
			which_file = raw_input('Which file 
		filepath = raw_input('Pleae enter the COMPLETE FILEPATH (includes the name of the database):')
		break
	if which_database != 'octopus' and which_database != '12.proteomes' and which_database != 'other':
		print 'I am sorry, but you did not enter one of the three options. Please recheck your input again.' + '\n'
#using the file name entered, open 
	

#get the file that the script will use as an input (the blast output)


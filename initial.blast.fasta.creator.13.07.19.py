#!/usr/bin/python
import sys,os,csv

#this script will blast the candidate geneset against the octopus proteome, the sort the results into a fasta file

#find the user dependent filepaths
#get the path and name of the cgs, the blast output, and the fasta output


#declare variables
in_path = '' #the path for inputting the blast report
out_path = '' #the path for outputting the fasta file
use_a_ionchannels = '' #
name_out = ''
log_path = ''
cgs_which = ''

#ask for the location of the file
print 'This script will blast the specified candidate geneset against the specified proteome (e=0.1,b=45), then create a fasta out of the hits' + '\n'
#ask the user which folder the cgs is located in
print 'Which folder is your candidate geneset located in?'
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'): #list the ionchannel folders that the user can enter
	print fileName
print '\n'
which_dir = raw_input(':') #whichdir is used to specify to the proper folder
print 'This script will only accept candidate genesets located in the /geneset/ folder' + '\n' + 'Which candidate geneset do you want to use?' + '\n'
for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/'): #list the contents of the /geneset/ folder in the chosen ionchannel folder
	print fileName
print '\n'
cgs_which = raw_input(':') #cgs_which is used to specify the candidate geneset
which_file = raw_input('What do you want to name the blast output:') #which_file is used to specify the blast output name
blast_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + which_file
blast_error_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + which_file + '.errors'
in_path_cgs = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + cgs_which
#ask the user for the name out the file to put the fasta into
name_out = raw_input('Enter the name of the fasta output file (located in the same folder as the input blast report):')
out_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_out
log_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/000.command.txt'
#-------



###IOin##


cgs_in = open(in_path_cgs, 'r')

###IOout##


#fasta_out frmt: >[pacID] [Hsa-top hit] \n [sequence]
#log_out frmt(pt1): 'RUN initial.blast.fasta.creator.13.07.19.py TO CREATE (blast output) AND (fasta output)
#log_out frmt(pt2): [fasta input files] \n [blast database] \n [command for blast] 

log_out = open(log_path, 'a')
fasta_out = open(out_path, 'a')
blast_out = open(blast_path, 'a')
list_headers_out = open('/Users/ionchannel/research/projects/ionchannels/temp.list.fa', 'a')

#specify the filepath used for the blast database

filepath = '/Users/ionchannel/research/tools/db/blast/oct.proteome/octProteomeDB'

###parse 1###

##blast the specified cgs against the blast database
command_line_output = 'blastp -db ' + filepath + ' -query ' + in_path_cgs + ' -out ' + blast_path + ' 2> ' + blast_error_path + ' -evalue 0.1 -matrix BLOSUM45 -outfmt 7 -num_threads 2'	
os.system(command_line_output)

##open the blast output
blast_in = open(blast_path, 'r')

###parse 2###

###using the blast report entered, create a formatted fasta file that contains each hit (the script asks if the user wants to remove repeats or to keep them)

##create a list that contains the headers of all hits. 
#declare variables
line_count = 0
header_list_2 = []
#execute
for line in blast_in:
	#if a line does not start with '#', put the result into header_list_2
	if line[0] != '#':
		lineSplit = line.split('\t')
		header_list_2.append(lineSplit[1])
#make all items in the list unique
header_list_2 = list(set(header_list_2))
#write each item in the list to a temporary output file
for item in header_list_2:
	output = item + '\n'
	list_headers_out.write(output)
	
	
###parse 3###

##activate the blastdbcmd command. use the command to create a new fasta file. once the new database is completed, delete the temporary file

os.system('blastdbcmd -db /Users/ionchannel/research/tools/db/blast/oct.proteome/octProteomeDB -dbtype prot -entry_batch /Users/ionchannel/research/projects/ionchannels/temp.list.fa -outfmt %f -out ' + out_path)
os.system('rm /Users/ionchannel/research/projects/ionchannels/temp.list.fa')

###parse 4###
	

#generate the formatted command log

log_out.write('\n' + '\n' + '\n' + '==================13.07.19===' + '\n' + '\n' + '\n' + 'RUN initial.blast.fasta.creator.13.07.19.py TO CREATE (' + which_file + ')' + ' AND (' + name_out + ')' + '\n' + '\n' + '\n' + '--------------------' + '\n' + '\n' + '\n' + '(script executed command) BLAST ' + name_out + ' AGAINST ' + 'octProtomeDB' + ', BLOSUM45, E=0.1, (' + which_file + ')' + '\n' + '\n' + 'fasta file' + '\n' + '      ./' + which_dir + '/' + name_out + '\n' + 'Database' + '\n' + '      ' + filepath + '\n' + '\n' + 'command:' + '\n' + '      ' + command_line_output )









blast_in.close()
cgs_in.close()
list_headers_out.close()
blast_out.close()
log_out.close()
fasta_out.close()
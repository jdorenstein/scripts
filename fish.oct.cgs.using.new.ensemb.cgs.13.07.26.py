import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this program executes a series of blasts that are used to create an octopus cgs out of the human cgs (cgs x 13.proteomes) (cgs+div x octProteome) (octTopHits x octProteome)

###IOin###

##ask the user for the location and name of the candidate geneset

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


ProteomesDB13_path = '/Users/ionchannel/13.PROTEOMES.PATH/13.proteomes.db'
octProteomeDB_path = '/Users/ionchannel/OCT.PROTEOME.PATH/octProteomeDB'
candidate_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + tempvar1
log_entry_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/0001.command.txt'
###IOout###
#assign the paths that will be used by the commands that are passed to the system

#blast 001: cgs x 13.proteomes:
cgs_13Prot_blast_out = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/out.blast.fishing.analysis.001'
cgs_13Prot_blast_errors = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/out.errors.blast.fishing.analysis.001'
cgs_diversity_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/cgs.div.blast.001.fa'

#blast 002: cgs+div x octProteome:
cgsdiv_octProt_blast_out = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/out.blast.fishing.analysis.002'
cgsdiv_octProt_blast_errors = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/out.errors.blast.fishing.analysis.002'
oct_top_hits_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/oct.top.hits.blast.002.fa'

#blast 003: oct top hits x octProteome:
octhits_octProt_blast_out = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/out.blast.fishing.analysis.003'
octhits_octProt_blast_errors = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/out.errors.blast.fishing.analysis.003'
oct_hits_fished_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/oct.cgs.fished.blast.003.fa'

#open log_entry

log_entry = open(log_entry_path, 'a')

###Parse 1###

#format each blast command. also format the log entry

#declare variables

blast_command_001 = ''
blast_command_002 = ''
blast_command_003 = ''
log_entry_formatted = ''

#format blast_command_001

blast_command_001 = 'blastp -query ' + candidate_path + ' -db ' + ProteomesDB13_path + ' -out ' + cgs_13Prot_blast_out + ' -evalue 10 -matrix BLOSUM45 -outfmt 7 -num_threads 2 2> ' + cgs_13Prot_blast_errors

#format blast_command_002

blast_command_002 = 'blastp -query ' + cgs_diversity_path + ' -db ' + octProteomeDB_path + ' -out ' + cgsdiv_octProt_blast_out + ' -evalue 10 -matrix BLOSUM45 -outfmt 7 -num_threads 2 2> ' + cgsdiv_octProt_blast_errors

#format blast_command_003

blast_command_003 = 'blastp -query ' + oct_top_hits_path + ' -db ' + octProteomeDB_path + ' -out ' + octhits_octProt_blast_out + ' -evalue 10 -matrix BLOSUM45 -outfmt 7 -num_threads 2 2> ' + octhits_octProt_blast_errors

#format log_entry

log_entry_script = '\n \n \n' + '-----------------------------' + '\n \n \n' + 'RUN (fish.oct.cgs.using.new.ensembl.cgs.13.07.26.py) TO CREATE (oct.cgs.fished.blast.003.fa)' + '\n \n' + 'command: ' + '\n \t' + 'python /Users/ionchannel/PYTHON.PATH/fish.oct.cgs.using.new.ensembl.cgs.13.07.26.py' 
log_entry_blast001 = '\n \n \n' + '-------------------' + '\n \n' + '(script generated command)' + '\n' + 'BLAST (candidate.geneset.fa) AGAINST (13.proteomes.db). (out.blast.fishing.analysis.001)' + '\n \n' + 'command: ' + '\n \t' + blast_command_001
log_entry_blast002 = '\n \n \n' + '-------------------' + '\n \n' + '(script generated command)' + '\n' + 'BLAST (cgs.div.blast.001.fa) AGAINST (octProteomeDB). (out.blast.fishing.analysis.002)' + '\n \n' + 'command: ' + '\n \t' + blast_command_002
log_entry_blast003 = '\n \n \n' + '-------------------' + '\n \n' + '(script generated command)' + '\n' + 'BLAST (oct.top.hits.blast.002.fa) AGAINST (octProteomeDB). (out.blast.fishing.analysis.003)' + '\n \n' + 'command: ' + '\n \t' + blast_command_003

#log_entry.write(log_entry_script)
#log_entry.write(log_entry_blast001)
#log_entry.write(log_entry_blast002)
#log_entry.write(log_entry_blast003)


###Parse 2###
##blast the cgs against the 13.proteomes.db. (blast 001). then, use biopython to fish out the top hit for each species and put it into cgs.div.blast.001.fa

os.system(blast_command_001)
#open the blast report
blast_report_001 = open(cgs_13Prot_blast_out)

#declare variables

top_hits_001_dict = {}
queryID = ''
resultID_list = []
#for each line in the blast report, look for # BLASTP 2.2.28+ to signify the new query. then, create a dictionary entry (using the query as the key) that contains the top hit for each species

#for line in blast_report_001:
	#if the script finds a new query, add the resultID_list to a dictionary entry that uses the queryID as the key (only if queryID isn't '') then reset all variables
	#if line[:8] == '# BLASTP':
		#if there is a saved queryID, create a new top_hits_001_dict entry
	#	if queryID != '':
	#		top_hits_001_dict[queryID] = [resultID_list]
	#	queryID = ''
	#	resultID_list = []
	#if the line is not a comment line, save the query id as 'queryID'. then, check to see if the 
	#if line[0] != '#':
		#split the line on tabs
	#	lineSplit = line.Split('\t')
	#	#set queryID to the query
	#	queryID = lineSplit[0]
	#	#split the result on '-' (resultSplit)
	#	resultSplit = lineSplit[1].split('-')
		#check to see if resultSplit[0] is in resultID_list. if yes, move on. if no, add the result to resultID_list
	#	if resultSplit[0] not in 














blast_report_001.close()
log_entry.close()
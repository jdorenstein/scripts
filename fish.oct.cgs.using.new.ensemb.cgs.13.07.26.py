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

candidate_path = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + tempvar1


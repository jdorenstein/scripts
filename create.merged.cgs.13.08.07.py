import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this script is designed to merge the hsa cgs id list (with prefixes) and the (cgs.list.parse.13.08.07) for dr and ce into (cgs.hsa.dr.ce.id.list.fa)

###IOin###
hsa_in = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/candidate.genesets.id.list.headers', 'r')
ce_in = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.celegans/cgs.list.parse.13.08.07', 'r')
dr_in = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.drosophila/cgs.list.parse.13.08.07', 'r')

###IOout###
cgs_id_out = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/cgs.hsa.dr.ce.id.list', 'a')


###Parse 1###
#for each line in the hsa cgs, add to the output
for line in hsa_in:
	output = line
	cgs_id_out.write(output)
hsa_in.close()

###Parse 2###
#for each line in ce_in, split the line on \t, write lineSplit[0] to the output
for line in ce_in:
	lineSplit = line.split('\t')
	output = lineSplit[0] + '\n'
	cgs_id_out.write(output)
	
ce_in.close()

###Parse 3###
#repeat 2 but with dr
for line in dr_in:
	lineSplit = line.split('\t')
	output = lineSplit[0] + '\n'
	cgs_id_out.write(output)
dr_in.close()

cgs_id_out.close()
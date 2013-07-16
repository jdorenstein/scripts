#!/usr/bin/python

#this script formats the new ciona proteome into a usable fasta file for the 12.proteomes.blast.db

#

###IOin##

#unformatted ciona proteome
#frmt example: >jgi|Cioin2|200987|fgenesh3_pm.C_chr_01p000005 \n peptide

ciona_in = open( '/Users/ionchannel/research/tools/db/blast/12.proteomes/000.origional.docs/origional.source.fastas/ciona.proteome.nonformatted.13.07.16.fa','r')

###IOout##

#formatted ciona proteome
#frmt example: >ciona-200987 jgi|Cioin2|200987|fgenesh3_pm.C_chr_01p000005 \n peptide

ciona_out = open( '/Users/ionchannel/research/tools/db/blast/12.proteomes/000.origional.docs/ciona.intestinalis.peptides.13.07.16.fa','a')

###parse 1###

#read in ciona_in. if a header is found, parse it. if a non header is found, copy the line into the new output file

for line in ciona_in:
	#look for '>'. if found, reformat the line. if not, copy the line into the output
	if line[0] == '>':
		lineSplit = line.split('|') #split the line on the pipes
		output = '>ciona-' + lineSplit[2] + ' ' + lineSplit[0][1:] + '|' + lineSplit[1] + '|' + lineSplit[2] + '|' + lineSplit[3] 
		ciona_out.write(output)
	else:
		output = line
		ciona_out.write(output)











ciona_in.close()
ciona_out.close()
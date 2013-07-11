#!/usr/bin/python

#this script will create working fasta files out of the results of the the hsa X octProtDB (mbh) (non-selective.k) blasts (simultaneously creates three fasta files


###IOin

#input the octopus genome fasta file (frmt: > [pacID] [Hsa-top hit (if present)] \n [sequence])

octFasta_in = open( '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/octProteome.fa', 'r' )

#input the three blast reports

blastE10_in = open( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.001','r' )
blastE1_in = open( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.002','r' )
blastE001_in = open( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.003' ,'r' )

###IOout

#output three fasta files (frmt: > [pacID] [Hsa-top hit (if present)] \n [sequence] )

blastE10_out = open ( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/mbh.candidate.e_val10.fa', 'a' )
blastE1_out = open ( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/mbh.candidate.e_val10.fa', 'a' )
blastE001_out = open ( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/mbh.candidate.e_val0.01','a')

###parse 1###

##for each blast report, read in all the top hits and add the hit pacID's to a list

#declare variables

blastE10_list = []
blastE1_list = []
blastE001_list = []


#read in the blast reports (uses same algorithim three times)

for line in blastE10_in:
	lineSplit = line.split(' ')
	
	#this identifies a hit in the blast report then appends it to a list of pacID's (the pacID's of the hits)
	if lineSplit[0][0:4] == 'lcl|': 
		blastE10_list.append(lineSplit[0][4:]) 
		print len(blastE10_list)
	
	
	
	
blastE10_in.close()
blastE10_out.close()
blastE1_in.close()
blastE1_out.close()
blastE001_in.close()
blastE001_out.close()	
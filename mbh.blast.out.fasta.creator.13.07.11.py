#!/usr/bin/python

#this script will create working fasta files out of the results of the the hsa X octProtDB (mbh) (non-selective.k) blasts (simultaneously creates three fasta files


###IOin

#input the octopus genome csv file (frmt: [PFAM description]	[genes with this PFAM]	[PANTHER]	[PANTHER description]	[genes with this PANTHER]	[best human hit]	[human hit description]	[peptide])

octFasta_in = open( '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/oct_v2_fasta.txt', 'r' )

#input the three blast reports

blastE10_in = open( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.001','r' )
blastE1_in = open( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.002','r' )
blastE001_in = open( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.003' ,'r' )

###IOout

#output three fasta files (frmt: > [pacID] [Hsa-top hit (if present)] \n [sequence] )

blastE10_out = open ( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/mbh.candidate.e_val10.fa', 'a' )
blastE1_out = open ( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/mbh.candidate.e_val1.fa', 'a' )
blastE001_out = open ( '/Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/mbh.candidate.e_val0.01.fa','a')

###parse 1###

##for each blast report, read in all the top hits and add the hit pacID's to a list, then make every entry in the lists unique

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

for line in blastE1_in:
	lineSplit = line.split(' ')
	
	#this identifies a hit in the blast report then appends it to a list of pacID's (the pacID's of the hits)
	if lineSplit[0][0:4] == 'lcl|': 
		blastE1_list.append(lineSplit[0][4:]) 
		
for line in blastE001_in:
	lineSplit = line.split(' ')
	
	#this identifies a hit in the blast report then appends it to a list of pacID's (the pacID's of the hits)
	if lineSplit[0][0:4] == 'lcl|': 
		blastE001_list.append(lineSplit[0][4:]) 


#make every entry in the lists unique

blastE10_list = list(set(blastE10_list))
blastE1_list = list(set(blastE1_list))
blastE001_list = list(set(blastE001_list))

###parse 2###

##for each entry in the list, fetch the corresponding octopus fasta entry

#declare variables

#read every line of csv file, then test to see if the pacID is in a blast_list. if there is a match, append the fasta entry into the fasta file

for line in octFasta_in:
	lineSplit = line.split('\t')
	pacID = lineSplit[ 0 ]
	if pacID in blastE1_list:
		bhh = lineSplit[12]
		peptide = lineSplit[14]
		output = '>' + pacID + ' ' #information is always present
		#append bhh onto output (this info may or may not be present
		if bhh:
			output = output + 'Hsa-' + bhh + '\n' + peptide + '\n'
		if not bhh:
			output = output + 'No best human hit identified in Excel file' + '\n' + peptide + '\n'
		blastE1_out.write(output)
	if pacID in blastE001_list:
		bhh = lineSplit[12]
		peptide = lineSplit[14]
		output = '>' + pacID + ' ' #information is always present
		#append bhh onto output (this info may or may not be present
		if bhh:
			output = output + 'Hsa-' + bhh + '\n' + peptide + '\n'
		if not bhh:
			output = output + 'No best human hit identified in Excel file' + '\n' + peptide + '\n'
		blastE001_out.write(output)
	if pacID in blastE10_list:
		bhh = lineSplit [12]
		peptide = lineSplit[14]
		output = '>' + pacID + ' ' #information is always present
		#append bhh onto output (this info may or may not be present
		if bhh:
			output = output + 'Hsa-' + bhh + '\n' + peptide + '\n'
		if not bhh:
			output = output + 'No best human hit identified in Excel file' + '\n' + peptide + '\n'
		blastE10_out.write(output)
    

print 'done'
 

	
	
blastE10_in.close()
blastE10_out.close()
blastE1_in.close()
blastE1_out.close()
blastE001_in.close()
blastE001_out.close()	
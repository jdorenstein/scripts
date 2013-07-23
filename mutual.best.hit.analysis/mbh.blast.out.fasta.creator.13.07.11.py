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
dict_key = 1
blastE10_hsa = []
blastE1_hsa = []
blastE001_hsa = []
is_top = True
#read in the blast reports (uses same algorithim three times)

for line in blastE10_in: #split the blast report up on the lines
	lineSplit = line.split(' ')
	if lineSplit[0] == 'Query=': #if the script finds a query, it appends the query's id onto the blast_hsa array's. then, it sets is_top to true, which tells the script to record the first top hit it finds
		blastE10_hsa.append(lineSplit[1])
		is_top = True
	#if the line is a result and is_top is True, then the result's id is appended onto blast_list
	if lineSplit[0][0:4] == 'lcl|' and is_top == True:
		blastE10_list.append(lineSplit[0][4:])
		is_top = False
		
for line in blastE1_in:
	lineSplit = line.split(' ')
	if lineSplit[0] == 'Query=': #if the script finds a query, it appends the query's id onto the blast_hsa array's. then, it sets is_top to true, which tells the script to record the first top hit it finds
		blastE1_hsa.append(lineSplit[1])
		is_top = True
	#if the line is a result and is_top is True, then the result's id is appended onto blast_list
	if lineSplit[0][0:4] == 'lcl|' and is_top == True: 
		blastE1_list.append(lineSplit[0][4:]) 
		is_top = False
			
for line in blastE001_in:
	lineSplit = line.split(' ')
	if lineSplit[0] == 'Query=': #if the script finds a query, it appends the query's id onto the blast_hsa array's. then, it sets is_top to true, which tells the script to record the first top hit it finds
		blastE001_hsa.append(lineSplit[1])
		is_top = True
	#if the line is a result and is_top is True, then the result's id is appended onto blast_list
	if lineSplit[0][0:4] == 'lcl|' and is_top == True: 
		blastE001_list.append(lineSplit[0][4:]) 
		is_top = False


###parse 2###

##for each entry in the list, fetch the corresponding octopus fasta entry

#new method for parsing the CSV file

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

#now, for each of the blast_list files, the script will use the entry as a key in the octopus fasta file to create the formatted output
num = 0
for item in blastE10_list:	
	output = '>' + octFasta[item][0] + ' ' + octFasta[item][1] + blastE10_hsa[num] + '\n' + octFasta[item][2] 
	blastE10_out.write(output)
	num = num + 1
num = 0
for item in blastE1_list:
	output = '>' + octFasta[item][0] + ' ' + octFasta[item][1] + blastE1_hsa[num] + '\n' + octFasta[item][2]
	blastE1_out.write(output)
	num = num + 1
num = 0
for item in blastE001_list:
	output = '>' + octFasta[item][0] + ' ' + octFasta[item][1] + blastE001_hsa[num] + '\n' + octFasta[item][2]
	blastE001_out.write(output)
	num = num + 1

print 'done'
 

	
	
blastE10_in.close()
blastE10_out.close()
blastE1_in.close()
blastE1_out.close()
blastE001_in.close()
blastE001_out.close()	
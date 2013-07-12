#!/usr/bin/python

#this script will sort the output of the blast reports in order to determine if the hsa query is the top hit when the octopus top hit is blasted against the human database

###IOin
#frmt: query= pacid hsa-xxx: hsa_input_query
#frmt: lcl|hsa_query_top_hit
blastE10_in = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.007' , 'r' )
blastE1_in = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.008' , 'r' )
blastE001_in = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.blast.mbh.009' , 'r' )

###IOout

mbhE10_out = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.mbh.e_val10','a')
notE10_out = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.not.mbh.e_val10','a')
mbhE1_out = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.mbh.e_val1','a')
notE1_out = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.not.mbh.e_val1','a')
mbhE001_out = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.mbh.e_val0.01','a')
notE001_out = open( 'Users/ionchannel/research/projects/ionchannels/non-selective.k/geneset/out.not.mbh.e_val0.01','a')

###parse 1###

#declare variables

hsa_input_query = ''
hsa_query_top_hit = ''
oct_input_query = ''
is_top = True

#look at each blast report and see if the last entry of the query matches the top hit (if hsa_input_query == hsa_query_top_hit)


#for e_value 10
for line in blastE10_in:
	lineSplit = line.split(' ')
		lineSplit = line.split(' ')
	if lineSplit[0] == 'Query=': #if the script finds a query, it sets hsa_input_query to the last part of the line
		is_top = True
		hsa_input_query = lineSplit[-1]
		oct_input_query = lineSplit[1]
	#if the line is a result and is_top is True, then the result's id is appended onto blast_list
	if lineSplit[0][0:3] == 'sp|' and is_top == True:
		hsa_query_top_hit = lineSplit[0]
		if hsa_input_query == hsa_query_top_hit:
			output = hsa_input_query + ' -> ' + oct_input_query + ' -> ' + hsa_query_top_hit 
			mbhE10_out.write(output)
		if hsa_input_query == hsa_query_top_hit:
			output = hsa_input_query + ' -> ' + oct_input_query + ' -> ' + hsa_query_top_hit
			notE10_out.write(output)
		is_top = False
		
#for e_value 1		
for line in blastE1_in:
	lineSplit = line.split(' ')
		lineSplit = line.split(' ')
	if lineSplit[0] == 'Query=': #if the script finds a query, it sets hsa_input_query to the last part of the line
		is_top = True
		hsa_input_query = lineSplit[-1]
		oct_input_query = lineSplit[1]
	#if the line is a result and is_top is True, then the result's id is appended onto blast_list
	if lineSplit[0][0:3] == 'sp|' and is_top == True:
		hsa_query_top_hit = lineSplit[0]
		if hsa_input_query == hsa_query_top_hit:
			output = hsa_input_query + ' -> ' + oct_input_query + ' -> ' + hsa_query_top_hit 
			mbhE1_out.write(output)
		if hsa_input_query == hsa_query_top_hit:
			output = hsa_input_query + ' -> ' + oct_input_query + ' -> ' + hsa_query_top_hit
			notE1_out.write(output)
		is_top = False
		
		
#for e_value 0.01	
for line in blastE001_in:
	lineSplit = line.split(' ')
		lineSplit = line.split(' ')
	if lineSplit[0] == 'Query=': #if the script finds a query, it sets hsa_input_query to the last part of the line
		is_top = True
		hsa_input_query = lineSplit[-1]
		oct_input_query = lineSplit[1]
	#if the line is a result and is_top is True, then the result's id is appended onto blast_list
	if lineSplit[0][0:3] == 'sp|' and is_top == True:
		hsa_query_top_hit = lineSplit[0]
		if hsa_input_query == hsa_query_top_hit:
			output = hsa_input_query + ' -> ' + oct_input_query + ' -> ' + hsa_query_top_hit 
			mbhE001_out.write(output)
		if hsa_input_query == hsa_query_top_hit:
			output = hsa_input_query + ' -> ' + oct_input_query + ' -> ' + hsa_query_top_hit
			notE001_out.write(output)
		is_top = False
		
#close files
blastE10_in = 
blastE1_in = 
blastE001_in = 

###IOout

mbhE10_out.close()
notE10_out.close()
mbhE1_out.close()
notE1_out.close()
mbhE001_out.close()
notE001_out.close()
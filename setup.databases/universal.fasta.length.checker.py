#!/usr/bin/python

IOfasta_in = open('./candidate.geneset.fa', 'r' )

PacID_array = [] #used to hold on to the pacID's so that they can be counted and then used to evaluate the BLASTS

for line in IOfasta_in:
	
	lineSplit = line.split(' ')  #split the line on the whitespaces. this allows the header to be split up
	
	if lineSplit[0][0] == '>':   #pick out the pacID by identifying which part of a line starts with '>'. this also avoides selecting lines
		pacID = lineSplit[0][1:] #assign the pacID to the variable pacID
		PacID_array.append( pacID )  #append pacID into PacID_array
		
print len(PacID_array)
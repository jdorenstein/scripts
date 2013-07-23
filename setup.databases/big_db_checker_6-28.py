#!C:\Python27 

#script: db_checker_6-17
#function: Check that the BLAST db (octProteomedb) was created properly. These script tests for 3 conditions. T
	#1: check that the number of headers in the FASTA db (octProteome.fa) matches the number of genes 
	#2: create a dictionary that contains the top hit and E-value for each query (key value is the queryID)_
	#3: check that every top hit in the BLAST matches the query and has an E-value of 0.0



### IOin



#input the FASTA file (octProteome.fa)
#file format: [>[pacid] Hsa-[best known human hit]]

IOfasta_in = open ( '/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/12.proteomes.fa', 'r' )
IOblast_in = open ( '/Users/ionchannel/research/db/blast/12.proteomes/000.command/12.BLAST.out', 'r' )


###IOout 


#output an array that is made up of the pacid's. NOTE: THIS IS ONLY FOR USE IN SCRIPT 2 AND 3
#file format: [pacid] \n [pacid] \n [pacid] ...

IOpacid_out = open( '/Users/ionchannel/research/db/blast/12.proteomes/000.command/line.test.txt', 'a' )
IOError_out = open( '/Users/ionchannel/research/db/blast/12.proteomes/000.command/12.BLAST.errors.script.txt', 'a' )


###PART 1###



##parse 1 part 1: create array, each entry is broken up and the PacID_array is created


PacID_array = [] #used to hold on to the pacID's so that they can be counted and then used to evaluate the BLASTS

for line in IOfasta_in:
	
	lineSplit = line.split(' ')  #split the line on the whitespaces. this allows the header to be split up
	#IOpacid_out.write( line )
	if lineSplit[0][0] == '>':   #pick out the pacID by identifying which part of a line starts with '>'. this also avoides selecting lines
		pacID = lineSplit[0][1:] #assign the pacID to the variable pacID
		PacID_array.append( pacID )  #append pacID into PacID_array

##parse 1 part 2: test the length of PacID_array, print the value to the screen

#print len(PacID_array)
	


###parse 2###



##parse 2: create dictionary of the queries and their results, use the pacID as the "key" for the entry

blastDict = {}
dict_key = 1
is_top_hit = 'TRUE'
position_in_alignments = 1


for line in IOblast_in:
	
	lineSplit = line.split(' ') #split the line based on whitespaces 
	if lineSplit[0] == 'Query=': #this creates the key that is to be used to create the dictionary entry
		dict_key = lineSplit [1] 
		is_top_hit = 'TRUE'
		position_in_alignments = 1
	if is_top_hit == 'TRUE': #is_top_hit is being used to only read the top hit
	
		if lineSplit[0][0:4] == 'lcl|': #this is to create the dictionary entry
			top_hit = lineSplit[0][4:]  #top_hit is the ID of the top hit
			#len_line = len( lineSplit)  #len_line is the length of the lineSplit array. this is used to retrieve the E-value
			#if len_line == 14:  #if len_line = 14, then the evalue is 0.0, so the value that is several spaced in is used
			#	E_val = lineSplit[ len_line -4 ] 
			#	E_val = float(E_val)
			
			array = lineSplit
			array.reverse()
			#print array
			for element in array:
				if element and element != '\n':
					break
			if element == '0.0':
				E_val = float(element)
			elif 'e' in element:
				E_val_temp = element
				E_split = E_val_temp.split( 'e' )
				E_head = int(E_split[0], base=10)
				E_tail = int(E_split[1], base=10)
				E_val =  10**E_tail
				E_val = E_val * E_head
				#print E_val
			if element != '0.0' and 'e' not in element:
				E_val = float(element)				
			if dict_key == top_hit:  #if the dict_key is equal to the top_hit, then the entry is put into the dictionary (records the id, the e_value and the position in the results
				blastDict[dict_key] = [ top_hit, E_val, position_in_alignments ] 
				is_top_hit = 'FALSE'  #this stops the program from scanning the descriptions until the next descriptions are reached
				position_in_alignmets = 1
				IOpacid_out.write( dict_key )
			if line != top_hit: #if line != top hit, then add 1 to position and move to next line
				position_in_alignments = position_in_alignments + 1
			
			if position_in_alignments > 11: #if the position exceedes the number of results, reset counter, exit loop, and create special entry in dictionary
				is_top_hit = 'FALSE'
				blastDict[dict_key] = [ 'null', 100, 11 ]
				print 's'
				#break
			



###parse 3###



##parse 3: test to see if, for every FASTA entry, the entry is its own top hit and the E-value is <= 0.001


no_probs = 'TRUE'
for id in PacID_array: #central for loop, this runs the test for each entry in the FASTA database
	is_top_match = 'FALSE'
	E_is_good = 'FALSE'
	#print (blastDict[id][0])
	if blastDict[id][0] == id: #if the top_hit matches the query, then is_top_match is set to TRUE
		is_top_match = 'TRUE'
		#print 'T'
		if blastDict[id][1] < 0.001: #if the E-value is less than 0.001, then E_is_good is set to TRUE
			E_is_good = 'TRUE' 
		else:
			if blastDict[id][2] < 11: 
				IOError_out.write( blastDict[id][0] + ' E VALUE IS TOO HIGH')
				no_probs = 'FALSE'
			else:
				IOError_out.write( blastDict[id][0] + ' QUERY IS NOT IN RESULTS' )
				no_probs = 'FALSE'
	else:
		IOError_out.write( id + ' Top Hit Does Not Match')
		no_probs = 'FALSE'
	#if is_top_match == 'FALSE': #prints out an error if there is not a match
	#	print 'ERROR'
	#if E_is_good == 'FALSE': #prints out an error if E is not 0.0
	#	print 'ERROR'
if no_probs == 'TRUE':
	print 'yay'



IOfasta_in.close()
IOblast_in.close()
IOError_out.close()
#print'end of script' 
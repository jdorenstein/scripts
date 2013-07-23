#this script reads in a blast report (outfmt 6 and 7 only), and checks that each query hits to itself

###IOin###
#note: for now, this script only checks in one location, but it can be adapted to parse other locations
blast_in = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/out.blast.test.db.001','r')

###IOout###

report_ok = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/db.checker.001.ok', 'a')
report_errors = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/db.checker.001.errors', 'a')


###Parse 1###

##read in the blast output. check that every query has a result
#declare variables
queryID = ''
resultID = ''
query_list = [] #query_list is the list of queryID's. this is used to keep track of all the queries
query_hits = [] #query_hits is the list of queryID's that blasted to themselves.

for line in blast_in:
	#if the line starts with '#', reset queryID and result ID
	if line[0] == '#':
		queryID = ''
		resultID = ''
	else:
		lineSplit = line.split('\t')
		#set queryID to the query
		queryID = lineSplit[0]
		#add the query to query_list if it is not already in the list
		if queryID not in query_list:
			query_list.append(queryID)
		#check to see if the result matches the query. if the result matches the query, then put the queryID into query_hits
		if queryID == lineSplit[1]:
			if queryID not in query_hits:
				query_hits.append(queryID)

print 'Finished gathering data'

###Parse 2###

##go through the query_list list. see if each entry is in query_hits. if it is, write it to db.checker.001.ok. if it is not, write it to db.checker.001.errors

for item in query_list:
	if item in query_hits:
		report_ok.write(item + '\n' )
	if item not in query_hits:
		report_errors.write(item + '\n')
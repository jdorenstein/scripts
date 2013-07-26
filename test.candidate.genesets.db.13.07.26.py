blast_in = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/out.blast.test.db.001','r')
headers_list = []
errors_list = []
query = ''
result = ''
top_hit = True
for line in blast_in:
	if line[0] != '#':
		if top_hit == True:
			lineSplit = line.split('\t')
			query = lineSplit[0]
			result = lineSplit[1]
			if query == result:
				headers_list.append(query)
			if query != result:
				errors_list.append(query + '  ' + result)
			top_hit = False
	if line[0] == '#':
		top_hit = True
		query = ''
		result = ''
		
print errors_list
blast_in.close()
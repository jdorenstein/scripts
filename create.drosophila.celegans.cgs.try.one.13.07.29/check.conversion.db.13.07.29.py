import os

###IOin###

conversion_path = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/id.hsa.drosophila.celegans.conversion'
conversion_in = open(conversion_path, 'r')

cgs_id_in = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/candidate.genesets.id.list'
cgs_in = open(cgs_id_in, 'r')
hsa_proteome_list = []
for line in conversion_in:
	lineSplit = line.split('\t')
	human_line = lineSplit[0].split(' ')
	for item in human_line:
		if item not in hsa_proteome_list:
			hsa_proteome_list.append(item)
			
for line in cgs_in:
	line = line[:-1]
	if line not in hsa_proteome_list:
		print line
	
	
conversion_in.close()
cgs_in.close()
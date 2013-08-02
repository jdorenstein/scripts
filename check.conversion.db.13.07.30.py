import os

###IOin###

conversion_path = '/Users/ionchannel/research/projects/ionchannels/k+/geneset/gene.hsa.drosophila.celegans.conversion'
conversion_in = open(conversion_path, 'r')
which_dir = raw_input('Enter the name of the ionchannel folder:')
cgs_id_in = '/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.genesets.gene.list'
cgs_in = open(cgs_id_in, 'r')
cgs_out = open('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/candidate.geneset.gene.hm.list', 'a')
hsa_proteome_list = []
for line in conversion_in:
	lineSplit = line.split('\t')
	human_line = lineSplit[0].split(' ')
	for item in human_line:
		if item not in hsa_proteome_list:
			hsa_proteome_list.append(item)
			
for line in cgs_in:
	line = line[:-1]
	if line in hsa_proteome_list:
		cgs_out.write(line + '\n')
	
	
conversion_in.close()
cgs_in.close()
cgs_out.close()
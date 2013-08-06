import os


conversion_in = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/hsa.least.coverage.13.08.05/hsa.least.coverage.conversion.13.08.05.noHits' ,'r')
hsa_cgs = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/create.drosophila.celegans.cgs.try.one.13.07.29/candidate.genesets.id.list', 'r')
conversion_list = []
for line in conversion_in:
	lineSplit = line.split('-')
	conversion_list.append(lineSplit[1])

for line in hsa_cgs:
	if line in conversion_list:
		print line
		
conversion_in.close()
hsa_cgs.close()
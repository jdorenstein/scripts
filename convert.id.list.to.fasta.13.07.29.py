drosophila = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.drosophila/candidate.geneset.id.list' ,'r')
celegans = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.celegans/candidate.geneset.id.list' , 'r')
drosophila_out = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.drosophila/candidate.geneset.id.list.header' ,'a')
celegans_out = open('/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.celegans/candidate.geneset.id.list.header' , 'a')
#add the header to the new file
for line in drosophila:
	output = 'drosophila-' + line
	drosophila_out.write(output)
for line in celegans:
	output = 'caenorhabditis-' + line
	celegans_out.write(output)
	
celegans.close()
drosophila.close()


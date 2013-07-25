import os

which_folder = raw_input('Enter folder name:')
os.system('mkdir /Users/ionchannel/research/projects/ionchannels/' + which_folder + '/geneset/candidate.geneset.uniprot')
os.system('mv /Users/ionchannel/research/projects/ionchannels/' + which_folder + '/geneset/candidate.geneset.fa /Users/ionchannel/research/projects/ionchannels/' + which_folder + '/geneset/candidate.geneset.uniprot/')
log_out = open('/Users/ionchannel/research/projects/ionchannels/' + which_folder + '/000.command.txt', 'a')
cgs_in = open('/Users/ionchannel/research/projects/ionchannels/' + which_folder +'/geneset/candidate.geneset.uniprot/candidate.geneset.fa', 'r')
headers_out = open('/Users/ionchannel/research/projects/ionchannels/' + which_folder +'/geneset/candidate.geneset.uniprot/candidate.geneset.headers.uniprot.txt', 'a')
for line in cgs_in:
	if line[0] == '>':
		headers_out.write(line)
log_entry = '\n' + '\n' + '\n' + '==================13.07.24===' + '\n' + '\n' + '\n' + 'MOVED candidate.geneset.fa INTO ./candidate.geneset.uniprot/' + '\n' + '\n' + '\n' + '--------------------------' + '\n' + '\n' + '\n' + 'RUN print.headers.of.cgs.13.07.24.py TO CREATE (candidate.geneset.headers.uniprot.txt)'		
#print log_entry
log_out.write(log_entry)
cgs_in.close()
headers_out.close()
log_out.close()
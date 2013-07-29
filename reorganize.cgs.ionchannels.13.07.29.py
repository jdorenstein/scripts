import os

#this script is designed to create a 'setup.ensembl.13.07.25' folder in each ionchannel folder except trp. then, it will move the cgs test(s), the header list, and the error report into the folder (git mv)

for fileName in os.listdir('/Users/ionchannel/research/projects/ionchannels/'):
	#the script ignores the '.<xxx>','trp','candidate.genesets.db',and 'README.md' files/folders
	if 'trp' not in fileName and 'candidate.genesets.db' not in fileName and 'README.md' not in fileName and fileName[0] != '.':
		#input the command log, append the log entry to the command log
		#log_path = '/Users/ionchannel/research/projects/ionchannels/' + fileName + '/000.command.txt'
		#log_in = open(log_path, 'a')
		#log_entry = '\n \n \n' + '==================13.07.29===' + '\n \n \n' + 'MOVE (errors.candidate.geneset.fa) (new.cgs.headers.txt) (out.blast.test.new.cgs.001(002)) INTO (/setup.ensembl.13.07.25)'
		#log_in.write(log_entry)
		#log_in.close()
		#create system path variables
		setup_path = '/Users/ionchannel/research/projects/ionchannels/' + fileName + '/geneset/setup.ensembl.13.07.25/'
		geneset_path = '/Users/ionchannel/research/projects/ionchannels/' + fileName + '/geneset/'
		#create a new folder named 'setup.ensembl.13.07.25'
		#sys_cmd = 'mkdir /Users/ionchannel/research/projects/ionchannels/' + fileName + '/geneset/setup.ensembl.13.07.25'
		#print sys_cmd
		#os.system(sys_cmd)
		sys_cmd = 'git mv ' + geneset_path + 'errors.candidate.geneset.fa ' + setup_path
		print sys_cmd
		os.system(sys_cmd)
		sys_cmd = 'git mv ' + geneset_path + 'new.cgs.headers.txt ' + setup_path
		print sys_cmd
		os.system(sys_cmd)
		sys_cmd = 'git mv ' + geneset_path + 'out.* ' + setup_path
		print sys_cmd
		os.system(sys_cmd)
		

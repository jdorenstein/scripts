#this script is designed to list the first line of all the files in the 13.proteomes library

for fileName in os.listdir('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/'): #list the ionchannel folders that the user can enter
	if fileName[0] == 'p':
		str = open(
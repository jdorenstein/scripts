
import os

which_dir = 'trp'
name_blast_report_out = 'out.blast.fam.' + raw_input('Enter blast report suffix (.###)')
cgs_in = open('/Users/ionchannel/research/projects/ionchannels/trp/geneset/candidate.geneset.mapped.fa','r')
###parse 5###

##scan the blast output. find the first hit that is a human gene, then see if it is located in the human cgs (look for homo-)
cgs_header_list = []
#scan the mapped candidate geneset. put each header into a list
for line in cgs_in:
	if line[0] == '>':
		lineSplit = line.split(' ')
		cgs_header_list.append(lineSplit[0][1:])

#scan the blast output, take the first human result and check if the header is in the cgs_header_list. if it is, output it to the match file. if it is not, output if to the non-match file (append match and non_match to the end of the name of the blast report)
blast_report = open('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_blast_report_out, 'r')
found_family = open('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_blast_report_out + 'fam', 'a')
not_family = open('/Users/ionchannel/research/projects/ionchannels/' + which_dir + '/geneset/' + name_blast_report_out + 'not.fam', 'a')
query_id_1 = ''
found_an_entry = False
output = ''
for line in blast_report:
	#for each line, see if it starts with #. if it does, reset the line counter (to 0). if it does not, see if the result is a human gene in the cgs folder. sort the gene into the appropriate file based on this information
	if line[0] == '#':
		lineSplit = line.split(' ')
		if lineSplit[2] == 'hits':
			if found_an_entry == False:
				not_family.write(output)
			found_an_entry = False
	else:
		lineSplit = line.split('\t')
		query_id_1 = lineSplit[0]
		if found_an_entry == False:
			output = lineSplit[0] + ' ' + lineSplit[1] + '\n'
			if lineSplit[1] in cgs_header_list:
				found_family.write(output)
				found_an_entry = True






blast_report.close()
found_family.close()
not_family.close()

#fasta_out.close()
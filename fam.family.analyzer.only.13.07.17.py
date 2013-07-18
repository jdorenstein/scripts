
import os
##output fmt: [query] [hit] [evalue] [bitscore]



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
human_gene_found = ''
line_number_count = 1
#scan each line, check for '#' and 'lcl|'
for line in blast_report:
	#check to see if the line is a comment line. if it is, see if it is the last comment line. if it is the last comment line, record the output list (if there are no hits, then put in 'no hits'
	if line[0] == '#':
		lineSplit = line.split(' ')
		if lineSplit[2] == 'hits':
			human_gene_found = ''
			if found_an_entry == False: #if the script reaches a new query and no human hit was found, then the script notes that no human hit was found (also, note that the script also checks to see if it is scanning the first lines of the output. if this is the case, it will skip these steps
				if line_number_count > 5: 
					output = query_id_1 + ' NO HUMAN HIT' + '\n'
					not_family.write(output)
				query_id_1 = ''
			if found_an_entry == True:
				lineSplit = output.split(' ')
				if lineSplit[1] in cgs_header_list:
					output = output + '\n'
					found_family.write(output)
			found_an_entry = False
	else:
		#look for the first human hit (must still figure out how to deal with ciona)
		lineSplit = line.split('\t')
		query_id_1 = lineSplit[0]
		if found_an_entry == True and human_gene_found == lineSplit[1]: #if the script has found an entry and if the hit id is equal to the first human gene found
			#append the evalue and the bit score to output
			output = output + ', ' + lineSplit[10] + ' ' + lineSplit[11][:-1]
		if found_an_entry == False and lineSplit[1][0:3] == 'hom': #if the script finds the FIRST human hit, record it as human_gene_found
			human_gene_found = lineSplit[1]
			output = lineSplit[0] + ' ' + lineSplit[1] + ' ' + lineSplit[10] + ' ' + lineSplit[11][:-1] #output frmt = [query (oct)] [hit] [evalue] [bit score], [evalue 2] [bit score 2] ...
			found_an_entry = True
	line_number_count = line_number_count + 1
			
			

print cgs_header_list




blast_report.close()
found_family.close()
not_family.close()

#fasta_out.close()
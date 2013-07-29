import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#this script reads in the conversion database and candidate.genesets.id.list (hsa); it creates (candidate.genesets.id.list) file in (geneset.drosophila/) and (geneset.celegans/) using the conversion file. also, it creates (id.hsa.drosophila.celegans.conversion) in (genesets/)

###IOin###

##read in (candidate.genesets.id.list)
cgs_id_list_path = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/candidate.genesets.id.list'
cgs_id_in = open(cgs_id_list_path, 'r')
##read in the conversion file
conversion_path = '/Users/ionchannel/research/tools/db/ortholog.conversion/Compara.72.protein.nhx.emf'
conversion_in = open(conversion_path, 'r')
###IOout###

##create the three output file paths
drosophila_id_path = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.drosophila/candidate.geneset.id.list'
celegans_id_path = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.celegans/candidate.geneset.id.list'
hsa_id_path = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/id.hsa.drosophila.celegans.conversion'

##open the three output files
drosophila_out = open(drosophila_id_path, 'a')
celegans_out = open(celegans_id_path, 'a')
hsa_id_out = open(hsa_id_path, 'a')  

###Parse 1###

##read in the conversion file and create a dictionary that uses the human identifier as the key and stores the list of drosophila orthologs in position [0] and the list of celegans orthologs in position [1]
###if there is more than one human gene, use both for the key (<id 1>, <id 2>)

##declare variables
hsa_key = ''
hsa_key_list = []
drosophila_list = ''
celegans_list = ''
line_number = 0
conversion_dict = {}
##read in each line of the conversion file
for line in conversion_in:
	line_number = line_number + 1
	#if the line starts with 'SEQ', see if the line contains a gene of interest. if so, append it to the correct string
	if line[0:3] == 'SEQ':
		#split the line on spaces, look to see if lineSplit[1] == caenorhabditis_elegans, homo_sapiens, or drosophila_melanogaster. then append the id to the correct string
		lineSplit = line.split(' ')
		if lineSplit[1] == 'homo_sapiens':
			if hsa_key == '':
				hsa_key = lineSplit[2]
				hsa_key_list.append(lineSplit[2])
			else:
				hsa_key = hsa_key + ' ' + lineSplit[2]
		if lineSplit[1] == 'drosophila_melanogaster':
			if drosophila_list == '':
				drosophila_list = lineSplit[2]
			else:
				drosophila_list = drosophila_list + ' ' + lineSplit[2]
		if lineSplit[1] == 'caenorhabditis_elegans':
			if celegans_list == '':
				celegans_list = lineSplit[2]
			else:
				celegans_list = celegans_list + ' ' + lineSplit[2]
	if line[0:4] == 'DATA':
		#if there is a human gene, create a dictionary entry using the human gene as the key. if there is no human gene, create a dictionary entry using the line number as an id. also, write the conversion info to hsa_id_out
		if hsa_key_list:
			output = hsa_key + '\t' + drosophila_list + '\t' + celegans_list + '\n'
		hsa_id_out.write(output)
		if hsa_key_list: #if there are any entries in hsa_key_list, create a dictionary entry for each entry
			for item_key_hsa in hsa_key_list:
				conversion_dict[item_key_hsa] = [drosophila_list,celegans_list]
		#if hsa_key == '':
		#	conversion_dict[line_number] = [drosophila_list,celegans_list]
		#reset the hsa, drosophila, and celegans strings for the next tree
		hsa_key = ''
		drosophila_list = ''
		celegans_list = ''
		hsa_key_list = []
###Parse 2###
drosophila_hits = 0
celegans_hits = 0
drosophila_out_list = []
celegans_out_list = []
##read in cgs_id_in. for each gene id, see if it is in the keys of conversion_dict. if it is, print the conversion info into the proper files
for key_name_long in cgs_id_in:
	key_name = key_name_long[:-1]
	if key_name in conversion_dict.keys():
		#see if drosophila has any hits, if so, add it to the drosophila id list
		if conversion_dict[key_name][0] != '':
			#split up line on spaces. save each entry into drosophila_out_list
			line_drosophila_split = conversion_dict[key_name][0].split(' ')
			for item in line_drosophila_split:
				if item not in drosophila_out_list: 
					drosophila_out_list.append(item)
			
		#see if celegans has any hits, if so, add it to the celegans id list
		if conversion_dict[key_name][1] != '':
			line_celegans_split = conversion_dict[key_name][1].split(' ')
			for item in line_celegans_split:
				if item not in celegans_out_list:
					celegans_out_list.append(item)
			


###Parse 3###
##write each list to its respective file
for item in drosophila_out_list:
	drosophila_out.write(item + '\n')
	drosophila_hits = drosophila_hits + 1
for item in celegans_out_list:
	celegans_out.write(item + '\n')
	celegans_hits = celegans_hits + 1


print 'DROSOPHILA GENES RECORDED: ' + str(drosophila_hits) + '\n'
print 'CELEGANS GENES RECORDED: ' + str(celegans_hits) + '\n'




conversion_in.close()
cgs_id_in.close()
drosophila_out.close()
celegans_out.close()
hsa_id_out.close()
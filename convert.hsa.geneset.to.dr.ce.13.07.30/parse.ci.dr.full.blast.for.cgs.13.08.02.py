import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def create_hits_dict(blast_in):
	#for each query gene, create a dictionary entry. if the query comes up again, append the hsa result (if present) to the dictionary entry (list). returns a dictionary object
	hits_dict = {}
	for line in blast_in:
		#split the line, set query_id, hit_id
		lineSplit = line.split('\t')
		#split the query on '-'. set the second part as the query_id
		query_split = lineSplit[0].split('-')
		query_id = query_split[1]
		hit_id = lineSplit[1][5:]
		#test to see if there is a human hit. if so, either create a new dictionary entry for the hsa gene containing the query_id or append the query_id to an existing entry (if the hit_id is in the dict keys)
		if hit_id != '':
			if hit_id in hits_dict.keys():
				hits_dict[hit_id][0].append(query_id)
			if hit_id not in hits_dict.keys():
				hits_dict[hit_id] = [[query_id]]
	return (hits_dict)
		

def create_hits_list(dict_in, hsa_id):
	##for each protein id in candidate.genesets.id.list, see if it is in the list of keys for the the hits dictionaries. if it is, add the contents to the proper hits list. returns a list of hits (not human) (unique)
	list_hits = []
	for item in hsa_id:
		line = item
		print line
		#if the line is in dict in, add the contents to the hits list (check each one to see if it is in the list
		if line in dict_in.keys():
			list_temp_hits = dict_in[line][0]
			for item in list_temp_hits:
				check_temp = item + '\t' + 'homo-' + line
				if check_temp not in list_hits:
					list_hits.append(check_temp)
	return (list_hits)


###this script is designed to parse the output of eric's formatted blast reports and pull out the top hit for each gene in the cgs

###IOin###

##this script does not ask the user for any input 
# OUTPUT top hits and no hits for each (proteome) x (proteome) blast
# format: (query) (top hit) (bit score) (evalue) (percent identity) (alignment length) (query start) (query stop)


path_to_blast = '/Users/ionchannel/research/projects/blast.reports.130801/'
ce_hs_path = path_to_blast + 'out.topHits.caenorhabditisQ.homoS'
dr_hs_path = path_to_blast + 'out.topHits.drosophilaQ.homoS'

ce_hs_blast = open(ce_hs_path, 'r')
dr_hs_blast = open(dr_hs_path, 'r')

#hsa cgs (frmt: (
hsa_id_list_path = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/create.drosophila.celegans.cgs.try.one.13.07.29/candidate.genesets.id.list'
hsa_id = open(hsa_id_list_path, 'r')


###IOout###

##output frmt: (proteinID) \n
path_cgs_out = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset.'
path_dr_out = path_cgs_out + 'drosophila/cgs.list.parse.13.08.02'
path_ce_out = path_cgs_out + 'celegans/cgs.list.parse.13.08.02'

dr_cgs_out = open(path_dr_out, 'a')
ce_cgs_out = open(path_ce_out, 'a')


###Parse 1###

##read in the candidate geneset id list (does not have three genes)
hsa_id_list = []
for line in hsa_id:
	#add in the human protein id, remove the newline
	hsa_id_list.append(line[:-1])
	
###Parse 2###

##parse through the formatted blast reports (xx_hs.blast). USES A FUNCTION (SEE create_hits_dict) 
ce_hits_dict = {}
dr_hits_dict = {}

ce_hits_dict = create_hits_dict(ce_hs_blast)
dr_hits_dict = create_hits_dict(dr_hs_blast)

###Parse 3###

##USES A FUNCTION (see create_hits_list)
ce_hits_list = []
dr_hits_list = []

ce_hits_list = create_hits_list(ce_hits_dict, hsa_id_list)
dr_hits_list = create_hits_list(dr_hits_dict, hsa_id_list)		

###Parse 4###

##output the contents of ce hits list and dr hits list to their respective files

for item in ce_hits_list:
	output = 'caenorhabditis-' + item + '\n'
	ce_cgs_out.write(output)
for item in dr_hits_list:
	output = 'drosophila-' + item + '\n'
	dr_cgs_out.write(output)




hsa_id.close()
ce_hs_blast.close()
dr_hs_blast.close()
dr_cgs_out.close()
ce_cgs_out.close()
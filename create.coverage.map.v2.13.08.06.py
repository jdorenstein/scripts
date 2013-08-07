import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def create_hits_dict(blast_in):
	#for each hit gene, create a dictionary entry (use hit as the key). if the query comes up again, append the hsa result (if present) to the dictionary entry (list). returns a dictionary object
	hits_dict = {}
	for line in blast_in:
		#split the line, set query_id, hit_id
		lineSplit = line.split('\t')
		#split the query on '-'. set the second part as the query_id
		query_split = lineSplit[0].split('-')
		query_id = query_split[1]
		hit_split = lineSplit[1].split('-')
		hit_id = hit_split[1]
		#test to see if there is a  hit. if so, either create a new dictionary entry for the gene containing the query_id or append the query_id to an existing entry (if the hit_id is in the dict keys)
		if hit_id != '':
			if hit_id in hits_dict.keys():
				hits_dict[hit_id][0].append(query_id)
			if hit_id not in hits_dict.keys():
				hits_dict[hit_id] = [[query_id]]
	return (hits_dict)
##this script creates a formatted coverage map (Query) (subject) (%coverage) using eric's formatted blast reports
####eric's format: (query) (top hit) (bit score) (evalue) (percent identity) (alignment length) (query start) (query stop)
###IOin###
hsa_prot_length_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteomes.lengths.13.08.07/proteome.homo.sapiens.primary.longest.peptide.lengths'
ce_prot_length_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteomes.lengths.13.08.07/proteome.caenorhabditis.elegans.longest.peptide.lengths'
dr_prot_length_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteomes.lengths.13.08.07/proteome.drosophila.melanogaster.longest.peptide.lengths'
hsa_length = open(hsa_prot_length_path, 'r')
ce_length = open(ce_prot_length_path, 'r')
dr_length = open(dr_prot_length_path, 'r')

###Parse 1###
##read in each length file, and create a dictionary entry for each protein (key = protein id, contains = length)
hsa_length_dict = {}
ce_length_dict = {}
dr_length_dict = {}
for line in hsa_length:
	lineSplit = line.split('\t')
	hsa_length_dict[lineSplit[0]] = [lineSplit[1]]
for line in ce_length:
	lineSplit = line.split('\t')
	ce_length_dict[lineSplit[0]] = [lineSplit[1]]
for line in dr_length:
	lineSplit = line.split('\t')
	dr_length_dict[lineSplit[0]] = [lineSplit[1]]
print '\n \n \n' + '---------------------------' + '\n \n \n' + 'RUN (create.coverage.map.v2.13.08.06.py) TO CREATE'

###Parse 2###
##for each file, create the name of the path and the name of the output file. then, 

for FileName in os.listdir('/Users/ionchannel/research/projects/proteome.analysis/blastReports.and.topHits.130806/'):
	#if the filename has 'out.topHits.', add it to FileNames_list
	if FileName[0:12] == 'out.topHits.' and FileName[-12:] != '.allS.noHits':
		##IOin##
		blast_in_path = '/Users/ionchannel/research/projects/proteome.analysis/blastReports.and.topHits.130806/' + FileName
		blast_in = open(blast_in_path, 'r')
		##IOout##
		output_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/top.hits.coverage.13.08.06/' + FileName + '.coverage'
		output_coverage = open(output_path, 'a')
		
		###Parse 1###
		##for each line in the blast output, check to see if there is a hit for the query. if so, grab the query id and the subject id and calculate the % coverage
		for line in blast_in:
			queryID = ''
			subjectID = ''
			coverage_score = 0
			query_length = ''
			top_hit_length = ''
			query_species = ''
			query_start = ''
			query_end = ''
			lineSplit = line.split('\t')
			#print lineSplit
			#if there is a hit, get the queryID and the subject ID. (do not remove the species name). then, calculate the % coverage using the query length(using the length dictionaries and the species name)
			if lineSplit[1] != '-':
				queryID = lineSplit[0]
				subjectID = lineSplit[1]
				query_start = lineSplit[6] #assign the smaller number
				query_end = lineSplit[7][:-1] #assign the larger number
				top_hit_length = lineSplit[5][:-1]
				#get the species of the query
				query_split = queryID.split('-')
				query_species = query_split[0]
				
				#use the query_species name to pick the correct dictionary and get the length of the query
				if query_species == 'homo':
					query_length = hsa_length_dict[queryID][0]
				if query_species == 'drosophila':
					query_length = dr_length_dict[queryID][0]
				if query_species == 'caenorhabditis':
					query_length = ce_length_dict[queryID][0]
				#calculate the % coverage
					#make all numbers integers
				query_length = float(query_length)
				top_hit_length = float(top_hit_length)
				query_start = float(query_start)
				query_end = float(query_end)
				#coverage_score = query_length / top_hit_length 
				#coverage_score = coverage_score * 100
				coverage_score = query_end - query_start
				coverage_score = coverage_score / query_length
				coverage_score = coverage_score * 100
				coverage_score = str(coverage_score)
				#format the output
				output = queryID + '\t' + subjectID + '\t' + coverage_score + '\n'
				output_coverage.write(output)
		print ' (' + FileName + '.coverage) '
		
		
		
		
		
		
		
		blast_in.close()
		output_coverage.close()
		
		
		
		
hsa_length.close()
ce_length.close()
dr_length.close()
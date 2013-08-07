import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

###this script is designed to take the three coverage maps (one for hsa,drosophila,celegans) and the output of the (models cgs x 13 proteomes [tophits/spp]). then, it calculates the percent coverage of each query/subject, and compares it to the stored coverage for the query.



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
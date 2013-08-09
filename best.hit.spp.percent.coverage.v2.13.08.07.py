import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

#######NOTE: this script REQUIRES THAT ALL INPUTED PROTEIN ID'S ARE FORMATTED AS (speciesName-id)###########
###this script is designed to take the 4 coverage maps (one for hsa,drosophila,celegans) and the output of the (models cgs x 13 proteomes [tophits/spp]). then, it calculates the percent coverage of each query/subject, and compares it to the stored coverage for the query in the inputed blast report. if the percent coverage is >= the stored coverage, it keeps the output and adds it (non-redundently) to the output list of protein id's

##functions##
##make_coverage_dict(coverage_path, noHits_coverage) - Inputs a filepath to the coverage file and the noHits_coverage number. returns a dictionary that contains the query as the key and [% coverage (float)]
def make_coverage_dict(coverage_path, noHits_coverage):
	coverage_in = open(coverage_path, 'r')
	coverage_dict = {}
	for line in coverage_in:
		#split the line on tabs. assign lineSplit[0] to query_id. 
		lineSplit = line.split('\t')
		query_id = lineSplit[0]
		#if lineSplit[1] == '-', create a dictionary entry using the noHits_coverage
		if lineSplit[1] == '-':
			coverage_dict[query_id] = [noHits_coverage]
		#if lineSplit[1] != '-', create a dictionary entry that contains the recorded % coverage value
		if lineSplit[1] != '-':
			percent_coverage = lineSplit[2][:-1]
			percent_coverage = float(percent_coverage)
			#create a new dictionary entry
			coverage_dict[query_id] = [percent_coverage]
	#close the input and return coverage_dict
	coverage_in.close()
	return (coverage_dict)


###IOin###
#import the 4 coverage maps (frmt: [query]\t[subject]\t[%coverage] (or, when no hit: [query]\t[-]\t[-]))
path_to_coverage = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/least.coverage.13.08.06/'
ce_coverage_path = path_to_coverage + 'ce.least.coverage.conversion.13.08.06.coverage'
dr_coverage_path = path_to_coverage + 'dr.least.coverage.conversion.13.08.06.coverage'
hsa_coverage_path = path_to_coverage + 'hsa.least.coverage.conversion.13.08.06.coverage'
ne_coverage_path = path_to_coverage + 'not_ensembl.least.coverage.conversion.13.08.09.coverage'
#ci_coverage_path = path_to_coverage + 'ci.least.coverage.conversion.13.08.07.coverage'
#ce_coverage_in = open(ce_coverage_path, 'r')
#dr_coverage_in = open(dr_coverage_path, 'r')
#hsa_coverage_in = open(hsa_coverage_path, 'r')
#ne_coverage_in = open(not_ensembl_path, 'r')
#ci_coverage_in = open(ci_coverage_path, 'r')

#declare the value of the % coverage to be used in the noHits
ce_noHits_coverage = 65.3411358933
dr_noHits_coverage = 64.3908996393
hsa_noHits_coverage = 60.9095521282
ne_noHits_coverage = 60.9095521282
#ci_noHits_coverage = 0.0 ####assign

#import the blast report (full cgs x 13.proteomes)
#(frmt: (query) (top hit) (bit score) (evalue) (percent identity) (alignment length) (query start) (query stop) (subject species))
blast_report_path = '/Users/ionchannel/research/projects/proteome.analysis/out.topHits.cgsPipeline.step1'
blast_report_in = open(blast_report_path, 'r')

###IOout###
#export the list of protein id's (frmt: [protein id] \n)
cgs_out_path = '/Users/ionchannel/research/projects/ionchannels/candidate.genesets.db/geneset/create.octopus.cgs.13.08.07/best.hit.spp.id.list.001'
redun_out_path = cgs_out_path + '.redundant'
rejects_out_path = cgs_out_path + '.rejects'
redun_out = open(redun_out_path, 'a')
rejects_out = open(rejects_out_path, 'a')
cgs_out = open(cgs_out_path, 'a')



###Parse 1###
##create a dictionary for hsa,ce,dr,ne,ci that contains the name of the query as the key and contains the % coverage as the entry (uses make_coverage_dict()). then, create a single, merged dictionary that contains all the information
#declare the 5 dictionaries
hsa_coverage_dict = {}
ce_coverage_dict = {}
dr_coverage_dict = {}
ne_coverage_dict = {}
#ci_coverage_dict = {}

#use make_coverage_dict() to fill in each dictionary
hsa_coverage_dict = make_coverage_dict(hsa_coverage_path, hsa_noHits_coverage)
ce_coverage_dict = make_coverage_dict(ce_coverage_path, ce_noHits_coverage)
dr_coverage_dict = make_coverage_dict(dr_coverage_path, dr_noHits_coverage)
ne_coverage_dict = make_coverage_dict(ne_coverage_path, ne_noHits_coverage)
#ci_coverage_dict = make_coverage_dict(ci_coverage_path, ci_noHits_coverage)

#merge all the dictionaries together
all_coverage_dict = {}
all_coverage_dict.update(hsa_coverage_dict)
all_coverage_dict.update(ce_coverage_dict)
all_coverage_dict.update(dr_coverage_dict)
all_coverage_dict.update(ne_coverage_dict)
#all_coverage_dict.update(ci_coverage_dict)

###Parse 2###
##create query_length_dict - universal dictionary that contains the length of each gene from each species (uses the new .lengths files) and uses the gene name as the key 
#declare dictionary
query_length_dict = {}

#for each file in /Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteomes.lengths.13.08.07/, add each entry to the dictionary
for fileName in os.listdir('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteomes.lengths.13.08.07/'):
	#test to make sure the fileName ends with .lengths by splitting the fileName on '.' then check to see if the filename ends with lengths. if it does not, skip the iteration of loop and move on to the next fileName
	fileNameSplit = fileName.split('.')
	if fileNameSplit[-1] != 'lengths':
		continue
	#open the .lengths file as (length_in) (frmt: [protein id]\t[length]\n)
	file_path_length = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/proteomes.lengths.13.08.07/' + fileName
	length_in = open(file_path_length, 'r')
	#for each line in the file, save the protein id and the length into query_length_dict
	for line in length_in:
		print line
		#split the line, save the protein id as (protein_id); save the length as (protein_length) (also strip the newline)
		lineSplit = line.split('\t')
		protein_id = lineSplit[0]
		protein_length = float(lineSplit[1][:-1])
		query_length_dict[protein_id] = [protein_length]
	#close the .lengths file
	length_in.close()

###Parse 3###
##using query_length_dict and the information in the blast report, calculate the percent coverage for each gene. then, check to see if each gene's percent coverage is greater than the percent coverage for that query. if it is, output the subject_id to the output file
query_id = ''
cgs_out_list = []
subject_id = ''
query_length = 0.0
query_start = 0
query_end = 0
coverage_score = 0.0
for line in blast_report_in:
	#split the line on '\t'
	lineSplit = line.split('\t')
	#check to see if the line contains - . if it does, skip the line
	if lineSplit[1] == '-':
		continue
	
	#assign lineSplit[0] to query_id. assign lineSplit[1] to subject_id. also, retrieve the query_start, query_end
	
	query_id = lineSplit[0]
	subject_id = lineSplit[1]
	query_start = lineSplit[6] #assign the smaller number
	query_end = lineSplit[7] #assign the larger number
	#using query_length_dict, retrieve the length of the query and assign it to query_length
	query_length = query_length_dict[query_id][0]
	#calculate the coverage_score
	query_start = float(query_start)
	query_end = float(query_end)
	coverage_score = query_end - query_start
	coverage_score = coverage_score / query_length
	coverage_score = coverage_score * 100

	#compare coverage_score to the coverage score recorded in all_coverage_dict for query_id. if coverage_score is >=, add the subjectID to the list of outputs (if it is not already in the list). also, always add the redundant output
	if round(coverage_score, 10) >= round(all_coverage_dict[query_id][0], 10):
		outputred = subject_id + '\n'
		redun_out.write(outputred)
		if subject_id not in cgs_out_list:
			cgs_out_list.append(subject_id)
	#if the coverage score is too low, add the subject id to the .rejects file
	else:
		outputr = subject_id + '\t' + str(coverage_score) + '\t' + str(all_coverage_dict[query_id][0]) + '\n'
		rejects_out.write(outputr)
###Parse 4###
##using cgs_out_list, create the output file
for item in cgs_out_list:
	output = item + '\n'
	cgs_out.write(output)




		
redun_out.close()
rejects_out.close()
blast_report_in.close()
cgs_out.close()
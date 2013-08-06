import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
###version 2 adds 3 calculated % coverage values to each noHit gene

#this script reads in the .conversion files for homoQdrosophilaS and homoQcelegansS and saves each entry as a dictionary entry with the human gene as the key. Then, it searches the two dictionaries, and adds the dr/ce gene (whichever is lower) to the output file
###functions
##create_conversion_dict(path to .conversion file) - returns a dictionary where the key is the human protein id, the entry is: [subject id, % coverage]
def create_conversion_dict(conversion_path):
	conversion_dict = {}
	#open the file that is pointed to by the path
	conversion_file = open(conversion_path, 'r')
	#for each line, create a dictionary with the format described above
	for line in conversion_file:
		lineSplit = line.split('\t')
		#remove the prefixes
		#header_id = lineSplit[0]
		#subject_id = lineSplit[1]
		#header_id_split = header_id.split('-')
		#subject_id_split = subject_id.split('-')
		#lineSplit[0] = header_id_split[1]
		#lineSplit[1] = subject_id_split[1] 

		#if there is already an entry using the hsa protein id, see if the current line has a lower % coverage. if so, replace the current value. if not, move on
		if lineSplit[0] in conversion_dict.keys():	

			if conversion_dict[lineSplit[0]][1] > lineSplit[2][:-1]:

				conversion_dict[lineSplit[0]] = [lineSplit[1], lineSplit[2][:-1]]
		#if there is no entry using the hsa protein id, add an entry
		if lineSplit[0] not in conversion_dict.keys():
			conversion_dict[lineSplit[0]] = [lineSplit[1], lineSplit[2][:-1]]
	conversion_file.close()

	return (conversion_dict)

##calculate_average_coverage_1(dictionary) - this function uses  sum_percent_cov() / total number of peptides in dictionary
def calculate_average_coverage_1(dict_in):
	average_coverage = 0.0
	average_coverage = sum_percent_cov(dict_in) / len(dict_in.keys())
	return (average_coverage)
	
##sum_percent_cov(dict_in) - adds up the percent coverage of all the dictionary entries, returns the value as a float
def sum_percent_cov(dict_in):
	#for each key in the dict, add the % coverage to (sum_coverage)
	
	sum_coverage = 0.0

	for key in dict_in.keys():
		sum_coverage = sum_coverage + float(dict_in[key][1])

	return (sum_coverage)

##find_lowest_coverage(dict_in) - returns the lowest % coverage as a float number
def find_lowest_coverage(dict_in):
	lowest_coverage = 1000000000.0
	lowest_coverage_name = ''
	#for each item in dict_in, see if float(dict_in[key][1]) is lower than lowest_coverage. if it is, replace the lowest_coverage with the new value
	for key in dict_in.keys():
		percent_coverage = float(dict_in[key][1])
		if percent_coverage < lowest_coverage:
			lowest_coverage = percent_coverage
			lowest_coverage_name = key + ' ' + dict_in[key][0]

	return (lowest_coverage, lowest_coverage_name)



def myround(x, base=5):
    return int(base * round(float(x)/base))

##get_list_cov(dict_in) - returns a list of the % coverages rounded to the nearest 5
def get_list_cov(dict_in):

	#also, round the coverage to the nearest 5 and add to the list_of_coverage
	list_coverage_noround = []
	list_of_coverage = []
	for key in dict_in.keys():
		list_coverage_noround.append(float(dict_in[key][1]))
		list_of_coverage.append(myround(float(dict_in[key][1])))
	return (list_of_coverage, list_coverage_noround)






###IOin###
##import the .conversion files
hQdS_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/top.hits.coverage.13.08.06/out.topHits.homoQ.drosophilaS.coverage'
hQcS_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/top.hits.coverage.13.08.06/out.topHits.homoQ.caenorhabditisS.coverage'


###IOout###
##the main output file
  #frmt: (hsa gene) (dr/ce gene) (% coverage)
conversion_out = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/hsa.least.coverage.13.08.06/hsa.least.coverage.conversion.13.08.06' ,'a')
##the averages file
  #frmt: (dr 1,2,3,4) \n (ce 1,2,3,4)  
averages_out = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/hsa.least.coverage.13.08.06/hsa.least.coverage.conversion.13.08.06.averages' ,'a')
##the distribution file
   #frmt: #drosophila \n [0] [frequency] \n [5] [frequency] ... #celegans ...
distr_out = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/hsa.least.coverage.13.08.06/hsa.least.coverage.conversion.13.08.06.distribution','a') 
no_hits_out = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/hsa.least.coverage.13.08.06/hsa.least.coverage.conversion.13.08.06.noHits' ,'a')








###Parse 2###
##create a list of human genes by scanning in the hsa proteome (longest peptide, patch)
hsa_proteome_path = '/Users/ionchannel/13.PROTEOMES.PATH/000.origional.docs/proteome.homo.sapiens.primary.longest.peptide.fa'
hsa_proteome_id_list = []
#for each fasta entry, add the id to (hsa_proteome_id_list)
for seq_record in SeqIO.parse(hsa_proteome_path, "fasta"):
	hsa_proteome_id_list.append(seq_record.id)

print 'Created list of human proteome ids' + '\n'



###Parse 1###
##create a dictionary for each .conversion file
hqds_dict = {}
hqcs_dict = {}

#call (create_conversion_dict)
hqds_dict = create_conversion_dict(hQdS_path)
hqcs_dict = create_conversion_dict(hQcS_path)
print 'Created both conversion dictionaries' + '\n'

###Parse 2###
##calculate the four values to assign to nohits (to go into the averages_out)
##sum of % coverage / total # of % coverage peptides (use calculate_average_coverage_1)
dr_avg_cov = 0.0
ce_avg_cov = 0.0
dr_avg_cov = calculate_average_coverage_1(hqds_dict)
ce_avg_cov = calculate_average_coverage_1(hqcs_dict)
##sum of % coverage / total longest peptides patched (use sum_percent_cov)
dr_cov_pep = 0.0
ce_cov_pep = 0.0
dr_cov_pep = sum_percent_cov(hqds_dict) / 22244.0
ce_cov_pep = sum_percent_cov(hqcs_dict) / 22244.0
##avg_cov * nohit/total
dr_cov_nohit = 0.0
ce_cov_nohit = 0.0

nohit_total = 5198.0 / 22244.0
dr_cov_nohit = dr_avg_cov * nohit_total

ce_cov_nohit = ce_avg_cov * nohit_total
##[lowest % coverage + avg_cov ] / 2 (use find_lowest_coverage)
#define variables
dr_name_lowest = ''
ce_name_lowest = ''
#get the lowest percent coverage and the name of the respective gene
dr_lowest_percent_coverage, dr_name_lowest = find_lowest_coverage(hqds_dict)
ce_lowest_percent_coverage, ce_name_lowest = find_lowest_coverage(hqcs_dict)
sum_dr = dr_lowest_percent_coverage + dr_avg_cov
sum_ce = ce_lowest_percent_coverage + ce_avg_cov
dr_low_avg = sum_dr / 2
ce_low_avg = sum_ce / 2
#format the output
output = '#format (line 1-Drosophila): average covererage (excludes noHits), sum % coverage / total # of hsa peptides (longest peptide), average coverage * (# of noHits / (# noHits + #hits)), (lowest % coverage + average coverage) / 2, lowest percent coverage (#), lowest percent coverage (name)' + '\n' + '#format (line 2-Celegans): same as line 1' + '\n'
output = output + str(dr_avg_cov) + '\t' + str(dr_cov_pep) + '\t' + str(dr_cov_nohit) + '\t' + str(dr_low_avg) + '\t' + str(dr_lowest_percent_coverage) + '\t' + dr_name_lowest + '\n' + str(ce_avg_cov) + '\t' + str(ce_cov_pep) + '\t' + str(ce_cov_nohit) + '\t' + str(ce_low_avg) + '\t' + str(ce_lowest_percent_coverage) + '\t' + ce_name_lowest + '\n'
averages_out.write(output)

###Parse 3###
##create a distribution of the percent coverages, when write to the distr_out file
#create a list of all the percent coverages (rounded to the nearest 5) - uses (get_list_cov)
#define variables
dr_list_cov = []
ce_list_cov = []
dr_list_cov_dict = {}
ce_list_cov_dict = {}
dr_list_noround = []
ce_list_noround = []
dr_highest_cov = 0.0
ce_highest_cov = 0.0
dr_lowest_cov = 0.0
ce_highest_cov = 0.0
#use the function get_list_cov to assign the values to each list
dr_list_cov, dr_list_noround = get_list_cov(hqds_dict)
ce_list_cov, ce_list_noround = get_list_cov(hqcs_dict)
#sort the lists from lowest to highest
dr_list_cov.sort()
ce_list_cov.sort()
dr_list_noround.sort()
ce_list_noround.sort()
#get the largest and smallest coverage for dr and ce
dr_highest_cov = max(dr_list_noround)
ce_highest_cov = max(ce_list_noround)
dr_lowest_cov = min(dr_list_noround)
ce_lowest_cov = min(ce_list_noround)
#create a dictionary using each number as a key. each time the script finds the number, it adds one to the entry
for item in dr_list_cov:
	#if item is in the keys of the dictionary, 
	if item in dr_list_cov_dict.keys():
		current_value = 0
		current_value = dr_list_cov_dict[item][0]
		new_value = current_value + 1
		dr_list_cov_dict[item] = [new_value]
	#if the item is not in the keys of the dict, add a new entry with a value of 1
	if item not in dr_list_cov_dict.keys():
		dr_list_cov_dict[item] = [1]
for item in ce_list_cov:
	#if item is in the keys of the dictionary, 
	if item in ce_list_cov_dict.keys():
		current_value = 0
		current_value = ce_list_cov_dict[item][0]
		new_value = current_value + 1
		ce_list_cov_dict[item] = [new_value]
	#if the item is not in the keys of the dict, add a new entry with a value of 1
	if item not in ce_list_cov_dict.keys():
		ce_list_cov_dict[item] = [1]
#create a sorted list of keys
dr_key_list = []
ce_key_list = []
dr_key_list = dr_list_cov_dict.keys()
ce_key_list = ce_list_cov_dict.keys()
dr_key_list.sort()
ce_key_list.sort()
#format the outputs
output_dr_header = '#Drosophila: (frmt: percent coverage, frequency)' + '\n' + 'Highest coverage: ' + str(dr_highest_cov) + '\n' + 'Lowest coverage: ' + str(dr_lowest_cov) + '\n'
distr_out.write(output_dr_header)
output_ce_header = '#Celegans: (frmt: percent coverage, frequency)' + '\n' + 'Highest coverage: ' + str(ce_highest_cov) + '\n' + 'Lowest coverage: ' + str(ce_lowest_cov) + '\n' 
#for each key in the dr dict (use dr_key_list), write the % coverage and the frequency
for item in dr_key_list:
	output = str(item) + '\t' + str(dr_list_cov_dict[item][0]) + '\n'
	distr_out.write(output)
#write the header for celegans, then write in the frequencies
distr_out.write(output_ce_header)
for item in ce_key_list:
	output = str(item) + '\t' + str(ce_list_cov_dict[item][0]) + '\n'
	distr_out.write(output)






###Parse 4###
##for each proteinid in the human id list, see if it is in the keys of either dictionary. if it is in only one, write the contents of that dictionary entry to file. if it is in two, write the dictionary entry with the lower % coverage. if there is none, write the hsa id to the the no hits file
#see if the protein id is in either one of the dictionaries
##dictionary names:


for protein_id in hsa_proteome_id_list:
	#if the protein id is in both lists, compare the % coverage and pick the lowest number (use 'continue' if a section of code executes to prevent other actions from being made)

	if protein_id in hqds_dict.keys() and protein_id in hqcs_dict.keys():
		dr_entry = []
		ce_entry = []
		dr_entry = hqds_dict[protein_id]
		ce_entry = hqcs_dict[protein_id]
		#convert the % coverage to a float number
		dr_entry[1] = float(dr_entry[1])
		ce_entry[1] = float(ce_entry[1])

		#if the dr entry has the smaller % coverage or has the same % coverage, save it to the output
		if dr_entry[1] < ce_entry[1] or dr_entry[1] == ce_entry[1]:
			output = protein_id + '\t' + dr_entry[0] + '\t' + str(dr_entry[1]) + '\n'
			conversion_out.write(output)
			#print output
			continue
		if ce_entry[1] < dr_entry[1]:
			output = protein_id + '\t' + ce_entry[0] + '\t' + str(ce_entry[1]) + '\n'
			conversion_out.write(output)
			#print output
			continue
	##if the protein_id is only in one of the dictionaries, save the entry to the output
	#if the protein_id is only in hqds_dict.keys()
	if protein_id in hqds_dict.keys() and protein_id not in hqcs_dict.keys():
		dr_entry = []
		dr_entry = hqds_dict[protein_id]
		output = protein_id + '\t' + dr_entry[0] + '\t' + dr_entry[1] + '\n'
		conversion_out.write(output)
		
		#print output
		continue
	#if the protein id is only in hqcs_dict.keys()
	if protein_id in hqcs_dict.keys() and protein_id not in hqds_dict.keys():
		ce_entry = []
		ce_entry = hqcs_dict[protein_id]
		output = protein_id + '\t' + ce_entry[0] + '\t' + ce_entry[1] + '\n'
		conversion_out.write(output)
		
		#print output
		continue
	##if the protein_id is not in either dictionaries' keys, write protein id to the noHits file
	if protein_id not in hqcs_dict.keys() and protein_id not in hqds_dict.keys():
		output = protein_id + '\t' + '-' + '\t' + '-' + '\n'
		conversion_out.write(output)
		no_hits_out.write(output)
		#print output
		continue




distr_out.close()
conversion_out.close()
averages_out.close()

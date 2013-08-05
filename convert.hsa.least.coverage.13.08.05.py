import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


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


###IOin###
##import the .conversion files
hQdS_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/top.hits.coverage.13.08.02/out.topHits.homoQ.drosophilaS.coverage'
hQcS_path = '/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/top.hits.coverage.13.08.02/out.topHits.homoQ.caenorhabditisS.coverage'


###IOout###
##the main output file
  #frmt: (hsa gene) (dr/ce gene) (% coverage)
conversion_out = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/hsa.least.coverage.13.08.05/hsa.least.coverage.conversion.13.08.05' ,'a')
no_hits_out = open('/Users/ionchannel/research/tools/db/blast/13.proteomes/000.origional.docs/hsa.least.coverage.13.08.05/hsa.least.coverage.conversion.13.08.05.noHits' ,'a')
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

###Parse 3###
##for each proteinid in the human id list, see if it is in the keys of either dictionary. if it is in only one, write the contents of that dictionary entry to file. if it is in two, write the dictionary entry with the lower % coverage. if there is none, write the hsa id to the the no hits file
#see if the protein id is in either one of the dictionaries
##dictionary names:

print hqcs_dict
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
		output = protein_id + '\n'
		no_hits_out.write(output)
		#print output
		continue





conversion_out.close()
no_hits_out.close()

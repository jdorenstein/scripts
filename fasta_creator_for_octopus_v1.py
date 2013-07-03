#!C:\Python27 

#script: fasta_creator_for_octopus_v1.0
#function: To create a fasta database for the entire octopus genome. 



### IOin



#input a CSV file from the octopus genome database
#file format: [PFAM description	genes with this PFAM	PANTHER	PANTHER description	genes with this PANTHER	best human hit	human hit description	peptide]

IOcsv_file = open ( '/Users/ionchannel/research/db/blast/oct.proteome/origional.docs/oct_v2_fasta.txt', 'r' )

###IOout


#output fasta database that is formatted
#file format: [>[pacid] Hsa-[best known human hit]]

IOfasta_out = open( '/Users/ionchannel/research/db/blast/oct.proteome/origional.docs/octProteome.fa', 'a' )

###parse 1: all query - All data




for line in IOcsv_file:
    lineSplit = line.split('\t')
    #print line + '\n \n \n \n'
    pacID = lineSplit[ 0 ]
    bhh = lineSplit [ 12 ]
    peptide = lineSplit [ 14 ]
	
	#format new addition into database file
    if bhh:
            output = ">" + pacID + " Hsa-" + bhh + '\n' + peptide + '\n' #note that the output prints to TWO lines

    if not bhh:
            output = ">" + pacID + " Hsa-" + "NO NAME FOR PROTEIN" + '\n' + peptide + '\n' #note that the output prints to TWO lines
	#append into fasta database file
	
    IOfasta_out.write( output )
	
IOcsv_file.close()
IOfasta_out.close()

#end of script

print'end of script' 
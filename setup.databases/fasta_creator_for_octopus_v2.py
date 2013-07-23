#!C:\Python27 

#script: fasta_creator_for_octopus_v2.0
#function: To create a fasta database for the entire octopus genome. 



### IOin



#input a CSV file from the octopus genome database
#file format: [PFAM description	genes with this PFAM	PANTHER	PANTHER description	genes with this PANTHER	best human hit	human hit description	peptide]

IOcsv_file = open ( '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/oct_v2_fasta.txt', 'r' )

###IOout


#output fasta database that is formatted
#file format: [>[pacid] Hsa-[best known human hit]]

IOfasta_out = open( '/Users/ionchannel/research/tools/db/blast/oct.proteome/000.origional.docs/octProteome.fa', 'a' )

###parse 1: all query - All data




for line in IOcsv_file:
    lineSplit = line.split('\t')
    #print line + '\n \n \n \n'
    pacID = lineSplit[ 0 ]
    bhh = lineSplit [ 12 ]
    bhhd = lineSplit[ 13 ]
    peptide = lineSplit [ 14 ]
    output = '>' + pacID + ' ' #information is always present
	#append bhh onto output. this information may or may not be present
    if bhh:
        output = output + 'Hsa-' + bhh + '\n' + peptide + '\n' 
    if not bhh:
        output = output + 'No best human hit identifed in Excel file' + '\n' + peptide + '\n'
 
 
	#append into fasta database file
	
    IOfasta_out.write( output )
	
IOcsv_file.close()
IOfasta_out.close()

#end of script

print'end of script' 
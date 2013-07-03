#!C:\Python27 


#this script creates one large FASTA file that is to be used to test the 12.proteomes db's against the fasta files

###IOin###
#input each fasta file as a variable

IOamphimedon_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.amphimedon.queenslandica.fa', 'r' )
IOcaenorhabditis_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.caenorhabditis.elegans.fa', 'r')
IOciona_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.ciona.intestinalis.fa', 'r' )
IOdrosophila_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.drosophila.melanogaster.fa' , 'r')
IOhomo_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.homo.sapiens.fa' , 'r' )
IOlottia_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.lottia.gigantea.fa','r')
IOmonosiga_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.monosiga.brevicollis.broad.fa','r')
IOnematostella_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.nematostella.vectensis.fa','r')
IOstronglycentrotus_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.stronglyocentrotus.purpuratus.fa','r')
IOtrichoplax_in = open ('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/proteome.trichoplax.adhaerens.fa','r')

###IOout###
#output file is stored in the same folder as the other fastas

IOfasta_out = open('/Users/ionchannel/research/db/blast/12.proteomes/000.origional.docs/12.proteomes.fa','a')

###part 1###
#create a variable for each file


v1 = IOamphimedon_in 
v2 = IOcaenorhabditis_in
v3 = IOciona_in
v4 = IOdrosophila_in
v5 = IOhomo_in
v6 = IOlottia_in
v7 = IOmonosiga_in
v8 = IOnematostella_in
v9 = IOstronglycentrotus_in
v10 = IOtrichoplax_in

for line in IOamphimedon_in:
	IOfasta_out.write( line )
for line in IOcaenorhabditis_in:
	IOfasta_out.write( line )
for line in IOciona_in:
	IOfasta_out.write( line )
for line in IOdrosophila_in:
	IOfasta_out.write( line )
for line in IOhomo_in:
	IOfasta_out.write( line )
for line in IOlottia_in:
	IOfasta_out.write( line )
for line in IOmonosiga_in:
	IOfasta_out.write( line )
for line in IOnematostella_in:
	IOfasta_out.write( line )
for line in IOstronglycentrotus_in:
	IOfasta_out.write( line )
for line in IOtrichoplax_in:
	IOfasta_out.write( line )
	
#append each file into the output file


#IOfasta_out.write( str(v2) )
#IOfasta_out.write( str(v3) )
#IOfasta_out.write( str(v4) )
#IOfasta_out.write( str(v5) )
#IOfasta_out.write( str(v6) )
#IOfasta_out.write( str(v7) )
#IOfasta_out.write( str(v8) )
#IOfasta_out.write( str(v9) )
#IOfasta_out.write( str(v10) )

print 'done'


IOfasta_out.close()
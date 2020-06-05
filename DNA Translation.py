Genetic_Code = {
  'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
  'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
  'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
  'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
  'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
  'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
  'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
  'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
  'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
  'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
  'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
  'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
  'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
  'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
  'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
  'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
     } 
 
 def   codons2Protein(ORF, Genetic_Code ):
 	protein = '   '
 	for i in range(0 , len(ORF),3):
 	codon  = ORF[i:i + 3]
 	protein  += Genetic_Code[  codon]
 	
 	
 
def translate(dna):
      if len(dna) > 2 and len(dna) % 3  != 0:
 	     	dna  =  dna[0: (len(dna)  //  3)  *  3]
      elif len(dna) < 2 :
          		return
  	
      return ' ' .join([Genetic_Code[codon] if codon in Genetic_Code.keys() else 'X' for codon in [dna[i : i + 3] for i in range (0, len(dna), 3)]])
          
          
def  Mutate(filename = 'originalDna.txt'):
  	    Dna =  ' '
  	    MutatedDna = ' '
    with open(filename,'r') as f :
       	      for c in ' ' . join(f.read().split()):
  	    	   	  Dna += c if c != 'a'  else 'A'
  	                 MutatdedDna += c if c != 'a' else 'T'
  
     
      with open('Dna.txt' , 'w')   as f:
           	  f . write(Dna)
  
      with open('MutatedDna.txt' , 'w') as f:
            	 f . write(MutatedDna)
  	 
  
def txtTranslate():
  	  with open('originalDna.txt' ,  'r') as f:
   	  	print(translate(' '.join(f.read().split())))
  	  with open('MutatedDna.txt' , 'r') as f:
   	  	print(translate(' '.join(f.read().split())
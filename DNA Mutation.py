Genetic_Code= {'ATT': 'I', 'ATC': 'I', 
                  'ATA': 'I','CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',          'TTA': 'L', 'TTG': 'L','GTT': 'V', 'GTC': 'V', 'GTA': 'V',
                  'GTG': 'V','TTT': 'F', 'TTC': 'F','ATG': 'M'}
                  
          
def  Mutate(filename = 'originaldna.txt'):
  	    normalDna =  ' '
  	    MutatedDna = ' '
    with open(filename,'r') as f :
       	      for c in ' ' . join(f.read().split()):
  	    	   	  normalDna += c if c != 'a'  else 'A'
  	                 MutatdedDna += c if c != 'a' else 'T'
  
     
      with open('MutatedDna.txt' , 'w')   as f:
           	  f . write(normalDna)
  
      with open('MutatedDna.txt' , 'w') as f:
            	 f . write(MutatedDna)
  	 
  
def txtTranslate():
  	  with open('originalDna.txt' ,  'r') as f:
   	  	print(translate(' '.join(f.read().split())))
  	  with open('MutatedDna.txt' , 'r') as f:
   	  	print(translate(' '.join(f.read().split())
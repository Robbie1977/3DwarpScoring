import numpy as np
import sys
import nrrd
import scipy.stats

if (len(sys.argv) < 3):
    print 'Error: missing arguments!'
else:

    print 'Checking alignment for ', str(sys.argv[1]), ' against the template (', str(sys.argv[2]), ')...'
  
    data1, header1 = nrrd.read(str(sys.argv[2]))
    
    
    
    data2, header2 = nrrd.read(str(sys.argv[1])) 
    
    
    Ravg = np.average(data1)  
    R=np.subtract(data1,Ravg)
    
    Gavg = np.average(data2)  
    G=np.subtract(data2,Gavg)
    
    N=np.sum(np.multiply(R,G))
    D=np.multiply(np.sum(R),np.sum(G))
    
    r=N/D
   
   
    print 'The alignment has a Object Pearson\'s Coefficient r value of:', r, ' (1=perfect)'
    
    print 'Outputing results to ', str(sys.argv[3])
    
    with open(str(sys.argv[3]), "a") as myfile: 
        myfile.write(str(r))
    
    print 'Done.'
    
  


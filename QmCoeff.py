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
    
      
    
    
    
   
   
    print 'The alignment has a RMS Diff value of:', r1, ' (0=perfect)'
    
    print 'Outputing results to ', str(sys.argv[3])
    
    with open(str(sys.argv[3]), "a") as myfile: 
        myfile.write(str(r1))
    
    print 'Done.'
    
  


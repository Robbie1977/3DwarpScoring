import numpy as np
import sys
import nrrd

if (len(sys.argv) < 4):
    print 'Error: missing arguments!'
    print 'e.g. python [measure].py image.nrrd template.nrrd results.csv'
else:

    print 'Checking alignment for ', str(sys.argv[1]), ' against the template (', str(sys.argv[2]), ')...'
  
    readdata, options = nrrd.read(str(sys.argv[2]))
    
    imt = readdata
    
    readdata, options = nrrd.read(str(sys.argv[1])) 
    im1 = readdata
      
    if (imt.size <> im1.size):
        print '\n\nError: Images must be the same size!!'
    else:
    
        lthreshold = 40
        hthreshold = 39
        
        low_val_ind = imt < lthreshold
        imt[low_val_ind] = 0
        
        low_val_ind = im1 < lthreshold
        im1[low_val_ind] = 0
        
        high_val_ind = imt > hthreshold
        imt[high_val_ind] = 101
        
        high_val_ind = im1 > hthreshold
        im1[high_val_ind] = 101
        
        d1 = np.subtract(imt,im1, dtype=np.float64) 
        low_val_ind = d1 < 0
        d1[low_val_ind] = -10
        s1 = np.power(d1,2, dtype=np.float64)
        r1 = np.sqrt(np.mean(s1), dtype=np.float64)
    
        print 'The alignment has a RMS Diff value of:', r1, ' (0=perfect)'
        
        print 'Outputing results to ', str(sys.argv[3])
        
        with open(str(sys.argv[3]), "a") as myfile: 
            myfile.write(str(r1) + ', RMS Diff, ' + str(sys.argv[1]) + ', ' + str(sys.argv[2]) + '\n')
        
        print 'Done.'
        
  


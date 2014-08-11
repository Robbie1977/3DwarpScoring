import numpy as np
import sys
import nrrd

if (len(sys.argv) < 4):
    print 'Error: missing arguments!'
    print 'e.g. python [measure].py image.nrrd template.nrrd results.csv'
else:
    
    quiet = False
    if (str(sys.argv[3]).upper() == 'Q'):
        quiet = True

    if (quiet == False):
        print 'Checking alignment for ', str(sys.argv[1]), ' against the template (', str(sys.argv[2]), ')...'
  
    data1, header1 = nrrd.read(str(sys.argv[2]))
        
    data2, header2 = nrrd.read(str(sys.argv[1])) 
      
    if (data1.size <> data2.size):
        if (quiet == False):
            print '\n\nError: Images must be the same size!!'
        else:
            print '%0.100f'% 0
        sys.exit(1)
    else:  
      
        Nd1 = np.squeeze(np.asarray(data1,dtype=np.float128))
        Nd2 = np.squeeze(np.asarray(data2,dtype=np.float128))
                                        
        r=np.sum(np.multiply(Nd1,Nd2))/np.sqrt(np.multiply(np.sum(np.square(Nd1)),np.sum(np.square(Nd2))))
        
        if (quiet == False):
            print 'The alignment has a overlap coefficient value of: %0.60f (1=perfect)'% r
        
            print 'Outputing results to ', str(sys.argv[3])
        
            with open(str(sys.argv[3]), "a") as myfile: 
                myfile.write('{0:.100f}'.format(float(r)) + ', Overlap Coeffient, ' + str(sys.argv[1]) + ', ' + str(sys.argv[2])+ '\n')
        
            print 'Done.'
        else:    
            print '%0.60f'% r
        
  


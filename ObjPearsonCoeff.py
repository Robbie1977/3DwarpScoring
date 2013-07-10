import numpy as np
import sys
import nrrd
import scipy.stats

if (len(sys.argv) < 4):
    print 'Error: missing arguments!'
else:

    print 'Checking alignment for ', str(sys.argv[1]), ' against the template (', str(sys.argv[2]), ')...'
  
    data1, header1 = nrrd.read(str(sys.argv[2]))
        
    data2, header2 = nrrd.read(str(sys.argv[1])) 
    
    Nd1 = np.squeeze(np.asarray(data1,dtype=np.float128))
    Nd2 = np.squeeze(np.asarray(data2,dtype=np.float128))
    
    th = 0
    
    for i in range(0,size(Nd1)):
        if ((Nd1[i] > th) or (Nd2 > th)):
            Na1[i] = Nd1[i]
            Na2[i] = Nd2[i]
            
                                        
    r=np.sum(np.multiply(np.subtract(Nd1,np.average(Na1)),np.subtract(Nd2,np.average(Na2))))/np.sqrt(np.multiply(np.sum(np.square(np.subtract(Nd1,np.average(Na1)))),np.sum(np.square(np.subtract(Nd2,np.average(Na2))))))
      
    print 'The alignment has a Object Pearson\'s Coefficient r value of: %0.60f (1=perfect)'% r
    
    print 'Outputing results to ', str(sys.argv[3])
    
    with open(str(sys.argv[3]), "a") as myfile: 
        myfile.write('{0:.100f}'.format(r) + ', Object Pearson Coefficent, ' + str(sys.argv[1]) + ', ' + str(sys.argv[2]) + '\n')
    
    print 'Done.'
    
  

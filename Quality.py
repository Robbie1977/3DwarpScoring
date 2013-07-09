import numpy as np
import matplotlib.pyplot as plt
import sys
import nrrd

if (len(sys.argv) < 3):
    print 'Error: missing arguments!'
else:

    print 'Checking alignment for ', str(sys.argv[1]), ' against the template (', str(sys.argv[2]), ')...'
    
    #def histeq(im,nbr_bins=256):
    #
    #   #get image histogram
    #   imhist,bins = np.histogram(im.flatten(),nbr_bins,normed=True)
    #   cdf = imhist.cumsum() #cumulative distribution function
    #   cdf = 255 * cdf / cdf[-1] #normalize
    #
    #   #use linear interpolation of cdf to find new pixel values
    #   im2 = np.interp(im.flatten(),bins[:-1],cdf)
    #
    #   return im2.reshape(im.shape), cdf    
        

    readdata, options = nrrd.read(str(sys.argv[2]))
    
    imt = readdata
    
    readdata, options = nrrd.read(str(sys.argv[1])) 
    im1 = readdata
    #readdata, options = nrrd.read('/Volumes/Macintosh HD/Users/robertcourt/BTSync/GMR_15E01_AE_01_19-fA01v_C080604_20080605015017781-rigid-BGwarp.nrrd')
    
    #im2 = readdata
    
    lthreshold = 40
    hthreshold = 39
    
    low_val_ind = imt < lthreshold
    imt[low_val_ind] = 0
    
    low_val_ind = im1 < lthreshold
    im1[low_val_ind] = 0
    
    #low_val_ind = im2 < lthreshold
    #im2[low_val_ind] = 0
    
    
    high_val_ind = imt > hthreshold
    imt[high_val_ind] = 101
    
    high_val_ind = im1 > hthreshold
    im1[high_val_ind] = 101
    
    #high_val_ind = im2 > hthreshold
    #im2[high_val_ind] = 101
    
    
    
    #print rmsdiff(im1, imt)
    
    #print rmsdiff(im2, imt)
    
    
    
    
    
    #imt = imt.point(lambda p: p > threshold and 255)
    #im1 = im1.point(lambda p: p > threshold and 255)
    #im2 = im2.point(lambda p: p > threshold and 255)
    
    #imt = (((imt > hthreshold).astype(np.uint8) * 155) + ((imt > lthreshold).astype(np.uint8) * 100))
    #im1 = (((im1 > hthreshold).astype(np.uint8) * 155) + ((im1 > lthreshold).astype(np.uint8) * 100))
    #im2 = (((im2 > hthreshold).astype(np.uint8) * 155) + ((im2 > lthreshold).astype(np.uint8) * 100))
    
    #print imt.max()
    #imt *= 2.0/imt.max()
    #im1 *= 2.0/im1.max()
    #im2 *= 2.0/im2.max()
    #print imt.max()
    #grt = np.gradient(imt[:,:,100],1,1,1, dtype=np.float)
    #gr1 = np.gradient(im1, dtype=np.float64)
    #gr2 = np.gradient(im2, dtype=np.float64)
    
    #im1 = ndimage.gaussian_filter(im1, 4)
    #im2 = ndimage.gaussian_filter(im2, 4)
    
    #imt = ndimage.gaussian_filter(imt, 4)
    
    
    d1 = np.subtract(imt,im1, dtype=np.float64) 
    low_val_ind = d1 < 0
    d1[low_val_ind] = -10
    s1 = np.power(d1,2, dtype=np.float64)
    r1 = np.sqrt(np.mean(s1), dtype=np.float64)
    #d2 = np.subtract(imt,im2, dtype=np.float64) 
    #low_val_ind = d2 < 0
    #d2[low_val_ind] = -10
    #s2 = np.power(d2,2, dtype=np.float64)
    #r2 = np.sqrt(np.mean(s2), dtype=np.float64)
    
    print 'The alignment has a RMS Diff value of:', r1, ' (0=perfect)'
    
    print 'Outputing results to ', str(sys.argv[3])
    
    with open(str(sys.argv[3]), "a") as myfile: 
        myfile.write(str(r1))
    
    print 'Done.'
    
    #print r2
    
    # display results
    #plt.figure(figsize=(8, 3))
    #
    #plt.subplot(131)
    #plt.imshow(imt[:,:,100], cmap=plt.cm.jet)
    #plt.axis('off')
    #plt.title('template', fontsize=20)
    #
    #plt.subplot(132)
    #plt.imshow(d1[:,:,100], cmap=plt.cm.jet)
    #plt.axis('off')
    #plt.title('Good', fontsize=20)
    #
    #plt.subplot(133)
    #plt.imshow(d2[:,:,100], cmap=plt.cm.jet)
    #plt.axis('off')
    #plt.title('Bad', fontsize=20)
    #
    #plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
    #                    bottom=0.02, left=0.02, right=0.98)
    #
    #
    #plt.show()



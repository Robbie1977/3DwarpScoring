import nrrd
import sys, warnings
from numpy import int,round,linspace, newaxis, shape, array, uint32, uint8, max, sqrt, abs, mean, dtype, int32, add, divide, subtract, sum, square, multiply, asarray, squeeze, float128, average, ones
#from matplotlib.pyplot import imshow, figure, show, colorbar
#import matplotlib.cm as cm

def zsampleslice(data):
    """Returns four sample Z slices through a 3d image array."""
    data = array(data,ndmin=3)
    l=shape(data)[2]
    a=data[:,:,0]
    s=int(l/3)
    b=data[:,:,(s)]
    c=data[:,:,(-s)]
    d=data[:,:,(l-1)]
    return array([a,b,c,d])

def ysampleslice(data):
    """Returns four sample Z slices through a 3d image array."""
    data = array(data,ndmin=3)
    l=shape(data)[1]
    a=data[:,0,:]
    s=int(l/4)
    b=data[:,s,:]
    c=data[:,-s,:]
    d=data[:,l-1,:]
    return array([a,b,c,d])

def xsampleslice(data):
    """Returns four sample Z slices through a 3d image array."""
    data = array(data,ndmin=3)
    l=shape(data)[0]
    a=data[0,:,:]
    s=int(l/4)
    b=data[s,:,:]
    c=data[-s,:,:]
    d=data[l-1,:,:]
    return array([a,b,c,d])

def RMSdiff(data1,data2):
    """Returns the RMS difference between two images."""
    return sqrt(mean(abs(data1-(data2+0.0))**2.0))

def OverlapCoeff(data1,data2):
    """Returns the Overlap Coefficent between two images."""
    Nd1 = squeeze(asarray(data1,dtype=float128))
    Nd2 = squeeze(asarray(data2,dtype=float128))
    return sum(multiply(Nd1,Nd2))/sqrt(multiply(sum(square(Nd1)),sum(square(Nd2))))

def minOverlapCoeff(data1,data2):
    """Returns the min Overlap Coefficent between image slices."""
    R=[]
    print shape(data1)
    for i in range(0,min(shape(data1))):
      Nd1 = squeeze(asarray(data1[i],dtype=float128))
      if sum(Nd1) < 1: Nd1[0,0] = 1.0
      print shape(Nd1)
      print sum(Nd1)
      Nd2 = squeeze(asarray(data2[i],dtype=float128))
      if sum(Nd2) < 1: Nd2[0,0] = 1.0
      print shape(Nd2)
      print sum(Nd2)
      if (sum(Nd1) + sum(Nd2)) > 0:
        R.append(sum(multiply(Nd1,Nd2))/sqrt(multiply(sum(square(Nd1)),sum(square(Nd2)))))
      else:
        print 'Note: both equal only as blank'
        R.append(1.0)
      print R
    return min(R)

def avgOverlapCoeff(data1,data2):
    """Returns the min Overlap Coefficent between image slices."""
    R=[]
    # print shape(data1)
    weights=ones(min(shape(data1)),dtype=float)
    weights[0]=0.1
    weights[-1]=0.1
    for i in range(0,min(shape(data1))):
      Nd1 = squeeze(asarray(data1[i],dtype=float128))
      if sum(Nd1) < 1: Nd1[0,0] = 1.0
      # print shape(Nd1)
      # print sum(Nd1)
      Nd2 = squeeze(asarray(data2[i],dtype=float128))
      if sum(Nd2) < 1: Nd2[0,0] = 1.0
      # print shape(Nd2)
      # print sum(Nd2)
      if (sum(Nd1) + sum(Nd2)) > 0:
        R.append(sum(multiply(Nd1,Nd2))/sqrt(multiply(sum(square(Nd1)),sum(square(Nd2)))))
      else:
        print 'Note: both equal only as blank'
        R.append(1.0)
    print R
    print weights
    print average(R, weights=weights)
    return average(R, weights=weights)

def symTest(function,data):
    """Applies the given function to the diagonal slices output from xslice. Can be used to assess the symetry of a 3D image using a comparison function such as OverlapCoeff."""
    if data.ndim < 3:
        warnings.warn("must be used with data output from xslice", SyntaxWarning)
        return False
    else:
        return function(data[0],data[1])

import nrrd
import sys, warnings
from numpy import int,round,linspace, newaxis, shape, array, uint32, uint8, max, sqrt, abs, mean, dtype, int32, add, divide, subtract, sum
#from matplotlib.pyplot import imshow, figure, show, colorbar
#import matplotlib.cm as cm

def zsampleslice(data):
    """Returns four sample Z slices through a 3d image array."""
    data = array(data,ndmin=3)
    l=shape(data)[2]
    a=data[:,:,0]
    s=int(l/4)
    b=data[:,:,s]
    c=data[:,:,-s]
    d=data[:,:,l]

def ysampleslice(data):
    """Returns four sample Z slices through a 3d image array."""
    data = array(data,ndmin=3)
    l=shape(data)[1]
    a=data[:,0,:]
    s=int(l/4)
    b=data[:,s,:]
    c=data[:,-s,:]
    d=data[:,l,:]
    return array([a,b,c,d])

def xsampleslice(data):
    """Returns four sample Z slices through a 3d image array."""
    data = array(data,ndmin=3)
    l=shape(data)[0]
    a=data[0,:,:]
    s=int(l/4)
    b=data[s,:,:]
    c=data[-s,:,:]
    d=data[L,:,:]
    return array([a,b,c,d])

def RMSdiff(data1,data2):
    """Returns the RMS difference between two images."""
    return sqrt(mean(abs(data1-(data2+0.0))**2.0))

def OverlapCoeff(data1,data2):
    """Returns the Overlap Coefficent between two images."""
    return sum(data1*(data2+0.0))/sqrt(sum(data1**2.0)*sum(data2**2.0))

def symTest(function,data):
    """Applies the given function to the diagonal slices output from xslice. Can be used to assess the symetry of a 3D image using a comparison function such as OverlapCoeff."""
    if data.ndim < 3:
        warnings.warn("must be used with data output from xslice", SyntaxWarning)
        return False
    else:
        return function(data[0],data[1])

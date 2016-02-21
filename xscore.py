import nrrd
import sys, warnings
from numpy import int, round, linspace, newaxis, shape, array, uint32, uint8, max, sqrt, abs, mean, dtype, int32, add, \
    divide, subtract, sum


# from matplotlib.pyplot import imshow, figure, show, colorbar
# import matplotlib.cm as cm

def xslice(data):
    """Returns two stacked diagonal slices through a 3d image array."""
    data = array(data, ndmin=3)
    l = max(shape(data)[0:2])
    y = array([round(i) for i in linspace(0, shape(data)[0] - 1, l)], dtype=uint32)
    x = array([round(i) for i in linspace(0, shape(data)[1] - 1, l)], dtype=uint32)
    a = data[y, x, :]
    b = data[y[::-1], x, :]

    return array([a, b])


def RMSdiff(data1, data2):
    """Returns the RMS difference between two images."""
    return sqrt(mean(abs(data1 - (data2 + 0.0)) ** 2.0))


def OverlapCoeff(data1, data2):
    """Returns the Overlap Coefficent between two images."""

    return (sum(data1 * data2)) / (sqrt(sum(data1 ** 2) * sum(data2 ** 2) + 0.0))


def symTest(function, data):
    """Applies the given function to the diagonal slices output from xslice. Can be used to assess the symetry of a 3D image using a comparison function such as OverlapCoeff."""
    if data.ndim < 3:
        warnings.warn("must be used with data output from xslice", SyntaxWarning)
        return False
    else:
        return function(data[0], data[1])

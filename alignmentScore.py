# Gives a score between 0 (bad) and 1 (excellant) for the alignment of two NRRD samples
import CheckImages as ci
import numpy as np


def score(template, alignment):
    # template file, alignment file (both NRRD)
    result = np.mean([np.float128(ci.rateOne(alignment ,results=None, methord=slicescore.OverlapCoeff, template=template)),np.float128(ci.rateOne(alignment ,results=None, methord=slicescore.avgOverlapCoeff, template=template))])
    return result

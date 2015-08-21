# Gives a score between 0 (bad) and 1 (excellant) for the alignment of two NRRD samples
import CheckImages as ci
import numpy as np


def score(template, alignment):
    # template file, alignment file (both NRRD)
    result = np.mean([np.float128(ci.rateOne(alignment ,results=None, methord=slicescore.OverlapCoeff, template=template)),np.float128(ci.rateOne(alignment ,results=None, methord=slicescore.avgOverlapCoeff, template=template))])
    return result

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print 'Error: missing arguments!'
        print 'e.g. python alignmentScore.py template.nrrd alignment.nrrd'
    else:
        print str(score(sys.argv[1],sys.argv[2]))
        

# Gives a score between 0 (bad) and 1 (excellent) for the alignment of two NRRD samples
import CheckImages as ci
import slicescore
import numpy as np
import sys


def score(template, alignment):
    # template file, alignment file (both NRRD)
    result = np.mean(
        [np.float128(ci.rateOne(alignment, results=None, methord=slicescore.OverlapCoeff, template=template)),
         np.float128(ci.rateOne(alignment, results=None, methord=slicescore.avgOverlapCoeff, template=template))])
    return result


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Error: missing arguments!'
        print 'e.g. python alignmentScore.py alignment.nrrd template.nrrd [results.csv]''
    else:
        r = score(sys.argv[2], sys.argv[1])
        print 'The final alignment score is ' + str(r)
        if len(sys.argv) > 3:
            with open(str(sys.argv[3]), "a") as myfile:
                myfile.write('{0:.100f}'.format(float(r)) + ', Alignment Score, ' + str(sys.argv[1]) + ', ' + str(
                    sys.argv[2]) + '\n')
        print 'Done.'

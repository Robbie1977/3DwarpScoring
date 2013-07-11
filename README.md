3DwarpScoring
=============

Scripts to assess 3D confocal image warping towards a template image.


all run as:

  python scriptname.py AlignedImage.nrrd Template.nrrd Results.csv



Results can be combined or sent to individual files and consist of:

  Score, Methord, AlignedImage.nrrd,Template.nrrd


Analysis methords available are:

  Overlap coefficient - OverlapCoeff.py

  Pearson's coefficient - PearsonCoeff.py

  Object Pearson's coefficient - ObjPearsonCoeff.py

  Spearman coefficient - SpearmanCoeff.py

  RMS difference - Quality.py

coefficient scores are all 1=perfect, 0=no correlation and with Pearson methords also returing -1 if anticorrelated.

RMSd returns a value that can only be compared when the same template is used. With 0 being bad and a good value range having to be experimentally estimated on the images used.

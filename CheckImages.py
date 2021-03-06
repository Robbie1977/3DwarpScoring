import nrrd, os, glob, sys, csv
import xscore, slicescore
import numpy as np

try:
  from cmtk import template
except:
  template = '/Volumes/Macintosh HD/Users/robertcourt/BTSync/usedtemplate.nrrd'

testtemp = template

if os.path.isfile(template):
    data1, header1 = nrrd.read(template)
elif os.path.isfile('/disk/data/VFBTools/Alignment/template/flyVNCtemplate20xA.nrrd'):
    data1, header1 = nrrd.read('/disk/data/VFBTools/Alignment/template/flyVNCtemplate20xA.nrrd')
else:
    print 'Template file missing!'
    data1 = []
if not data1==[]:
    ctemplate = xscore.xslice(data1)
    ztemplate = slicescore.zsampleslice(data1)
    ytemplate = slicescore.ysampleslice(data1)
    xtemplate = slicescore.xsampleslice(data1)
    del data1, header1

def rateAll(path,match="*BG*.nrrd",results="./OverlapResults.csv", methord=slicescore.OverlapCoeff):
    r=[]
    for file in glob.glob(path + os.sep + match):
        print "testing:" + os.path.basename(file)
        data2, header2 = nrrd.read(file)
        calignment = xscore.xslice(data2)
        zalignment = slicescore.zsampleslice(data2)
        yalignment = slicescore.ysampleslice(data2)
        xalignment = slicescore.xsampleslice(data2)
        del data2, header2
        r.append((os.path.basename(file),xscore.symTest(methord,calignment),methord(ctemplate,calignment),methord(ztemplate,zalignment),methord(ytemplate,yalignment),methord(xtemplate,xalignment)))
        if not results==None:
            with open(results, 'a') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([path,r[-1][0],"[Symmetry,Diagonal,Zsample,Ysample,Xsample,Final]score",r[-1][1],r[-1][2],r[-1][3],r[-1][4],r[-1][5],min(r[-1][1:])])
        del xalignment
    if r == []:
      print 'no files found matching: ' + path + match
    return r

def rateOne(file,results="./OverlapResults.csv", methord=slicescore.OverlapCoeff, template=template):
    if os.path.isfile(template):
        data1, header1 = nrrd.read(template)
    else:
        print 'Template file missing!'
        data1 = []
    if not data1==[]:
        ctemplate = xscore.xslice(data1)
        ztemplate = slicescore.zsampleslice(data1)
        ytemplate = slicescore.ysampleslice(data1)
        xtemplate = slicescore.xsampleslice(data1)
        del data1, header1
    r=np.float128(0.0)
    if os.path.isfile(file):
      print "testing:" + os.path.basename(file)
      data2, header2 = nrrd.read(file)
      calignment = xscore.xslice(data2)
      zalignment = slicescore.zsampleslice(data2)
      yalignment = slicescore.ysampleslice(data2)
      xalignment = slicescore.xsampleslice(data2)
      del data2, header2
      r = np.fmin(np.array([xscore.symTest(slicescore.OverlapCoeff,calignment),methord(ctemplate,calignment),methord(ztemplate,zalignment),methord(ytemplate,yalignment),methord(xtemplate,xalignment)]))
      if not results==None:
        with open(results, 'a') as csvfile:
          spamwriter = csv.writer(csvfile)
          spamwriter.writerow([path,r[-1][0],"[Symmetry,Diagonal,Zsample,Ysample,Xsample,Final]score",r[-1][1],r[-1][2],r[-1][3],r[-1][4],r[-1][5],min(r[-1][1:])])
      del xalignment
    return r

#out = rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned/failed",results="/Volumes/Macintosh HD/Users/robertcourt/BTSync/failed-xscore.csv")

#out = rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned",results=None)
if __name__ == "__main__":
    print 'example: out = rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned",results="/Volumes/Data0/BTDataSync/NewLineageScans/Aligned/aligned-xscore.csv")'

#print 'Done.'

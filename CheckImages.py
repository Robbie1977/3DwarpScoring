import nrrd, os, glob, sys, csv
import xscore, slicescore

if os.path.isfile('/Volumes/Macintosh HD/Users/robertcourt/BTSync/usedtemplate.nrrd'):
    data1, header1 = nrrd.read('/Volumes/Macintosh HD/Users/robertcourt/BTSync/usedtemplate.nrrd')
elif os.path.isfile('/disk/data/VFBTools/Alignment/template/flyVNCtemplate20xA.nrrd'):
    data1, header1 = nrrd.read('/disk/data/VFBTools/Alignment/template/flyVNCtemplate20xA.nrrd')
else:
    print 'Template file missing!'
    data1 = []
if not data1==[]:
    xtemplate = xscore.xslice(data1)
    ztemplate = slicescore.zsampleslice(data1)
    ytemplate = slicescore.ysampleslice(data1)
    xtemplate = slicescore.xsampleslice(data1)
    del data1, header1

def rateAll(path,match="*BG*.nrrd",results="./OverlapResults.csv"):
    r=[]
    for file in glob.glob(path + os.sep + match):
        print "testing:" + os.path.basename(file)
        data2, header2 = nrrd.read(file)
        xalignment = xscore.xslice(data2)
        zalignment = slicescore.zsampleslice(data2)
        yalignment = slicescore.ysampleslice(data2)
        xalignment = slicescore.xsampleslice(data2)
        del data2, header2
        r.append((os.path.basename(file),xscore.symTest(xscore.OverlapCoeff,xalignment),xscore.OverlapCoeff(xtemplate,xalignment),slicescore.OverlapCoeff(ztemplate,zalignment),slicescore.OverlapCoeff(ytemplate,yalignment),slicescore.OverlapCoeff(xtemplate,xalignment)))
        if not results==None:
            with open(results, 'a') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([path,os.path.basename(file),"xscore",r[-1][1],r[-1][2],r[-1][3]r[-1][4]r[-1][5]])
        del xalignment
    return r

#out = rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned/failed",results="/Volumes/Macintosh HD/Users/robertcourt/BTSync/failed-xscore.csv")

#out = rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned",results=None)

print 'example: out = rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned",results="/Volumes/Data0/BTDataSync/NewLineageScans/Aligned/aligned-xscore.csv")'

#print 'Done.'

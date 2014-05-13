import nrrd, os, glob, sys, csv
import xscore

data1, header1 = nrrd.read('/Volumes/Macintosh HD/Users/robertcourt/BTSync/usedtemplate.nrrd')
template = xscore.xslice(data1)
del data1, header1

def rateAll(path,match="*BG*.nrrd",results="./OverlapResults.csv"):
    r=[]
    for file in glob.glob(path + os.sep + match):
        print "testing:" + os.path.basename(file)
        data2, header2 = nrrd.read(file)
        alignment = xscore.xslice(data2)
        del data2, header2
        r.append((os.path.basename(file),xscore.symTest(xscore.OverlapCoeff,alignment),xscore.OverlapCoeff(template,alignment)))
        if not results==None:
            with open(results, 'a') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([path,os.path.basename(file),"xscore",r[-1][1],r[-1][2]])
        del alignment
    return r
        
#rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned",results="/Volumes/Macintosh HD/Users/robertcourt/BTSync/xscore.csv")

out = rateAll("/Volumes/Data0/BTDataSync/NewLineageScans/Aligned",results=None)
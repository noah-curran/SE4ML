# kmean.py
import sys
import random
from datapoint import DataPoint
from centroid  import Centroid

def distance(datapoint, centroid):
    sum = 0
    dim = datapoint.getDimension()
    for ind in range(0, dim):
        val1 = datapoint._data[ind]
        val2 = centroid.data[ind]
        diff = val1 - val2
        sum = sum + diff * diff
    return sum

def cluster(dataArray, kval):
    numdp = len(dataArray)
    centroidArray = []
    dim = dataArray[0].getDimension()
    for ind in range(0, kval):
        ctd = Centroid(dim, ind)
        centroidArray.append(ctd)
    done = False
    while (done == False):
        done = True
        for cluindex in range(0, kval):
            centroidArray[cluindex].reset()
        # calculate the centroid of each cluster
        for dpindex in range(0, numdp):
            clu = dataArray[dpindex].getCluster()
            centroidArray[clu].addPoint(dataArray[dpindex])
        for cluindex in range(0, kval):
            centroidArray[cluindex].findCenter()
        # find the closet centroid
        for dpindex in range(0, numdp):
            mindist = sys.maxint # minimum distance so far
            minclu  = -1
            for cluindex in range(0, kval):
                dist = distance(dataArray[dpindex], centroidArray[cluindex])
                if (mindist > dist):
                    mindist = dist
                    minclu = cluindex
            curclu = dataArray[dpindex].getCluster()
            if (curclu != minclu):
                # this data point is assigned to a different cluster
                done = False
                dataArray[dpindex].changeCluster(minclu)
    return centroidArray

def readfile(fhd, kval):
    dataArray = []
    for oneline in fhd:
        # assign each data point to a cluster randomly
        clu = random.randint(0, kval - 1)
        dp = DataPoint(map(int, oneline.split()), clu)
        dataArray.append(dp)
    return dataArray

def kmean(filename, kval):
    print "kmean", filename, kval
    try:
        fhd = open(filename)
    except:
        sys.exit('open fail')
    dataArray = readfile(fhd, kval)
    fhd.close()
    numdp = len(dataArray)    
    for dpindex in range(0, numdp):
        dataArray[dpindex].printData()
    print '-------------------------------'
    centroidArray = cluster(dataArray, kval)
    print '+++++++++++++++++++++++++++++++'
    for dpindex in range(0, numdp):
        dataArray[dpindex].printData()

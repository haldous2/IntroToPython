
import math

def distance(x1,y1,x2,y2):

    """Calculate distance between two points x & y. Not sure what units this calculation is in, assuming miles"""

    cDistance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
    return cDistance

print "distance %f" % distance(1,2,3,4)


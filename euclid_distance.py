import math

def scalar(v1, v2):
    return sum([x*y for x,y in zip(v1,v2)])

def square(v):
    return scalar(v,v)
  
def sub(v1, v2):
    return tuple([x-y for x,y in zip(v1,v2)])

# euclidean distance is ||v1-v2|| => sqrt((v1-v2)^2) => sqrt( (v1-v2) * (v1-v2)) 
def euclid_distance(v1, v2):
    return math.sqrt(square(sub(v1,v2)))
  
v1 = (9,8,6,2)
v2 = (7,8,5,3)

#check here: http://calculator-fx.com/calculator/distance/euclidean-distance
print "Euclidean distance of",v1,",",v2,"is:",round(euclid_distance(v1, v2), 5),"(2.44949 expected)"
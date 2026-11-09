import math
def location(a1,a2,l1,l2):
    x=(l1 * math.cos(math.radians(a1)))+ (l2 * math.cos(math.radians(a1+ a2)))
    y=(l1 * math.sin(math.radians(a1)))+ (l2 * math.sin(math.radians(a1+ a2)))
    return x,y
print(location(0,90,2,1))
print(location(30,60,2,1))
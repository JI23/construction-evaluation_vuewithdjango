import math
import numpy

pi = 3.14159
miu = math.log(0.04)
#miu = 0.827658
sigma = 0.4
lowlimit = 0.0000001
deviation = 0.001



def fp(x):
    #return math.exp(-(math.log(x)-miu))/2/pow(sigma,2)/x/sigma
    return math.exp(-pow(math.log(x)-miu,2)/2/sigma/sigma)/x/sigma/numpy.sqrt(2*pi)

def setp(EDP):
    return getp(EDP)

def getp(EDP):
    if(sigma == 0 or miu == 0):
        return 1
    if(EDP > (10 * math.exp(miu) + 10 * sigma)):
        return 1
    f1 = fp(lowlimit) + fp(EDP)
    f2 = fp((lowlimit+EDP)/2)
    f3 = 0
    s = (EDP - lowlimit) / 6 * (f1 + 4 * f2)
    n = 2
    h = (EDP - lowlimit) / 4
    f2 = f2 + f3
    s0 = s
    f3 = 0
    for i in range(n+1):
        if i == 0:
            continue
        else:
            f3 = f3 + fp(lowlimit + (2 * i - 1) * h)
    s = h / 3 * (f1 + 2 * f2 + 4 * f3)
    n *= 2
    h /= 2
    while((abs(s-s0) > deviation) or (abs(s - s0) > 0.001 * s) or (4 * h > sigma)):
        f2 = f2 + f3
        s0 = s
        f3 = 0
        for i in range(n+1):
            if i == 0:
                continue
            else:
                f3 = f3 + fp(lowlimit + (2 * i - 1) * h)
        s = h / 3 * (f1 + 2 * f2 + 4 * f3)
        n *= 2
        h /= 2
    return s

def main(x):
    print (setp(x))

#print (miu)
j = 0.02
for i in range(16):
    main(j)
    j = j + 0.02
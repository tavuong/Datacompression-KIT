from math import cos, pi, sqrt
import numpy as np
#-----------------------------------------------------------------------
def dct_2(x):
    retval = np.zeros_like(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            for k in range(x.shape[0]):
                for l in range(x.shape[1]):
                    retval[i,j] += x[k,l] * np.cos(np.pi*i*(2*k+1)/2/x.shape[0]) * np.cos(np.pi*j*(2*l+1)/2/x.shape[1])

            if i == 0:
                retval[i,j] *= np.sqrt(1/x.shape[0])
            else:
                retval[i,j] *= np.sqrt(2/x.shape[0])
            if j == 0:
                retval[i,j] *= np.sqrt(1/x.shape[0])
            else:
                retval[i,j] *= np.sqrt(2/x.shape[0])
    return retval
#-----------------------------------------------------------------------
def idct_2(X):
    temp = np.zeros_like(X)
    # IDCT in horizontal direction
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            temp[i,j] = X[i,0] / np.sqrt(X.shape[1])
            for k in range(1,X.shape[1]):
                temp[i,j] += X[i,k] * np.cos(np.pi*k*(2*j+1)/2/X.shape[1]) * np.sqrt(2/X.shape[1])
    
    # IDCT in vertical direction
    retval = np.zeros_like(X)
    for j in range(X.shape[1]):
        for i in range(X.shape[0]):
            retval[i,j] = temp[0,j] / np.sqrt(X.shape[0])
            for k in range(1,X.shape[0]):
                retval[i,j] += temp[k,j] * np.cos(np.pi*k*(2*i+1)/2/X.shape[0]) * np.sqrt(2/X.shape[0])
                   
    return retval
#-----------------------------------------------------------------------
def lowpass_2d (x,nbit=0):
# 2d  Lowpass Filter
# x: SpektralMatrix
# nbit : Blocklänge des 2d Filter nbit*nbit 
    retval = np.zeros_like(x)
    map = np.zeros_like(x)    
    nmap2 = x.shape[0]
    nmap = nbit
#    print ("nmap2=" + str(nmap2))
#    print ("nmap=" + str(nmap))
#    for i in range (nmap2):
#        for j in range (nmap2):
#            map [i, j] = 0.0
    for i in range (nmap):
        for j in range (nmap):
            map [i, j] = 1.0

    for i in range(nmap2):
        for j in range(nmap2):
            retval[i,j] = x[i,j] * map [i,j] 
    return retval

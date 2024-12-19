import numpy as np
arr = np.array([i for i in range(1,11)])
wight_arr = np.array([120,35,65,34,84,63,12,65.7,42.2,75.6])
A_sloop = np.vstack([arr,np.ones(len(arr))]).T
a, b = np.linalg.lstsq(A_sloop,wight_arr,rcond=None)[0]
def calculate(y,x,a,b,sigma):
    N = len(y)
    square = np.sum(((y-a -b*x)/sigma)**2)
    free_dgree =  N-2
    # if we have more than two for instane a, b, c it could be 3
    return  square, free_dgree

print(calculate(wight_arr,arr,a,b,10))

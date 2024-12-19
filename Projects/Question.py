import numpy as np
b = np.linspace(2,19,10)
print(b)
np.set_printoptions(formatter={'float': lambda x: format(x,'5.1e')})
print(b)
#[ 2.          3.88888889  5.77777778  7.66666667  9.55555556 11.44444444
 #13.33333333 15.22222222 17.11111111 19.        ]
#[2.0e+00 3.9e+00 5.8e+00 7.7e+00 9.6e+00 1.1e+01 1.3e+01 1.5e+01 1.7e+01
 #1.9e+01]
c= np.linspace(2,19,10)
print(c)
np.set_printoptions(formatter={'float':lambda x : format(x,'4.2f')})
print(c)

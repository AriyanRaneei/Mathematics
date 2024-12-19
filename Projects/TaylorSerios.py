def taylorss_sin(x):
    term = x
    sin = 1
    pow1 = 3
    while True:
        yield term
        sin *= -1
        term  = sin *np.power(x,3)/math.factorial(pow1)
        pow1 += 2


e = taylorss_sin(15) 
print(next(e))
print(next(e)) 
print(next(e))

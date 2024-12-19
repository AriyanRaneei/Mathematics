def deriv(f, x, h=1.e-9, *params):
    return (f(x + h, *params) - f(x - h, *params))/(2.*h)

def f0(x):
    return 4*x**5

print(deriv(f0,3))
def f1(x,a,p):
    return a *x **p
print(deriv(f1,3,1.e-9,*(4,5)))

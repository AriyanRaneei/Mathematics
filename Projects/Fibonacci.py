def fibol0(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    else:
        return fibol0(n-1) + fibol0(n-2)


print(fibol0(5))

def odd_finder(n):
    if (-1)** n <0:
        return ("your number that you manetioned is an odd number")
    else:
        return ("its even number")


print(odd_finder(3))
print(odd_finder(2))

def odd_finder_mirkhan_way(n):
    if n % 2 ==0:
        return ("your number that you manetioned  is an even number")
    else:
        return ("its odd number")
print(odd_finder_mirkhan_way(2))
print(odd_finder_mirkhan_way(3))

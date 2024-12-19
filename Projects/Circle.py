def circle(r,x0,y0,n):
    theta = np.linspace(0.,2*np.pi,n,endpoint=False)
    x,y = r * np.cos(theta),r * np.sin(theta)
    return x0 +x , y0 +y

a1 = circle(100,50,80,180)
fig, ax = plt.subplots(1,1 ,figsize=(8,8),facecolor="lightgray")
ax.plot(a1,'C0')
plt.savefig("circle.pdf")
plt.show()

def circle(r,x0,y0,n):
    theta = np.linspace(0.,2*np.pi,n,endpoint=False)
    x,y = r * np.cos(theta),r * np.sin(theta)
    return x0 +x , y0 +y
a = circle(3,n= 3,y0=4,x0=-2)
print(a)
def product(*agrs):
    print("args={}".format(agrs))
    p =1
    for num in agrs:
        p*= num
    return p


print(product(2.31,7))

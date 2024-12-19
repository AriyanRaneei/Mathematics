def circle(r,x0,y0,n):
    theta = np.linspace(0.,2*np.pi,n,endpoint=False)
    x,y = r * np.cos(theta),r * np.sin(theta)
    return x0 +x , y0 +y

a1 = circle(100,50,80,180)
fig, ax = plt.subplots(1,1 ,figsize=(8,8),facecolor="lightgray")
ax.plot(a1,'C0')
plt.savefig("circle.pdf")
plt.show()

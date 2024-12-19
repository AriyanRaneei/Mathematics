b = -3
w = 2.3
p = 2
n = w+b*p

def hardlim(x):
    if x< 0 :
        return 0
    else:
        return 1
def purelin(x):
    return x

def satlin(x):
    if x<0:
        return 0
    elif 0<= x <= 1:
        return x
   
    else:
        
        return 1

def logsig(x):
    a = 1/1+np.power(np.e,-x)
    return a



s =  [i for i in range(1000)]

lst = []
for i in s:
     a = logsig(i)
     lst.append(a)


plt.plot(s, lst)


lst2 = []
for i in s: 
    a = satlin(i)
    lst2.append(a)
    
    
s, lst2 = np.meshgrid(s,lst2)
fig2, ax2 = plt.subplots(subplot_kw={"projection":"3d"})
ax2.plot_surface(s,lst,lst2,cmap = cm.coolwarm)



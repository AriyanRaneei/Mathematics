import numpy as np
import matplotlib.pyplot as plt
theta = np.arange(0.01,8.,0.04)
equation = np.sqrt(np.power(8/theta,2)-1)
ytan = np.tan(theta)
ytantan = np.ma.masked_where(np.abs(ytan)>20.,ytan)
ycot = 1/np.tan(theta)
ycot = np.ma.masked_where(np.abs(ycot)>20.,ycot)
plt.figure(figsize=(8,5),edgecolor="red",facecolor="gray")

plt.plot(theta,equation,linestyle=':')
plt.plot(theta,ytan)
plt.xlim(0,8)
plt.ylim(-8,8)
plt.axhline(color="pink", zorder=-1)
plt.axvline(x=np.pi/2., color="pink",linestyle='--',zorder=-1 )
plt.axvline(x=5.*np.pi/2,color="black",linestyle='--', zorder=-1)
plt.xlabel("thetha")
plt.ylabel("tan(theta)")
plt.savefig("figuresub.pdf")

plt.show()

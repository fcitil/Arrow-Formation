import matplotlib.pylab as plt
import math
"""
distance between adjacent agent : u_b
“arrow head” half of arraw head angle: a_b
guida following distance : u_k
guide reference angle (wrt compass) : a_k"""
#açı değerleri +x eksenine göre alınmıştır(birim çember)
x=180#can rotate all agents wrt guide agent
n=11 #number of agent must be in 2n+1 for (except guide agent)
u_b=60
a_b=math.radians(30)
u_k=60
a_k=math.radians(0+x)

#uav_guide
#location=[39.924980,32.839794]
location=[10,10]
#The agent which is closest to guide agent
uav1location=[location[0]+u_k*math.cos(a_k),location[1]+u_k*math.sin(a_k)]

uavlocations = []

xy1 = [location[0]+u_k*math.cos(a_k), location[1]+u_k*math.sin(a_k)]
xy2 = [location[0]+u_k*math.cos(a_k), location[1]+u_k*math.sin(a_k)]

angle1 = a_k- a_b
angle2 = a_k+ a_b

for _ in range(int((n-1)/ 2)):
    xy1 = [xy1[0]+u_b*math.cos(angle1), xy1[1]+ u_b*math.sin(angle1)]
    xy2 = [xy2[0]+u_b*math.cos(angle2), xy2[1]+ u_b*math.sin(angle2)]
    uavlocations.append(xy1)
    uavlocations.append(xy2)
x=[uav1location[0], location[0]]
y=[uav1location[1], location[1]]

for i in uavlocations:
    x.append(i[0])
    y.append(i[1])

#plotting the data
plt.plot(x, y, 'r+',label="Agents")
plt.plot(x[1], y[1], 'bo', label="Guide Agent")
plt.xlabel("Number of Agent: "+str(n))
plt.ylabel("Arrow Head Angle: "+str(math.degrees(a_b)*2))
plt.legend()
plt.axis('square')
plt.grid()
plt.show()

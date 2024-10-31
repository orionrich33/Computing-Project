import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

#inputs
m_m = 7.348*1e22               #Mass of Moon
m_e = 5.972*1e24            #Mass of Earth
r_e = 4670*1e3                       #Radius of Earth to C.O.M. in km
r_m = 379728*1e3                 #Radius of Moon to C.O.M.
G = 6.67*1e-11                   #Gravitational constant
a = 10             #Time step 
phi = np.pi           #phase
d = 3.844*1e8               #earth-moon distance

#compute L2
l2_delta_r = d*(m_m/(3*m_e))**(1/3)
l2 = l2_delta_r+r_m 

#compute T
T = 2*np.pi*np.sqrt(((r_e+r_m)**3)/(G*(m_e+m_m)))

#compute l2_v
l2_v = 0.9*(l2*2*np.pi)/T

#create arrays
i_r_pos = np.array([l2*1.1,0])            #Initial position of rocket
i_r_vel = np.array([0,l2_v])            #Initial velocity of rocket
l_period = 29.5*24*60*60               #lunar period
N = round(l_period/a)         #number of iterations
s = (N,2)
s2 = (N+1,2)
m_pos = np.zeros(s)
e_pos = np.zeros(s)
r_pos = np.zeros(s2)
r_vel = np.zeros(s2)
r_acc = np.zeros(s)
r_pos[0] = i_r_pos
r_vel[0] = i_r_vel

for i in range(0,N):
    theta = (2*np.pi*(i*a))/T
    e_pos[i] = np.array([r_e*np.cos(theta+phi), r_e*np.sin(theta+phi)])
    m_pos[i] = np.array([r_m*np.cos(theta), r_m*np.sin(theta)])
    de_x = r_pos[i][0]-e_pos[i][0]
    dm_x = r_pos[i][0]-m_pos[i][0]
    de_y = r_pos[i][1]-e_pos[i][1]
    dm_y = r_pos[i][1]-m_pos[i][1]
    de = np.sqrt((de_x)**2+(de_y)**2)
    dm = np.sqrt((dm_x)**2+(dm_y)**2)
    r_acc_x = (-1*G*m_e*(de_x))/(de**3) - ((G*m_m*(de_x))/(de**3))
    r_acc_y = (-1*G*m_e*(de_y))/(de**3) - ((G*m_m*(de_y))/(de**3))
    r_acc[i] = np.array([r_acc_x, r_acc_y])
    r_vel_x = r_vel[i][0] + a*r_acc_x
    r_vel_y = r_vel[i][1] + a*r_acc_y
    r_vel[i+1] = np.array([r_vel_x, r_vel_y])
    r_pos_x = r_pos[i][0]+a*r_vel_x+(((a**2)/2)*r_acc_x)
    r_pos_y = r_pos[i][1]+a*r_vel_y+(((a**2)/2)*r_acc_y)
    r_pos[i+1] = [r_pos_x, r_pos_y]

xrocket = r_pos[0::1000][:,0]
yrocket = r_pos[0::1000][:,1]
xmoon = m_pos[0::1000][:,0]
ymoon = m_pos[0::1000][:,1]
xearth = e_pos[0::1000][:,0]
yearth = e_pos[0::1000][:,1]

plt.style.use('dark_background')

fig, ax = plt.subplots(figsize=(5, 5))
ax = plt.axes(xlim=(min(xrocket)+0.1*min(xrocket), max(xrocket)+0.1*max(xrocket)), ylim=(min(ymoon)+0.1*min(ymoon), max(yrocket)+0.1*max(yrocket)))
rocket, = ax.plot([], [], color='g', lw=1, label='Rocket')
moon, = ax.plot([], [], color='blue', lw=1, label='Moon')
earth, = ax.plot([], [], color='r', lw=1, label='Earth')


def animate(i):
    rocket.set_data(xrocket[:i],yrocket[:i])
    moon.set_data(xmoon[:i],ymoon[:i])
    earth.set_data(xearth[:i],yearth[:i])
    return rocket,moon,earth

anim = FuncAnimation(fig, animate, frames=len(xrocket), interval=100, repeat=False)
anim.save('cirlce_ani.gif', writer='pillow')
plt.legend()
plt.show()





    


import numpy as np
import matplotlib.pyplot as plt

#inputs
m_m = 7.348*1e22               #Mass of Moon
m_e = 5.972*1e24            #Mass of Earth
r_e = 4670*1e3                       #Radius of Earth to C.O.M. in km
r_m = 379728*1e3                 #Radius of Moon to C.O.M.
G = 6.67*1e-11                   #Gravitational constant
a = 10             #Time step 
phi = 0           #phase
d = 3.844*1e8               #earth-moon distance

#compute L2
l2_delta_r = d*(m_m/(3*m_e))**(1/3)
l2 = l2_delta_r+r_m 

#compute T
T = 2*np.pi*np.sqrt(((r_e+r_m)**3)/(G*(m_e+m_m)))

#compute l2_v
l2_v = (l2*2*np.pi)/T

#create arrays
i_r_pos = np.array([l2*1.1,0])            #Initial position of rocket
i_r_vel = np.array([0,l2_v])            #Initial velocity of rocket
N = 5000000         #number of iterations
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
    e_pos[i] = np.array([r_e*np.cos(theta), r_e*np.sin(theta)])
    m_pos[i] = np.array([r_m*np.cos(theta+phi), r_m*np.sin(theta+phi)])
    de_x = r_pos[i][0]-e_pos[i][0]
    dm_x = r_pos[i][0]-m_pos[i][0]
    de_y = r_pos[i][1]-e_pos[i][1]
    dm_y = r_pos[i][1]-m_pos[i][1]
    de = np.sqrt((de_x)**2+(r_pos[i][1]-e_pos[i][1])**2)
    dm = np.sqrt((dm_x)**2+(r_pos[i][1]-m_pos[i][1])**2)
    r_acc_x = (-1*G*m_e*(de_x))/(de**3) - ((G*m_m*(de_x))/(de**3))
    r_acc_y = (-1*G*m_e*(de_y))/(de**3) - ((G*m_m*(de_y))/(de**3))
    r_acc[i] = np.array([r_acc_x, r_acc_y])
    r_vel_x = r_vel[i][0] + a*r_acc_x
    r_vel_y = r_vel[i][1] + a*r_acc_y
    r_vel[i+1] = np.array([r_vel_x, r_vel_y])
    r_pos_x = r_pos[i][0]+a*r_vel_x+(((a**2)/2)*r_acc_x)
    r_pos_y = r_pos[i][1]+a*r_vel_y+(((a**2)/2)*r_acc_y)
    r_pos[i+1] = [r_pos_x, r_pos_y]

print(m_pos)
    
plt.plot(r_pos[:,0], r_pos[:,1], color='red', label='rocket')
plt.plot(e_pos[:,0], e_pos[:,1], color='blue', label='earth')
plt.plot(m_pos[:,0], m_pos[:,1], color='green', label='moon')
plt.legend()
plt.show()





    


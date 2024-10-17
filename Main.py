import numpy as np
import matplotlib.pyplot as plt

#inputs
m_m = 7.348*1e22               #Mass of Moon
m_e = 5.972*1e23            #Mass of Earth
r_e = 4670                       #Radius of Earth to C.O.M. in km
r_m = 379728                 #Radius of Moon to C.O.M.
i_r_pos = np.array([100000,0])            #Initial position of rocket
i_r_vel = np.array([-10000,30000])            #Initial velocity of rocket
G = 6.67*1e-11                   #Gravitational constant
a = 100                  #Time step 

#create arrays
N = 50            #number of iterations
s = (N,2)
m_pos = np.zeros(s)
e_pos = np.zeros(s)
r_pos = np.zeros(s)
r_vel = np.zeros(s)
r_acc = np.zeros(s)
t = np.zeros(s)
r_pos[0] = i_r_pos
r_vel[0] = i_r_vel

#compute T
T = 2*np.pi*np.sqrt(((r_e+r_m)**3)/(G*(m_e+m_m)))


for i in range(N):
    theta = (2*np.pi*(i*a))/T
    xe = r_e*np.sin(theta)
    ye = r_e*np.cos(theta)
    xm = r_m*np.sin(theta)
    ym = r_m*np.cos(theta)
    de_x = r_pos[-1][0]-xe
    dm_x = r_pos[-1][0]-xm
    de_y = r_pos[-1][1]-ye
    dm_y = r_pos[-1][1]-ym
    de = np.sqrt((de_x)**2+(r_pos[-1][1]-ye)**2)
    dm = np.sqrt((dm_x)**2+(r_pos[-1][1]-ym)**2)
    r_acc_x = (-1*G*m_e*(de_x))/(de**3) - ((G*m_e*(de_x))/(de**3))
    r_acc_y = (-1*G*m_e*(de_y))/(de**3) - ((G*m_e*(de_y))/(de**3))
    r_acc[i] = np.array([r_acc_x, r_acc_y])
    r_vel_x = r_vel[-1][0] + a*r_acc_x
    r_vel_y = r_vel[-1][1] + a*r_acc_y
    r_vel[i] = np.array([r_vel_x, r_vel_y])
    r_pos_x = r_pos[-1][0]+a*r_vel_x+((a**2/2)*r_acc_x)
    r_pos_y = r_pos[-1][1]+a*r_vel_y+((a**2/2)*r_acc_y)
    r_pos[i] = [r_pos_x, r_pos_y]
    t[i] = a*i
 
    

plt.plot(r_pos)
plt.show()


    


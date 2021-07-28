import numpy as np
import matplotlib.pyplot as plt

# 상수 정의
G = 6.67384e-11; M = 5.972e24; R = 6.3781e+6

# 시뮬레이션 조건
r = R
v = 10000
angle_i = 0
v_r = v*np.sin(angle_i)
r2w = v*np.cos(angle_i)*r
w1 = r2w/r**2
theta = 0
dt = 0.1

x = [r*np.cos(theta)]
y = [r*np.sin(theta)]

while -2 * np.pi < theta < 3 * np.pi:
    dr = v_r*dt
    d_theta = w1*dt
    dv = G*M/(r**2)*dt

    r += dr
    theta += d_theta
    
    w2 = r2w/r**2
    v_r1 = v_r
    if v_r - dv < 0 :
        v_r = -1
    else :
        v_r = 1
    v_r *= (r2w*(w1 - w2) + (v_r1 - dv)**2)**0.5
    w1 = w2

    print (theta) 

    x.append(r*np.cos(theta))
    y.append(r*np.sin(theta))

# 출력
plt.figure(figsize=(7,7))
plt.axis('equal')
plt.scatter(x, y, c ='r', s= 0.005)
plt.scatter(0,0, c='k')
plt.show()
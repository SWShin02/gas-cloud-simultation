import numpy as np
import matplotlib.pyplot as plt

# 상수 정의
G = 6.67384e-11; M = 5.972e24; R = 6.3781e+6

# 시뮬레이션 조건
r = R
v = 5800
angle_i = 0.25*np.pi
v_r = v*np.sin(angle_i)
r2w = v*np.cos(angle_i) * r
w1 = r2w/r**2
theta = 0
dt = 0.1

x = [r*np.cos(theta)]
y = [r*np.sin(theta)]

while -2 * np.pi < theta < 2 * np.pi:
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


    if r < R:
        v_r *= -1    
    x.append(r*np.cos(theta))
    y.append(r*np.sin(theta))

# 출력
plt.figure(figsize=(7,7))
a = plt.axes(xlim=(-2*R,2*R),ylim=(-2*R,2*R))
c = plt.Circle((0,0),R)
a.add_patch(c)
plt.axis('equal')
plt.plot(x, y, c ='r')
plt.show()

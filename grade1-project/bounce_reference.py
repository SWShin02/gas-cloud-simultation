import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
rc('animation', html = 'jshtml')

def reflection(x,y,vx,vy,px,py):
  m = y / x 
  v = np.sqrt(vx**2 + vy**2)
  vx_h = vx / v
  vy_h = vy / v
  a = np.array([[vx_h], [vy_h]]) 
  b = np.array([[1-m**2, 2*m], [2*m, -1+m**2]])
  c = 1/(m**2 + 1) * np.dot(b,a)
  vx = v * -c[0][0]
  vy = v * -c[1][0]  
  x += vx*dt
  y += vy*dt
  px.append(x)
  py.append(y)
  return (x, y, vx, vy, px, py)

G = 6.673e-11; M = 5.97e+24; R = 6.3781e+6; v0 = 5.8e+3; dt = 0.1
x = 0; y = R; m = 0; k = 0
px, py = [], []

theta = 45
theta *= np.pi/180.

vx = v0*np.cos(theta)
vy = v0*np.sin(theta)

for i in range(10):
  while 1:
    x += vx * dt
    y += vy * dt
    r = np.sqrt(x**2 + y**2)
    vx += -G*M*x*dt / (r**3)
    vy += -G*M*y*dt / (r**3)
    px.append(x)
    py.append(y)
    if r <= R:
      break
  x, y, vx, vy, px, py = reflection(x,y,vx,vy, px, py)

a = plt.axes(xlim=(-2*R,2*R),ylim=(-2*R,2*R))
c = plt.Circle((0,0),R)
a.add_patch(c)
plt.axis('equal')
plt.plot(px, py, c ='r')
plt.show()
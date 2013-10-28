from matplotlib.pyplot import * 
from matplotlib.mlab import *   
from numpy import *

name = 'AG_HD_week2_a45'
fid = open(name+'.dat')

lines, phi = [], []
phi0 = 0
for line in fid:
    data = line.split(',')
    lines.append(data[0])
    angle = float(data[1]) + float(data[2])/3 + float(data[3])/30
    print(angle)
    #if len(phi)>0:
    #angle =  (angle - phi0)
        #else:
        #phi0 = angle
        #angle = 90
    
        
    phi.append(angle)
    #print(pi*angle/360)


fid.close()

d = (10**(4))/6
newname = name + 'lam.dat'
f = open(newname, 'w')
for i in range(len(lines)-1):
    #theta = pi/4 - phi[i+1]
    print str(d*(sin(-pi/4)+sin(pi*(45-(phi[0]-phi[i+1]))/180)))+'     ' + str(phi[i+1])+'     ' + lines[i+1] + '\n'
    f.write(str(str(d*(sin(-pi/4)+sin(pi*(45-(phi[0]-phi[i+1]))/180)))+'     ' + str(phi[i+1])+'     ' + lines[i+1] + '\n'))
    #f.write(str(str(K*(sqrt(2)/2+sin(phi[0]-phi[i+1])))+'     ' + lines[i+1] + '\n'))
f.close()


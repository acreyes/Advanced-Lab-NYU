
# Imports:
from matplotlib.pyplot import * 
from matplotlib.mlab import *   
from numpy import *

<<<<<<< HEAD
####################LOCAL FUNCTIONS##############
def lam(phi0, phi, d):
    lamda = d*(sin(-pi/4) + sin(pi*(45-(phi0 - phi))/180))
    return(lamda)
    
name = 'AG_HD_week3_a45'
fid = open(name+'.dat')

deg_e = 0.0023 
lines, phi, shift_phi = [], [], []
=======
# Edit name here
name = 'AG_HD_week2_a45'


fid = open(name+'.dat')

# Read data into arrays
lines, phi = [], []
phi0 = 0
>>>>>>> fc44e2baa3f97de288cacdab4cd08e567fc5824c
for line in fid:
    data = line.split(',')
    lines.append(data[0])
    angle = float(data[1]) + float(data[2])/3 + float(data[3])/30
<<<<<<< HEAD
    if len(phi) > 0 :
        first = angle + deg_e*float(data[4])
        second = angle + deg_e*float(data[5])
        phi.append(first)
        shift_phi.append(second)
    else:
        phi0=angle
        phi.append('blank')
        shift_phi.append('blank')
    
    
    #print(angle)
    #if len(phi)>0:
    #angle =  (angle - phi0)
        #else:
        #phi0 = angle
        #angle = 90
    
        
    #print(pi*angle/360)


=======
    print(angle)
    phi.append(angle)
>>>>>>> fc44e2baa3f97de288cacdab4cd08e567fc5824c
fid.close()


d = (10**(4))/6
newname = name + 'lam.dat'
f = open(newname, 'w')
for i in range(len(lines)-1):
<<<<<<< HEAD
    lam1 = lam(phi0, phi[i+1], d)
    lam2 = lam(phi0, shift_phi[i+1], d)
    wline = str(lam1) + '    ' + str(lam2) + '    ' + str(lam1-lam2) + '    ' + lines[i+1] + '\n'
    f.write(wline)
    '''
    #theta = pi/4 - phi[i+1]
    print str(d*(sin(-pi/4)+sin(pi*(45-(phi[0]-phi[i+1]))/180)))+'     ' + str(phi[i+1])+'     ' + lines[i+1] + '\n'
    f.write(str(str(d*(sin(-pi/4)+sin(pi*(45-(phi[0]-phi[i+1]))/180)))+'     ' + str(phi[i+1])+'     ' + lines[i+1] + '\n'))
    #f.write(str(str(K*(sqrt(2)/2+sin(phi[0]-phi[i+1])))+'     ' + lines[i+1] + '\n'))
    '''
=======
    print str(d*(sin(-pi/4)+sin(pi*(45-(phi[0]-phi[i+1]))/180)))+'     ' + str(phi[i+1])+'     ' + lines[i+1] + '\n'
    f.write(str(str(d*(sin(-pi/4)+sin(pi*(45-(phi[0]-phi[i+1]))/180)))+'     '+ str(phi[i+1])+'     ' + lines[i+1] + '\n'))
>>>>>>> fc44e2baa3f97de288cacdab4cd08e567fc5824c
f.close()


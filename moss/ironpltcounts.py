import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import glob
import os
#!/usr/bin/python
# -*- coding: utf-8 -*-


##############THINGS TO CHANGE##########
folder = "neg_steel_0.7v"
tit = (u'Mossbauer Spectrum of Iron')
centers = [-5.2, -1.5, 1.2, 4.9, 8.3]
global nPeaks 
nPeaks = len(centers)
 
##########LOCAL FUNCTIONS #############
# p is a list of parameters
# hwhm,  intensity. c is center of peak
def lorentzian(x,c,*p):
    numerator =  (p[0]**2 )
    denominator = ( x - (c) )**2 + p[0]**2
    y = p[1]*(numerator/denominator) 
    return y

def velocity(freq):
    amp = 0.508 #in mm
    v = amp * freq
    return(v)
def multlor(x, *p): 
    centers = p[0:nPeaks]
    y = p[nPeaks]
    intensities = p[nPeaks +1: 2*nPeaks+1]
    widths = p[2*nPeaks+1:3*nPeaks+1]
    for i in range(nPeaks):
        q = [widths[i], intensities[i]]
        y += lorentzian(x, centers[i], *q) 
    return(y)


    ################READ IN DATA#######################
    ###################################################
folder = "pos_fe_07"
os.chdir(folder)
net, pm, vel = [], [], []
#########pos values#########
for files in glob.glob("*.Rpt"): #loop over files
    name = files.split('.Rpt')
    v = velocity(float(name[0].strip('p')))
    vel.append(v)
    fid = open(files)
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    data = a.split()
    net.append(float(data[4]))
    pm.append(float(data[5]))

folder = "neg_iron_two"
os.chdir('./..')
os.chdir(folder)

#########neg values#########
for files in glob.glob("*.Rpt"): #loop over files
    name = files.split('.Rpt')
    v = -1*velocity(float(name[0].strip('n')))
    vel.append(v)
    fid = open(files)
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    data = a.split()
    #print files
    net.append(float(data[4]))
    pm.append(float(data[5]))
#############FITTING######################
intensity = -2000
width = 0.5
vshift = 5500
p = centers
p.append(vshift)
#p should be [centers, vshift, intensities, widths]

for i in range(nPeaks):
    p.append(intensity)
for i in range(nPeaks):
    p.append(width)
print p

x = np.linspace(-12, 12, 1000)
#plt.plot(x, multlor(x, *p))

popt, pcov = curve_fit(multlor, vel, net, p,maxfev=3000)
print 'lorentzian parameters'
print(popt)
#print pcov[0,0], pcov[1,1], pcov[2,2], pcov[3,3]
plt.plot(x, multlor(x,*popt), label = 'Lorentzian Fit')

plt.plot(vel, net, 'o')
plt.title(tit)
plt.xlim(-12, 12)
plt.xlabel('velocity (mm/s)')
plt.ylabel('Net Counts')
plt.show()

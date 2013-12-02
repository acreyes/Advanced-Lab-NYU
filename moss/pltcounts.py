import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import glob
import os
#!/usr/bin/python
# -*- coding: utf-8 -*-


##############THINGS TO CHANGE##########
folder = "neg_steel_0.7v"
tit = (u'Mossbauer Spectrum of Steel')

 
##########LOCAL FUNCTIONS #############
# p is a list of parameters
# hwhm, peak center, intensity, vertshift.
def lorentzian(x,*p):
    numerator =  (p[0]**2 )
    denominator = ( x - (p[1]) )**2 + p[0]**2
    y = p[2]*(numerator/denominator) + p[3]
    return y
def gaussian(x, *p):
    y = p[2]*np.exp(-((x-p[1])/p[0])**2) + p[3]
    return y

def velocity(freq):
    amp = 0.508 #in mm
    v = amp * freq
    return(v)

    ################READ IN DATA#######################
    ###################################################
os.chdir(folder)
net, pm, vel = [], [], []
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
    net.append(float(data[4]))
    pm.append(float(data[5]))

    #plt.plot(vel, net, 'o')
#plt.errorbar(vel, net, pm, fmt='bo', label = 'data')

#########positive values##########
folder = "pos_steel_0.7v"
os.chdir('./..')
os.chdir(folder)
#net, pm, vel = [], [], []
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

    #plt.plot(vel, net, 'o')
#plt.errorbar(vel, net, pm, fmt='bo', label = 'data')
folder = "pos_steel_v0.7_2"
os.chdir('./..')
os.chdir(folder)
#net, pm, vel = [], [], []
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

    ###############################################
    ###############################################

plt.plot(vel, net, 'o')

#############FITTING######################
p = [ 1, 0, 4000, 5000]
x = np.linspace(-10, 10, 1000)

popt, pcov = curve_fit(lorentzian, vel, net, p)
print 'lorentzian parameters'
print(popt)
plt.plot(x, lorentzian(x,*popt), label = 'Lorentzian Fit')

popt, pcov = curve_fit(gaussian, vel, net, p)
print 'Gaussian parameters'
print(popt)
plt.plot(x, gaussian( x, *popt), label = 'Gaussian Fit')

plt.legend(loc = 'lower right')

plt.title(tit)
plt.xlim(-10, 10)
plt.xlabel('velocity (mm/s)')
plt.ylabel('Net Counts')
plt.show()

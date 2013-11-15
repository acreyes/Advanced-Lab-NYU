import numpy as np 
import matplotlib.pyplot as plt
import glob
import os

##########LOCAL FUNCTIONS #############
def velocity(freq):
    amp = 0.508 #in mm
    v = amp * freq
    return(v)

os.chdir("pos_steel_0.7v")
net, pm, vel = [], [], []

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

plt.plot(vel, net, '-o')
plt.errorbar(vel, net, pm, fmt='bo', label = 'data')

plt.xlabel('velocity (mm/s)')
plt.ylabel('Net Counts')
plt.show()

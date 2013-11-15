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
net, pm, freqs = [], [], []

for files in glob.glob("*.Rpt"): #loop over files
    name = files.split('.Rpt')
    v = velocity(float(name[0].strip('p')))
    freqs.append(v)
    fid = open(files)
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    a = fid.readline()
    data = a.split()
    net.append(data[4])
    pm.append(data[5])

plt.plot(freqs, net, '-o')
plt.xlabel('velocity (mm/s)')
plt.ylabel('Net Counts')
plt.show()

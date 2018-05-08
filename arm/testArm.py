import tinyik
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def test():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
#     zline = np.linspace(0, 15, 1000)
#     xline = np.sin(zline)
#     yline = np.cos(zline)
#     ax.plot3D(xline, yline, zline, 'gray')   
#     # Data for three-dimensional scattered points
#     zdata = 15 * np.random.random(100)
#     xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
#     ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
#     ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
    Link1=[1., 0., 0.]
    Link2=[1., 0., 0.]
    
    arm = tinyik.Actuator(['z', Link1, 'z', Link2])
    print(arm.angles)
    print(arm.ee)
    #arm.angles = [np.pi / 6, np.pi / 6, np.pi / 3]  # or np.deg2rad([30, 60])
    arm.ee=[1, 1, 0.]
    print(arm.angles)
    print(np.round(np.rad2deg(arm.angles)))
   
    #arm.ee = [2 / np.sqrt(2), 2 / np.sqrt(2), 0.5]
    #print(arm.angles)
    #print(np.round(np.rad2deg(arm.angles)))
    
    #zline = np.linspace(0, 1)
    #ax.plot3D(zline, 5, zline, 'gray')   
    #ax.scatter3D(myList[0], myList[1], myList[2], 'gray')   
    
    
    N = 8
    
    
    
    Link1x = np.linspace(0, np.cos(np.round(np.rad2deg(arm.angles[0]))), N)
    Link1y = np.linspace(0, Link1[1], N)
    Link1z = np.linspace(0, np.sin(np.round(np.rad2deg(arm.angles[0]))), N)
    
    Link2x = np.linspace(np.cos(np.round(np.rad2deg(arm.angles[0]))), np.cos(np.round(np.rad2deg(arm.angles[0])))+np.cos(np.round(np.rad2deg(arm.angles[1]))), N)
    Link2y = np.linspace(Link2[1], Link1[1]+Link2[1], N)
    Link2z = np.linspace(np.sin(np.round(np.rad2deg(arm.angles[0]))), np.sin(np.round(np.rad2deg(arm.angles[0])))+np.sin(np.round(np.rad2deg(arm.angles[1]))), N)
    
    print(np.sin(np.round(np.rad2deg(arm.angles[0]))))
    
    plt.plot(Link1x, Link1y, Link1z)
    plt.plot(Link2x, Link2y, Link2z)
    
    #plt.ylim([-0.5, 1])
    plt.show()


test()
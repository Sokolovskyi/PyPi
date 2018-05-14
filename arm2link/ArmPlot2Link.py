'''
Copyright (C) 2013 Travis DeWolf
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import numpy as np
#import pyglet

import Arm2Link
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot():
    """A function for plotting an arm, and having it calculate the
    inverse kinematics such that given the mouse (x, y) position it
    finds the appropriate joint angles to reach that point."""

    # create an instance of the arm
    arm = Arm2Link.Arm3Link(L=np.array([300, 200]))

    # make our window for drawin'
    #window = pyglet.window.Window()

#     label = pyglet.text.Label(
#         'Mouse (x,y)', font_name='Times New Roman',
#         font_size=36, x=window.width//2, y=window.height//2,
#         anchor_x='center', anchor_y='center')

    def get_joint_positions():
        """This method finds the (x,y) coordinates of each joint"""

        x = np.array([
            0,
            arm.L[0]*np.cos(arm.q[0]),
            arm.L[0]*np.cos(arm.q[0]) + arm.L[1]*np.cos(arm.q[0]+arm.q[1])]) #+ window.width/2

        y = np.array([
            0,
            arm.L[0]*np.sin(arm.q[0]),
            arm.L[0]*np.sin(arm.q[0]) + arm.L[1]*np.sin(arm.q[0]+arm.q[1])])

        return np.array([x, y]).astype('int')

    #window.jps = get_joint_positions()
    
    fig = plt.figure()
    #ax = Axes3D(fig, axisbg='w')
    ax = Axes3D(fig, facecolor='w')
    
       
    ax.plot(get_joint_positions()[0], get_joint_positions()[1], c='k', alpha=.5)
    #ax.scatter(x, y, z, s=50)
        
    #plt.legend(bbox_to_anchor=(0, 0))
    plt.xlabel('X');
    plt.ylabel('Y');
    plt.axis('equal')
    ax.view_init(0, -135)
    
#    def onclick(event):
#       print('%f %f' %(event.xdata, event.ydata))
        
    def callback(event):
        if event.button==3:
            print(ax.format_coord(event.xdata, event.ydata))
            strx, stry, strz =ax.format_coord(event.xdata, event.ydata).split(',')
            mx=float(strx.strip('x='))
            my=float(stry.strip().strip('y='))
            #mx, my, mz = map(float, ax.format_coord(event.xdata, event.ydata).strip().strip('x=').strip('y=').strip('z=').split(','))
            #print(mx, my, mz)
            arm.q = arm.inv_kin([mx, my])  # get new arm angles
            print(math.degrees(arm.q[0]), math.degrees(arm.q[1]))
            ax.plot(get_joint_positions()[0], get_joint_positions()[1], c='k', alpha=.5)
        
    

    #plt.connect('button_press_event', onclick)
    fig.canvas.callbacks.connect('button_press_event', callback)
    plt.show()

#     @window.event
#     def on_draw():
#         window.clear()
#         label.draw()
#         for i in range(3):
#             pyglet.graphics.draw(
#                 2,
#                 pyglet.gl.GL_LINES,
#                 ('v2i', (window.jps[0][i], window.jps[1][i],
#                          window.jps[0][i+1], window.jps[1][i+1])))
# 
#     @window.event
#     def on_mouse_motion(x, y, dx, dy):
#         # call the inverse kinematics function of the arm
#         # to find the joint angles optimal for pointing at
#         # this position of the mouse
#         label.text = '(x,y) = (%.3f, %.3f)' % (x, y)
#         arm.q = arm.inv_kin([x - window.width/2, y])  # get new arm angles
#         window.jps = get_joint_positions()  # get new joint (x,y) positions
# 
#     pyglet.app.run()

 

plot()
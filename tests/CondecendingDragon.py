# To change this template, choose Tools | Templates
# and open the template in the editor.

from Panda import *

grassScene()
boyBalloon(position = p3(0,0,sin(time)/3-1))
dragon(position = p3(-3,5,-2), hpr=hpr(-5,0,0), size=4)
bee(position = p3(1.1*sin(integral(time)-pi) , -1.1*cos(integral(time)-pi), -0.88), hpr = hpr(integral(time),0,0), color= cyan, size = .5)
panda(position = p3(0,0,-1), hpr = hpr(integral(time),10,0), color=pink)

start()
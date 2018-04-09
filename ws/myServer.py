#!/usr/bin/env python

import asyncio
import datetime
import random

import websockets
import json

import servo.servoblaster
#from servo import stepperMotor


servoChannel = 2

async def time(websocket, path):
    while True:
        val = await websocket.recv()
        print("Try to go {}".format(val))
        axis = json.loads(val)
        for axe in axis:        # Second Example
            print ('Current axe :', axe, ' ', axis[axe])
        
        if 'axe1' in axis.keys():
            print ('Axe 1 will be controled with value ', axis['axe1'])
            #stepperMotor.forward(0.1, axis['axe1'])
        if 'axe2' in axis.keys():
            print ('Axe 2 will be controled with value ', axis['axe2'])
            #servo.servoblaster.setServo(servoChannel, val)
        if 'axe3' in axis.keys():
            print ('Axe 3 will be controled with value ', axis['axe3'])
            #servo.servoblaster.setServo(servoChannel, val)
        
        greeting  = "Position {} is reached at ".format(val) + datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(greeting )

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

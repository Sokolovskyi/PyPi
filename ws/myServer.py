#!/usr/bin/env python

import asyncio
import datetime
import random

import websockets

import servo.servoblaster


servoChannel = 2

async def time(websocket, path):
    while True:
        val = await websocket.recv()
        print("Try to go {}".format(val))
        
        #servo.servoblaster.setServo(servoChannel, val)
        
        greeting  = "Position {} is reached at ".format(val) + datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(greeting )

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:39:22 2022

@author: ghosty
"""

# 訂閱者（subscriber）指令稿 subscriber1.py
import paho.mqtt.client as mqtt
import time
from mqtt_common import broker, topic

test_count=0
msg_count = 0
start_tick = 0
stop_tick = 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):    
    global start_tick, stop_tick, msg_count, test_count    
    payload= msg.payload.decode()
    print(payload)
    if payload=='start':
        test_count = test_count +1
        print('Start...',test_count)
        start_tick = time.perf_counter()        
        msg_count = 0
        return
    if payload=='stop':
        stop_tick = time.perf_counter()  
        #print('Stop...')
        elapsed = stop_tick - start_tick
        print('   elapsed ',elapsed,'s, msg_count=', msg_count,', performance=',msg_count/elapsed,' msg/s')
        return
    if payload=='end':
        print('End')
        client.disconnect() # disconnect gracefully
        client.loop_stop() # stops network loop        
        return
      
    print('Count',  msg_count)
    msg_count = msg_count + 1
    #print("[{}]: {}".format(msg.topic, payload))  

# main
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883)
client.loop_forever()
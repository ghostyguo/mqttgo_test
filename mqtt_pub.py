# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:39:52 2022

@author: ghosty
"""

# 發布者（publisher）指令稿 publisher1.py
import paho.mqtt.client as mqtt
import time
from mqtt_common import broker, topic
#
#broker = "localhost"
client = mqtt.Client()
client.connect(broker, 1883)

max_count=10000
#

def delay(count):
    for i in range(count):
        pass
    
def test():
    client.publish(topic, "start")
    start_tick = time.perf_counter()
    for i in range(max_count):
        client.publish(topic, "count", qos=1)
        delay(50000)
    client.publish(topic, "stop")
    stop_tick = time.perf_counter()
    elapsed = stop_tick - start_tick
    print('performance=',max_count/elapsed,'msg/s')
    
for i in range(100):
    test()    
client.publish(topic, "end")
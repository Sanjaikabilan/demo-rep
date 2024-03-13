import paho.mqtt.client as mqtt
from time import sleep
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    #parse json data
    data = json.loads(msg.payload.decode())
    print(data['acio'])
    print(data['gyrio'])


def float_to_string(o):
    if isinstance(o, float):
        return str(o)
    raise TypeError

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("xxjfwlqo:xxjfwlqo", "9agKXHW-5duIFt7ehaLp6JSM4-L-SMkc")
client.connect("fly.rmq.cloudamqp.com", 1883, 60)

client.loop_start()

while True:
    a = 65
    b = 65

    data = {
        "acio": a,
        "gyrio": b
    }

    client.publish("test", json.dumps(data))

    sleep(1)

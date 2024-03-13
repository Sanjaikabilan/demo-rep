import paho.mqtt.client as mqtt
from time import sleep

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    messa = msg.payload.decode()
    print(messa)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("vwjxbkan:vwjxbkan", "Uwu1CG2LOPdpWCJ6p7_GFDohPcSJNTBC")
client.connect("jackal.rmq.cloudamqp.com", 1883, 60)

client.loop_start()

while True:
    for x in range(1,15,1):
        client.publish("test", str(x))
        sleep(1)

    
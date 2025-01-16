#https://www.hivemq.com/public-mqtt-broker/

import paho.mqtt.client as mqtt
import time

client_id = "clientId-..."

port = 1883
broker_address = "broker.hivemq.com"

client = mqtt.Client(client_id)  # clientId- add 10 random characters
client.connect(broker_address, port)

# Receives data from any subscription on the server
def on_message(client, userdata, msg):
    print("TOPIC: '{}'   MSG:'{}'".format(msg.topic, msg.payload.decode()))

# Prepares to subscribe to a channel
client.on_message = on_message
client.loop_start()
client.subscribe("streaming/OMIoT/team/valores_medios")

# Performs 10 publish operations to the server's topic
for i in range(1, 100):
    # v1/username/things/clientID/data/channel
    client.publish("streaming/OMIoT/team/valores_instantaneos", str(i))
    print(i)
    time.sleep(1)

client.disconnect()

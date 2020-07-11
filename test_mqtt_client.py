import paho.mqtt.client as mqtt
import random

mqttc = mqtt.Client()
mqttc.connect("192.168.0.88", 1883, 60)


value = random.choice([10, 20, 30, 49,23, 34, 12, 5])
stype = random.choice(['h', 't', 'g'])

message = '{"v": ' +str( value) + ', "t": "' + stype + '",  "id": "sensor1", "ts": "04-03-12 12:00"}'


topic = "/esp32/dhtreadings"
mqttc.publish(topic, payload=message, qos=0, retain=False)


# import paho.mqtt.client as paho
# broker="192.168.1.184"
# port=1883

# def on_publish(client,userdata,result):             #create function for callback
#     print("data published \n")
#     pass
# client1= paho.Client("control1")                           #create client object
# client1.on_publish = on_publish                          #assign function to callback
# client1.connect(broker,port)                                 #establish connection

# ret= client1.publish("house/bulb1","on")   



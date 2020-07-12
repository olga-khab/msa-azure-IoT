import random
import time

# we will simulate a car

from azure.iot.device import IoTHubDeviceClient, Message
CONNECTION_STRING = "HostName=msa-iot-hub.azure-devices.net;DeviceId=iot-device;SharedAccessKey=4q8VLNeau4Xg+K9NHzVzf7bDHSwuugIVE+HTNmxkWIc="

# measurements transmitted by device - set default values
SPEED = 60 # km/h
#LATITUDE =
#LONGITUDE =
ENGINE_TEMP = 20
EMISSIONS = 20
MESSAGE = '{{"speed": {speed},"engine temperature": {engine_temperature}, "emissions": {emissions}}}'

# authenitication string to connect to the IoT Hub
def iothub_client_telemetry_sample_run():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        #print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # simulate telemetry values to be transmitted
            speed = SPEED + (random.random() * 10)
            engine_temperature = ENGINE_TEMP + (random.random() * 10)
            emissions = EMISSIONS + (random.random() * 10)
            # format the message
            message = Message(MESSAGE.format(speed = speed,
            engine_temperature=engine_temperature, emissions = emissions))

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            #if temperature > 30:
            #  message.custom_properties["temperatureAlert"] = "true"
            #else:
            #  message.custom_properties["temperatureAlert"] = "false"

            # send message every 5 seconds
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(5)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
#    print ( "IoT Hub Quickstart #1 - Simulated device" )
#    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()

'''
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyCOg0z_8A31ZZP6uE9JMk5iZsRRFyz3ilg')
start = 'Constitution Ave NW & 10th St NW, Washington, DC'
end   = 'Independence and 6th SW, Washington, DC 20024, USA'
dirs  = gmaps.directions(start, end)[0]['legs'][0]['steps']
print(dirs)

'''

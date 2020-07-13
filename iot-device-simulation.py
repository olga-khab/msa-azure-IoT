import random
import time
from math import cos, sin, asin, sqrt, pi

from azure.iot.device import IoTHubDeviceClient, Message
CONNECTION_STRING = "HostName=msa-iot-hub.azure-devices.net;DeviceId=iot-device;SharedAccessKey=4q8VLNeau4Xg+K9NHzVzf7bDHSwuugIVE+HTNmxkWIc="

# measurements transmitted by device - set default values
SPEED = 60 # km/h
# startung coordinates in Sydney
LATITUDE = -33.861262
LONGITUDE = 151.180457
# standard car engine temperature is between 90-105 degrees Celcius
ENGINE_TEMP = 95
DISTANCE = 0
MESSAGE = '{{"speed": {speed},"engine temperature": {engine_temperature}, "distance": {distance}, "latitude": {lat}, "longitude": {long}}}'

# calculate distance between two locations
def haversine_distance(lat1, long1, lat2, long2):
    a = 0.5 - cos((lat2-lat1)*pi/180)/2 + cos(lat1*pi/180) * cos(lat2*pi/180) * (1-cos((long2-long1)*pi/180))/2
    return 2*6371*asin(sqrt(a))

# authenitication string to connect to the IoT Hub
def iothub_client_telemetry_sample_run():
    lat = LATITUDE
    long = LONGITUDE
    distance = DISTANCE
    try:
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        while True:
            # simulate telemetry values to be transmitted
            speed = SPEED + random.random()*50
            # make engine tempertaure a function of speed
            engine_temperature = ENGINE_TEMP + random.random()*speed
            # simulate movement by changing location
            lat = lat + random.random()*0.00001
            long = long + random.random()*0.00001
            # calculate distance travelled
            distance = distance + haversine_distance(LATITUDE, LONGITUDE, lat, long)

            # format the message
            message = Message(MESSAGE.format(speed = speed,
            engine_temperature=engine_temperature, lat = lat,
            long = long, distance=distance))
            # send message every 5 seconds
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(5)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub - simulated car device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()

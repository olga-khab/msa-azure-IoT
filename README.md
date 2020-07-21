# msa-azure-IoT
This is a python script that simulates a simple IoT vehicle monitoring system generating values for speed, engine temperature, distance travelled and current location (latitude and longitude). The message is sent to the Azure IoT Hub where we use a Stream Analytics job to pass the data into a Power BI dataset for live processing.

## Installations

The Azure IoT Device SDK - provides functionality for communicating with the Azure IoT Hub:

`pip install azure-iot-device`

### Sample Power BI report

![Power BI report snapshot](./report_img.png)

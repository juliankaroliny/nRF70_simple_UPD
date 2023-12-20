# nRF70_simple_UPD

This is an example project to get a very simple UDP client communication running on the nRF70. It was tested with the nRF7002DK and the Nordic Connect SDK V2.4.1. The data communication is only one-way (station two access point) to simulate a typical IoT sensor scenario. 

## Structure
This example builds on top of the [Wi-Fi: Station](https://github.com/nrfconnect/sdk-nrf/tree/main/samples/wifi/sta) for the nRF7002DK in the Nordic Connect SDK samples which is executed in a separate thread. 

To connect to an access point you have to adapt the SSID and PWD in the [prj.conf](/prj.conf) file accordingly

```c
CONFIG_STA_SAMPLE_SSID="Myssid"
CONFIG_STA_SAMPLE_PASSWORD="Mypassword"
```

With this example, arbitrary data can be transmitted by simply adapting the transmit data struct:

```c
#define SENSOR_DATA_LENGTH 100
struct sensorData
{
    uint16_t frame_number;
    uint8_t data[SENSOR_DATA_LENGTH];
};
struct sensorData transmit_data;
```
For now, it just consists of a frame_number and data. The frame_number is increased for every transmission and the data is filled randomly.


## UDP Server
TODO: Describe Python example

## Power Consumption
TODO: add power consumption for sample configuration

### Additional Power Saving
TODO: add additional power-saving features
from operator import invert
from time import sleep
from data import *
from ha_mqtt_device import *
from inverter import update
import socket

MQTT_SERVER = "192.168.5.245"
MQTT_UPDATE_INTERVAL = 60


def on_connect(client, userdata, flags, rc):
    print("MQTT connected")


def on_disconnect(client, userdata, flags):
    print("MQTT disconnected")


def start_mqtt():
    # Start up the server to expose the metrics.
    mqtt_client = mqtt.Client(socket.gethostname())
    mqtt_client.on_connect = on_connect
    mqtt_client.on_disconnect = on_disconnect
    #mqtt_client.on_message = on_message
    #mqtt_client.username_pw_set("", "")
    mqtt_client.connect(MQTT_SERVER, 1883, 60)
    mqtt_client.loop_start()
    loop(mqtt_client)


def loop(mqtt_client):
    example_device = Device.from_config("example_device.yaml")
    input_ac_voltage = Sensor(
        mqtt_client,
        "Input AC Voltage",
        parent_device=example_device,
        unit_of_measurement="V",
        topic_parent_level="inside",
    )
    input_ac_frequency = Sensor(
        mqtt_client,
        "Input AC Frequency",
        parent_device=example_device,
        unit_of_measurement="Hz",
        topic_parent_level="inside",
    )

    output_ac_voltage = Sensor(
        mqtt_client,
        "Output AC Voltage",
        parent_device=example_device,
        unit_of_measurement="V",
        topic_parent_level="inside",
    )

    output_ac_frequency = Sensor(
        mqtt_client,
        "Output AC Frequency",
        parent_device=example_device,
        unit_of_measurement="Hz",
        topic_parent_level="inside",
    )

    load_in_watt = Sensor(
        mqtt_client,
        "Load in Watt",
        parent_device=example_device,
        unit_of_measurement="W",
        topic_parent_level="inside",
    )

    battery_voltage = Sensor(
        mqtt_client,
        "Battery Voltage",
        parent_device=example_device,
        unit_of_measurement="V",
        topic_parent_level="inside",
    )
    pv_input_voltage = Sensor(
        mqtt_client,
        "PV Input Voltage",
        parent_device=example_device,
        unit_of_measurement="V",
        topic_parent_level="inside",
    )

    pv_input_watt = Sensor(
        mqtt_client,
        "PV Input Watt",
        parent_device=example_device,
        unit_of_measurement="W",
        topic_parent_level="inside",
    )
    while True:
        if update():
            input_ac_voltage.send(LastData.Input_AC_Voltage)
            input_ac_frequency.send(LastData.Input_AC_Frequency)
            output_ac_voltage.send(LastData.Output_AC_Voltage)
            output_ac_frequency.send(LastData.Output_AC_Frequency)
            load_in_watt.send(LastData.Load_In_Watt)
            battery_voltage.send(LastData.Battery_Voltage)
            pv_input_voltage.send(LastData.PV_Input_Voltage)
            pv_input_watt.send(LastData.PV_Input_Watt)
            sleep(MQTT_UPDATE_INTERVAL)

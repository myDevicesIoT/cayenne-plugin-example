# Cayenne Example Plugin
A plugin for the [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent) that sends example data to the [Cayenne Dashboard](https://cayenne.mydevices.com).

## Requirements
### Hardware
* [Rasberry Pi](https://www.raspberrypi.org).

### Software
* [Cayenne Pi Agent](https://github.com/myDevicesIoT/Cayenne-Agent). This can be installed from the [Cayenne Dashboard](https://cayenne.mydevices.com).
* [Git](https://git-scm.com/).

## Getting Started
### Installation
From the command line run the following commands to install this plugin.
```
cd /etc/myDevices/plugins
sudo git clone https://github.com/myDevicesIoT/cayenne-plugin-example.git
sudo service myDevices restart
```
This will causes temporary widgets for the plugin to show up in the [Cayenne Dashboard](https://cayenne.mydevices.com). You can make them permanent by clicking the plus sign.

## Modifying the Plugin
To modify the plugin you can add, update or remove sections and attributes in the `example-device.plugin` file. Each section corresponds to a sensor/actuator device widget that will be displayed in the [Cayenne Dashboard](https://cayenne.mydevices.com). The attributes determine which Python module, class and function is used to read and write data for that widget.

Each section can have the following attributes.

| Attribute     | Required      | Description  |
| ------------- |:-------------:| ------------ |
| enabled   | yes | If `true` this will send data to Cayenne, otherwise it will not |
| channel   | yes | The channel to use for this sensor/actuator device, e.g. 0 |
| module    | yes | The python module to use for the sensor/actuator device. It can be installed anywhere in the `PYTHONPATH` or just be in the plugin folder as the `.plugin` file, as it is for this example. |
| class     | yes | The class within the specified module to use for the sensor/actuator device. |
| init_args | no  | A JSON value for the arguments to use when creating an instance of the class, e.g. `{"max":40, "min": 20}`. |
| read      | yes | The function to use to read values for the sensor/actuator device. This function should return a tuple of the form `(value, type, unit)` if this device widget requires type and unit to be specified. |
| write     | no  | The function to use to write values to an actuator device. The value is passed in as a float. |
| name      | no  | The initial display name used for the widget. If this is not specified the section name will be used. |

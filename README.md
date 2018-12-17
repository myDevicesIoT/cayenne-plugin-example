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
Temporary widgets for the plugin should now show up in the [Cayenne Dashboard](https://cayenne.mydevices.com). You can make them permanent by clicking the plus sign.

NOTE: If the temporary widgets do not show up try refreshing the [Cayenne Dashboard](https://cayenne.mydevices.com) or restarting the agent again using `sudo service myDevices restart`.

## Modifying the Plugin
To modify the plugin you can add, update or remove sections and attributes in the `example-device.plugin` file. Each section corresponds to a sensor/actuator device widget that will be displayed in the [Cayenne Dashboard](https://cayenne.mydevices.com). The attributes determine which Python module, class and function is used to read and write data for that widget.

Each section can have the following attributes.

| Attribute     | Required      | Description  |
| ------------- |:-------------:| ------------ |
| enabled   | yes | If `true` this will send data to Cayenne, otherwise it will not. |
| channel   | no | The channel to use for this sensor/actuator device, e.g. 0. This should be a unique value for each section within the plugin file. Any devices that send data to Cayenne need to set the channel attribute. If the device does not send data directly to Cayenne, e.g. an extension, it does not need to set the channel. |
| module    | yes | The python module to use for the sensor/actuator device. It can be installed anywhere in the `PYTHONPATH` or just be in the same plugin folder as the `.plugin` file, as it is for this example. |
| class     | yes | The class within the specified module to use for the sensor/actuator device. |
| init_args | no  | A JSON value for the arguments to use when creating an instance of the class, e.g. `{"max":40, "min": 20}`. If `$channel` is used as a value it will be replaced by the channel attribute for the section.|
| read      | yes | The function to use to read values for the sensor/actuator device. This function should return a tuple of the form `(value, type, unit)` if this device widget requires type and unit to be specified. For example, `(25.0, 'temp', 'c')` would specify a temperature of 25.0 degrees Celsius. To see the types and units available run `python3 -m myDevices.datatypes` from a command line. For more information run `python3 -m myDevices.datatypes -h`. |
| read_args | no  | A JSON value for the arguments to use when calling the `read` function, e.g. `{"channel":$channel}`. If `$channel` is used as a value it will be replaced by the channel attribute for the section. |
| write     | no  | The function to use to write values to an actuator device. The value is passed in as a float. |
| write_args | no  | A JSON value for the arguments to use when calling the `write` function, e.g. `{"channel":$channel}`. If `$channel` is used as a value it will be replaced by the channel attribute for the section. |
| name      | no  | The initial display name to use for the widget. If this is not specified the section name will be used. |
| inherit   | no  | The name of a section to inherit attributes from. The section to inherit from must precede the inheriting section in the plugin file. The *enabled*, *channel* and *name* attributes are not inherited. Attributes can be overridden by specifying new values in the inheriting section. If the *module*, *class* and *init_args* attributes are not overridden the inheriting section will use the same class instance as the section it inherits from. |
| register_callback   | no  | The function to use to register a callback that can be called in real-time when data changes. The callback parameter should be the same as the value returned from the `read` function. Data sent to the callback may be dropped if the number of calls exceed the rate limit for the Pi agent. |
| unregister_callback | no  | The function to use to unregister the callback that was registered via `register_callback`. |

## Adding a Plugin
To add a new plugin you can create a new `.plugin` file and define sections as described above. The `.plugin` file can be in its own directory under `/etc/myDevices/plugins`, with its Python code if needed, or in an existing one. Restart the Cayenne Agent (`sudo service myDevices restart`) to load the plugin.

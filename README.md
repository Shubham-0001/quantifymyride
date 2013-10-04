# Quantify My Ride

Gather some data about your car. Uses a OBD-2 adapter to gather data from your onboard computer.
More details: http://hackingroom.de/wiki/Quantified_Car

Uses pyobdlib via a submodule.

## Setup
* Get submodules: `git submodule update --init`
* Connect your ELM 327 device
* Adjust path to your ELM327 device, and the sensors to be logged, in `obd_logger.py`

	PORTNAME = "/dev/ttyUSB0"
	LOG_SENSORS = ["rpm", "speed", "load", "temp", "intake_air_temp", "engine_time", "fuel_rail_pressure", "bar_pressure", "control_module_voltage", "accelerator_pos_D" ]

* Start the loger: `./obd_logger.py`


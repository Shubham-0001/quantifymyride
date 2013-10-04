# Quantify My Ride

Gather some data about your car. Uses a OBD-2 adapter to gather data from your onboard computer.
More details: http://hackingroom.de/wiki/Quantified_Car

Uses pyobdlib via a submodule.

## Get started
* Get submodules: `git submodule update --init`
* Connect your ELM 327 device
* Adjust path to your ELM327 device, and the sensors to be logged, in `obd_logger.py`, using the variables `PORTNAME` and `LOG_SENSORS`
* Start the loger: `./obd_logger.py`


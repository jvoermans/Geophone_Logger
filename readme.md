# Geophone logger

**Introduction:** the geophone logger was designed with the aim to measure sea ice vibrations at high sampling rates (1000Hz) and accurate time synchronization using GPS (accuracy <<1ms). The logger records 5-ADC channels simultaneously at 12-bit and uses an Arduino Due as microcontroller. Files are written on SD-card.

**Hardware:** the logger consists of an Arduino Due, GPS Ultimate breakout module, SD-card breakout module, voltage-regulator and 5x INA122 amplifiers. The gain of the amplifiers is set by resistors (connecting pins 1 and 8), we refer to the INA122 datasheet on gain-values. For the voltage dividers we use 100 Ohm resistors. Geophones are connected to the amplifiers, noting that the signal of one geophone is split to three amplifiers, allowing for higher sensitivity by chosing different gains. We refer to the Fritzing-diagram for further details on the hardware.

**Data**: timeseries of the analog signals are stored as binary files on the SD-card and can be parsed usng the parsing files.

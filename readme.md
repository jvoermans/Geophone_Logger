**About**: This logger was designed as part of project "A method to identify sea-ice breakup: a pilot study (MISIB)", part of the Svalbard Science Forum program. Work and results are published in (see preprint at https://arxiv.org/pdf/2305.06490.pdf ). Data obtained during this project can be accessed at https://adc.met.no/datasets/10.21343/5vhg-a209 .

# Geophone logger

**Introduction:** the geophone logger was designed with the aim to measure sea ice vibrations at high sampling rates (1000Hz) and accurate time synchronization using GPS (accuracy <<1ms). The logger records 5-ADC channels simultaneously at 12-bit and uses an Arduino Due as microcontroller. All ADC acquisition is performed using interrupt driven functions and a system of "double buffers". Dumping to the SD card is performed from the main thread of the program as soon as one of the "double buffers" is filled with data. This allows to log the ADC output without interruption while data are being periodically dumped to the SD card. In addition, a GPS PPS input is used to provide microsecond accuracy of all signal timings.

<img src="https://github.com/jvoermans/Geophone_Logger/blob/main/Hardware/Photos/Picture3.jpg" width="400" />

**Hardware:** the logger consists of an Arduino Due, GPS Ultimate breakout module, SD-card breakout module, voltage-regulator and 5x INA122 amplifiers. The gain of the amplifiers is set by resistors (connecting pins 1 and 8), we refer to the INA122 datasheet on gain-values. For the voltage dividers we use 100 Ohm resistors. Geophones are connected to the amplifiers, noting that the signal of one geophone is split to three amplifiers, allowing for higher sensitivity by chosing different gains. We refer to the Fritzing-diagram for further details on the hardware.

**Firmware:** code is provided in firmware folder. We use Visual Studio Code (VSCode) with PlatformIO (PIO).

**Data Analysis**: timeseries of the analog signals are stored as binary files on the SD-card and can be parsed usng the parsing files.

# Previous resources / possible extended materials

The content on the present repository is obtained from curating our "development" repository, available at: https://github.com/jvoermans/Vibration_Logger . There may be some additional (outdated, and / or not used in the end) information and code at the corresponding location, that may be useful to developers looking for more details and discussions (see the issues there for the discussions during development of the instruments, firmware, and decoder).

# How to cite

If using the materials here, please cite our paper:

```
Voermans, J. J., Rabault, J., Marchenko, A., Nose, T., Waseda, T., & Babanin, A. V. (2023).
Estimating sea ice properties from wave observations in sea ice.
arXiv preprint, arXiv:2305.06490.
```

And, if relevant, the data:

```
Voermans, J., Rabault, J., Marchenko, A., Nose, T., Waseda, T., & Babanin, A. (2023).
Geophone and Hydrophone deployments is Svalbard for 2022 [Data set].
Norwegian Meteorological Institute.
https://doi.org/10.21343/5VHG-A209
```

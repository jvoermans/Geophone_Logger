## Hardware
The following wiring diagram can be followed when building a geophone logger:
<img src="https://github.com/jvoermans/Geophone_Logger/blob/main/Hardware/Fritzing_diagram.png" width="700" />

### Component List
The basics consist of the following components:
- 1x Arduino Due (e.g., Mouser No: 782-A000062);
- 1x GPS Ultimate Breakout (Adafruit ID:746);
- 1x MicroSD card Breakout (Adafruit ID:254);
- 5x INA122 gain amplifiers (e.g., Mouser No: 595-INA122P);
- 1x 3.3V step-up/down voltage converter (Pololu S7V8F3);
- 1x GPS Antenna (Adafruit ID:960);
- 1x SMA to uFL adapter cable (Adafruit ID:851);
- 1x cable gland (geophone cable into casing)
- 1x triaxys geophone;
- 1x Pelican Case (we used the 1400 cause of the large size of the battery we used);
- 1x battery (most batteries can be used, but double check the step-up/down converter datasheet for stuiability, https://www.pololu.com/product/2122).
- Wire and resistors.

The above totals about 175 USD, excluding the geophone, battery, and Pelican case. We used a GS-One geophone in a weather proof casing, roughly 300 USD.

_Optional_:
- LiFePO4 solar charger, only for LiFePO4 batteries! (www.tindie.com/products/silicognition/lifepo4weredsolar1/);
- if a solar charger included, then a solar panel as well (Adafruit ID:200)
- Micro SD Card extender (Adafruit ID:3688).
- We housed the main electronics in a separate weather tight enclosure so that the SD-card and battery could be swapped in the field.

We further put a switch between the battery and the logger and some foam to keep all components from moving inside the case. In the end, the electronics looked like this:

<img src="https://github.com/jvoermans/Geophone_Logger/blob/main/Hardware/Photos/Picture2.jpg" width="700" />


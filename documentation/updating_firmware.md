# Updating Firmware of Motorcontroller

The project is using smoothieboards to execute implemented functions. The configuration of the connected peripherals (e.g. stepper motor) is stored on the smoothieboard's SD card and has to be updated initially. When parts with a different specification (e.g. step size of a stepper motor) are used, the configuration files have to be modified to accommodate the physical changes. A list of most configuration options is provided by the Smoothie Project (http://smoothieware.org/configuration-options).

The configuration for the developed modules with the implemented parts can be found in the design files section.

Building upon the Opentrons open source products (https://opentrons.com), this project is using Opentrons' firmware for the smoothieboard.

### Download Files

[Download the zipped files from here](https://github.com/opentrons/smoothie-config/archive/1.2.0.zip) and unpack them.

### Update config file
Open `config` file, update specifications for your developed module, such as step size for stepper motor), and save file.

### Update files on the smoothieboard's SD card

Open the SD card of your smoothieboard and copy the `FIRMWARE.CUR` (downloaded from Github) and `config` (updated in the previous step) files onto the SD card.

### Restart

Insert the SD card into the smoothieboard and restart the smoothieboard by connecting the USB or power supply. The board will read the `firmware.bin` file, then save it as `FIRMWARE.CUR`. Functionalities are executed based on the updated `config` file.

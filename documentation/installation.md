# Pre-requisites and installation

The following instructions are written for a Raspberry Pi (RPi) single-board computer; however also Windows 8, 10 and macOS 10.12+ have been successfully used with the presented workstation:

#### Python version

Make sure that you have at least Python 3.5 on your system.

#### Update the system's package list

```
sudo apt-get update
```

#### Upgrade all the installed packages

```
sudo apt-get dist-upgrade
```

#### Restart the Raspberry Pi

```
sudo reboot
```

#### Install Python pip

```
sudo apt-get install python3-pip
```

#### Create a Python virtual environment

It is recommended to setup an [Python Virtual Environment](https://realpython.com/python-virtual-environments-a-primer/) to store all packages and dependencies in one place. By doing this, your current Opentrons API is not impacted by any changes.

Install the virtualenv tool
```
pip3 install virtualenv
```

Create a new virtual environment
```
python3 -m venv OpenWorkstation
```

Activate the Python virtual environment
```
source OpenWorkstation/bin/activate
```


#### Install OpenWorkstation API
```
pip3 install openworkstation
```

#### Install opentrons API

The opentrons API is only required, if the OT-1 or the OT-2 is used as the pipetting module.

For OT-1 API
```
pip3 install opentrons==2.5.2
```

For OT-2 API
```
pip3 install opentrons
```

The current version has been tested successfully with the OT-1 API and should be compatible with the OT-2 API.

#### Test successful API installation

```
python3
>>> import openworkstation
>>> import opentrons
```

The programming section will be updated within the next weeks to include more details about the code and general organization. If you have any questions, please do no hesitate to [get in touch](mailto:s.eggert@qut.edu.au) to discuss potential applications.

# Programming

The OpenWorkstation API is a simple Python framework designed to allow the operation of hardware modules.

## How it’s Organized
Protocol scripts generally contain the following sections:

Imports
Commands
Module-specific Commands
Protocol script

#### Import

Always include the OpenWorkstation API within your file.
```
pip3 install openworkstation
```

Currently, specific commands for a single module are saved in a separate module file. For example, the positions for the transport module are saved in the `moduleTransport.py` file. These module-specific have to be imported into the main `protocol.py` file. General commands, such as connect to USB port and homing, are defined in a separate `commands.py` file.

```
from commands import *
from modulePipetting import *
from moduleCrosslinker import *
from moduleStorage import *
from moduleTransportation import *
```

#### Connect to USB port(s)

The command `connect()` will connect to board to the USB port(s) which are defined in the `commands.py` file.


```
robot2USB  = '/dev/ttyACM1'
```

#### Homing
The command `home()` will start with the homing process for the defined axis.

```
def home_all():
    robot2._driver.send_command('G28.2 Y Z')
    robot2._driver.send_command('G28.2 A')
    robot2._driver.send_command('G28.2 B')
    robot2._driver.send_command('G28.2 X')
    robot2._driver.send_command('G90')
```

#### Move to defined positions
Basic commands are written in the [Gcode language](https://en.wikipedia.org/wiki/G-code) to enable customization of movements and make it accessible to anyone with basic programming skills.

##### Switching between relative and absolute coordinates

Switch to absolute coordinates
```
robot2._driver.send_command(G90)
```
Switch to relative coordinates
```
robot2._driver.send_command(G91)
```

##### Define movement speed

Define speed in mm/min
```
robot2._driver.send_command(G0 F1000)
```

##### Define movement steps


```
robot2._driver.send_command(G0 X5 Y100 A88)
robot2._driver.send_command(G0 X0 Y150 A33)
```


#### Advanced control

If specific protocol blocks or general functionalities are repeated from time to time, parameters can be defined at the beginning and called in a function.

```
# definitions of module positions for the moduleTransport
transportposition['modulePipetting']  = 'G0 X481 Y5 Z5 A4 B5 F2000'
transportposition['moduleCrosslinker']  = 'G0 X170 Y5 Z5 A4 B5 F2000'
transportposition['moduleStorage']  = 'G0 X21.3 Y5 Z5 A4 B5 F2000'
# definition of crosslinker parameters for the moduleCrosslinker
# used to initiate photo-induced polymerization of hydrogels
lightON  = 'M106'
lightOFF  = 'M107'

# define function
def crosslinking1min():
    #absolute positioning
    robot2._driver.send_command('G90')
    # move plate to crosslinker module
    robot2._driver.send_command(transportposition['moduleCrosslinker'])
    # specifiy intensity
    robot2._driver.send_command(intensity_P1)
    # LEDs on
    robot2._driver.send_command(lightON)
    # duration
    sleep(60)
    # LEDs off
    robot2._driver.send_command(lightOFF)
    # move plate to pipetting module
    robot2._driver.send_command(transportposition['modulePipetting'])

# call function in protocol
crosslinking1min()

```

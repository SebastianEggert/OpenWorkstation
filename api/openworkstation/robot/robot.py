import copy
import os
from threading import Event

from openworkstation import drivers



class Robot(object):
    """
    This class is the main interface to the robot.

    """

    def __init__(self):
        """
        Initializes a robot instance.

        Notes
        -----
        This class is a singleton. That means every time you call
        :func:`__init__` the same instance will be returned. There's
        only once instance of a robot.
        """

        self._commands = None  # []
        self.INSTRUMENT_DRIVERS_CACHE = {}

        self.can_pop_command = Event()
        self.can_pop_command.set()

        self.mode = None
        self.smoothie_drivers = {
            'live': None,
            'simulate': drivers.get_virtual_driver(
                options={'limit_switches': False}
            ),
            'simulate_switches': drivers.get_virtual_driver(
                options={'limit_switches': True}
            )
        }

        null_driver = drivers.get_virtual_driver()

        def _null(*args, **kwargs):
            return

        null_driver.move = _null
        null_driver.home = _null
        self.smoothie_drivers['null'] = null_driver

        self._driver = drivers.get_virtual_driver()
        self.disconnect()
        self.arc_height = 5
        self.cmds_total = None
        self.set_connection('simulate')
        self.reset()


    def reset(self):
        """
        Resets the state of the robot and clears:
            * Command queue
            * Runtime warnings

        """
        self._commands = []
        self._runtime_warnings = []


        self.axis_homed = {
            'x': False, 'y': False, 'z': False, 'a': False, 'b': False}

        return self


    def add_warning(self, warning_msg):
        """
        Internal. Add a runtime warning to the queue.
        """
        self._runtime_warnings.append(warning_msg)

    def get_warnings(self):
        """
        Get current runtime warnings.

        Returns
        -------

        Runtime warnings accumulated since the last :func:`run`
        or :func:`simulate`.
        """
        return list(self._runtime_warnings)

    """def get_motor(self, axis):
        
        Get robot's head motor.

        Parameters
        ----------
        axis : {'a', 'b'}
            Axis name. Please check stickers on robot's gantry for the name.
        
        instr_type = 'instrument'
        key = (instr_type, axis)

        motor_obj = self.INSTRUMENT_DRIVERS_CACHE.get(key)
        if not motor_obj:
            motor_obj = InstrumentMotor(self, axis)
            self.INSTRUMENT_DRIVERS_CACHE[key] = motor_obj
        return motor_obj"""


    def connect(self, port=None, options=None):
        """
        Connects the robot to a serial port.

        Parameters
        ----------
        port : str
            OS-specific port name or ``'Virtual Smoothie'``
        options : dict
            if :attr:`port` is set to ``'Virtual Smoothie'``, provide
            the list of options to be passed to :func:`get_virtual_device`

        Returns
        -------
        ``True`` for success, ``False`` for failure.
        """
        device = None

        # Maintain backwards compatibility
        if port == 'Virtual Smoothie':
            port = 'edge-1c222d9NOMSD'

        # Default port virtual smoothie 2.0.0 port
        port = port or 'edge-1c222d9NOMSD'

        if port in drivers.VIRTUAL_SMOOTHIE_PORTS:
            device = drivers.get_virtual_driver(options=options, port=port)
        else:
            device = drivers.get_serial_driver(port)

        self._driver = device
        self.smoothie_drivers['live'] = device

        # set virtual smoothie do have same dimensions as real smoothie
        ot_v = device.ot_version
        self.smoothie_drivers['simulate'].ot_version = ot_v
        self.smoothie_drivers['simulate_switches'].ot_version = ot_v
        self.smoothie_drivers['null'].ot_version = ot_v

    """def add_command(self, command):
        if self.mode == 'live':
            cmd_run_event = {'caller': 'ui'}
            cmd_run_event['mode'] = 'live'
            cmd_run_event['name'] = 'command-run'
            cmd_run_event.update({
                'command_description': command,
                'command_index': len(self._commands),
                'commands_total': self.cmds_total
            })
            trace.EventBroker.get_instance().notify(cmd_run_event)
        self._commands.append(command)"""

    def set_connection(self, mode):
        self.mode = mode
        if mode not in self.smoothie_drivers:
            raise ValueError(
                'mode expected to be "live", "simulate_switches", '
                '"null" or "simulate", {} provided'.format(mode)
            )

        d = self.smoothie_drivers[mode]

        # set VirtualSmoothie's coordinates to be the same as physical robot
        if d and d.is_simulating():
            if self._driver and self._driver.is_connected():
                d.connection.serial_port.set_position_from_arguments({
                    ax.upper(): val
                    for ax, val in self._driver.get_current_position().items()
                })

        self._driver = d
        if self._driver and not self._driver.is_connected():
            self._driver.toggle_port()

    def disconnect(self):
        """
        Disconnects from the robot.
        """
        if self._driver:
            self._driver.disconnect()

        self.axis_homed = {
            'x': False, 'y': False, 'z': False, 'a': False, 'b': False}

    def get_serial_ports_list(self):
        ports = []
        # TODO: Store these settings in config
        if os.environ.get('ENABLE_VIRTUAL_SMOOTHIE', '').lower() == 'true':
            ports.extend(drivers.VIRTUAL_SMOOTHIE_PORTS)
        ports.extend(drivers.get_serial_ports_list())
        return ports

    def is_connected(self):
        if not self._driver:
            return False
        return self._driver.is_connected()

    def is_simulating(self):
        if not self._driver:
            return False
        return self._driver.is_simulating()

    def get_connected_port(self):
        return self._driver.get_connected_port()


    """def diagnostics(self):
       
        Access diagnostics information for the robot.

        Returns
        -------
        Dictionary with the following keys:
            * ``axis_homed`` — axis that are currently in home position.
            * ``switches`` — end stop switches currently hit.
            * ``steps_per_mm`` — steps per millimeter calibration
            values for ``x`` and ``y`` axis.
        
        # TODO: Store these versions in config
        return {
            'axis_homed': self.axis_homed,
            'switches': self._driver.get_endstop_switches(),
            'steps_per_mm': {
                'x': self._driver.get_steps_per_mm('x'),
                'y': self._driver.get_steps_per_mm('y')
            }
        }"""

    """def commands(self):
        
        Access the human-readable list of commands in the robot's queue.

        Returns
        -------
        A list of string values for each command in the queue, for example:

        ``'Aspirating 200uL at <Deck>/<Slot A1>/<Container plate>/<Well A1>'``
        
        return self._commands"""

    """def comment(self, msg):
        self.add_command(msg)"""

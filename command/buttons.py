#!/usr/bin/env python


# -----------------------------
# Receivers
# -----------------------------


class Device(object):

    """ Device interface """

    def on(self):
        raise NotImplementedError()

    def off(self):
        raise NotImplementedError()

    def volume_up(self):
        raise NotImplementedError()

    def volume_down(self):
        raise NotImplementedError()



class Television(Device):

    def __init__(self):
        self._volume = 0

    def on(self):
        print "TV is ON"

    def off(self):
        print "TV is OFF"

    def volume_up(self):
        if self._volume < 10:
            self._volume += 1
        print "TV volume is", self._volume

    def volume_down(self):
        if self._volume > 0:
            self._volume -= 1
        print "TV volume is", self._volume



class Radio(Device):

    def __init__(self):
        self._volume = 0

    def on(self):
        print "Radio is ON"

    def off(self):
        print "Radio is OFF"

    def volume_up(self):
        if self._volume < 10:
            self._volume += 1
        print "Radio volume is", self._volume

    def volume_down(self):
        if self._volume > 0:
            self._volume -= 1
        print "Radio volume is", self._volume



# ----------------------------------
# Commands
# ----------------------------------


class Command(object):

    """ command interface """

    def execute(self):
        raise NotImplementedError()



class DoNothing(Command):

    def execute(self):
        pass



class TurnOn(Command):

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.on()



class TurnOff(Command):

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.off()



class TurnUp(Command):

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.volume_up()



class TurnDown(Command):

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.volume_down()



class TurnThemOff(Command):

    def __init__(self, devices):
        self._devices = devices

    def execute(self):
        for device in self._devices:
            device.off()



# --------------------------------
# Invokers
# --------------------------------


class Button(object):

    """ Button interface """

    def press(self):
        raise NotImplementedError()



class PushButton(Button):

    def __init__(self, command):
        self._command = command

    def press(self):
        self._command.execute()



class ToggleButton(Button):

    def __init__(self, on_command, off_command):
        self._on_command = on_command
        self._off_command = off_command
        self._state = 'off'

    def press(self):
        if self._state == 'off':
            self._state = 'on'
            self._on_command.execute()
        else:
            self._state = 'off'
            self._off_command.execute()



# --------------------------------
# Application code
# --------------------------------

# create devices

tv = Television()
radio = Radio()

# create various commands

turn_tv_on = TurnOn(device=tv)
turn_radio_on = TurnOn(device=radio)
turn_tv_off = TurnOff(device=tv)
turn_radio_off = TurnOff(device=radio)
turn_tv_up = TurnUp(device=tv)
turn_radio_up = TurnUp(device=radio)
turn_tv_down = TurnDown(device=tv)
turn_radio_down = TurnDown(device=radio)
turn_them_off = TurnThemOff(devices=[tv, radio])
do_nothing = DoNothing()

# create 10-button remote control

buttons = [PushButton(command=do_nothing)] * 10
buttons[0] = ToggleButton(
    on_command=turn_tv_on, off_command=turn_tv_off)
buttons[1]=ToggleButton(
    on_command=turn_radio_on, off_command=turn_radio_off)
buttons[2] = PushButton(command=turn_tv_up)
buttons[3] = PushButton(command=turn_tv_down)
buttons[4] = PushButton(command=turn_radio_up)
buttons[5] = PushButton(command=turn_radio_down)
buttons[6] = PushButton(command=turn_them_off)

# playing with the buttons

buttons[0].press()
buttons[1].press()
buttons[0].press()
buttons[0].press()
buttons[2].press()
buttons[2].press()
buttons[2].press()
buttons[4].press()
buttons[5].press()
buttons[6].press()
buttons[8].press()

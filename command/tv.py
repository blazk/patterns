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
# Application
# --------------------------------


tv = Television()
radio = Radio()

# create various commands
turn_tv_on = TurnOn(device = tv)
turn_radio_on = TurnOn(device = radio)
turn_tv_off = TurnOff(device = tv)
turn_radio_off = TurnOff(device = radio)
turn_tv_up = TurnUp(device = tv)
turn_radio_up = TurnUp(device = radio)
turn_tv_down = TurnDown(device = tv)
turn_radio_down = TurnDown(device = radio)
turn_them_off = TurnThemOff(devices = [tv, radio])

# create remote control buttons

button1 = ToggleButton(
    on_command = turn_tv_on,
    off_command = turn_tv_off)

button2 = ToggleButton(
    on_command = turn_radio_on,
    off_command = turn_radio_off)

button3 = PushButton(command = turn_tv_up)
button4 = PushButton(command = turn_tv_down)

button5 = PushButton(command = turn_radio_up)
button6 = PushButton(command = turn_radio_down)

button7 = PushButton(command = turn_them_off)

# playing with the buttons

button1.press()
button2.press()
button1.press()
button1.press()
button3.press()
button3.press()
button4.press()
button5.press()
button6.press()
button7.press()

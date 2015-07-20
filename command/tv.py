#!/usr/bin/env python


# -----------------------------
# Receivers
# -----------------------------


class Television(object):

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


class Radio(object):

    def __init__(self):
        self._volume = 0

    def on(self):
        print "Radio is ON"

    def off(self):
        print "Radio is OFF"

    def volume_up(self):
        if self._volume < 10:
            self._volume += 1
        print "TV volume is", self._volume

    def volume_down(self):
        if self._volume > 0:
            self._volume -= 1
        print "TV volume is", self._volume



# ----------------------------------
# Commands
# ----------------------------------

class TurnOn(object):

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.on()


class TurnOff(object):

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.off()


class TurnUp(object):

    def __init__(self, device):
        self._device = device

    def execute(self):
        self._device.volume_up()


class TurnThemOff(object):

    def __init__(self, devices):
        self._devices = devices

    def execute(self):
        for device in self._devices:
            device.off()


# --------------------------------
# Invoker
# --------------------------------


class Button(object):

    def __init__(self, command):
        self._command = command

    def press(self):
        self._command.execute()


# --------------------------------
# Application
# --------------------------------

if __name__ == "__main__":

    tv = Television()
    radio = Radio()

    # create various commands
    turn_tv_on = TurnOn(device = tv)
    turn_tv_off = TurnOff(device = tv)
    turn_tv_up = TurnUp(device = tv)
    turn_radio_on = TurnOn(device = radio)
    turn_them_off = TurnThemOff(devices = [tv, radio])

    # create remote control buttons
    button1 = Button(command = turn_tv_on)
    button2 = Button(command = turn_tv_off)
    button3 = Button(command = turn_tv_up)
    button4 = Button(command = turn_radio_on)
    button5 = Button(command = turn_them_off)

    # playing with the buttons
    button1.press()
    button2.press()
    button1.press()
    button3.press()
    button3.press()
    button3.press()
    button4.press()
    button5.press()

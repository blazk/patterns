#!/usr/bin/env python

# ---------------------------------------
# Strategy class
# * Behavior is factored out of the
#   context class into strategy class.
# * Strategy instance has a reference to the
#   context. The context should have an interface
#   through which the strategy class accesses it.
# ---------------------------------------


class MoveStrategy(object):

    def move(self, new_location):
        raise NotImplementedError


class Walking(MoveStrategy):

    def __init__(self):
        pass

    def move(self, player, new_location):
        print '{} is walking from {} to {}'.format(
                player.name, player.location, new_location)
        player.location = new_location


class Flying(MoveStrategy):

    def __init__(self, height):
        self.height = height

    def move(self, player, new_location):
        print '{} is flying at {} from {} to {}'.format(
                player.name, self.height, player.location, new_location)
        player.location  = new_location


# ---------------------------------------
# Player
# ---------------------------------------


class Player(object):

    # Clients call player.move(). Player
    # in turn delegates the move() to
    # the strategy. A reference to the player
    # is passed as an argument to the
    # strategy operation.

    def move(self, new_location):
        self.move_strategy.move(self, new_location)

    # Strategy can use the player's interface
    # below to access player's data.

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def move_strategy(self):
        return self._move_strategy

    @move_strategy.setter
    def move_strategy(self, strategy):
        self._move_strategy = strategy

    @property
    def name(self):
        return self._name



class Robot(Player):

    def __init__(self, name, initial_location):
        self._name = name
        self._location = initial_location
        self._move_strategy = None



# ----------------------------------------
# Action!
# ----------------------------------------

# player
robot = Robot('R2D2', 'start')

# move strategies
walking = Walking()
flying_low = Flying('10 meters')
flying_high = Flying('50 meters')

# action
robot.move_strategy = walking
robot.move('garage')
robot.move('backyard')
robot.move_strategy = flying_low
robot.move('beach')
robot.move('forest')
robot.move_strategy = flying_high
robot.move('mountain')

#!/usr/bin/python3

import random


class Location(object):
    """
    Location class
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def dist_from(self, other):
        other_x = other.x
        other_y = other.y
        x_dist = self.x - other_x
        y_dist = self.y - other_y
        return (x_dist ** 2 + y_dist ** 2) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):

    def __init__(self):
        self.drunks = {}

    def add_drunk(self, name, location):
        if name in self.drunks:
            raise ValueError("Drunk already exists.")
        else:
            self.drunks[name] = location

    def move_drunk(self, name):
        if name not in self.drunks:
            raise ValueError("Drunk does not exists.")
        x_dist, y_dist = name.take_step()
        current_location = self.drunks[name]
        self.drunks[name] = current_location.move(x_dist, y_dist)

    def get_loc(self, name):
        if name not in self.drunks:
            raise ValueError("Drunk does not exists.")
        return self.drunks[name]


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'


class UsualDrunk(Drunk):

    def take_step(self):
        step_choices = [(0.0, 1.0), (1.0, 0.0), (0.0, -1.0), (-1.0, 0.0)]
        return random.choice(step_choices)


class WinterDrunk(Drunk):

    def take_step(self):
        step_choices = [(0.0, 0.9), (1.0, 0.0), (0.0, -1.1), (-1.0, 0.0)]
        return random.choice(step_choices)


def walk(field, name, num_steps):
    """
    One walk of num_steps of drunk - name.
    """
    start = field.get_loc(name)
    for s in range(num_steps):
        field.move_drunk(name)

    return start.dist_from(field.get_loc(name))


def sim_walk(num_steps, num_trials, drunk_class):
    """
    for number_trials, runs the num_steps and returns the distance conversed
    each time.
    """
    prasham = drunk_class('prasham')
    origin = Location(0.0, 0.0)
    distances = []
    for trial in range(num_trials):
        f = Field()
        f.add_drunk(prasham, origin)
        distances.append(walk(f, prasham, num_steps))
    return distances

def drunk_test(walk_lengths, num_trials, drunk_class):
    """
    For each steps in walk_lengths, the walk is simulated over the number of
    trials.
    """
    for num_steps in walk_lengths:
        distances = sim_walk(num_steps, num_trials, drunk_class)
        print(drunk_class.__name__, 'random walk of', str(num_steps), 'steps')
        print('Mean' + str(sum(distances)/num_trials))
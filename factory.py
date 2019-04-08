# -*- coding: utf-8 -*-
__author__ = 'WangJianyu'
__date__ = '2019/2/28'

import xml.etree.ElementTree as etree


#
# import json
#
# class JSONConnector:
#
#     def ___init__(self,filepath):
#         self.data = dict()
#         with open(filepath, mode='r', encoding='utf-8') as f:
#             self.data = json.load(f)
#
#
#     @property
#     def parsed_data(self):
#         return self.data
#
#
#
# class XMLConnector:
#
#     def __init__(self, filepath):
#         self.tree = etree.parse(filepath)
#
#     @property
#     def parsed_data(self):
#         return self.tree
#
# def connection_factory(filepath):
#     if filepath.endswith('json'):
#         connector = JSONConnector
#     elif filepath.endswith('xml'):
#         connector = XMLConnector
#     else:
#         raise ValueError('Cannot connect to {}'.format(filepath))
#     return connector(filepath)
#
# def connect_to(filepath):
#     factory = None
#     try:
#         factory = connection_factory(filepath)
#     except ValueError as e:
#         print(e)
#     return factory

class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {} !'.format(self, obstacle, obstacle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return '\n\n\t --------Forg World--------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {} !'.format(self, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        self.player_name = name

    def __str__(self):
        return '\n\n\t--------Wizard World--------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)

    except ValueError as err:
        print("Age {} is invalid, please try again....")
        return False
    return (True, age)


def main():
    name = input("Hello . What's your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)

        game = FrogWorld if age < 18 else WizardWorld
        environment = GameEnvironment(game(name))
        environment.play()


import json


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connector_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connector_factory(filepath)

    except ValueError as e:
        print(e)
    return factory


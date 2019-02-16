from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from utils import cp
from statistics import median

author = 'Philip Chapkovski, HSE-Moscow'

doc = """
Age collecting, and splitting of population based on median age
"""


class Constants(BaseConstants):
    name_in_url = 'age'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def split_on_age(self):
        m = median([p.age for p in self.get_players()])
        for p in self.get_players():
            p.participant.vars['supergroup'] = 'high' if p.age>= m else 'low'


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField()

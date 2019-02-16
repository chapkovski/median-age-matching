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
    def creating_session(self):
        assert len(self.get_players()) % 2 == 0, 'The number of players should be even'

    def split_on_age(self):

        ps = sorted(self.get_players(), key=lambda x: x.age)
        low = ps[:len(ps) // 2]
        high = ps[len(ps) // 2:]
        for p in low:
            p.participant.vars['supergroup'] = 'low'
        for p in high:
            p.participant.vars['supergroup'] = 'high'


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField()

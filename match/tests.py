from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        assert self.participant.vars['supergroup'] != self.player.other.participant.vars['supergroup']
        yield (pages.Results)

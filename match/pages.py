from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class MatchingWP(WaitPage):
    group_by_arrival_time = True
    def get_players_for_group(self, waiting_players):
        low = [w for w in waiting_players if w.participant.vars['supergroup'] == 'low']
        high= [w for w in waiting_players if w.participant.vars['supergroup'] == 'high']
        if len(low)>=1 and len(high)>=1:
            return [low[0],  high[0]]


class Results(Page):
    pass


page_sequence = [
    MatchingWP,
    Results
]

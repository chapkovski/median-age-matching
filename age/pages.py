from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Age(Page):
    form_model = 'player'
    form_fields = ['age']

class MedianWP(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        self.subsession.split_on_age()



page_sequence = [
    Age,
    MedianWP,
]

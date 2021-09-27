from otree.api import *
from gettext import gettext
from settings import LANGUAGE_CODE


class Constants(BaseConstants):
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

# FUNCTIONS
# PAGES
class Instructions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(lang=LANGUAGE_CODE)

page_sequence = [Instructions]

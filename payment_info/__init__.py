from otree.api import *
import secrets
import string
from settings import LANGUAGE_CODE
import random


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


def generate_code():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(6))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password


def set_payoff(result, player):
    prizes = player.session.vars['payoffs'][result[0]][player.role]
    keys = result[1].keys()
    key = list(keys)[0]
    y = result[1][key]

    player.participant.payoff = prizes[key][y]



def draw_prize(player):
    if player.role == Constants.DECISION_MAKER_ROLE:
        drawn = player.participant.drawn
        result =  random.choice(list(drawn.items()))

        players = player.get_others_in_group()
        partner = players[0]

        set_payoff(result, player)
        set_payoff(result, partner)








class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = 2
    RECEIVER_ROLE = 'Receiver'
    DECISION_MAKER_ROLE = 'Decision Maker'
    num_rounds = 1


class Player(BasePlayer):
    redemption_code = models.StringField()


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class WaitForGroup(WaitPage):

    def after_all_players_arrive(group: Group):
        for player in group.get_players():

            draw_prize(player)


def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        player.redemption_code = generate_code()


# FUNCTIONS
# PAGES
class PaymentInfo(Page):
    form_model = 'player'

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        return {
            'participant_id': participant.code,
            'redemption_code': player.redemption_code,
            'lang': LANGUAGE_CODE
        }


page_sequence = [WaitForGroup, PaymentInfo]

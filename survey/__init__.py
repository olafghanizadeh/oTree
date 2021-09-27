from otree.api import *
import requests
from gettext import gettext
from settings import LANGUAGE_CODE


def get_districts():
    url = 'https://gist.githubusercontent.com/olafghanizadeh/372922acf042bcfe1472b29ec7389060/raw/d261cf98c59dd28f3255053938df23d055902362/regions.json'
    districts = requests.get(url)
    districts = districts.json()

    districts_list = []
    for district in districts:
        districts_list.append([district['code'], district['name']])

    return districts_list


def make_fields(dictionary):
    investment_list = []
    for key, value in dictionary.items():
        investment_list.append(key)
    return investment_list


def make_field(value):
    return models.BooleanField(
        blank=True,
        label=value,
        widget=widgets.CheckboxInput
    )


investments = {
    'commercialPaper': gettext('Commercial Paper'),
    'cryptoCurrency': gettext('Bitcoin, ICOs or other cryptocurrency related investment'),
    'crowdFunding': gettext('Crowdfunding'),
    'corporateBonds': gettext('Corporate Bonds'),
    'complex': gettext('Complex Financial Products (derivatives, options or other leveraged products)'),
    'tBonds': gettext('Treasury Bonds'),
    'funds': gettext('Investment Funds'),
    'stocks': gettext('Stocks'),
    'retirement': gettext('Retirement savings')
}


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    investments = make_fields(investments)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    accessCode = models.StringField()
    prizeChoice = models.IntegerField(
        choices=[[0, gettext("Apple AirPods")], [1, gettext("Samsung Galaxy Buds Pro")]],
        label=gettext("In case you win one of the bluetooth headphones, which one would you prefer?")
    )
    age = models.IntegerField(label=gettext('What year were you born?'), min=1980, max=2003)
    gender = models.StringField(
        choices=[[0, gettext('Male')], [1, gettext('Female')], [2, gettext('Other/Prefer not to disclose')]],
        label=gettext('What is your gender?'),
        widget=widgets.RadioSelect,
    )
    district = models.StringField(
        choices=get_districts(),
        label=gettext('In which region do you have your fiscal residence?')
    )

    education = models.IntegerField(
        label=gettext('Please indicate your highest level of completed education'),
        choices=[
            [0, gettext('Primary education')],
            [1, gettext('Lower secondary education')],
            [2, gettext('Upper secondary education')],
            [3, gettext("Undergraduate/bachelor's degree")],
            [4, gettext('Master, MBA or Doctorate degree')]
        ]

    )
    work = models.IntegerField(
        label=gettext('Please indicate your work situation'),
        choices=[
            [0, gettext('Unemployed')],
            [1, gettext('Self employed')],
            [2, gettext('Employed')],
            [3, gettext('Retired')],
            [4, gettext('Student')],
            [5, gettext('Other')]
        ]
    )

    income = models.IntegerField(
        label=gettext('Please indicate your monthly household income'),
        choices=[
            [0, gettext('Up to 500€ per month')],
            [1, gettext('Between 501€ and 1000€ per month')],
            [2, gettext('Between 1001€ and 2500€ per month')],
            [3, gettext('Between 2510€ and 4000€ per month')],
            [4, gettext('More than 4000€ per month')]
        ]
    )
    economics = models.BooleanField(
        choices=[[False, gettext("No")], [True, gettext("Yes")]],
        label=gettext("Have you ever studied economics?")
    )

    riskAssesment = models.IntegerField(
        choices=[[0, gettext("Very risk averse")], [1, gettext("Risk averse")], [2, gettext("Risk neutral")],
                 [3, gettext("Risk lover")], [4, gettext("Risk lover (more)")]],
        widget=widgets.RadioSelectHorizontal,
        label=gettext("What is your own perception of your willingness to take risks?")
    )
    gambling = models.BooleanField(
        choices=[[False, gettext("No")], [True, gettext("Yes")]],
        label=gettext("Have you ever gambled online through online casinos or sport betting services such as Betclic?")
    )
    # Investment question multiple choice
    for key, value in investments.items():
        locals()[key] = make_field(value)


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'district', 'prizeChoice']



class SocioEconomic(Page):
    form_model = 'player'
    form_fields = ['education', 'work', 'economics', 'income']


class RiskSurvey(Page):
    form_model = 'player'
    form_fields = ['riskAssesment', 'gambling']
    form_fields.extend(Constants.investments)

    @staticmethod
    def vars_for_template(player: Player):
        risk = ['riskAssesment']
        gambling = ['gambling']
        investment = ['commercialPaper', 'cryptoCurrency', 'crowdFunding', 'corporateBonds', 'complex', 'tBonds',
                      'funds', 'stocks', 'retirement']

        return dict(risk=risk, gambling=gambling, investment=investment)


page_sequence = [Demographics, SocioEconomic, RiskSurvey]

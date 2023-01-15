from os import environ


SESSION_CONFIGS = [
    dict(
        name='BASELINE',
        display_name='BASLINE',
        num_demo_participants=2,
        app_sequence=['hl_mpl_decision_maker', 'payment_info'],
        payoffs='BASELINE'
    ),
    dict(
        name='BASELINE_BOTS',
        display_name='BASLINE With Bots',
        num_demo_participants=2,
        app_sequence=['hl_mpl_decision_maker', 'payment_info'],
        payoffs='BASELINE',
        use_browser_bots=True
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00,
    participation_fee=0,
    doc=""
)
PARTICIPANT_FIELDS = ["payoffs", "drawn"]
USE_POINTS=False

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree']

#from django.db import models

# Create your models here.


ARTISTS = {
    'francis-cabrel': {'name': 'Francis Cabrel'},
    'lej' : {'name': 'Elijay'},
    'rosana': {'name': 'Rosana'},
    'maria-dolores-pradera': {'name': 'Maria dolores Prodera'},
}


ALBUMS = [
    {'name': 'Sabarcane', 'artists': [ARTISTS['francis-cabrel']]},
    {'name': 'la Dalle', 'artists': [ARTISTS['lej']]},
    {'name': 'Luna nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]
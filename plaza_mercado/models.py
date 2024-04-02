import requests
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MercadoPlace:
    BASE_URL = 'https://microservices-utadeo-arqfea471e6a9d4.herokuapp.com/api/v1/software-architecture/market-place'

    @staticmethod
    def get_ingredient_quantity(ingredient_name):
        response = requests.get(f'{MercadoPlace.BASE_URL}?ingrediente={ingredient_name}')
        return response.json()['cantidades_vendidas']
    
    
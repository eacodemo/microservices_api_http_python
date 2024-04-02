import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MARKET_PLACE_API_URL = 'https://microservices-utadeo-arqfea471e6a9d4.herokuapp.com/api/v1/software-architecture/market-place'
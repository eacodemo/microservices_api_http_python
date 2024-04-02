from flask import Flask
from flask import Blueprint

myapp = Blueprint('plaza_mercado', __name__, url_prefix='/mercado')


app = Flask(__name__)

@app.route('/')
def index():
    return '¡Bienvenido al microservicio de la plaza de mercado!'

if __name__ == '__main__':
    app.run(debug=True)

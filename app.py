from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes and initialize the Flask app
from gestion_estados.myapp import myapp
from gestion_ingredientes.myapp import myapp
from gestion_ordenes.myapp import myapp
from gestion_receta.myapp import myapp
from plaza_mercado.myapp import myapp

app.register_blueprint(myapp)

if __name__ == '__main__':
    app.run(debug=True)
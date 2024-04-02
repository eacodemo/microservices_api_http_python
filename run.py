from flask import Flask
from gestion_estados import myapp, models
from gestion_ingredientes import myapp, models
from gestion_ordenes import myapp, models
from gestion_receta import myapp, models
from plaza_mercado import myapp, models


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize blueprints and extensions
    from.import gestion_ingredientes, gestion_recetas, gestion_estados, gestion_ordenes, plaza_mercado
    app.register_blueprint(gestion_ingredientes.myapp)
    app.register_blueprint(gestion_recetas.myapp)
    app.register_blueprint(gestion_estados.myapp)
    app.register_blueprint(gestion_ordenes.myapp)
    app.register_blueprint(plaza_mercado.myapp)

    return app

    if __name__ == '__main__':
        app.run(debug=True)
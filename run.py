from flask import Flask

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
from flask import Flask

# Import the required modules and configurations
from config import Config
from gestion_estados import myapp as gestion_estados_app
from gestion_ingredientes import myapp as gestion_ingredientes_app
from gestion_receta import myapp as gestion_recetas_app
from gestion_ordenes import myapp as gestion_ordenes_app
from plaza_mercado import myapp as plaza_mercado_app

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize blueprints and extensions
    app.register_blueprint(gestion_ingredientes_app, url_prefix="/ingredientes")
    app.register_blueprint(gestion_recetas_app, url_prefix="/recetas")
    app.register_blueprint(gestion_estados_app, url_prefix="/estados")
    app.register_blueprint(gestion_ordenes_app, url_prefix="/ordenes")
    app.register_blueprint(plaza_mercado_app, url_prefix="/plaza_mercado")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
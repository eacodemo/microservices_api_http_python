# settings.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define la ruta del archivo de base de datos SQLite
#db_dir = os.path.abspath('../data.sqlite')

# Configuración de la aplicación Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin'
app.config["DEBUG"] = True

# Configuración de la conexión a la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Conexion para base de datos windows
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_dir

db = SQLAlchemy(app)

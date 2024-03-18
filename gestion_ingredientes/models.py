from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ingrediente(db.Model):
    __tablename__ = 'Ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    ingrediente = db.Column(db.String(50), nullable=False)
    inventario = db.Column(db.Integer, nullable=False)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class IngredienteReceta(db.Model):
    __tablename__ = 'Ingrediente_receta'
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    ingredientes_id = db.Column(db.Integer, db.ForeignKey('Ingredientes.Id'), nullable=False)
    recetas_id = db.Column(db.Integer, db.ForeignKey('Recetas.Id'), nullable=False)

class Receta(db.Model):
    __tablename__ = 'Recetas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)


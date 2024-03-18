from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orden(db.Model):
    __tablename__ = 'Orden '  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Text, nullable=False)
    recetas_id = db.Column(db.Integer, db.ForeignKey('Recetas.Id'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('Estado.Id'), nullable=False)

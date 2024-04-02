from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orden(db.Model):
    __tablename__ = 'Orden '  # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Text, nullable=False)
    recetas_id = db.Column(db.Integer, db.ForeignKey('Recetas.Id'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('Estado.Id'), nullable=False)

    def __repr__(self):
        return f'<Orden {self.id} ({self.receta_id}, {self.estado_id})>'

class Estado(db.Model):
    __tablename__ = 'Estado'
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Estado {self.estado}>'
    

class OrdenIngrediente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.id'), nullable=False)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<OrdenIngrediente {self.ingrediente_id} ({self.cantidad}) for {self.orden_id}>'
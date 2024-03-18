from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Estado(db.Model):
    __tablename__ = 'Estado'
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Integer, nullable=False)


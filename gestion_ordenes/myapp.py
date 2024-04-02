from flask import Flask
from flask.json import jsonify
from requests import request
from settings import db, app
from models import Orden
from flask import Blueprint, request
from gestion_ordenes.models import Estado
from plaza_mercado.models import MercadoPlace

myapp = Blueprint('gestion_ordenes', __name__, url_prefix='/ordenes')
@app.route('/')
def index():
    return '¡Bienvenido al microservicio de ordenes!'


@app.route('/ordenes', methods=['GET'])
def get_all_ordenes():
    try:
        ordenes = Orden.query.all()
        ordenes_data = [{'id': orden.id, 'timestamp': orden.timestamp,
                         'recetas_id': orden.recetas_id, 'estado_id': orden.estado_id} for orden in ordenes]
        return jsonify({'status': 200, 'message': 'Se recuperan todas las órdenes', 'data': ordenes_data})
    except Exception as e:
        return jsonify({'status': 500, 'message': 'Error al recuperar órdenes', 'error': str(e)})

@app.route('/ordenes', methods=['POST'])
def create_orden():
    try:
        data = request.get_json()
        nueva_orden = Orden(timestamp=data['timestamp'], recetas_id=data['recetas_id'], estado_id=data['estado_id'])
        db.session.add(nueva_orden)
        db.session.commit()
        return jsonify({'status': 201, 'message': 'Orden creada exitosamente'})
    except Exception as e:
        return jsonify({'status': 500, 'message': 'Error al crear orden', 'error': str(e)})

@app.route('/ordenes/<int:orden_id>', methods=['GET'])
def get_orden_by_id(orden_id):
    try:
        orden = Orden.query.get(orden_id)
        if orden:
            orden_data = {'id': orden.id, 'timestamp': orden.timestamp,
                          'recetas_id': orden.recetas_id, 'estado_id': orden.estado_id}
            return jsonify({'status': 200, 'message': 'Orden encontrada', 'data': orden_data})
        else:
            return jsonify({'status': 404, 'message': 'Orden no encontrada'})
    except Exception as e:
        return jsonify({'status': 500, 'message': 'Error al recuperar orden', 'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)

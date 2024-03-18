from flask import Flask
from flask.json import jsonify
from requests import request
from settings import db, app
from models import Orden

@app.route('/')
def index():
    return '¡Bienvenido al microservicio de ordenes!'


# Endpoint para obtener todas las órdenes
@app.route('/ordenes', methods=['GET'])
def get_ordenes():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        ordenes = Orden.query.all()
        data = []
        for orden in ordenes:
            data.append({
                'id': orden.id,
                'timestamp': orden.timestamp,
                'recetas_id': orden.recetas_id,
                'estado_id': orden.estado_id
            })
        message.update({
            'status': 200,
            'message': 'Se recuperan todas las órdenes',
            'data': data
        })
    except Exception as e:
        print(e)
    return jsonify(message)

# Endpoint para agregar una nueva orden
@app.route('/ordenes', methods=['POST'])
def agregar_orden():
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        data = request.get_json()
        nueva_orden = Orden(
            timestamp=data['timestamp'],
            recetas_id=data['recetas_id'],
            estado_id=data['estado_id']
        )
        db.session.add(nueva_orden)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'Orden agregada exitosamente'
        })
    except Exception as e:
        print(e)
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)

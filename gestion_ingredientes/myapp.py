from flask import Flask
from flask.json import jsonify
from requests import request
from settings import db, app
from models import Ingrediente



@app.route('/')
def index():
    return '¡Bienvenido al microservicio de gestion de ingredientes!'


# Ruta para obtener la lista de ingredientes disponibles
@app.route('/ingredientes', methods=['GET'])
def get_all_ingredientes():
    message = {
      'status': 404,
      'message': 'Algo salió mal'
    }
    try:
        data = Ingrediente.query.with_entities(
          Ingrediente.id, Ingrediente.ingrediente, Ingrediente.inventario).all()
        message.update({
          'status': 200,
          'message': 'Se recuperan TODOS los ingredientes',
          'data': data
        })
    except:
        pass
    return jsonify(message)


# Ruta para agregar un nuevo ingrediente
@app.route('/ingredientes', methods=['POST'])
def agregar_ingrediente():
    data = request.get_json()
    nuevo_ingrediente = Ingrediente(ingrediente=data['ingrediente'], inventario=data['inventario'])
    db.session.add(nuevo_ingrediente)
    db.session.commit()
    return jsonify({'status': 201, 'message': 'Ingrediente agregado exitosamente'}), 201

@app.route('/ingredientes/<int:ingrediente_id>', methods=['GET'])
def get_ingrediente(ingrediente_id):
    message = {
      'status': 404,
      'message': 'Ingrediente no encontrado'
    }
    ingrediente = Ingrediente.query.get(ingrediente_id)
    if ingrediente:
        message.update({
          'status': 200,
          'message': 'Ingrediente recuperado exitosamente',
          'data': {
            'id': ingrediente.id,
            'ingrediente': ingrediente.ingrediente,
            'inventario': ingrediente.inventario
          }
        })
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)

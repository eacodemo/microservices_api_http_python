from flask import Flask
from flask.json import jsonify
from requests import request
from settings import db, app
from models import Receta, IngredienteReceta
from flask import Blueprint

myapp = Blueprint('gestion_recetas', __name__, url_prefix='/recetas')



@app.route('/')
def index():
    return '¡Bienvenido al microservicio de la Cocina!'


@app.route('/recetas', methods=['GET'])
def get_all_recetas():
    """
    Esta función está asignada al endpoint /recetas y
    devuelve todas las recetas utilizando el método GET HTTP.
    """
    message = {
        'status': 500,  # Cambiado a 500 para indicar un error interno del servidor
        'message': 'Algo salió mal'
    }
    try:
        data = Receta.query.all()
        recetas = []
        for receta in data:
            recetas.append({
                'id': receta.id,
                'nombre': receta.nombre,
                'descripcion': receta.descripcion
            })
        message.update({
            'status': 200,
            'message': 'Se recuperan TODAS las recetas',
            'data': recetas
        })
    except Exception as e:
        message['message'] = f"Error: {str(e)}"  # Agrega el mensaje de error específico
    return jsonify(message)


@app.route('/recetas/<int:receta_id>', methods=['GET'])
def get_receta(receta_id):
    """
    Esta función está asignada al endpoint /recetas/<receta_id> y
    devuelve una receta específica utilizando el método GET HTTP.
    """
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        receta = Receta.query.get(receta_id)
        if receta:
            data = {
                'id': receta.id,
                'nombre': receta.nombre,
                'descripcion': receta.descripcion
            }
            message.update({
                'status': 200,
                'message': 'Receta encontrada',
                'data': data
            })
        else:
            message['message'] = 'Receta no encontrada'
    except:
        pass
    return jsonify(message)


# Endpoint para agregar una nueva receta
@app.route('/recetas', methods=['POST'])
def agregar_receta():
    """
    Esta función está asignada al endpoint /recetas y
    permite agregar una nueva receta utilizando el método POST HTTP.
    """
    message = {
        'status': 400,
        'message': 'Error al agregar la receta'
    }
    try:
        data = request.get_json()
        nueva_receta = Receta(nombre=data['nombre'], descripcion=data['descripcion'])
        db.session.add(nueva_receta)
        db.session.commit()
        message.update({
            'status': 201,
            'message': 'Receta agregada exitosamente',
            'data': {
                'id': nueva_receta.id,
                'nombre': nueva_receta.nombre,
                'descripcion': nueva_receta.descripcion
            }
        })
    except:
        pass
    return jsonify(message)

# Endpoint para actualizar una receta existente
@app.route('/recetas/<int:receta_id>', methods=['PUT'])
def actualizar_receta(receta_id):
    """
    Esta función está asignada al endpoint /recetas/<receta_id> y
    permite actualizar una receta existente utilizando el método PUT HTTP.
    """
    message = {
        'status': 400,
        'message': 'Error al actualizar la receta'
    }
    try:
        receta = Receta.query.get(receta_id)
        if receta:
            data = request.get_json()
            receta.nombre = data['nombre']
            receta.descripcion = data['descripcion']
            db.session.commit()
            message.update({
                'status': 200,
                'message': 'Receta actualizada exitosamente',
                'data': {
                    'id': receta.id,
                    'nombre': receta.nombre,
                    'descripcion': receta.descripcion
                }
            })
        else:
            message['message'] = 'Receta no encontrada'
    except:
        pass
    return jsonify(message)

# Endpoint para eliminar una receta existente
@app.route('/recetas/<int:receta_id>', methods=['DELETE'])
def eliminar_receta(receta_id):
    """
    Esta función está asignada al endpoint /recetas/<receta_id> y
    permite eliminar una receta existente utilizando el método DELETE HTTP.
    """
    message = {
        'status': 400,
        'message': 'Error al eliminar la receta'
    }
    try:
        receta = Receta.query.get(receta_id)
        if receta:
            db.session.delete(receta)
            db.session.commit()
            message.update({
                'status': 200,
                'message': 'Receta eliminada exitosamente'
            })
        else:
            message['message'] = 'Receta no encontrada'
    except:
        pass
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask.json import jsonify
from models import Estado
from settings import db, app


@app.route('/')
def index():
    return '¡Bienvenido al microservicio del Restaurante!'



# Ruta para obtener todos los estados
@app.route('/estados', methods=['GET'])
def get_all_estados():
    """
    Esta función está asignada con el punto final /estados y
    representa todos los registros de estados utilizando el método GET HTTP.
    """
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        # Recupera todos los registros de estados
        data = Estado.query.all()
        # Formatea los datos para devolverlos como JSON
        estados = [{
            'id': estado.id,
            'estado': estado.estado
        } for estado in data]
        message.update({
            'status': 200,
            'message': 'Se recuperan TODOS los registros de estados',
            'data': estados
        })
    except:
        pass
    return jsonify(message)

# Otra ruta para obtener un estado específico por su ID
@app.route('/estados/<int:estado_id>', methods=['GET'])
def get_estado_by_id(estado_id):
    """
    Esta función está asignada con el punto final /estados/<id> y
    representa un registro de estado específico utilizando el método GET HTTP.
    """
    message = {
        'status': 404,
        'message': 'Algo salió mal'
    }
    try:
        # Recupera el estado por su ID
        estado = Estado.query.get(estado_id)
        if estado:
            # Formatea el estado para devolverlo como JSON
            estado_data = {
                'id': estado.id,
                'estado': estado.estado
            }
            message.update({
                'status': 200,
                'message': 'Se recupera el estado con el ID proporcionado',
                'data': estado_data
            })
        else:
            message.update({
                'status': 404,
                'message': 'No se encontró ningún estado con el ID proporcionado'
            })
    except:
        pass
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)

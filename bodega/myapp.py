from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Bienvenido al microservicio de la bodega!'

if __name__ == '__main__':
    app.run(debug=True)

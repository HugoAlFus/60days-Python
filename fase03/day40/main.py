from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreto-super-seguro'
socketio = SocketIO(app, cors_allowed_origins='*')

historial = []


@app.route('/')
def home():
    return render_template("chat.html")


@socketio.on('connect')
def handle_connect():
    emit('historial', historial)


@socketio.on('mensaje')
def handle_message(msg):
    print(f"Mensaje recibido: {msg}")
    historial.append(msg)
    emit('mensaje', msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)

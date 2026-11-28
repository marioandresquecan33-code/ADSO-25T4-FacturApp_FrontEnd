import requests
from flask import Blueprint, render_template, request, redirect, url_for

usuario_bp = Blueprint('usuario_bp', __name__)
API_URL = "http://localhost:5002/api"

# Listar usuarios reales desde MySQL
@usuario_bp.route('/users')
def listar_usuarios():
    try:
        respuesta = requests.get(f"{API_URL}/usuarios")
        usuarios = respuesta.json() if respuesta.status_code == 200 else []
    except Exception:
        usuarios = []
    return render_template('usuarios/list_users.html', usuarios=usuarios)

# Crear usuario nuevo enviando JSON al Backend
@usuario_bp.route('/user/new', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        datos = {
            "documento": request.form['documento'],
            "nombre": request.form['nombre'],
            "email": request.form['email'],
            "rol": request.form.get('rol', 'Vendedor'),
            "password": request.form['password']
        }
        requests.post(f"{API_URL}/usuarios", json=datos)
        return redirect(url_for('usuario_bp.listar_usuarios'))

    return render_template('usuarios/form_users.html')

# Eliminar usuario llamando al DELETE del Backend
@usuario_bp.route('/user/delete/<int:id>')
def eliminar_usuario(id):
    try:
        requests.delete(f"{API_URL}/usuarios/{id}")
    except Exception:
        pass
    return redirect(url_for('usuario_bp.listar_usuarios'))

# Editar usuario (GET precarga los datos actuales, POST guarda los cambios en MySQL)
@usuario_bp.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    if request.method == 'POST':
        datos = {
            "documento": request.form['documento'],
            "nombre": request.form['nombre'],
            "email": request.form['email'],
            "rol": request.form['rol']
        }
        # Solo envía contraseña si el usuario escribió una nueva
        if request.form.get('password'):
            datos["password"] = request.form['password']

        requests.put(f"{API_URL}/usuarios/{id}", json=datos)
        return redirect(url_for('usuario_bp.listar_usuarios'))

    respuesta = requests.get(f"{API_URL}/usuarios")
    usuarios = respuesta.json() if respuesta.status_code == 200 else []
    usuario = next((u for u in usuarios if u['id_usuario'] == id), None)

    return render_template('usuarios/form_users.html', usuario=usuario)

import requests
from flask import Blueprint, render_template, request, redirect, url_for

clients_bp = Blueprint('clients', __name__)
API_URL = "http://127.0.0.1:5002/api"

# Listar clientes reales desde MySQL
@clients_bp.route('/list_clients')
def list_clients():
    try:
        respuesta = requests.get(f"{API_URL}/clientes")
        clientes = respuesta.json() if respuesta.status_code == 200 else []
    except Exception:
        clientes = []
    return render_template('clients/list_clients.html', clientes=clientes)

# Crear nuevo cliente enviando JSON al Backend
@clients_bp.route('/form_clients', methods=['GET', 'POST'])
@clients_bp.route('/client/new', methods=['GET', 'POST'])
def form_clients():
    if request.method == 'POST':
        datos = {
            "documento": request.form['documento'],
            "nombre": request.form['nombre'],
            "email": request.form.get('email'),
            "telefono": request.form.get('telefono'),
            "direccion": request.form.get('direccion')
        }
        requests.post(f"{API_URL}/clientes", json=datos)
        return redirect(url_for('clients.list_clients'))

    return render_template('clients/form_clients.html', cliente=None)

# Editar cliente existente
@clients_bp.route('/client/edit/<int:id>', methods=['GET', 'POST'])
def edit_client(id):
    if request.method == 'POST':
        datos = {
            "documento": request.form['documento'],
            "nombre": request.form['nombre'],
            "email": request.form.get('email'),
            "telefono": request.form.get('telefono'),
            "direccion": request.form.get('direccion')
        }
        requests.put(f"{API_URL}/clientes/{id}", json=datos)
        return redirect(url_for('clients.list_clients'))

    respuesta = requests.get(f"{API_URL}/clientes")
    clientes = respuesta.json() if respuesta.status_code == 200 else []
    cliente = next((c for c in clientes if c['id_cliente'] == id), None)

    return render_template('clients/form_clients.html', cliente=cliente)

# Eliminar cliente
@clients_bp.route('/client/delete/<int:id>')
def delete_client(id):
    try:
        requests.delete(f"{API_URL}/clientes/{id}")
    except Exception:
        pass
    return redirect(url_for('clients.list_clients'))

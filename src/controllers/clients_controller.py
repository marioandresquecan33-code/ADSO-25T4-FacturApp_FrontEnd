import requests
from flask import Blueprint, render_template, request, redirect, url_for

clients_bp = Blueprint('clients_bp', __name__)
API_URL = "http://localhost:5002/api"

# Listar todos los clientes
@clients_bp.route('/list_clients')
def listar_clientes():
    try:
        resp = requests.get(f"{API_URL}/clientes")
        clientes = resp.json() if resp.status_code == 200 else []
    except Exception:
        clientes = []
    return render_template('clients/list_clients.html', clientes=clientes)

# Registrar nuevo cliente (muestra alerta roja si la cédula ya existe con otro nombre)
@clients_bp.route('/client/new', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        datos = {
            "documento": request.form['documento'],
            "nombre": request.form['nombre'],
            "email": request.form.get('email', ''),
            "telefono": request.form.get('telefono', ''),
            "direccion": request.form.get('direccion', '')
        }
        try:
            resp = requests.post(f"{API_URL}/clientes", json=datos)
            if resp.status_code == 201:
                return redirect(url_for('clients_bp.listar_clientes'))
            else:
                error_msg = resp.json().get('error', 'Error al registrar el cliente.')
                return render_template('clients/form_clients.html', cliente=datos, error=error_msg)
        except Exception:
            return render_template(
                'clients/form_clients.html',
                cliente=datos,
                error="No se pudo conectar con el servidor Backend (puerto 5002)."
            )

    return render_template('clients/form_clients.html', cliente=None, error=None)

# Editar cliente existente
@clients_bp.route('/client/edit/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    if request.method == 'POST':
        datos = {
            "documento": request.form['documento'],
            "nombre": request.form['nombre'],
            "email": request.form.get('email', ''),
            "telefono": request.form.get('telefono', ''),
            "direccion": request.form.get('direccion', '')
        }
        try:
            resp = requests.put(f"{API_URL}/clientes/{id}", json=datos)
            if resp.status_code == 200:
                return redirect(url_for('clients_bp.listar_clientes'))
            error_msg = resp.json().get('error', 'Error al actualizar el cliente.')
            datos['id_cliente'] = id
            return render_template('clients/form_clients.html', cliente=datos, error=error_msg)
        except Exception:
            datos['id_cliente'] = id
            return render_template(
                'clients/form_clients.html',
                cliente=datos,
                error="No se pudo conectar con el servidor Backend (puerto 5002)."
            )

    try:
        resp = requests.get(f"{API_URL}/clientes")
        clientes = resp.json() if resp.status_code == 200 else []
    except Exception:
        clientes = []
    cliente = next((c for c in clientes if c['id_cliente'] == id), None)
    return render_template('clients/form_clients.html', cliente=cliente, error=None)

# Eliminar cliente
@clients_bp.route('/client/delete/<int:id>')
def eliminar_cliente(id):
    try:
        requests.delete(f"{API_URL}/clientes/{id}")
    except Exception:
        pass
    return redirect(url_for('clients_bp.listar_clientes'))

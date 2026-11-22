import requests
from flask import Blueprint, render_template, request, redirect, url_for, flash

factura_bp = Blueprint('factura_bp', __name__)
API_URL = "http://127.0.0"

# Historial de facturas emitidas desde MySQL
@factura_bp.route('/facturas')
def listar_facturas():
    try:
        respuesta = requests.get(f"{API_URL}/facturas")
        facturas = respuesta.json() if respuesta.status_code == 200 else []
    except Exception:
        facturas = []
    return render_template('facturas/list_facturas.html', facturas=facturas)

# Punto de Venta (POS): Crear nueva factura y descontar stock
@factura_bp.route('/factura/new', methods=['GET', 'POST'])
def nueva_factura():
    if request.method == 'POST':
        # Recibir listas de productos y cantidades desde el formulario dinámico
        ids_productos = request.form.getlist('id_producto[]')
        cantidades = request.form.getlist('cantidad[]')

        items = []
        for prod_id, cant in zip(ids_productos, cantidades):
            if prod_id and cant and int(cant) > 0:
                items.append({
                    "id_producto": int(prod_id),
                    "cantidad": int(cant)
                })

        datos = {
            "cliente_nombre": request.form['cliente_nombre'],
            "cliente_documento": request.form['cliente_documento'],
            "items": items
        }

        respuesta = requests.post(f"{API_URL}/facturas", json=datos)
        if respuesta.status_code == 201:
            return redirect(url_for('factura_bp.listar_facturas'))
        else:
            error_msg = respuesta.json().get('error', 'Error al registrar la factura')
            # Recargar datos si hubo error (ej. stock insuficiente)
            clientes = requests.get(f"{API_URL}/clientes").json()
            productos = requests.get(f"{API_URL}/productos").json()
            return render_template('facturas/form_factura.html', clientes=clientes, productos=productos, error=error_msg)

    # Cargar clientes y productos reales desde MySQL para los selectores
    try:
        clientes = requests.get(f"{API_URL}/clientes").json()
        productos = requests.get(f"{API_URL}/productos").json()
    except Exception:
        clientes, productos = [], []

    return render_template('facturas/form_factura.html', clientes=clientes, productos=productos, error=None)

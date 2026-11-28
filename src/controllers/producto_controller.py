import requests
from flask import Blueprint, render_template, request, redirect, url_for

producto_bp = Blueprint('producto_bp', __name__)
API_URL = "http://localhost:5002/api"

# Listar productos reales desde MySQL
@producto_bp.route('/products')
def listar_productos():
    try:
        respuesta = requests.get(f"{API_URL}/productos")
        productos = respuesta.json() if respuesta.status_code == 200 else []
    except Exception:
        productos = []
    return render_template('productos/list_products.html', productos=productos)

# Crear producto nuevo enviando JSON al Backend y cargando categorías de MySQL
@producto_bp.route('/product/new', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        datos = {
            "barcode": request.form['barcode'],
            "nombre_producto": request.form['nombre_producto'],
            "precio": float(request.form['precio']),
            "stock": int(request.form['stock']),
            "id_categoria": int(request.form['id_categoria'])
        }
        requests.post(f"{API_URL}/productos", json=datos)
        return redirect(url_for('producto_bp.listar_productos'))

    try:
        resp_cat = requests.get(f"{API_URL}/categorias")
        categorias = resp_cat.json() if resp_cat.status_code == 200 else []
    except Exception:
        categorias = []

    return render_template('productos/form_products.html', producto=None, categorias=categorias)

# Eliminar producto llamando al DELETE del Backend
@producto_bp.route('/product/delete/<int:id>')
def eliminar_producto(id):
    try:
        requests.delete(f"{API_URL}/productos/{id}")
    except Exception:
        pass
    return redirect(url_for('producto_bp.listar_productos'))

# Editar producto (GET muestra el formulario con los datos actuales, POST guarda los cambios)
@producto_bp.route('/product/edit/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    if request.method == 'POST':
        datos = {
            "barcode": request.form['barcode'],
            "nombre_producto": request.form['nombre_producto'],
            "precio": float(request.form['precio']),
            "stock": int(request.form['stock']),
            "id_categoria": int(request.form['id_categoria'])
        }
        requests.put(f"{API_URL}/productos/{id}", json=datos)
        return redirect(url_for('producto_bp.listar_productos'))

    resp_prod = requests.get(f"{API_URL}/productos")
    productos = resp_prod.json() if resp_prod.status_code == 200 else []
    producto = next((p for p in productos if p['id_producto'] == id), None)

    resp_cat = requests.get(f"{API_URL}/categorias")
    categorias = resp_cat.json() if resp_cat.status_code == 200 else []

    return render_template('productos/form_products.html', producto=producto, categorias=categorias)

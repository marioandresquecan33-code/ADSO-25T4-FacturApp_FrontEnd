import requests
from flask import Blueprint, render_template, request, redirect, url_for

categories_bp = Blueprint('categories', __name__)
API_URL = "http://127.0.0.1:5002/api"

# Listar categorías reales desde MySQL
@categories_bp.route('/list_categories')
def list_categories():
    try:
        respuesta = requests.get(f"{API_URL}/categorias")
        categorias = respuesta.json() if respuesta.status_code == 200 else []
    except Exception:
        categorias = []
    return render_template('categories/list_categories.html', categorias=categorias)

# Crear categoría (soporta las rutas /form_categories y /category/new)
@categories_bp.route('/form_categories', methods=['GET', 'POST'])
@categories_bp.route('/category/new', methods=['GET', 'POST'])
def form_categories():
    if request.method == 'POST':
        datos = {
            "nombre": request.form['nombre'],
            "descripcion": request.form.get('descripcion', '')
        }
        requests.post(f"{API_URL}/categorias", json=datos)
        return redirect(url_for('categories.list_categories'))

    return render_template('categories/form_categories.html', categoria=None)

# Eliminar categoría
@categories_bp.route('/category/delete/<int:id>')
def delete_category(id):
    try:
        requests.delete(f"{API_URL}/categorias/{id}")
    except Exception:
        pass
    return redirect(url_for('categories.list_categories'))

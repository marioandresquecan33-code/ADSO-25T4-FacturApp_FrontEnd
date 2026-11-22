import requests
from flask import Blueprint, render_template, request, redirect, url_for

producto_bp = Blueprint('producto_bp', __name__)

productos_prueba = [
    {
        "id_producto": 1,
        "barcode": "770123456",
        "nombre_producto": "Teclado USB",
        "categoria": "tecnologia",
        "precio": 45000,
        "stock": 10
    }
]

@producto_bp.route('/products')
def listar_productos():
    return render_template('productos/list_products.html', productos=productos_prueba)

@producto_bp.route('/product/new', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        nuevo = {
            "id_producto": len(productos_prueba) + 1,
            "barcode": request.form['barcode'],
            "nombre_producto": request.form['nombre_producto'],
            "categoria": request.form['categoria'],
            "precio": float(request.form['precio']),
            "stock": int(request.form['stock'])
        }
        productos_prueba.append(nuevo)
        return redirect(url_for('producto_bp.listar_productos'))

    return render_template('productos/form_products.html')

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

    # Cargar todos los productos para buscar el que coincide con el ID
    resp_prod = requests.get(f"{API_URL}/productos")
    productos = resp_prod.json() if resp_prod.status_code == 200 else []
    producto = next((p for p in productos if p['id_producto'] == id), None)

    # Cargar las categorías para el desplegable
    resp_cat = requests.get(f"{API_URL}/categorias")
    categorias = resp_cat.json() if resp_cat.status_code == 200 else []

    return render_template('productos/form_products.html', producto=producto, categorias=categorias)




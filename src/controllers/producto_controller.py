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





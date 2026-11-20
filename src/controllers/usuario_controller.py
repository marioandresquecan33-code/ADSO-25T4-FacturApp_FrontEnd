from flask import Blueprint, render_template, request, redirect, url_for

usuario_bp = Blueprint('usuario_bp', __name__)

usuarios_prueba = [
    {
        "id_usuario": 1,
        "documento": "1000123456",
        "nombre": "Admin Principal",
        "email": "admin@facturapp.com",
        "rol": "Administrador"
    }
]

@usuario_bp.route('/users')
def listar_usuarios():
    return render_template('usuarios/list_users.html', usuarios=usuarios_prueba)

@usuario_bp.route('/user/new', methods=['GET', 'POST'])
def nuevo_usuario():
    if request.method == 'POST':
        nuevo = {
            "id_usuario": len(usuarios_prueba) + 1,
            "documento": request.form['documento'],
            "nombre": request.form['nombre'],
            "email": request.form['email'],
            "rol": request.form['rol']
        }
        usuarios_prueba.append(nuevo)
        return redirect(url_for('usuario_bp.listar_usuarios'))

    return render_template('usuarios/form_users.html')

from flask import Flask


def create_app():
    app = Flask(__name__)

    from src.controllers.home_controller import home_bp
    from src.controllers.clients_controller import clients_bp
    from src.controllers.categories_controller import categories_bp
    from src.controllers.producto_controller import producto_bp
    from src.controllers.usuario_controller import usuario_bp




    app.register_blueprint(home_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(usuario_bp)

    return app




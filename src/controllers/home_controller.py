import requests
from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)
API_URL = "http://localhost:5002/api"

@home_bp.route('/')
def home():
    totales = {"clientes": 0, "facturas": 0, "productos": 0, "usuarios": 0}
    try:
        r_cli = requests.get(f"{API_URL}/clientes")
        if r_cli.status_code == 200:
            totales["clientes"] = len(r_cli.json())

        r_fac = requests.get(f"{API_URL}/facturas")
        if r_fac.status_code == 200:
            totales["facturas"] = len(r_fac.json())

        r_pro = requests.get(f"{API_URL}/productos")
        if r_pro.status_code == 200:
            totales["productos"] = len(r_pro.json())

        r_usu = requests.get(f"{API_URL}/usuarios")
        if r_usu.status_code == 200:
            totales["usuarios"] = len(r_usu.json())
    except Exception:
        pass

    return render_template('home.html', totales=totales)

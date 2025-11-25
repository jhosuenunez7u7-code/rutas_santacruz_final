from flask import Flask
from sistema_rutas.controllers.rutas_controller import rutas_bp

app = Flask(__name__)
app.register_blueprint(rutas_bp)

if __name__ == "__main__":
    app.run(debug=True)

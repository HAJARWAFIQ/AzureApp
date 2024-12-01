from flask import Flask
from app.routes import bp

def create_app():
    """Créer et configurer l'application Flask"""
    app = Flask(__name__)

    # Enregistrer le Blueprint
    app.register_blueprint(bp)

    return app

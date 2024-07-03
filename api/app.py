import logging
import os
from flask import Flask, jsonify
from route import api_hello
from model import db
from sqlalchemy.exc import SQLAlchemyError


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI", None)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DB_INITIALIZED"] = False  # Inicialmente, establecer como False

# Configurar el logger
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

# Intentar inicializar la base de datos
if app.config["SQLALCHEMY_DATABASE_URI"]:
    try:
        app.logger.info("Starting database...")
        db.init_app(app)
        with app.app_context():
            db.create_all()  # Intentar crear las tablas para verificar la conexión
        app.config["DB_INITIALIZED"] = True
        app.logger.info("Database initialized successfully.")
    except SQLAlchemyError as e:
        app.logger.error(f"Failed to connect to the database: {e}")
else:
    app.logger.warning("No database connection string provided. Continuing without database...")


app.logger.info("Starting blueprints...")
app.register_blueprint(api_hello)


@app.route("/alive", methods=["GET"])
@app.route("/", methods=["GET"])
def alive():
    return jsonify({"message": "api is alive!"}, 200)


if __name__ == "__main__":
    app.run()
    app.logger.info("Starting api_hello...")

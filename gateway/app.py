import logging
from flask import Flask
from route import api_hello


app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

app.logger.info("Iniciando blueprints")
app.register_blueprint(api_hello)


@app.route("/alive", methods=["GET"])
@app.route("/", methods=["GET"])
def hello_world():
    return {"message": "gateway is alive!"}


if __name__ == "__main__":
    app.logger.info("Iniciando aplicacion")
    app.run()

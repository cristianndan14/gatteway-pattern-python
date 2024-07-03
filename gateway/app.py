import logging
from flask import Flask, jsonify
from route import api_hello


app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

app.logger.info("Starting blueprints...")
app.register_blueprint(api_hello)


@app.route("/alive", methods=["GET"])
@app.route("/", methods=["GET"])
def hello_world():
    return jsonify(
        {"message": "gateway is alive!"}, 200)


if __name__ == "__main__":
    app.run()
    app.logger.info("Starting gateway...")

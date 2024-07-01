from flask import Flask, request


app = Flask(__name__)


@app.route("/alive", methods=["GET"])
@app.route("/", methods=["GET"])
def hello_world():
    return {"message": "api is alive!"}


@app.route("/custom-message", methods=["POST"])
def custom_hello_world():
    custom_msg = request.json.get("message", None)
    msg_info = "Porfavor ingrese su mensaje dentro del campo 'message' en formato JSON."
    return {"message": f"{custom_msg if custom_msg else msg_info}!"}


@app.route("/<language>", methods=["GET"])
def choose_language(language):
    en = "Hello World!"
    es = "Hola Mundo!"
    ja = "こんにちは、世界！ (Konnichiwa, sekai!)"
    fr = "Bonjour, le monde!"
    pt = "Olá, mundo!"

    languages = {"en": en, "es": es, "ja": ja, "fr": fr, "pt": pt}

    if language in languages.keys():
        return {"message": languages[language]}
    else:
        return {"message": "Please, input a valid language: en/es/ja/fr/pt)"}


if __name__ == "__main__":
    app.run()

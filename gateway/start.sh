#!/bin/sh

# Exportar variables de entorno necesarias para Flask
export FLASK_APP=${FLASK_APP}
export FLASK_ENV=${FLASK_ENV}
# export APP_CONFIG_FILE=${APP_CONFIG_FILE}

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones de base de datos (opcional)
# flask db upgrade

# Iniciar la aplicación
flask run --host=${FLASK_HOST} --port=${FLASK_PORT}
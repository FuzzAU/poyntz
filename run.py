from poyntz.app import app, create_tables
from poyntz import views


if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0')
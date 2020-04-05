from poyntz.app import app, db, create_tables


if __name__ == '__main__':
    create_tables()
    app.run()
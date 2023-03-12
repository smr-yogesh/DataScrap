from routes import app
from routes.api import B_api
from routes.gui import B_gui

app.register_blueprint(B_api)
app.register_blueprint(B_gui)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)


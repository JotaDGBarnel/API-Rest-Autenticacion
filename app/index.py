from aplicacion import app
from models.usuario import user
from models.rol import role
from models.permiso import permission

app.register_blueprint(user)
app.register_blueprint(role)
app.register_blueprint(permission)

if __name__ == "__main__":
    app.run(debug=True)
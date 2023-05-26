"""
import json
from flask import Flask
import flask
import flask_login
from sirope import Sirope
from flask_login import LoginManager, login_required
from model.userdto import UserDto
from routes.historial import historial_bp
from routes.medicamentos import medicamentos_bp
from routes.personal import personal_bp


def create_app():
    login_manager = LoginManager()
    app = Flask(__name__)
    app.config.from_file("config.json", load=json.load)
    syrp = Sirope()
    login_manager.init_app(app)
    login_manager.id_attribute = "id"
    app.register_blueprint(medicamentos_bp)
    app.register_blueprint(personal_bp)
    app.register_blueprint(historial_bp)
    return app, login_manager, syrp


app, login_manager, srp = create_app()


@login_manager.user_loader
def user_loader(username):
    return UserDto.find(srp, username)


@login_manager.unauthorized_handler
def unauthorized_handler():
    flask.flash("Unauthorized")
    return flask.redirect("/pyPharmacy")



@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
        user = buscar_usuario(username)
        if user and user.chk_password(password):
            flask_login.login_user(user)
            return flask.redirect(flask.url_for("get_view_historial"))
        else:
            flask.flash("Nombre de usuario o contraseña inválidos")  

    return flask.render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    flask_login.logout_user()
    return flask.redirect("/pyPharmacy")


@app.route("/pyPharmacy")
def get_index():
    return flask.render_template("login.html")

def buscar_usuario(username):
    users_list = list(srp.load_all(UserDto))
    for user in users_list:
        if user.username == username:
            return user
    return None
    
"""

    


import json
from flask import Flask
import flask
import flask_login
from sirope import Sirope
from flask_login import LoginManager, login_required
from model.userdto import UserDto
from routes.historial import historial_bp
from routes.medicamentos import medicamentos_bp
from routes.personal import existe_usuario, personal_bp


def create_app():
    lmanager = flask_login.login_manager.LoginManager()
    fapp = flask.Flask(__name__)
    syrp = Sirope()
    fapp.config.from_file("config.json", load=json.load)
    lmanager.init_app(fapp)
    fapp.register_blueprint(medicamentos_bp)
    fapp.register_blueprint(personal_bp)
    fapp.register_blueprint(historial_bp)
    flask_login.LoginManager.id_attribute = "id"
    return fapp, lmanager, syrp


app, lm, srp = create_app()


@lm.user_loader
def user_loader(username):
    return UserDto.find(srp, username)


@lm.unauthorized_handler
def unauthorized_handler():
    flask.flash("Unauthorized")
    return flask.redirect("/pyPharmacy")


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
        user = user_loader(username)
        if user and user.chk_password(password):
            flask_login.login_user(user)
            return flask.redirect(flask.url_for("historial.get_view_historial"))
        else:
            flask.flash("Nombre de usuario o contraseña inválidos")  

    return flask.render_template("login.html")


@app.route("/logout")
def logout():
    flask_login.logout_user()
    return flask.redirect("/pyPharmacy")


@app.route("/pyPharmacy")
def get_index():
    return flask.render_template("login.html")

@app.route("/personal/registrar/login", methods=["POST"])
def get_registrar_personal_login():
    username = flask.request.form.get("usernameLog")
    nombre = flask.request.form.get("nombreLog")
    apellidos = flask.request.form.get("apellidosLog")
    password = flask.request.form.get("passwordLog")
    if existe_usuario(username):
        flask.flash("El usuario ya existe")
        return flask.redirect("/pyPharmacy")
    else:
        srp.save(UserDto(username, password, nombre, apellidos))
        user = user_loader(username)
        flask_login.login_user(user)
        return flask.redirect(flask.url_for("historial.get_view_historial"))


from flask import Blueprint
import flask
from flask_login import login_required
from model.userdto import UserDto
import sirope

personal_bp = Blueprint("personal", __name__)
srp = sirope.Sirope()


@personal_bp.route("/personal")
@login_required
def get_view_personal():
    users_list = list(srp.load_all(UserDto))
    sust = {"users_list": users_list}
    return flask.render_template("personal.html", **sust)


@personal_bp.route("/personal/registrar", methods=["POST"])
@login_required
def get_registrar_personal():
    username = flask.request.form.get("username")
    nombre = flask.request.form.get("nombre")
    apellidos = flask.request.form.get("apellidos")
    password = flask.request.form.get("password")
    if existe_usuario(username):
        flask.flash("El usuario ya existe")
        return flask.redirect("/personal")
    else:
        srp.save(UserDto(username, password, nombre, apellidos))
        return flask.redirect("/personal")


@personal_bp.route("/personal/modificar", methods=["POST"])
@login_required
def modificar_personal():
    username = flask.request.form.get("username")
    nombre = flask.request.form.get("nombre")
    apellidos = flask.request.form.get("apellidos")
    for usr in srp.load_all(UserDto):
        if str(usr.username) == str(username):
            usr.nombre = nombre
            usr.apellidos = apellidos
            srp.save(usr)
            return flask.redirect("/personal")
    flask.flash("No se puede modificar el usuario")
    return flask.redirect("/personal")


@personal_bp.route("/personal/eliminar", methods=["POST"])
@login_required
def eliminar_usuario():
    username = flask.request.form.get("username")
    if username is not None and username != "":
        for usr in srp.load_all(UserDto):
            if str(usr.username) == str(username):
                oid = usr.__dict__[srp.OID_ID]
                srp.delete(oid)
                return flask.redirect("/personal")
    flask.flash("Ha habido un error al eliminar el usuario")
    return flask.redirect("/personal")


def existe_usuario(username):
    users_list = list(srp.load_all(UserDto))
    for usr in users_list:
        print(usr.username)
        if usr.username == username:
            return True
    return False



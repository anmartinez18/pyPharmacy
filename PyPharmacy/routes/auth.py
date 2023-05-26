""""
from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import login_user, logout_user, login_required, current_user
from model.userdto import UserDto
from app import login_manager

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return UserDto.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    flash("Unauthorized")
    return redirect("/pyPharmacy")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = UserDto.query.filter_by(username=username).first()
        if user and user.chk_password(password):
            login_user(user)
            return redirect(url_for("historial.get_view_historial"))
        else:
            flash("Nombre de usuario o contraseña inválidos")

    return render_template("login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/pyPharmacy")

@auth_bp.route("/pyPharmacy")
def get_index():
    return render_template("login.html")

    
    
"""

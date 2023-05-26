from flask import Blueprint, render_template
import flask
from flask_login import login_required
from model.medicamentodto import MedicamentoDto
import sirope

medicamentos_bp = Blueprint("medicamentos", __name__)
srp = sirope.Sirope()


@medicamentos_bp.route("/medicamentos")
@login_required
def get_view_medicamentos():
    medicamentos_list = list(srp.load_all(MedicamentoDto))
    sust = {
        "medicamentos_list": medicamentos_list,
    }
    return render_template("medicamentos.html", **sust)


@medicamentos_bp.route("/medicamentos/registrar", methods=["POST"])
@login_required
def registrar_medicamentos():
    id_medicamento = flask.request.form.get("id_medicamento")
    nombre = flask.request.form.get("nombreMedicamento")
    categoria = flask.request.form.get("categoria")
    num_unidades = flask.request.form.get("num_unidades")
    if comprobar_id_medicamento(id_medicamento) is None:
        if num_unidades is None or num_unidades == "":
            num_unidades = 0
        srp.save(
            MedicamentoDto(id_medicamento.upper(), nombre, categoria, num_unidades)
        )
        return flask.redirect("/medicamentos")
    flask.flash("El medicamento introducido ya existe")
    return flask.redirect("/medicamentos")


@medicamentos_bp.route("/medicamentos/modificar", methods=["POST"])
@login_required
def modificar_medicamentos():
    id_medicamento = flask.request.form.get("id_medicamento")
    nombre = flask.request.form.get("nombreMedicamento")
    categoria = flask.request.form.get("categoria")
    num_unidades = flask.request.form.get("num_unidades")
    for medicamento in srp.load_all(MedicamentoDto):
        if str(medicamento.id) == str(id_medicamento):
            oid = medicamento.__dict__[srp.OID_ID]
            if num_unidades is None or num_unidades == "":
                num_unidades = 0
            medicamento.nombre = nombre
            medicamento.categoria = categoria
            medicamento.num_unidades = int(num_unidades)
            srp.save(medicamento)
            return flask.redirect("/medicamentos")
    flask.flash("No se puede modificar el elemento")
    return flask.redirect("/medicamentos")


@medicamentos_bp.route("/medicamentos/eliminar", methods=["POST"])
@login_required
def eliminar_medicamento():
    medicamento_id = flask.request.form.get("medicamento_id")
    print(medicamento_id)
    if medicamento_id is not None and medicamento_id != "":
        for medicamento in srp.load_all(MedicamentoDto):
            if str(medicamento.id) == str(medicamento_id):
                oid = medicamento.__dict__[srp.OID_ID]
                srp.delete(oid)
                return flask.redirect("/medicamentos")
    flask.flash("Ha habido un error al eliminar el medicamento")
    return flask.redirect("/medicamentos")

def comprobar_id_medicamento(id_medicamento):
    medicamentos_list = list(srp.load_all(MedicamentoDto))
    for medicamento in medicamentos_list:
        if str(medicamento.id) == str(id_medicamento):
            return True
    return None

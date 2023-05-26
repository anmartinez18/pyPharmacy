# routes.historial.py

from flask import Blueprint
import flask
from flask_login import login_required
import flask_login
from model.historialdto import HistorialDto
import sirope

from model.medicamentodto import MedicamentoDto

historial_bp = Blueprint("historial", __name__)
srp = sirope.Sirope()


@historial_bp.route("/historial")
@login_required
def get_view_historial():
    historial_list = list(srp.load_all(HistorialDto))
    sust = {
        "historial_list": historial_list,
    }
    return flask.render_template("index.html", **sust)


@historial_bp.route("/historial/registrar", methods=["POST"])
@login_required
def registar_ventas():
    id_medicamento = flask.request.form.get("id_medicamento")
    nombre_cliente = flask.request.form.get("nombreCliente")
    medicamento = buscar_medicamento(id_medicamento)
    id_venta = comprobar_id_venta()
    if id_venta is not None:
        if medicamento is not None:
            if int(medicamento.num_unidades) > 0:
                medicamento.vender_medicamento()
                srp.save(medicamento)
            else:
                flask.flash("No existen unidades disponibles de ese medicamento")
                return flask.redirect("/historial")
        else:
            flask.flash("No existe ese medicamento")
            return flask.redirect("/historial")
        usr = flask_login.current_user
        srp.save(
            HistorialDto(id_venta, medicamento.id, usr.nombre_completo, nombre_cliente)
        )
        return flask.redirect("/historial")
    return flask.redirect("/historial")


@historial_bp.route("/historial/eliminar", methods=["POST"])
@login_required
def eliminar_ventas():
    venta_id = flask.request.form.get("venta_id")
    if venta_id is not None and venta_id != "":
        for venta in srp.load_all(HistorialDto):
            if str(venta.id) == str(venta_id):
                oid = venta.__dict__[srp.OID_ID]
                srp.delete(oid)
                return flask.redirect("/historial")
    flask.flash("Ha habido un error al eliminar la venta")
    return flask.redirect("/historial")


def buscar_medicamento(id_medicamento_venta):
    medicamentos_list = list(srp.load_all(MedicamentoDto))
    for medicamento in medicamentos_list:
        if str(medicamento.id) == str(id_medicamento_venta):
            return medicamento
    return None


def comprobar_id_venta():
    id_venta = HistorialDto.generate_id()
    id_list = list(srp.load_all(HistorialDto))
    if id_venta not in id_list:
        return id_venta
    return None

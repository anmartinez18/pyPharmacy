$(document).ready(function () {

    $('#botonRegistrarMedicamento').click(function () {
        $('#modalRegistroMedicamento').modal('show');
    })

    $('#btnCerrarRegistroMedicamento').click(function () {
        $('#modalRegistroMedicamento').modal('hide');
    })

    $('#botonRegistrarUsuario').click(function () {
        $('#modalRegistrarUsuario').modal('show');
    })

    $('#btnCerrarRegistroUsuarios').click(function () {
        $('#modalRegistrarUsuario').modal('hide');
    })

    $('#botonRegistrarUsuarioLogin').click(function () {
        $('#modalRegistrarUsuarioLogin').modal('show');
    })

    $('#btnCerrarRegistroUsuariosLogin').click(function () {
        $('#modalRegistrarUsuarioLogin').modal('hide');
    })

    $('#botonRegistrarVenta').click(function () {
        $('#modalRegistrarVenta').modal('show');
    })

    $('#btnCerrarRegistroVentas').click(function () {
        $('#modalRegistrarVenta').modal('hide');
    })

    $("[id^='btn-editar-medicamento-']").click(function () {
        var id = $(this).data("id");
        var nombre = $(this).data("nombre");
        var categoria = $(this).data("categoria");
        var unidades = $(this).data("unidades");

        $("#modalModificarMedicamento #id_medicamento").val(id);
        $("#modalModificarMedicamento #nombreMedicamento").val(nombre);
        $("#modalModificarMedicamento #categoria").val(categoria);
        $("#modalModificarMedicamento #num_unidades").val(unidades);

        $("#modalModificarMedicamento").modal("show");
    });

    $("#btnCerrarModificarMedicamento").click(function () {
        $("#modalModificarMedicamento").modal("hide");
    })


    $("[id^='btn-editar-personal-']").click(function () {
        var username = $(this).data("username");
        var nombre = $(this).data("nombre");
        var apellidos = $(this).data("apellidos");

        $("#modalModificarPersonal #usernameMod").val(username);
        $("#modalModificarPersonal #nombreMod").val(nombre);
        $("#modalModificarPersonal #apellidosMod").val(apellidos);

        $("#modalModificarPersonal").modal("show");
    });

    $("#btnCerrarModificarPersonal").click(function () {
        $("#modalModificarPersonal").modal("hide");
    })

});

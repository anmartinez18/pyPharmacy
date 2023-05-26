from datetime import datetime as dt
import random

class HistorialDto:

    def __init__(self, id, medicamento, user, nombre_cliente):
        self._id = id
        self._id_medicamento = medicamento
        self._vendedor = user
        self._cliente = nombre_cliente
        self._fecha_venta = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    def __getattr__(self, item):
        if item == "id":
            return self._id
        elif item == "id_medicamento":
            return self._id_medicamento
        elif item == "vendedor":
            return self._vendedor
        elif item == "cliente":
            return self._cliente
        elif item == "fecha_venta":
            return self._fecha_venta

        raise AttributeError(item)

    def generate_id():
        id = random.randint(10000, 99999)
        id_str = str(id).zfill(5)
        return id_str


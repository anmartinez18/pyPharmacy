from typing import Any


class MedicamentoDto:
    def __init__(self, id, nombre, categoria, num_unidades):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        self._num_unidades = int(num_unidades)

    def __getattr__(self, item):
        if item == "id":
            return self._id
        elif item == "nombre":
            return self._nombre
        elif item == "categoria":
            return self._categoria
        elif item == "num_unidades":
            return self._num_unidades

        raise AttributeError(item)
    
    def vender_medicamento(self):
        self._set_num_unidades(self._num_unidades - 1)

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_categoria(self, categoria):
        self._categoria = categoria

    def _set_num_unidades(self, value):
        self._num_unidades = value

    

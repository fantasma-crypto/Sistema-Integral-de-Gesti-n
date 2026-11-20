"""
servicio.py - Clase abstracta que representa los servicios de Software FJ.
"""

from abc import ABC, abstractmethod
from typing import Any
import math

from entidad_base import EntidadBase
from excepciones import (
    ParametroObligatorioError,
    CalculoCostoError
)


class Servicio(EntidadBase, ABC):
    """
    Clase abstracta base para los diferentes servicios del sistema.
    """

    def __init__(
        self,
        id_servicio: str,
        nombre: str,
        costo_base: float
    ):
        # Validar identificador
        if not isinstance(id_servicio, str):
            raise ParametroObligatorioError(
                "El identificador del servicio debe ser texto."
            )

        if not id_servicio.strip():
            raise ParametroObligatorioError(
                "El identificador del servicio es obligatorio."
            )

        # Validar nombre
        if not isinstance(nombre, str):
            raise ParametroObligatorioError(
                "El nombre del servicio debe ser texto."
            )

        if not nombre.strip():
            raise ParametroObligatorioError(
                "El nombre del servicio es obligatorio."
            )

        # Validar costo base
        if (
            isinstance(costo_base, bool)
            or not isinstance(costo_base, (int, float))
            or not math.isfinite(costo_base)
            or costo_base < 0
        ):
            raise CalculoCostoError(
                "El costo base debe ser un número válido mayor o igual a cero."
            )

        self._id_servicio = id_servicio.strip()
        self._nombre = nombre.strip()
        self._costo_base = float(costo_base)

    @property
    def id_servicio(self) -> str:
        return self._id_servicio

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def costo_base(self) -> float:
        return self._costo_base

    @abstractmethod
    def calcular_costo(self, duracion: int, **kwargs) -> float:
        """
        Método abstracto para calcular el costo de cada servicio.

        Las clases hijas deben sobrescribir este método.
        """
        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, int)
            or duracion <= 0
        ):
            raise CalculoCostoError(
                "La duración debe ser un número entero mayor que cero."
            )

        return self._costo_base * duracion

    def __str__(self) -> str:
        return (
            f"Servicio ID: {self._id_servicio} | "
            f"Nombre: {self._nombre} | "
            f"Costo base: ${self._costo_base:,.2f}"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id_servicio": self._id_servicio,
            "nombre": self._nombre,
            "costo_base": self._costo_base
        }

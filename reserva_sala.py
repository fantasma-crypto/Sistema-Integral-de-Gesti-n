"""
reserva_sala.py - Servicio de reserva de salas de Software FJ.
"""

from typing import Any
import math

from servicio import Servicio
from excepciones import (
    CalculoCostoError,
    ParametroObligatorioError
)


class ReservaSala(Servicio):
    """
    Servicio para reservar salas de reuniones y eventos.
    """

    def __init__(
        self,
        id_servicio: str,
        nombre: str,
        costo_base: float,
        capacidad: int
    ):
        super().__init__(id_servicio, nombre, costo_base)

        if (
            isinstance(capacidad, bool)
            or not isinstance(capacidad, int)
            or capacidad <= 0
        ):
            raise CalculoCostoError(
                "La capacidad debe ser un número entero mayor que cero."
            )

        self._capacidad = capacidad

    @property
    def capacidad(self) -> int:
        return self._capacidad

    def calcular_costo(
        self,
        duracion: int,
        impuesto: float = 0.10,
        descuento: float = 0.0,
        personas: int = 1
    ) -> float:
        """
        Calcula el costo de la reserva de sala.
        Permite aplicar impuestos y descuentos.
        """

        # Validar duración utilizando la clase padre
        super().calcular_costo(duracion)

        # Validar cantidad de personas
        if (
            isinstance(personas, bool)
            or not isinstance(personas, int)
            or personas <= 0
        ):
            raise CalculoCostoError(
                "La cantidad de personas debe ser un entero positivo."
            )

        if personas > self._capacidad:
            raise CalculoCostoError(
                "La cantidad de personas supera la capacidad de la sala."
            )

        # Validar impuesto
        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, (int, float))
            or not math.isfinite(impuesto)
            or impuesto < 0
        ):
            raise CalculoCostoError(
                "El impuesto debe ser un número mayor o igual a cero."
            )

        # Validar descuento
        if (
            isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
            or not math.isfinite(descuento)
            or not 0 <= descuento <= 1
        ):
            raise CalculoCostoError(
                "El descuento debe estar entre 0 y 1."
            )

        costo_base = self._costo_base * duracion
        costo_con_impuesto = costo_base * (1 + impuesto)
        costo_final = costo_con_impuesto * (1 - descuento)

        return round(costo_final, 2)

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Capacidad: {self._capacidad} personas"
        )

    def to_dict(self) -> dict[str, Any]:
        datos = super().to_dict()
        datos["capacidad"] = self._capacidad
        datos["tipo"] = "Reserva de sala"

        return datos

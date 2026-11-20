"""
asesoria_especializada.py - Servicio de asesorías especializadas.
"""

from typing import Any

from servicio import Servicio
from excepciones import (
    CalculoCostoError,
    ParametroObligatorioError
)


class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesorías profesionales y especializadas.
    """

    def __init__(
        self,
        id_servicio: str,
        nombre: str,
        costo_base: float,
        tematica: str,
        duracion_maxima: int
    ):
        super().__init__(id_servicio, nombre, costo_base)

        if not isinstance(tematica, str) or not tematica.strip():
            raise ParametroObligatorioError(
                "La temática de la asesoría es obligatoria."
            )

        if (
            isinstance(duracion_maxima, bool)
            or not isinstance(duracion_maxima, int)
            or duracion_maxima <= 0
        ):
            raise CalculoCostoError(
                "La duración máxima debe ser un entero positivo."
            )

        self._tematica = tematica.strip()
        self._duracion_maxima = duracion_maxima

    @property
    def tematica(self) -> str:
        return self._tematica

    @property
    def duracion_maxima(self) -> int:
        return self._duracion_maxima

    def calcular_costo(
        self,
        duracion: int,
        preparacion: bool = False,
        material: bool = False
    ) -> float:
        """
        Calcula el costo de la asesoría.
        Permite agregar costos por preparación y material.
        """

        # Validar duración
        super().calcular_costo(duracion)

        if duracion > self._duracion_maxima:
            raise CalculoCostoError(
                f"La duración ({duracion} horas) supera "
                f"el máximo permitido de {self._duracion_maxima} horas."
            )

        if not isinstance(preparacion, bool):
            raise CalculoCostoError(
                "El parámetro preparacion debe ser verdadero o falso."
            )

        if not isinstance(material, bool):
            raise CalculoCostoError(
                "El parámetro material debe ser verdadero o falso."
            )

        costo = self._costo_base * duracion

        if preparacion:
            costo += 50000

        if material:
            costo += 30000

        return round(costo, 2)

    def __str__(self) -> str:
        return (
            f"{super().__str__()} | "
            f"Temática: {self._tematica} | "
            f"Duración máxima: {self._duracion_maxima} horas"
        )

    def to_dict(self) -> dict[str, Any]:
        datos = super().to_dict()
        datos["tematica"] = self._tematica
        datos["duracion_maxima"] = self._duracion_maxima
        datos["tipo"] = "Asesoría especializada"

        return datos

"""
entidad_base.py - Clase abstracta base para las entidades del sistema.
"""

from abc import ABC, abstractmethod
from typing import Any


class EntidadBase(ABC):
    """
    Clase abstracta que establece la estructura general
    de las entidades del sistema Software FJ.
    """

    @abstractmethod
    def __str__(self) -> str:
        """
        Devuelve una representación en texto del objeto.
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """
        Convierte los datos del objeto en un diccionario.
        """
        pass

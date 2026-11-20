"""
cliente.py - Clase que representa a un cliente del sistema Software FJ.
"""

from typing import Any
import re

from entidad_base import EntidadBase
from excepciones import (
    ClienteInvalidoError,
    ParametroObligatorioError
)


class Cliente(EntidadBase):
    """
    Representa un cliente con validaciones y atributos encapsulados.
    """

    def __init__(
        self,
        nombre: str,
        documento: str,
        contacto: str,
        cliente_id: int = None
    ):
        # Validar tipos de datos
        if not isinstance(nombre, str):
            raise ClienteInvalidoError("El nombre debe ser texto.")

        if not isinstance(documento, str):
            raise ClienteInvalidoError("El documento debe ser texto.")

        if not isinstance(contacto, str):
            raise ClienteInvalidoError("El contacto debe ser texto.")

        # Validar parámetros obligatorios
        if not nombre.strip():
            raise ParametroObligatorioError(
                "El nombre del cliente es obligatorio."
            )

        if not documento.strip():
            raise ParametroObligatorioError(
                "El documento del cliente es obligatorio."
            )

        if not contacto.strip():
            raise ParametroObligatorioError(
                "El contacto del cliente es obligatorio."
            )

        nombre_limpio = nombre.strip()
        documento_limpio = documento.strip()
        contacto_limpio = contacto.strip()

        # Validar nombre
        if len(nombre_limpio) < 2 or len(nombre_limpio) > 100:
            raise ClienteInvalidoError(
                "El nombre debe tener entre 2 y 100 caracteres."
            )

        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s'-]+", nombre_limpio):
            raise ClienteInvalidoError(
                "El nombre contiene caracteres no permitidos."
            )

        # Validar documento
        if not documento_limpio.isdigit():
            raise ClienteInvalidoError(
                "El documento debe contener únicamente números."
            )

        if not 7 <= len(documento_limpio) <= 10:
            raise ClienteInvalidoError(
                "El documento debe tener entre 7 y 10 dígitos."
            )

        # Validar correo electrónico
        patron_email = (
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        )

        if not re.fullmatch(patron_email, contacto_limpio):
            raise ClienteInvalidoError(
                "El correo electrónico no tiene un formato válido."
            )

        # Validar identificador personalizado
        if cliente_id is not None:
            if isinstance(cliente_id, bool) or not isinstance(cliente_id, int):
                raise ClienteInvalidoError(
                    "El identificador debe ser un número entero."
                )

            if cliente_id <= 0:
                raise ClienteInvalidoError(
                    "El identificador debe ser mayor que cero."
                )

            self.__id = cliente_id
        else:
            # Identificador estable entre ejecuciones
            self.__id = int(documento_limpio)

        # Guardar atributos privados
        self.__nombre = nombre_limpio
        self.__documento = documento_limpio
        self.__contacto = contacto_limpio

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def documento(self) -> str:
        return self.__documento

    @property
    def contacto(self) -> str:
        return self.__contacto

    @property
    def id(self) -> int:
        return self.__id

    def __str__(self) -> str:
        """Devuelve una representación del cliente."""
        documento_oculto = (
            "*" * (len(self.__documento) - 4)
            + self.__documento[-4:]
        )

        return (
            f"Cliente ID: {self.__id} | "
            f"Nombre: {self.__nombre} | "
            f"Documento: {documento_oculto} | "
            f"Contacto: {self.__contacto}"
        )

    def to_dict(self) -> dict[str, Any]:
        """Convierte los datos del cliente en un diccionario."""
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "documento": self.__documento,
            "contacto": self.__contacto
        }

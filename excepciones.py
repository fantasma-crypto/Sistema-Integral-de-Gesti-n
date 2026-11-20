"""
excepciones.py - Excepciones personalizadas para el sistema Software FJ.
"""


class ClienteInvalidoError(Exception):
    """Error cuando los datos de un cliente no son válidos."""
    pass


class ServicioNoDisponibleError(Exception):
    """Error cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(Exception):
    """Error cuando una reserva contiene datos incorrectos."""
    pass


class DuracionInvalidaError(Exception):
    """Error cuando la duración de una reserva no es válida."""
    pass


class ParametroObligatorioError(Exception):
    """Error cuando falta un parámetro obligatorio."""
    pass


class EstadoReservaError(Exception):
    """Error cuando se intenta realizar una transición de estado no permitida."""
    pass


class CalculoCostoError(Exception):
    """Error cuando ocurre un problema al calcular el costo de un servicio."""
    pass


class ArchivoError(Exception):
    """Error relacionado con la lectura o escritura de archivos."""
    pass

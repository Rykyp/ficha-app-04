"""Ficha técnica de una aplicación móvil antes de publicarla en la tienda."""
from typing import Final

# Añadid aquí las importaciones que necesitéis.
import sys
from decimal import Decimal, ROUND_HALF_UP

# ---------------------------------------------------------------------------
# Datos de la aplicación. Sustituid los del ejemplo APP-00 por los vuestros.
# ---------------------------------------------------------------------------
CODIGO: Final[str] = "APP-04"
NOMBRE: Final[str] = "Notas de Clase"
PAQUETE: Final[str] = "es.estudio.notasclase"
VERSION_MAYOR, VERSION_MENOR, VERSION_PARCHE = 1, 12, 3
TAMANO_APK: Final[int] = 41_943_040          # bytes
DESCARGAS: Final[int] = 5_300
PRECIO: Final[float] = 2.99                  # euros, IVA incluido
VALORACIONES: Final[int] = 300
ESTRELLAS: Final[int] = 1_125                # suma de todas las valoraciones
PERMISOS: Final[int] = 0b1000111
COLOR_ICONO: Final[int] = 0xFF6A1B9A         # ARGB

# ---------------------------------------------------------------------------
# Datos del programa. Solo hay que cambiar AUTORES.
# ---------------------------------------------------------------------------
VERSION_PROGRAMA: Final[str] = "1.0.0"
AUTORES: Final[str] = "Ricardo Palomares Viseras y Pablo Morales Gabarron"
PENDIENTE: Final[str] = "  (opción pendiente de implementar)"

# ---------------------------------------------------------------------------
# Constantes de la pareja. Todo valor fijo del programa va aquí, con nombre.
# ---------------------------------------------------------------------------
ANCHO: Final[int] = 48

BYTES_MB: Final[int] = 10**6
BYTES_MIB: Final[int] = 2**20
COMISION_TIENDA: Final[float] = 0.15

PERMISO_INTERNET: Final[int] = 0b0000001
PERMISO_NOTIFICACIONES: Final[int] = 0b0000010
PERMISO_CAMARA: Final[int] = 0b0000100
PERMISO_UBICACION: Final[int] = 0b0001000
PERMISO_CONTACTOS: Final[int] = 0b0010000
PERMISO_MICROFONO: Final[int] = 0b0100000
PERMISO_ALMACENAMIENTO: Final[int] = 0b1000000

# ---------------------------------------------------------------------------
# Funciones auxiliares de la pareja. Al menos una, usada en varias opciones.
# ---------------------------------------------------------------------------
def formatear_fila(etiqueta: str, valor: str) -> str:
    """Devuelve una cadena con la etiqueta a la izquierda y el valor a la derecha."""
    espacios = ANCHO - len(etiqueta) - len(str(valor))
    return f"{etiqueta}{' ' * espacios}{valor}"

# ---------------------------------------------------------------------------
# Las diez opciones. Sustituid el docstring y el print(PENDIENTE).
# ---------------------------------------------------------------------------
def opcion_1_identificacion() -> None:
    """Muestra código, nombre, paquete y versión de la aplicación."""
    version_texto = f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"
    
    print(formatear_fila("Código:", CODIGO))
    print(formatear_fila("Nombre:", NOMBRE))
    print(formatear_fila("Paquete:", PAQUETE))
    print(formatear_fila("Versión:", version_texto))


def opcion_2_tamano() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_3_ingresos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_4_version() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_5_permisos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_6_color() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_7_tipos() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_8_redondeo() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_9_ficha() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


def opcion_10_acerca_de() -> None:
    """[Docstring: qué hace esta opción.]"""
    print(PENDIENTE)


# ---------------------------------------------------------------------------
# Función principal y punto de entrada. Vienen hechos: no los modifiquéis.
# ---------------------------------------------------------------------------
def main() -> None:
    """Ejecuta las diez opciones, una detrás de otra."""
    print("--- Opción 1. Identificación de la app ---")
    opcion_1_identificacion()
    print("\n--- Opción 2. Tamaño del APK ---")
    opcion_2_tamano()
    print("\n--- Opción 3. Ingresos ---")
    opcion_3_ingresos()
    print("\n--- Opción 4. versionCode ---")
    opcion_4_version()
    print("\n--- Opción 5. Permisos ---")
    opcion_5_permisos()
    print("\n--- Opción 6. Color del icono ---")
    opcion_6_color()
    print("\n--- Opción 7. Tipos de datos ---")
    opcion_7_tipos()
    print("\n--- Opción 8. Redondeo de la valoración ---")
    opcion_8_redondeo()
    print("\n--- Opción 9. Ficha completa ---")
    opcion_9_ficha()
    print("\n--- Opción 10. Acerca de ---")
    opcion_10_acerca_de()


if __name__ == "__main__":
    main()
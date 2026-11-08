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
DESPLAZAMIENTO_MENOR: Final[int] = 8
DESPLAZAMIENTO_MAYOR: Final[int] = 16
MASCARA_BYTE: Final[int] = 0xFF

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
    """Calcula y muestra el tamaño del APK en Bytes, MB y MiB."""
    tamano_mb = TAMANO_APK / BYTES_MB
    tamano_mib = TAMANO_APK / BYTES_MIB
    diferencia_porc = ((tamano_mb - tamano_mib) / tamano_mb) * 100

    print(formatear_fila("Bytes:", f"{TAMANO_APK} B"))
    print(formatear_fila("En la tienda:", f"{tamano_mb:.2f} MB"))
    print(formatear_fila("En el móvil:", f"{tamano_mib:.2f} MiB"))
    print(formatear_fila("Diferencia:", f"{diferencia_porc:.1f} %"))


def opcion_3_ingresos() -> None:
    """Calcula y muestra los ingresos brutos, comisión y netos."""
    ingresos_brutos = DESCARGAS * PRECIO
    comision_calculada = ingresos_brutos * COMISION_TIENDA
    ingresos_netos = ingresos_brutos - comision_calculada

    print(formatear_fila("Descargas:", f"{DESCARGAS} uds."))
    print(formatear_fila("Precio:", f"{PRECIO:.2f} €"))
    print(formatear_fila("Ingresos brutos:", f"{ingresos_brutos:.2f} €"))
    print(formatear_fila("Comisión tienda:", f"{comision_calculada:.2f} €"))
    print(formatear_fila("Ingresos netos:", f"{ingresos_netos:.2f} €"))


def opcion_4_version() -> None:
    """Empaqueta y desempaqueta el versionCode con operadores de bit."""
    version_empaquetada = (
        (VERSION_MAYOR << DESPLAZAMIENTO_MAYOR) 
        | (VERSION_MENOR << DESPLAZAMIENTO_MENOR) 
        | VERSION_PARCHE
    )
    
    desempaquetado_mayor = (version_empaquetada >> DESPLAZAMIENTO_MAYOR) & MASCARA_BYTE
    desempaquetado_menor = (version_empaquetada >> DESPLAZAMIENTO_MENOR) & MASCARA_BYTE
    desempaquetado_parche = version_empaquetada & MASCARA_BYTE
    
    version_restaurada = f"{desempaquetado_mayor}.{desempaquetado_menor}.{desempaquetado_parche}"
    
    print(formatear_fila("Versión:", f"{VERSION_MAYOR}.{VERSION_MENOR}.{VERSION_PARCHE}"))
    print(formatear_fila("versionCode:", str(version_empaquetada)))
    print(formatear_fila("En hexadecimal:", f"0x{version_empaquetada:06X}"))
    print(formatear_fila("Desempaquetado:", version_restaurada))


def opcion_5_permisos() -> None:
    """Evalúa los permisos asignados utilizando máscaras binarias."""
    tiene_internet = (PERMISOS & PERMISO_INTERNET) != 0
    tiene_notificaciones = (PERMISOS & PERMISO_NOTIFICACIONES) != 0
    tiene_camara = (PERMISOS & PERMISO_CAMARA) != 0
    tiene_ubicacion = (PERMISOS & PERMISO_UBICACION) != 0
    tiene_contactos = (PERMISOS & PERMISO_CONTACTOS) != 0
    tiene_microfono = (PERMISOS & PERMISO_MICROFONO) != 0
    tiene_almacenamiento = (PERMISOS & PERMISO_ALMACENAMIENTO) != 0

    permisos_sin_ubicacion = PERMISOS & ~PERMISO_UBICACION
    
    print(formatear_fila("En binario:", f"{PERMISOS:07b}"))
    print(formatear_fila("Internet:", str(tiene_internet)))
    print(formatear_fila("Notificaciones:", str(tiene_notificaciones)))
    print(formatear_fila("Cámara:", str(tiene_camara)))
    print(formatear_fila("Ubicación:", str(tiene_ubicacion)))
    print(formatear_fila("Contactos:", str(tiene_contactos)))
    print(formatear_fila("Micrófono:", str(tiene_microfono)))
    print(formatear_fila("Almacenamiento:", str(tiene_almacenamiento)))
    print(formatear_fila("Sin ubicación:", f"{permisos_sin_ubicacion:07b}"))


def opcion_6_color() -> None:
    """Descompone el color ARGB en canales decimal, binario, hex y CSS."""
    # Las constantes DESPLAZAMIENTO_ROJO, VERDE y AZUL se asumen locales a esta función 
    # o reutilizan DESPLAZAMIENTO_MENOR/MAYOR que dejó tu compañero.
    canal_alfa = (COLOR_ICONO >> 24) & MASCARA_BYTE
    canal_rojo = (COLOR_ICONO >> DESPLAZAMIENTO_MAYOR) & MASCARA_BYTE
    canal_verde = (COLOR_ICONO >> DESPLAZAMIENTO_MENOR) & MASCARA_BYTE
    canal_azul = COLOR_ICONO & MASCARA_BYTE

    opacidad_porcentaje = (canal_alfa / 255) * 100
    color_css = f"#{canal_rojo:02X}{canal_verde:02X}{canal_azul:02X}"

    desglose_rojo = f"{canal_rojo:>3}  {canal_rojo:08b}  {canal_rojo:02X}"
    desglose_verde = f"{canal_verde:>3}  {canal_verde:08b}  {canal_verde:02X}"
    desglose_azul = f"{canal_azul:>3}  {canal_azul:08b}  {canal_azul:02X}"

    print(formatear_fila("ARGB:", f"0x{COLOR_ICONO:08X}"))
    print(formatear_fila("Rojo:", desglose_rojo))
    print(formatear_fila("Verde:", desglose_verde))
    print(formatear_fila("Azul:", desglose_azul))
    print(formatear_fila("Opacidad:", f"{opacidad_porcentaje:.1f}%"))
    print(formatear_fila("Para CSS:", color_css))


def opcion_7_tipos() -> None:
    """Muestra el tipo y valor de variables directas e intermedias."""
    media_valoracion = ESTRELLAS / VALORACIONES
    pide_camara = (PERMISOS & PERMISO_CAMARA) != 0
    texto_descargas = str(DESCARGAS)
    
    version_empaquetada = (
        (VERSION_MAYOR << DESPLAZAMIENTO_MAYOR) 
        | (VERSION_MENOR << DESPLAZAMIENTO_MENOR) 
        | VERSION_PARCHE
    )

    print(f"NOMBRE:          {type(NOMBRE)}  {NOMBRE}")
    print(f"DESCARGAS:       {type(DESCARGAS)}  {DESCARGAS}")
    print(f"PRECIO:          {type(PRECIO)}  {PRECIO}")
    print(f"media:           {type(media_valoracion)}  {media_valoracion:.2f}")
    print(f"pide_camara:     {type(pide_camara)}  {pide_camara}")
    print(f"texto_descargas: {type(texto_descargas)}  {texto_descargas}")
    print(f"codigo:          {type(version_empaquetada)}  {version_empaquetada}")


def opcion_8_redondeo() -> None:
    """Compara el redondeo estándar con el redondeo ROUND_HALF_UP."""
    media_exacta = ESTRELLAS / VALORACIONES
    decimal_media = Decimal(str(media_exacta))

    redondeo_python_1 = round(media_exacta, 1)
    redondeo_escolar_1 = decimal_media.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

    redondeo_python_2 = round(media_exacta, 2)
    redondeo_escolar_2 = decimal_media.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    print(formatear_fila("Valor exacto:", f"{media_exacta:.2f}"))
    print(formatear_fila("round(), 1 dec.:", f"{redondeo_python_1:.1f}"))
    print(formatear_fila("Escolar, 1 dec.:", f"{redondeo_escolar_1:.1f}"))
    print(formatear_fila("round(), 2 dec.:", f"{redondeo_python_2:.2f}"))
    print(formatear_fila("Escolar, 2 dec.:", f"{redondeo_escolar_2:.2f}"))


def opcion_9_ficha() -> None:
    """Imprime la ficha completa reutilizando las opciones anteriores."""
    linea_doble = "=" * ANCHO
    linea_simple = "-" * ANCHO
    
    # Calculamos espacios para centrar el título a mano, sin usar .center()
    titulo = "FICHA DE LA APLICACIÓN"
    espacios_titulo = (ANCHO - len(titulo)) // 2
    
    print(linea_doble)
    print(" " * espacios_titulo + titulo)
    print(linea_doble)
    
    opcion_1_identificacion()
    print(linea_simple)
    
    print("TAMAÑO DEL APK")
    opcion_2_tamano()
    print(linea_simple)
    
    print("INGRESOS")
    opcion_3_ingresos()
    print(linea_simple)
    
    print("VERSIONCODE")
    opcion_4_version()
    print(linea_doble)


def opcion_10_acerca_de() -> None:
    """Muestra la información del módulo, autores y versión de Python."""
    docstring_modulo = (__doc__ or "").strip().split('\n')[0]
    version_py = sys.version.split()[0]

    print(docstring_modulo)
    print(formatear_fila("Versión del programa:", VERSION_PROGRAMA))
    print(formatear_fila("Autores:", AUTORES))
    print(formatear_fila("Versión de Python:", version_py))


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
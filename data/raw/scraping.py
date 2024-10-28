import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


# Función para generar las URLs a partir de un rango de fechas
def generar_urls(fecha_inicio, fecha_fin):
    urls = []
    fecha_actual = fecha_inicio
    while fecha_actual <= fecha_fin:
        anio_mes = fecha_actual.strftime('%Y%m')
        urls.append(f'http://earg.fcaglp.unlp.edu.ar/meteorologia/boletin/boletin{anio_mes}.html')
        urls.append(f'http://earg.fcaglp.unlp.edu.ar/meteorologia/boletin/boletin{anio_mes}w.html')
        fecha_actual = fecha_actual.replace(
            year=fecha_actual.year + 1 if fecha_actual.month == 12 else fecha_actual.year,
            month=1 if fecha_actual.month == 12 else fecha_actual.month + 1
        )
    return urls


# Función para extraer datos de una URL
def extraer_datos(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        soup = BeautifulSoup(respuesta.content, 'html.parser')
        contenido = soup.find('pre')
        if contenido is None:
            return None
        filas = [fila.split() for fila in contenido.get_text().split('\n')[3:-4] if fila.strip()]
        return filas
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return None


def main():
    # Solicita al usuario que ingrese el año y mes de inicio y fin
    anio_inicio = int(input('Ingrese el año de inicio (YYYY): '))
    mes_inicio = int(input('Ingrese el mes de inicio (MM): '))
    anio_fin = int(input('Ingrese el año de fin (YYYY): '))
    mes_fin = int(input('Ingrese el mes de fin (MM): '))

    # Convierte las entradas de año y mes a objetos de fecha
    fecha_inicio = datetime(anio_inicio, mes_inicio, 1)
    fecha_fin = datetime(anio_fin, mes_fin, 1)
    urls = generar_urls(fecha_inicio, fecha_fin)

    datos_completos = []
    urls_procesadas = set()

    # Recorre cada URL generada
    for url in urls:
        if url in urls_procesadas:
            continue
        print(f'Procesando {url}')
        datos = extraer_datos(url)
        if datos:
            datos_completos.extend(datos)
            urls_procesadas.add(url)

    # Si se encontraron datos, los exporta a un archivo Excel
    if datos_completos:
        df = pd.DataFrame(datos_completos)
        archivo_salida = f'boletin_{anio_inicio}_{str(mes_inicio).zfill(2)}-{anio_fin}_{str(mes_fin).zfill(2)}.xlsx'
        df.to_excel(archivo_salida, index=False, header=False)
        print(f'Datos exportados a {archivo_salida}')
    else:
        print('No se encontraron datos en las URLs especificadas')


# Punto de entrada principal del script
if __name__ == '__main__':
    main()

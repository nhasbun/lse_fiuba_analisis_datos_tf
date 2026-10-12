import locale
from contextlib import contextmanager
from pathlib import Path

import pandas as pd

CARPETA = Path(__file__).resolve().parent
ARCHIVO = "Crimes_-_2015_20260905.csv"


@contextmanager
def _lc_time_c():
    original_lc_time = locale.setlocale(locale.LC_TIME, None)
    if original_lc_time != "C":
        locale.setlocale(locale.LC_TIME, "C")
    try:
        yield
    finally:
        locale.setlocale(locale.LC_TIME, original_lc_time)


def get_data(nombre_archivo: str = ARCHIVO) -> pd.DataFrame:
    ruta = CARPETA / nombre_archivo
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo en: {ruta}")

    # IUCR y FBI Code son alfanuméricos, pandas los tiene que leer como string, no ints
    df = pd.read_csv(ruta, dtype={"IUCR": str, "FBI Code": str})

    # Fechas: conversión explícita -> si el formato no coincide, falla en voz alta
    formatos = {
        "Date": "%m/%d/%Y %I:%M:%S %p",
        "Updated On": "%Y %b %d %I:%M:%S %p",
    }
    with _lc_time_c():
        for col, fmt in formatos.items():
            df[col] = pd.to_datetime(df[col], format=fmt, errors="raise")
    return df

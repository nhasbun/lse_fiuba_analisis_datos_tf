from pathlib import Path

import pandas as pd

CARPETA = Path(__file__).resolve().parent
ARCHIVO = "Crimes_-_2015_20260905.csv"

def get_data(nombre_archivo: str = ARCHIVO) -> pd.DataFrame:
    ruta = CARPETA / nombre_archivo
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo en: {ruta}")

    # IUCR y FBI Code son alfanuméricos, pandas los tiene que leer como string, no ints
    # Date y Updated On son fechas
    df = pd.read_csv(
        ruta,
        dtype={"IUCR": str, "FBI Code": str},
        parse_dates=["Date"],
        date_format="%m/%d/%Y %I:%M:%S %p",
    )
    df["Updated On"] = pd.to_datetime(
        df["Updated On"], format="%Y %b %d %I:%M:%S %p", errors="coerce"
    )
    return df
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
    return pd.read_csv(
        ruta,
        dtype={"IUCR": str, "FBI Code": str},
        parse_dates=["Date", "Updated On"],
        date_format={
            "Date": "%m/%d/%Y %I:%M:%S %p",
            "Updated On": "%Y %b %d %I:%M:%S %p",
        },
    )

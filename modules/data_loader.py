import pandas as pd
import streamlit as st
from pathlib import Path
import numpy as np

DATA_PATH = Path("dataset_final_glp.parquet")

@st.cache_data(show_spinner=False)
def cargar_datos():
    """
    Carga el dataset desde parquet.

    📌 NEGOCIO:
    Se usa parquet porque permite:
    - Mejor rendimiento
    - Menor tamaño
    - Compatible con pipelines ETL

    📌 TÉCNICO:
    - Si no existe el archivo → devuelve DataFrame vacío
    - Se implementa CACHE para mejorar rendimiento

    🆕 MEJORA:
    - Se agrega feature engineering básico
    """

    if DATA_PATH.exists():
        df = pd.read_parquet(DATA_PATH)

        # ── FEATURE ENGINEERING ─────────────────────
        # 🆕 Transformación para análisis más robusto
        df["precio_log"] = np.log(df["precio_de_venta_(soles)"].replace(0, np.nan)).fillna(0)

        return df

    return pd.DataFrame()
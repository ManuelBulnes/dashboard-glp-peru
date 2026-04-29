import pandas as pd
import streamlit as st
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "dataset_final_glp.parquet"

@st.cache_data(show_spinner=False)
def cargar_datos():

    try:

        st.write("📂 Ruta:", DATA_PATH)

        if not DATA_PATH.exists():
            st.error(f"❌ Archivo no encontrado:\n{DATA_PATH}")
            return pd.DataFrame()

        df = pd.read_parquet(DATA_PATH)

        df.columns = [
            c.strip().lower().replace(" ", "_")
            for c in df.columns
        ]

        if "precio_de_venta_(soles)" in df.columns:
            df["precio_log"] = np.log(
                df["precio_de_venta_(soles)"]
                .replace(0, np.nan)
            ).fillna(0)

        st.success(f"✅ Dataset cargado: {len(df):,} registros")

        return df

    except Exception as e:

        st.error(f"❌ Error cargando parquet:\n{e}")

        return pd.DataFrame()
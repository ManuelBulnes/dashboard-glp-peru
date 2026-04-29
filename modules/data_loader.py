import pandas as pd
import streamlit as st
from pathlib import Path
import numpy as np

# ── CONFIGURACIÓN DE RUTAS
# BASE DEL PROYECTO

BASE_DIR = Path(__file__).resolve().parents[1]

# PARQUET

DATA_PATH = BASE_DIR / "data" / "dataset_final_glp.parquet"

@st.cache_data(show_spinner=False)
def cargar_datos():

    try:

        st.write("📂 Ruta:", DATA_PATH)

        if not DATA_PATH.exists():

            st.error(f"❌ No existe:\n{DATA_PATH}")

            return pd.DataFrame()

        df = pd.read_parquet(DATA_PATH)

        df.columns = [
            c.strip().lower().replace(" ", "_")
            for c in df.columns
        ]

        return df

    except Exception as e:

        st.error(f"❌ Error cargando parquet:\n{e}")

        return pd.DataFrame()

        # LOAD
        df = pd.read_parquet(DATA_PATH)

        # NORMALIZAR COLUMNAS        
        df.columns = [
            c.strip().lower().replace(" ", "_")
            for c in df.columns
        ]

        # FIX NUMÉRICOS
        columnas_numericas = [
            "precio_de_venta_(soles)",
            "indice_demanda",
            "año",
            "mes"
        ]

        for col in columnas_numericas:

            if col in df.columns:

                df[col] = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )

        # FEATURE ENGINEERING
        if "precio_de_venta_(soles)" in df.columns:

            df["precio_log"] = np.log(
                df["precio_de_venta_(soles)"]
                .replace(0, np.nan)
            ).fillna(0)

        
        return df

    except Exception as e:
        st.error(f"❌ Error cargando parquet: {e}")
        return pd.DataFrame()
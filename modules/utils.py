import pandas as pd
def normalizar(valor, min_val, max_val):
    """
    Normaliza valores entre 0 y 1.

    📌 NEGOCIO:
    Permite comparar métricas distintas en un mismo radar.

    📌 TÉCNICO:
    Escalamiento Min-Max
    """

    if pd.isna(valor):
        return 0

    if max_val == min_val:
        return 0  # 🔥 evita división por cero

    return max(0, min(1, (valor - min_val) / (max_val - min_val)))
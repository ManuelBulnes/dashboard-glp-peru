def calcular_kpis(df):
    """
    KPIs principales del dashboard.

    📌 NEGOCIO:
    - Registros → volumen de mercado
    - Precio promedio → referencia general
    - Máximo → posible sobreprecio
    - Mínimo → competencia agresiva

    📌 TÉCNICO:
    Uso de funciones agregadas pandas

    🆕 MEJORA:
    - Protección contra dataset vacío
    """

    if df.empty:
        return {
            "registros": 0,
            "precio_promedio": 0,
            "precio_max": 0,
            "precio_min": 0
        }

    return {
        "registros": len(df),
        "precio_promedio": round(df["precio_de_venta_(soles)"].mean(), 2),
        "precio_max": round(df["precio_de_venta_(soles)"].max(), 2),
        "precio_min": round(df["precio_de_venta_(soles)"].min(), 2)
    }
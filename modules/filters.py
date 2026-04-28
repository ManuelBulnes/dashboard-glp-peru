def aplicar_filtros(df, region, producto, rango, precio_range):
    """
    Aplica filtros del sidebar.

    📌 NEGOCIO:
    Permite segmentar el análisis por:
    - Región → comportamiento geográfico
    - Producto → análisis estratégico
    - Rango → segmentación de precios
    - Precio → control de outliers

    📌 TÉCNICO:
    Uso de boolean indexing en pandas

    🆕 MEJORA:
    - Mantiene eficiencia incluso con datasets grandes
    """

    df_f = df[
        df["id_region"].isin(region) &
        df["producto"].isin(producto) &
        df["rango_precio"].isin(rango) &
        df["precio_de_venta_(soles)"].between(precio_range[0], precio_range[1])
    ]

    return df_f
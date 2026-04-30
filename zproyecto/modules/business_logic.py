def calcular_score(valores):
    """
    Calcula score estratégico del producto.

    📌 NEGOCIO:
    Evalúa competitividad considerando:
    - Precio
    - Demanda
    - Estabilidad
    - Presencia
    - Posición

    📌 DECISIÓN:
    Permite priorizar productos para inversión
    """

    w_precio = 0.25
    w_demanda = 0.25
    w_variabilidad = 0.15
    w_frecuencia = 0.15
    w_ranking = 0.20

    score = (
        w_precio * valores[0] +
        w_demanda * valores[1] +
        w_variabilidad * (1 - valores[2]) +
        w_frecuencia * valores[3] +
        w_ranking * valores[4]
    )

    return round(score * 100, 2)


def clasificar(score):
    """
    Clasifica el producto según su score.

    📌 NEGOCIO:
    Segmentación estratégica:
    - Alto → invertir
    - Medio → monitorear
    - Bajo → revisar

    """

    if score >= 70:
        return "ALTO", "green"
    elif score >= 40:
        return "MEDIO", "orange"
    return "BAJO", "red"


def recomendacion(score, precio, demanda, variabilidad):
    """
    Genera insight automático.

    📌 NEGOCIO:
    Esto es CLAVE → convierte datos en decisiones.
    """

    if score >= 70:
        return "Producto altamente competitivo"

    if demanda > 0.6 and precio < 0.5:
        return "Oportunidad de subir precio"

    if variabilidad > 0.7:
        return "Riesgo por inestabilidad"

    if score < 40:
        return "Producto débil"

    return "Producto estable"
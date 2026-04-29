arquitectura = """
🧠 ARQUITECTURA FINAL — Plataforma Analítica GLP Perú
============================================================================

📌 ENFOQUE GENERAL
------------------

Arquitectura modular orientada a:

✔ Escalabilidad
✔ Reutilización
✔ Separación de responsabilidades
✔ Compatibilidad LOCAL + WEB
✔ Integración ETL + Dashboard
✔ Analítica empresarial ligera

La solución integra:

1. Pipeline ETL automatizado
2. API REST simulada con Flask
3. Dataset analítico optimizado
4. Dashboard interactivo en Streamlit
5. Arquitectura híbrida resiliente

============================================================================
📁 ESTRUCTURA REAL DEL PROYECTO
----------------------------------------------------------------------------

PROYECTO_GLP/
│
├── app.py
│   → Aplicación principal Streamlit
│   → Orquestador general del dashboard
│
├── requirements.txt
│   → Dependencias del proyecto
│
├── README.md
│   → Documentación general
│
├── .gitignore
│   → Exclusión de archivos temporales y pesados
│
├── 📂 data/
│   └── dataset_final_glp.parquet
│       → Dataset final procesado y optimizado
│
├── 📂 modules/
│   ├── data_loader.py
│   │   → Carga híbrida parquet
│   │
│   ├── filters.py
│   │   → Aplicación de filtros dinámicos
│   │
│   ├── metrics.py
│   │   → KPIs ejecutivos
│   │
│   ├── visualizations.py
│   │   → Gráficos y visualizaciones
│   │
│   ├── business_logic.py
│   │   → Score estratégico y recomendaciones
│   │
│   ├── utils.py
│   │   → Funciones auxiliares
│   │
│   └── arquitectura.py
│       → Documentación de arquitectura
│
├── 📂 notebooks/
│   ├── costos_Peru_ver06.ipynb
│   │   → Pipeline ETL completo
│   │
│   ├── servidor_api.py
│   │   → API REST local simulada (Flask)
│   │
│   ├── *.xlsx
│   │   → Archivos auxiliares
│   │
│   └── notebooks de análisis
│
└── (Futuro)
    ├── config/
    ├── assets/
    └── models/

============================================================================
🔁 FLUJO GENERAL DEL SISTEMA
----------------------------------------------------------------------------

                 ┌───────────────────────┐
                 │ API REST (Flask)      │
                 │ servidor_api.py       │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌───────────────────────┐
                 │ Pipeline ETL          │
                 │ notebooks/*.ipynb     │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌───────────────────────┐
                 │ Dataset Parquet       │
                 │ data/                 │
                 └──────────┬────────────┘
                            │
                            ▼
                 ┌───────────────────────┐
                 │ Dashboard Streamlit   │
                 │ app.py                │
                 └───────────────────────┘

============================================================================
⚙️ CAPA 1 — API REST LOCAL (FLASK)
----------------------------------------------------------------------------

Archivo:
→ notebooks/servidor_api.py

📌 FUNCIÓN:
Simular una API REST para pruebas ETL y consumo de datos.

📌 ENDPOINTS:
✔ /api/v1/precios-glp
✔ /health

📌 TECNOLOGÍAS:
- Flask
- JSON
- Requests

📌 BENEFICIO:
Permite desacoplar la fuente de datos del dashboard.

============================================================================
📥 CAPA 2 — PIPELINE ETL AUTOMATIZADO
----------------------------------------------------------------------------

Ubicación:
→ notebooks/costos_Peru_ver06.ipynb

============================================================================
2.1 EXTRACT — INGESTA
----------------------------------------------------------------------------

✔ Consumo automático desde API REST
✔ Validación de conexión
✔ Inicio automático de servidor Flask
✔ Obtención de datos JSON

LIBRERÍAS:
- requests
- subprocess
- socket

📌 NEGOCIO:
Automatiza la captura de información energética.

============================================================================
2.2 INYECCIÓN CONTROLADA DE ERRORES
----------------------------------------------------------------------------

✔ Inserción de valores nulos
✔ Inserción de precios negativos
✔ Inserción de outliers extremos

📌 OBJETIVO:
Simular corrupción de datos para validar reglas de calidad.

📌 RESULTADO:
Permite demostrar robustez del pipeline ETL.

============================================================================
2.3 AUDITORÍA DE CALIDAD DE DATOS
----------------------------------------------------------------------------

Métricas implementadas:

✔ Completitud
✔ Unicidad
✔ Validez
✔ Consistencia
✔ Actualidad

📌 OBJETIVO:
Detectar corrupción y problemas en el dataset.

📌 RESULTADO:
Datos confiables para análisis estratégico.

============================================================================
2.4 LIMPIEZA E IMPUTACIÓN
----------------------------------------------------------------------------

PROCESOS:

✔ Imputación estadística (mediana)
✔ Manejo de valores nulos
✔ Limpieza de marcas vacías
✔ Conversión robusta de tipos
✔ Validación de reglas de negocio

TECNOLOGÍAS:
- Pandas
- NumPy
- Scikit-Learn

📌 NEGOCIO:
Garantiza calidad mínima para análisis.

============================================================================
2.5 DETECCIÓN DE OUTLIERS
----------------------------------------------------------------------------

✔ Método IQR
✔ Detección de precios extremos
✔ Validación de anomalías

📌 NEGOCIO:
Permite identificar posibles sobreprecios.

============================================================================
2.6 FEATURE ENGINEERING
----------------------------------------------------------------------------

Variables generadas:

✔ precio_log
✔ precio_norm
✔ rango_precio
✔ trimestre
✔ indice_demanda
✔ año
✔ mes

📌 NEGOCIO:
Mejora el análisis estratégico y predictivo.

============================================================================
2.7 INTEGRACIÓN DE FUENTES
----------------------------------------------------------------------------

✔ Cruce con dataset maestro
✔ Generación de regiones
✔ Índice de demanda sintético

📌 RESULTADO:
Dataset enriquecido para inteligencia de negocio.

============================================================================
2.8 LOAD — ALMACENAMIENTO
----------------------------------------------------------------------------

FORMATO:
✔ Apache Parquet

COMPRESIÓN:
✔ Snappy

OPTIMIZACIONES:
✔ Downcasting
✔ Reducción de memoria RAM
✔ Almacenamiento columnar

RUTA:
→ data/dataset_final_glp.parquet

📌 BENEFICIO:
Mayor velocidad de lectura en Streamlit.

============================================================================
📂 CAPA 3 — CARGA DE DATOS (data_loader.py)
----------------------------------------------------------------------------

FUNCIÓN PRINCIPAL:
→ cargar_datos()

============================================================================
🔄 ARQUITECTURA HÍBRIDA
----------------------------------------------------------------------------

El sistema implementa carga optimizada desde archivo Parquet:

✔ Lectura eficiente
✔ Cache de datos
✔ Normalización automática
✔ Conversión robusta de tipos

============================================================================
FLUJO DE CARGA
----------------------------------------------------------------------------

1. Verificación de existencia del parquet
2. Lectura optimizada
3. Normalización de columnas
4. Conversión de tipos numéricos
5. Creación de precio_log
6. Cache de datos

============================================================================
TECNOLOGÍAS
----------------------------------------------------------------------------

✔ pandas
✔ pathlib
✔ numpy
✔ st.cache_data

============================================================================
📌 BENEFICIOS
----------------------------------------------------------------------------

✔ Alta velocidad de lectura
✔ Compatibilidad local y cloud
✔ Menor consumo de memoria
✔ Mayor estabilidad del dashboard

============================================================================
🎛️ CAPA 4 — FILTROS DINÁMICOS
----------------------------------------------------------------------------

Archivo:
→ filters.py

FUNCIÓN:
→ aplicar_filtros()

FILTROS:

✔ Región
✔ Producto
✔ Rango de precio
✔ Slider de precio

TÉCNICA:
✔ Boolean Indexing

📌 NEGOCIO:
Segmentación dinámica del mercado.

============================================================================
📊 CAPA 5 — KPIs EJECUTIVOS
----------------------------------------------------------------------------

Archivo:
→ metrics.py

FUNCIÓN:
→ calcular_kpis()

KPIs:

✔ Registros
✔ Precio promedio
✔ Precio máximo
✔ Precio mínimo

📌 NEGOCIO:
Vista ejecutiva inmediata.

============================================================================
📈 CAPA 6 — VISUALIZACIONES
----------------------------------------------------------------------------

Archivo:
→ visualizations.py

GRÁFICOS IMPLEMENTADOS:

1. 📊 Bar Chart
   → Precio promedio por producto

2. 🥧 Pie Chart
   → Distribución por rango

3. 📍 Gráfico geográfico
   → Precio por región

4. 📈 Línea temporal
   → Tendencia de precios

5. 📦 Boxplot
   → Dispersión por marca

6. 🕸️ Radar Chart
   → Perfil estratégico

7. 📊 Scatter Plot
   → Relación precio vs demanda

8. 🔥 Heatmap
   → Correlación entre variables

TECNOLOGÍAS:
✔ Plotly Express
✔ Plotly Graph Objects

============================================================================
🧠 CAPA 7 — LÓGICA DE NEGOCIO
----------------------------------------------------------------------------

Archivo:
→ business_logic.py

FUNCIONES:

✔ normalizar()
✔ calcular_score()
✔ clasificar()
✔ recomendacion()

============================================================================
MODELO DE SCORE
----------------------------------------------------------------------------

Variables consideradas:

✔ Precio
✔ Demanda
✔ Estabilidad
✔ Frecuencia
✔ Ranking

CLASIFICACIÓN:

✔ ALTO
✔ MEDIO
✔ BAJO

📌 NEGOCIO:
Convierte datos en decisiones estratégicas.

============================================================================
🖥️ CAPA 8 — DASHBOARD STREAMLIT
----------------------------------------------------------------------------

Archivo:
→ app.py

FUNCIONES PRINCIPALES:

✔ Sidebar interactivo
✔ KPIs dinámicos
✔ Tabs analíticos
✔ Explorador de productos
✔ Correlación
✔ Radar analítico

============================================================================
SECCIONES DEL DASHBOARD
----------------------------------------------------------------------------

TABS:

✔ Arquitectura
✔ Resumen
✔ Geográfico
✔ Análisis
✔ Correlación
✔ Explorador

============================================================================
⚡ OPTIMIZACIONES IMPLEMENTADAS
----------------------------------------------------------------------------

✔ st.cache_data
✔ Sampling inteligente
✔ Manejo robusto de NaN
✔ Prevención división por cero
✔ Downcasting
✔ Reducción saturación visual
✔ Lectura optimizada parquet
✔ Conversión robusta de tipos

============================================================================
🌐 COMPATIBILIDAD DE ENTORNOS
----------------------------------------------------------------------------

✔ LOCAL:
    - Flask
    - API REST
    - Streamlit

✔ WEB:
    - GitHub
    - Streamlit Cloud
    - Lectura parquet

============================================================================
🚀 ESCALABILIDAD FUTURA
----------------------------------------------------------------------------

✔ PostgreSQL
✔ BigQuery
✔ Docker
✔ FastAPI
✔ Machine Learning
✔ Alertas automáticas
✔ Predicción de precios
✔ Clustering
✔ Mapas geográficos
✔ Integración con APIs reales

============================================================================
🎯 CONCLUSIÓN
----------------------------------------------------------------------------

La arquitectura implementada permite:

✔ Separación modular real
✔ Reutilización de componentes
✔ Integración ETL + BI
✔ Compatibilidad local y cloud
✔ Análisis estratégico automatizado
✔ Escalabilidad futura

El proyecto evoluciona de un dashboard tradicional a:

→ Una plataforma analítica orientada a soporte de decisiones.
"""
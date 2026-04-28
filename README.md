# README.md

````
# ⛽ Dashboard Analítico GLP Perú

Proyecto de Ciencia de Datos y Analítica desarrollado en Python y Streamlit para el monitoreo y análisis estratégico de precios de combustibles GLP en Perú.

---

# 📌 Objetivo

Construir una solución analítica capaz de:

- Integrar y transformar datos de combustibles.
- Aplicar validaciones y métricas de calidad.
- Generar análisis exploratorio y KPIs.
- Visualizar tendencias de precios.
- Facilitar la toma de decisiones logísticas.

---

# 🧠 Arquitectura del Proyecto

```
PROYECTO_GLP/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── dataset_final_glp.parquet
│
├── notebooks/
│   └── costos_Peru_ver06.ipynb
│
├── modules/
│   ├── business_logic.py
│   ├── data_loader.py
│   ├── filters.py
│   ├── metrics.py
│   ├── utils.py
│   └── visualizations.py
│
├── api/
│   └── servidor_api.py
````

---

# 🚀 Tecnologías Utilizadas

* Python
* Pandas
* NumPy
* Streamlit
* Plotly
* PyArrow
* Scikit-learn
* Requests
* Jupyter Notebook

---

# 📊 Funcionalidades

## ✅ Pipeline de Datos

* Ingesta automatizada de datos.
* Limpieza y transformación.
* Validación de calidad.
* Normalización.
* Exportación optimizada en formato Parquet.

## ✅ Dashboard Interactivo

* KPIs dinámicos.
* Filtros interactivos.
* Scatter plots.
* Tendencias temporales.
* Boxplots.
* Radar charts.
* Matriz de correlación.

## ✅ Análisis de Calidad

* Completitud.
* Unicidad.
* Validez.
* Consistencia.
* Actualidad.

---

# ⚙️ Instalación

## 1. Clonar repositorio

```
git clone <URL_DEL_REPOSITORIO>
cd PROYECTO_GLP
```

## 2. Crear entorno virtual

### Windows

```
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```
pip install -r requirements.txt
```

---

# ▶️ Ejecución del Proyecto

## Ejecutar Streamlit

```
streamlit run app.py
```

---

# 📁 Dataset

El dataset final procesado se almacena en:

```
data/dataset_final_glp.parquet
```

Formato optimizado:

* Apache Parquet
* Compresión Snappy
* Optimización de memoria

---

# 📈 KPIs Principales

* Precio promedio
* Precio máximo
* Precio mínimo
* Índice de demanda
* Variabilidad de precios
* Score estratégico

---

# 🛠️ Mejoras Futuras

* Integración con PostgreSQL.
* API REST con FastAPI.
* Machine Learning predictivo.
* Alertas automáticas.
* Despliegue en nube.

---

# 👨‍💻 Autor

Proyecto académico de Ciencia de Datos enfocado en:

* Ingeniería de Datos
* Analítica de Negocio
* Visualización Interactiva
* Optimización Logística

---

# 📄 Licencia

Uso académico y educativo.


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Dashboard de Encuesta", layout="wide")
st.title("📊 Dashboard de Encuesta - Análisis de Datos")

# URL del CSV en GitHub (asegúrate que sea el link 'raw')
URL_CSV = "https://raw.githubusercontent.com/usuario/repositorio/rama/nombre_del_archivo.csv"

@st.cache_data
def cargar_datos():
    df = pd.read_csv(URL_CSV)
    return df

df = cargar_datos()

# Buscar por folio
st.sidebar.header("🔎 Búsqueda por Folio")
folio = st.sidebar.text_input("Ingresa un número de folio")

if folio:
    resultado = df[df['folio'].astype(str) == folio]
    if not resultado.empty:
        st.sidebar.success("Folio encontrado")
        st.sidebar.dataframe(resultado)
    else:
        st.sidebar.warning("Folio no encontrado")

# Eliminar columna folio para análisis
df_viz = df.drop(columns=['folio'])

# Mostrar gráficos por variable
st.subheader("📈 Gráficas de Porcentaje por Variable")

for columna in df_viz.columns:
    st.markdown(f"### {columna.capitalize()}")
    
    # Calcular porcentajes
    conteo = df[columna].value_counts(normalize=True) * 100
    fig, ax = plt.subplots()
    conteo.plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_ylabel('Porcentaje (%)')
    ax.set_xlabel(columna)
    ax.set_title(f"Distribución porcentual de {columna}")
    for i, v in enumerate(conteo):
        ax.text(i, v + 1, f"{v:.1f}%", ha='center')
    st.pyplot(fig)

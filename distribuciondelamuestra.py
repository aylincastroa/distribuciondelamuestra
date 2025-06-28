import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ✅ URL RAW directa al CSV en GitHub

@st.cache_data
def cargar_datos():
    df = pd.read_csv("📊 Dashboard de Encuesta - Análisis de Datos")
    return df


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

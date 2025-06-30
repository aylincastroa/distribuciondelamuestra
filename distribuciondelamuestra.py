import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# RAW embebido
CSV_DATA = """Folio,Edad,Grado,Sexo,EDP,NSE,ZDR
1,19,1,1,0,2,0
2,19,1,1,0,1,0
3,18,1,1,0,1,0
4,19,1,1,0,1,0
5,19,1,1,0,1,0
6,18,1,0,0,1,1
7,17,1,1,0,1,1
8,18,1,0,0,1,1
9,17,1,0,0,1,1
10,17,1,1,0,1,0
"""  # 🔁 Puedes seguir agregando el resto aquí si gustas

# Cargar datos desde el texto CSV embebido
@st.cache_data
def cargar_datos():
    data = StringIO(CSV_DATA)
    df = pd.read_csv(data)
    return df

# Cargar el DataFrame
df = cargar_datos()

# Título de la app
st.title("Dashboard de distribución de variables")

# Mostrar el dataframe
st.subheader("Vista previa de los datos")
st.dataframe(df)

# Gráficas de porcentaje por variable (excepto 'Folio')
variables = ['Edad', 'Grado', 'Sexo', 'EDP', 'NSE', 'ZDR']
for var in variables:
    st.subheader(f"Distribución porcentual de {var}")
    fig, ax = plt.subplots()
    df[var].value_counts(normalize=True).sort_index().plot(kind='bar', ax=ax)
    ax.set_ylabel("Porcentaje")
    ax.set_xlabel(var)
    ax.set_title(f"{var} (% del total)")
    st.pyplot(fig)

# Búsqueda por folio
st.subheader("Buscar información por Folio")
folio = st.number_input("Introduce el número de folio:", min_value=int(df["Folio"].min()), max_value=int(df["Folio"].max()), step=1)
resultado = df[df["Folio"] == folio]

if not resultado.empty:
    st.success("Resultado encontrado:")
    st.write(resultado)
else:
    st.warning("Folio no encontrado.")

    st.pyplot(fig)

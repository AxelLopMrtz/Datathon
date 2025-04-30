import streamlit as st
import pandas as pd

# Cargar archivo limpio
df = pd.read_csv("datos_salud_adolescentes_limpio.csv")

st.title("Dashboard de Salud en Adolescentes 🧑‍⚕️📊")

# Filtros
sexo = st.selectbox("Selecciona sexo:", ["Todos"] + df["SEXO"].dropna().unique().tolist())
edad = st.slider("Edad:", int(df["EDAD"].min()), int(df["EDAD"].max()))

# Aplicar filtros
if sexo != "Todos":
    df = df[df["SEXO"] == sexo]
df = df[df["EDAD"] == edad]

# KPIs básicos
st.metric("Total registros", len(df))

# Gráfico de ejemplo
st.subheader("Distribución de P6_1 (Accidentes)")
st.bar_chart(df["P6_1"].value_counts())

# Puedes repetir esto con cualquier columna
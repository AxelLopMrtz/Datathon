import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(
    page_title="Dashboard de Salud",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Forzar tema claro y estilos
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #ffffff;
            color: #000000;
        }
        .card {
            background-color: #ffffff;
            padding: 20px;
            margin-bottom: 25px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            color: #000000;
        }
        h4 {
            font-size: 18px;
            font-weight: bold;
            color: #222222;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Cargar archivo de datos limpio
df = pd.read_csv("data/datos_salud_adolescentes_limpio.csv")

# Título principal
st.markdown("<h1 style='text-align:center;'>📊 Dashboard de Salud en Adolescentes</h1>", unsafe_allow_html=True)
st.markdown("---")

# Tarjetas de resumen
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.metric("👥 Total registros", len(df))
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.metric("📍 Estados únicos", df["ENT"].nunique())
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.metric("📊 Variables analizadas", 10)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Gráficas configuradas
graficas = [
    ("¿Tuviste algún accidente? (P6_1)", "P6_1"),
    ("¿Recibiste atención médica? (P2_38)", "P2_38"),
    ("¿Se te ofreció algún servicio de salud? (P2_31_8)", "P2_31_8"),
    ("¿Recibiste orientación médica o psicológica? (P7_19)", "P7_19"),
    ("Lugar donde recibiste atención médica (P2_40_1)", "P2_40_1"),
    ("Otro lugar de atención (P2_40_2)", "P2_40_2"),
    ("Otro lugar de atención (P2_40_3)", "P2_40_3"),
    ("Otro lugar de atención (P2_40_4)", "P2_40_4"),
    ("Otro lugar de atención (P2_40_5)", "P2_40_5"),
    ("Otro lugar de atención (P2_40_6)", "P2_40_6"),
]

# Mostrar de 3 en 3
for i in range(0, len(graficas), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(graficas):
            with cols[j]:
                titulo, columna = graficas[i + j]
                st.markdown(f"<div class='card'><h4>{titulo}</h4>", unsafe_allow_html=True)
                st.bar_chart(df[columna].value_counts())
                st.markdown("</div>", unsafe_allow_html=True)

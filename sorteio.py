import streamlit as st
import random
from pathlib import Path
import base64

# -------- CONFIGURAÇÕES --------
TITULO = "Escola Industrial - Sorteio de Cadeiras"
LOGO_PATH = "logo.png"  # Caminho para a logo
alunos = [
    "Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4",
    "Aluno 5", "Aluno 6", "Aluno 7", "Aluno 8",
    "Aluno 9", "Aluno 10", "Aluno 11", "Aluno 12",
    "Aluno 13", "Aluno 14", "Aluno 15", "Aluno 16"
]
# -------------------------------

st.set_page_config(page_title="Sorteio de Cadeiras", page_icon="🎯", layout="wide")

# Função para converter imagem para base64
def get_base64_image(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Centraliza logo
if Path(LOGO_PATH).exists():
    img_base64 = get_base64_image(LOGO_PATH)
    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{img_base64}" width="180">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Logo não encontrada. Verifique o caminho em LOGO_PATH.")

# Título centralizado
st.markdown(f"<h1 style='text-align:center;color:#222;margin-top:10px;'>{TITULO}</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# Botão centralizado e menor
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    sortear = st.button("🎲 Sortear Cadeiras")

# Resultado do sorteio
if sortear:
    sorteio = alunos.copy()
    random.shuffle(sorteio)

    for cadeira, aluno in enumerate(sorteio, start=1):
        st.markdown(
            f"""
            <div style="
                background-color:#f0f0f0;
                padding:12px 16px;
                margin-bottom:8px;
                border-radius:10px;
                display:flex;
                justify-content:space-between;
                align-items:center;
                box-shadow:0 1px 3px rgba(0,0,0,0.06);
                max-width:800px;
                margin-left:auto;
                margin-right:auto;
            ">
                <span style="font-weight:700;font-size:17px;color:#333;">Cadeira {cadeira}</span>
                <span style="font-size:17px;color:#0056b3;">{aluno}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("Clique em **🎲 Sortear Cadeiras** para gerar a distribuição.")

import streamlit as st
import random
from pathlib import Path

# -------- CONFIGURAÇÕES --------
TITULO = "Escola Industrial - Sorteio de Cadeiras"
LOGO_PATH = "logo.png"  # Caminho para a logo (na mesma pasta)
alunos = [
    "Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4",
    "Aluno 5", "Aluno 6", "Aluno 7", "Aluno 8",
    "Aluno 9", "Aluno 10", "Aluno 11", "Aluno 12",
    "Aluno 13", "Aluno 14", "Aluno 15", "Aluno 16"
]
# -------------------------------

st.set_page_config(page_title="Sorteio de Cadeiras", page_icon="🎯", layout="centered")

# LOGO CENTRALIZADA
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if Path(LOGO_PATH).exists():
        st.image(LOGO_PATH, width=160)
    else:
        st.warning("Logo não encontrada. Verifique o caminho em LOGO_PATH.")

# TÍTULO CENTRALIZADO
st.markdown(f"<h1 style='text-align:center;color:#222;margin: 0.2rem 0 0.6rem 0;'>{TITULO}</h1>", unsafe_allow_html=True)
st.markdown("---")

# BOTÃO DE SORTEIO
if st.button("🎲 Sortear Cadeiras", use_container_width=True):
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
            ">
                <span style="font-weight:700;font-size:17px;color:#333;">Cadeira {cadeira}</span>
                <span style="font-size:17px;color:#0056b3;">{aluno}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("Clique em **🎲 Sortear Cadeiras** para gerar a distribuição.")

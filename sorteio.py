import streamlit as st
import random

# -------- CONFIGURAÇÕES --------
TITULO = "Escola Industrial - Sorteio de Cadeiras"
LOGO_PATH = "logo.png"  # Caminho para a logo
alunos = [
    "Adriele Domeneghini", "Aluno 2", "Aluno 3", "Aluno 4",
    "Aluno 5", "Aluno 6", "Aluno 7", "Aluno 8",
    "Aluno 9", "Aluno 10", "Aluno 11", "Aluno 12",
    "Aluno 13", "Aluno 14", "Aluno 15", "Aluno 16"
]
# -------------------------------

# Título e logo
st.set_page_config(page_title="Sorteio de Cadeiras", page_icon="🎯", layout="centered")
st.image(LOGO_PATH, width=150)
st.markdown(f"<h1 style='text-align: center; color: #222;'>{TITULO}</h1>", unsafe_allow_html=True)
st.markdown("---")

# Botão de sorteio
if st.button("🎲 Sortear Cadeiras", use_container_width=True):
    sorteio = alunos.copy()
    random.shuffle(sorteio)

    for cadeira, aluno in enumerate(sorteio, start=1):
        st.markdown(
            f"""
            <div style='background-color: #f0f0f0; padding: 10px; margin-bottom: 5px; border-radius: 8px; display: flex; justify-content: space-between;'>
                <span style='font-weight: bold; font-size: 16px; color: #333;'>Cadeira {cadeira}</span>
                <span style='font-size: 16px; color: #0056b3;'>{aluno}</span>
            </div>
            """,
            unsafe_allow_html=True
        )


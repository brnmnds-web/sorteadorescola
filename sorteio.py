import streamlit as st
import random
from pathlib import Path
import base64

# -------- CONFIGURAÇÕES --------
TITULO = "Escola Industrial - Sorteio de Cadeiras"
LOGO_PATH = "logo.png"  # Caminho para a logo
alunos = [
    "Adriele Domeneghini", "Alexandre Pereira", "André Pompeu", "Daniel Fernandes",
    "Expedito Mota", "Fabio Melo", "Floriano Correia", "Gabriel Messias",
    "Gabriela Diógenes", "Indira Santana", "João Carlos Marques", "Milena Borges",
    "Raphael Silva", "Ricardo de Jesus", "Samya Celestino", "Sandra Lucena"
]
# -------------------------------

st.set_page_config(page_title="Sorteio de Cadeiras", page_icon="🎯", layout="wide")

# Função para converter imagem para base64
def get_base64_image(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# CSS para estilizar os elementos, incluindo o fundo da página
st.markdown("""
<style>
    /* Altera a cor de fundo do corpo da página */
    body {
        background-color: #09124F;
    }
    
    .stApp {
        background-color: #09124F;
    }
    
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stMarkdown h1 {
        text-align: center;
        color: #fff; /* Altera a cor do texto para branco para contraste */
        margin-top: 10px;
    }
    .centered-logo {
        text-align: center;
    }
    /* Estilo para o texto do st.info */
    .st-emotion-cache-1218f60 { /* Seletor específico para o st.info */
        color: #fff;
    }
</style>
""", unsafe_allow_html=True)

# Centraliza logo
if Path(LOGO_PATH).exists():
    img_base64 = get_base64_image(LOGO_PATH)
    st.markdown(
        f"""
        <div class="centered-logo">
            <img src="data:image/png;base64,{img_base64}" width="180">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Logo não encontrada. Verifique o caminho em LOGO_PATH.")

# Título centralizado
st.markdown(f"<h1>{TITULO}</h1>", unsafe_allow_html=True)

# ---
# Linha branca estilizada com HTML e st.markdown
st.markdown(
    """
    <hr style="
        border-top: 2px solid #fff;
        border-radius: 5px;
        margin-top: 20px;
        margin-bottom: 20px;
    ">
    """,
    unsafe_allow_html=True
)
# ---

# Centraliza o botão usando st.columns
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🎲 Sortear Cadeiras", use_container_width=True):
        # Resultado do sorteio
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


#  nova ideia usar apis publicas no quiz, primeiro:
# começo, bibliotecas
# =========================
# 1️⃣ Importação das bibliotecas
# =========================
# Streamlit para interface web
# datetime para exibir a data atual
# plotly.express para gráficos interativos (resultado do quiz)
# requests para integrar a API do Zelda
import streamlit as st       # Biblioteca principal para criar a interface web
import datetime as dt        # Permite manipular datas, usada para exibir a data atual
import plotly.express as px  # Biblioteca para criar gráficos interativos (usada para resultados do quiz)
import requests              # Biblioteca para fazer requisições a APIs externas (Zelda)
# =========================
# 7️⃣ Exibição centralizada do card do jogo
# =========================
# Usamos st.columns para centralizar horizontalmente
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(info['imagem'], width=200)  # Imagem do jogo
        st.markdown(f"## {game}")  # Nome do jogo
        st.markdown(f"**Gênero:** {info['genero']}")  # Gênero
        st.markdown(f"**Lançamento:** {info['lancamento']}")  # Ano de lançamento
        st.markdown(f"[🔗 Página oficial]({info['link']})")  # Link oficial
        st.markdown("### 📝 Destaques")
        st.write(info.get("detalhes", "Detalhes não disponíveis."))  # Detalhes do jogo
        st.markdown("### ✨ Curiosidades")
        for c in info["curiosidades"]:  # Lista todas as curiosidades
            st.write(f"- {c}")
# O Markdown é uma linguagem de marcação simples que o Streamlit interpreta para formatar texto. Ele é
# usado para títulos, listas, links, negrito, itálico e separadores. No seu projeto, o Markdown é usado em várias partes:
#  esse foi o código da ideia inicial, porém estava bem simples e não estava consumindo api nenhuma
import streamlit as st
import datetime as dt

st.set_page_config(page_title="Games Hub • Infos & Curiosidades", page_icon="🎮")

st.title("🎮 Games Hub: Infos & Curiosidades")
st.caption(f"Data: {dt.date.today():%d/%m/%Y}")
st.write("Selecione um jogo para ver informações, datas marcantes e curiosidades.")

games = {
    "Minecraft": {
        "lancamento": "2009",
        "genero": "Sandbox / Criativo",
        "curiosidades": [
            "Criado por Markus 'Notch' Persson.",
            "Mundos praticamente infinitos via geração procedural.",
            "Um dos jogos mais vendidos da história.",
        ],
    },
    "The Legend of Zelda: Breath of the Wild": {
        "lancamento": "2017",
        "genero": "Aventura / Mundo aberto",
        "curiosidades": [
            "Exploração não linear revolucionou a série.",
            "Física e clima afetam a jogabilidade.",
            "Vencedor de múltiplos prêmios de Jogo do Ano.",
        ],
    },
    "Fortnite": {
        "lancamento": "2017",
        "generro": "Battle Royale",
        "curiosidades": [
            "Eventos ao vivo dentro do jogo.",
            "Crossplay entre várias plataformas.",
            "Temporadas mudam mapa e gameplay.",
        ],
    },
    "Roblox": {
        "lancamento": "2006",
        "genero": "Plataforma / UGC",
        "curiosidades": [
            "Usuários criam experiências e jogos.",
            "Economia interna com itens da comunidade.",
            "Muito usado para aprender lógica e game design.",
        ],
    },
}

st.sidebar.header("Filtro")
game = st.sidebar.selectbox("Escolha um jogo", list(games.keys()))
mostrar_curiosidades = st.sidebar.checkbox("Mostrar curiosidades", True)
mostrar_detalhes = st.sidebar.checkbox("Mostrar detalhes", True)

info = games[game]
st.subheader(f"🕹️ {game}")
st.write(f"- Gênero: {info.get('genero', 'N/D')}")
st.write(f"- Lançamento: {info['lancamento']}")

if mostrar_detalhes:
    st.markdown("### Destaques")
    detalhes = {
        "Minecraft": "Exploração e construção em mundos gerados por algoritmo.",
        "The Legend of Zelda: Breath of the Wild": "Mundo aberto com física integrada e puzzles variados.",
        "Fortnite": "Batalhas de 100 jogadores, construção e eventos sazonais.",
        "Roblox": "Plataforma UGC com inúmeras modalidades criadas pela comunidade.",
    }
    st.write(detalhes.get(game, "Detalhes não disponíveis."))

if mostrar_curiosidades:
    st.markdown("### Curiosidades")
    for c in info["curiosidades"]:
        st.write(f"- {c}")

st.markdown("### Linha do tempo (anotações)")
data_ref = st.date_input("Escolha uma data", value=dt.date.today())
nota = st.text_input("Anote algo sobre o jogo nesta data")
if st.button("Salvar anotação"):
    st.success(f"Anotação salva para {data_ref:%d/%m/%Y}: {nota}")

st.markdown("---")
st.caption("Exemplo em Streamlit. Edite o dicionário 'games' para adicionar mais títulos e curiosidades.")
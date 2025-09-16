# =========================
# 1️⃣ Importação das bibliotecas
# =========================
import streamlit as st
import datetime as dt
import plotly.express as px
import requests

# =========================
# 2️⃣ Configuração da página
# =========================
st.set_page_config(
    page_title="Games Hub • Infos & Curiosidades",
    page_icon="🎮",
    layout="centered"
)

# =========================
# 3️⃣ Base de dados dos jogos
# =========================
def get_games_data():
    return {
        "Minecraft": {
            "lancamento": "2009",
            "genero": "Mundo aberto / Criativo",
            "curiosidades": [
                "Criado por Markus 'Notch' Persson.",
                "Mundos praticamente infinitos via geração procedural.",
                "Um dos jogos mais vendidos da história.",
            ],
            "detalhes": "Exploração e construção em mundos gerados por algoritmo.",
            "imagem": "https://i.pinimg.com/736x/5f/f0/e9/5ff0e997a4a8ba449056ed679660f4cc.jpg",
            "link": "https://clickjogos.com.br/minecraft/minecraft-oficial"
        },
        "The Legend of Zelda: Breath of the Wild": {
            "lancamento": "2017",
            "genero": "Aventura / Mundo aberto",
            "curiosidades": [
                "Exploração não linear revolucionou a série.",
                "Física e clima afetam a jogabilidade.",
                "Vencedor de múltiplos prêmios de Jogo do Ano.",
            ],
            "detalhes": "Mundo aberto com física integrada e puzzles variados.",
            "imagem": "https://i.pinimg.com/1200x/31/59/2d/31592dd53c1d4976a8d5cadfd3fd07c5.jpg",
            "link": "https://www.nintendo.com/pt-br/store/products/the-legend-of-zelda-breath-of-the-wild-switch/"
        },
        "Fortnite": {
            "lancamento": "2017",
            "genero": "Battle Royale",
            "curiosidades": [
                "Eventos ao vivo dentro do jogo.",
                "Crossplay entre várias plataformas.",
                "Temporadas mudam mapa e gameplay.",
            ],
            "detalhes": "Batalhas de 100 jogadores, construção e eventos sazonais.",
            "imagem": "https://i.pinimg.com/736x/7e/e8/c4/7ee8c4361736ed806711ae99f7d6762c.jpg",
            "link": "https://www.fortnite.com/"
        },
        "Roblox": {
            "lancamento": "2006",
            "genero": "Plataforma / UGC",
            "curiosidades": [
                "Usuários criam experiências e jogos.",
                "Economia interna com itens da comunidade.",
                "Muito usado para aprender lógica e game design.",
            ],
            "detalhes": "Plataforma UGC com inúmeras modalidades criadas pela comunidade.",
            "imagem": "https://i.pinimg.com/736x/a6/8c/0b/a68c0bc57047b77fa9c25cb0a9a0cebb.jpg",
            "link": "https://www.roblox.com/"
        }
    }

# =========================
# 4️⃣ Função para integrar API do Zelda
# =========================
def fetch_zelda_curiosities(info):
    try:
        url_monsters = "https://botw-compendium.herokuapp.com/api/v2/category/monsters"
        data_monsters = requests.get(url_monsters).json()
        monstros_exemplo = [m['name'] for m in data_monsters['data'][:5]]
        info["curiosidades"].extend([f"Monstro no jogo: {m}" for m in monstros_exemplo])

        url_weapons = "https://botw-compendium.herokuapp.com/api/v2/category/equipment"
        data_weapons = requests.get(url_weapons).json()
        armas_exemplo = [w['name'] for w in data_weapons['data'][:5]]
        info["curiosidades"].extend([f"Arma famosa: {a}" for a in armas_exemplo])

    except Exception as e:
        st.warning("Não foi possível carregar informações adicionais do Zelda.")
        print(e)

# =========================
# 5️⃣ Função para exibir o card do jogo
# =========================
def display_game_card(info, game_name):
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(info['imagem'], width=200)
            st.markdown(f"## {game_name}")
            st.markdown(f"**Gênero:** {info['genero']}")
            st.markdown(f"**Lançamento:** {info['lancamento']}")
            st.markdown(f"[🔗 Página oficial]({info['link']})")
            st.markdown("### 📝 Destaques")
            st.write(info.get("detalhes", "Detalhes não disponíveis."))
            st.markdown("### ✨ Curiosidades")
            for c in info["curiosidades"]:
                st.write(f"- {c}")

# =========================
# 6️⃣ Função para exibir o quiz
# =========================
def display_quiz():
    st.markdown("---")
    st.markdown("### ❓ Quiz de Games (10 Perguntas)")
    quiz = [
        {"pergunta": "Qual jogo foi lançado primeiro?", "opcoes": ["Minecraft", "Fortnite", "Zelda BOTW", "Roblox"], "correta": "Roblox"},
        {"pergunta": "Qual jogo é exclusivo da Nintendo?", "opcoes": ["Fortnite", "Minecraft", "Zelda BOTW", "Roblox"], "correta": "Zelda BOTW"},
        {"pergunta": "Qual desses jogos tem 'mundos infinitos'?", "opcoes": ["Roblox", "Minecraft", "Fortnite"], "correta": "Minecraft"},
        {"pergunta": "Qual é um Battle Royale?", "opcoes": ["Minecraft", "Zelda BOTW", "Fortnite"], "correta": "Fortnite"},
        {"pergunta": "Qual jogo permite criar experiências próprias?", "opcoes": ["Roblox", "Zelda BOTW", "Fortnite"], "correta": "Roblox"},
        {"pergunta": "Quem criou o Minecraft?", "opcoes": ["Markus 'Notch' Persson", "Shigeru Miyamoto", "Epic Games"], "correta": "Markus 'Notch' Persson"},
        {"pergunta": "Qual jogo tem física e clima afetando a jogabilidade?", "opcoes": ["Fortnite", "Zelda BOTW", "Roblox"], "correta": "Zelda BOTW"},
        {"pergunta": "Qual desses é considerado um dos jogos mais vendidos da história?", "opcoes": ["Minecraft", "Fortnite", "Roblox"], "correta": "Minecraft"},
        {"pergunta": "Qual desses jogos tem temporadas que mudam o mapa?", "opcoes": ["Fortnite", "Roblox", "Zelda BOTW"], "correta": "Fortnite"},
        {"pergunta": "Qual jogo saiu em 2006?", "opcoes": ["Roblox", "Minecraft", "Zelda BOTW"], "correta": "Roblox"},
    ]

    if "respostas" not in st.session_state:
        st.session_state.respostas = {}

    for i, q in enumerate(quiz, 1):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            resposta = st.radio(f"Q{i}. {q['pergunta']}", q["opcoes"], key=f"q{i}")
            st.session_state.respostas[f"q{i}"] = resposta

    if st.button("📊 Finalizar Quiz"):
        score = 0
        resultados_detalhados = []
        for i, q in enumerate(quiz, 1):
            resposta = st.session_state.respostas[f"q{i}"]
            correta = q["correta"]
            if resposta == correta:
                score += 1
                resultados_detalhados.append(f"✅ Q{i}. {q['pergunta']} — Você respondeu **{resposta}** (Correto)")
            else:
                resultados_detalhados.append(f"❌ Q{i}. {q['pergunta']} — Você respondeu **{resposta}**, mas o certo é **{correta}**")

        st.success(f"Você acertou {score} de {len(quiz)} perguntas! 🎉")
        st.progress(score / len(quiz))

        resultados = {"Acertos": score, "Erros": len(quiz) - score}
        fig = px.pie(
            names=list(resultados.keys()),
            values=list(resultados.values()),
            color=list(resultados.keys()),
            color_discrete_map={"Acertos": "green", "Erros": "red"},
            title="Resultado do Quiz"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 📋 Resultado detalhado")
        for r in resultados_detalhados:
            st.write(r)

# =========================
# 7️⃣ Função principal do app
# =========================
def main():
    st.title("🎮 Games Hub: Infos & Curiosidades")
    st.caption(f"Data: {dt.date.today():%d/%m/%Y}")
    st.write("Selecione um jogo para ver informações, destaques e curiosidades.")

    games = get_games_data()

    # Sidebar para seleção do jogo
    st.sidebar.header("Escolha um jogo")
    game = st.sidebar.selectbox("🎮 Jogos disponíveis", list(games.keys()))
    info = games[game]

    # API do Zelda
    if game == "The Legend of Zelda: Breath of the Wild":
        fetch_zelda_curiosities(info)

    # Exibir card do jogo
    display_game_card(info, game)

    # Exibir quiz
    display_quiz()

    # Rodapé
    st.markdown("---")
    st.caption("Games Hub em Streamlit — Quiz com pontuação, gráfico e feedback detalhado 🎮✨")

# =========================
# 8️⃣ Executa o app
# =========================
if __name__ == "__main__":
    main()
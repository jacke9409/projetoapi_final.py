# =========================
# 6️⃣ Integração com API do Zelda (somente para BOTW)
# =========================
if game == "The Legend of Zelda: Breath of the Wild":
    try:
        # 🔹 Buscar monstros
        url_monsters = "https://botw-compendium.herokuapp.com/api/v2/category/monsters"
        response_monsters = requests.get(url_monsters)
        data_monsters = response_monsters.json()
        monstros_exemplo = [monster['name'] for monster in data_monsters['data'][:5]]
        info["curiosidades"].extend([f"Monstro no jogo: {m}" for m in monstros_exemplo])

        # 🔹 Buscar armas/equipamentos
        url_weapons = "https://botw-compendium.herokuapp.com/api/v2/category/equipment"
        response_weapons = requests.get(url_weapons)
        data_weapons = response_weapons.json()
        armas_exemplo = [weapon['name'] for weapon in data_weapons['data'][:5]]
        info["curiosidades"].extend([f"Arma famosa: {a}" for a in armas_exemplo])

    except Exception as e:
        st.warning("Não foi possível carregar informações adicionais do Zelda.")
        print(e)
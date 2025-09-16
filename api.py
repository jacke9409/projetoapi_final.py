# =========================
# 9️⃣ Finalizar o quiz e mostrar resultados
# =========================
# Botão para finalizar o quiz
if st.button("📊 Finalizar Quiz"):
    score = 0  # Contador de acertos
    resultados_detalhados = []  # Lista para armazenar feedback detalhado de cada questão
    # Loop pelas perguntas usando enumerate para obter índice e pergunta
    for i, q in enumerate(quiz, 1):  # 'i' é o número da pergunta (começando em 1), 'q' é o dicionário da pergunta
        resposta = st.session_state.respostas[f"q{i}"]  # Recupera a resposta do usuário da sessão
        correta = q["correta"]  # Obtém a resposta correta da pergunta

        # Verifica se a resposta do usuário está correta
        if resposta == correta:
            score += 1  # Incrementa o contador de acertos
            # Adiciona feedback detalhado indicando que o usuário acertou
            resultados_detalhados.append(
                f"✅ Q{i}. {q['pergunta']} — Você respondeu **{resposta}** (Correto)"
            )
        else:
            # Adiciona feedback detalhado indicando que o usuário errou e mostra a resposta correta
            resultados_detalhados.append(
                f"❌ Q{i}. {q['pergunta']} — Você respondeu **{resposta}**, mas o certo é **{correta}**"
            )
    # Exibe mensagem de sucesso com a pontuação final
    st.success(f"Você acertou {score} de {len(quiz)} perguntas! 🎉")
    # Mostra uma barra de progresso proporcional à quantidade de acertos
    st.progress(score / len(quiz))
    # Cria um gráfico de pizza para mostrar visualmente acertos e erros
    resultados = {"Acertos": score, "Erros": len(quiz) - score}
    fig = px.pie(
        names=list(resultados.keys()),          # "Acertos" e "Erros"
        values=list(resultados.values()),       # Valores correspondentes
        color=list(resultados.keys()),          # Define cores baseadas nas categorias
        color_discrete_map={"Acertos": "green", "Erros": "red"},  # Mapeia cores
        title="Resultado do Quiz"               # Título do gráfico
    )
    st.plotly_chart(fig, use_container_width=True)  # Mostra o gráfico no app
    # Exibe lista detalhada de respostas com acertos e erros
    st.markdown("### 📋 Resultado detalhado")
    for r in resultados_detalhados:
        st.write(r)  # Escreve cada feedback de pergunta na tela
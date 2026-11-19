# Ajuste da aba de parâmetros de earn

Mensagem para colar na ferramenta que está construindo a pasta de trabalho.

---

A aba "Parâmetros Earn" precisa ser refeita. Hoje ela tem cinco linhas genéricas por alavanca (Ligada, Piso ou gatilho, Passo, Fichas por bloco, Teto), iguais para todas, e isso não reflete como cada alavanca funciona. Refaça assim:

1. **Duas abas com o mesmo layout:** `Earn Referência`, travada, e `Earn Simulado`, editável. Nada de Referência e Simulado como colunas da mesma tabela.

2. **Uma linha por alavanca.** Colunas: momento da jornada, alavanca, medida do cliente e unidade, ligada (sim ou não), mecânica (lista), campos da mecânica, máximo de fichas da alavanca (calculado), observação.

3. **Três mecânicas, e cada alavanca mostra só os campos da sua:**
   - *Tem ou não tem:* valor mínimo (quando houver) e fichas.
   - *A cada valor:* a partir de, a cada, fichas por bloco, teto de fichas.
   - *Por faixas:* tabela separada, logo abaixo, em formato longo (alavanca, faixa, de, até, fichas), com até seis faixas por alavanca; faixas em branco são ignoradas.

   Campos que não pertencem à mecânica escolhida ficam esmaecidos e fora do cálculo.

4. **Rótulos:** não use "passo" nem "piso ou gatilho". Use "a cada", "a partir de" e "valor mínimo".

5. **Configuração inicial:**
   - Tem ou não tem: Open Finance (1 ficha); Planejamento financeiro, PFM 3.0 e Seguro Conta e Cartão (desligadas, fichas a definir); Previdência (valor mínimo R$ 100, 1 ficha); Boletos (valor mínimo R$ 5.000, 2 fichas); Seguro de vida (valor mínimo de PA R$ 100, 5 fichas).
   - A cada valor: AUC (Referência a partir de R$ 0, Simulado a partir de R$ 30.000; a cada R$ 5.000, 1 ficha, teto 10); TPV (a cada R$ 500, 1 ficha, teto 15); Câmbio, pelo valor da remessa (desligada na Referência; no Simulado, a cada US$ 2.000, 1 ficha, teto 10); Crédito, pelo valor do crédito, e Consórcio, pelo valor da carta (a cada R$ 10.000, 1 ficha, teto 20).
   - Por faixas: Aporte recorrente, pelo valor aportado no mês (faixa inicial: qualquer valor acima de zero vale 5 fichas; deixe faixas em branco para preencher depois); Salário portado (até R$ 5.000: 0; acima de R$ 5.000 até R$ 10.000: 2; acima de R$ 10.000: 5).

6. **Cálculo:** para cada alavanca, três colunas auxiliares, uma por mecânica, e uma quarta que escolhe o resultado conforme a mecânica selecionada e zera quando a alavanca está desligada. Trocar a mecânica na lista não pode exigir mexer em fórmula.

7. **Na aba Earn Simulado:** coluna "Difere da Referência" e o valor inicial ao lado de cada entrada.

8. **Verificações:** faixas sem sobreposição nem lacuna; máximo de fichas da régua igual à soma dos máximos das alavancas ligadas.

9. **Nova aba `Calibração do Earn`:** por alavanca, com a base de outubro: contas que pontuam, fichas médias, participação no total de fichas, esforço do cliente por ficha, margem de contribuição estimada (entrada pendente) e fichas por R$ de margem.

Mantenha os padrões de template: sem células mescladas, entradas em amarelo-claro com fonte azul, uma fórmula por linha.

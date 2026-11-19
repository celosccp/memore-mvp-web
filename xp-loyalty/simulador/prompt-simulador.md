# Prompt revisado · Simulador de Loyalty Digital (Jornada XP)

> Revisão do prompt original, alinhada às decisões tomadas no protótipo da experiência.
> Trechos marcados com **[a confirmar]** são hipóteses que nasceram no protótipo, com números ilustrativos,
> e precisam de validação antes de virarem regra do modelo.

---

Crie uma nova pasta de trabalho para um simulador de Loyalty Digital da XP. Esta mensagem contém o contexto e os requisitos necessários para começar. Vou fornecer uma base agregada de outubro e, quando disponíveis, as premissas de custo dos benefícios.

O arquivo precisa ser rápido, auditável e fácil de ajustar durante uma reunião. Construa por etapas e valide cada uma antes de acrescentar a próxima.

## Vocabulário

O programa tem o nome de trabalho **Jornada XP**. A moeda do programa se chama **fichas** (nome provisório). Use "fichas" em toda a pasta para a moeda do Loyalty e reserve "pontos" para os pontos de recompensa do cartão, por US$. Assim as duas coisas nunca se confundem.

O cliente **junta** fichas com o que faz na XP (earn) e **usa** fichas para ativar benefícios (burn). Fichas em uso ficam travadas enquanto o benefício está ativo e voltam ao saldo quando ele é desativado. O produto antes chamado Cofrinho passa a se chamar **Cofre XP**.

## Objetivo do modelo

Quero editar as regras de geração de fichas (earn) e os preços em fichas dos benefícios (burn). O modelo deve mostrar:

* Quantas fichas um perfil de cliente junta na Referência e no Simulado.
* Qual é o máximo de fichas possível em cada régua (soma dos tetos das alavancas ligadas).
* Como a população de outubro se distribui por faixa de fichas.
* Quais benefícios ficam ao alcance dessa população.
* Quanto o programa pode custar sob diferentes hipóteses de adesão e escolha.
* Quanto relacionamento adicional precisaria ser gerado para cobrir o custo incremental.

O perímetro inicial é XP B2C e XP B2B. Rico fica fora desta versão. Os resultados devem permitir abertura por canal e arquétipo.

## Diretrizes de desempenho e construção

Use fórmulas curtas e divida as contas em colunas auxiliares com nomes claros. Por exemplo, para AUC, calcule em etapas a parcela acima do piso, os blocos completos, as fichas brutas e as fichas após o teto.

Calcule cada resultado intermediário uma vez e reutilize a célula ou coluna. Evite repetir buscas de parâmetros dentro de várias fórmulas. Traga os parâmetros para uma área de apoio e use referências absolutas.

Use tabelas e intervalos limitados às linhas existentes. Evite referências a colunas inteiras, fórmulas matriciais extensas, funções voláteis como INDIRETO e DESLOC e cadeias longas de condições. Evite vínculos externos e dependências circulares. Use validação de dados para escolhas.

Reserve formatação condicional para o painel e indicadores de erro. Nas bases, mantenha formatação simples. Use poucos gráficos, alimentados por tabelas-resumo pequenas.

Para consolidar resultados, avalie tabelas dinâmicas onde forem adequadas. Indique quando exigirem atualização. Os controles principais de cenário devem recalcular os resultados que dependem deles de forma compreensível.

Antes de replicar fórmulas na base completa, valide o fluxo com um pequeno conjunto de linhas. Depois aplique à população inteira. Ao concluir cada etapa, registre os testes que passaram e os dados ainda pendentes.

## Padrões de template e design

Siga as práticas dos padrões de modelagem mais usados (FAST Standard e Financial Modelling Code do ICAEW). Aplique o mesmo padrão em todas as abas, desde a primeira etapa, para que qualquer pessoa entenda o arquivo sem explicação.

**Tipos de célula, sempre distinguíveis**

Marque o tipo com preenchimento, e não só com a cor da fonte, para funcionar em projetor e para quem não distingue cores.

| Tipo | Aparência | Uso |
| --- | --- | --- |
| Entrada editável | Preenchimento amarelo-claro, fonte azul | Parâmetros e premissas que a pessoa pode mudar |
| Fórmula | Sem preenchimento, fonte preta | Todo cálculo |
| Vínculo de outra aba | Sem preenchimento, fonte verde | Valor trazido sem transformação |
| Dado importado | Preenchimento cinza-claro | Base de outubro e conferências do Databricks |
| Premissa pendente | Preenchimento laranja-claro e a palavra "Pendente" na coluna de status | Valor provisório ou a confirmar |
| Verificação | Verde quando passa, vermelho quando falha | Células de teste e reconciliação |

Coloque a legenda desses tipos na aba Instruções. Use no máximo seis a oito cores no arquivo inteiro. Dê às guias a cor do seu tipo: entradas, cálculos, saídas e testes.

**Entradas**

* Cada entrada existe em um único lugar. Todo cálculo que precisa dela aponta para essa célula.
* Nenhum número digitado dentro de fórmula. Pisos, passos, tetos, preços e percentuais ficam sempre em células de entrada.
* Cada entrada tem, na mesma linha: rótulo, unidade, valor, valor inicial de referência, fonte, data e status (confirmado ou pendente).
* Use validação de dados em toda entrada: lista para escolhas, limites mínimo e máximo para números, com mensagem de entrada explicando o que se espera.
* Reúna os controles de cenário em um bloco só, no topo da aba de parâmetros, e repita o estado atual deles no topo do painel, por vínculo.
* Proteja as abas deixando desbloqueadas apenas as células de entrada, sem senha.

**Layout**

* Nenhuma célula mesclada. Para centralizar um título sobre várias colunas, use "Centralizar na seleção".
* Mesma estrutura de colunas em todas as abas de cálculo: rótulo, unidade, observação e depois os valores, sempre nas mesmas posições.
* Uma fórmula por linha: a mesma fórmula do início ao fim do bloco, sem exceções no meio. Se uma coluna precisar de regra diferente, crie outra linha.
* O cálculo flui de cima para baixo e da esquerda para a direita; as abas seguem a ordem entradas, cálculos, saídas, testes.
* Nada de linhas ou colunas ocultas. Para recolher detalhe, use agrupamento, que deixa visível que há algo ali.
* Sem linhas ou colunas em branco dentro de tabelas. Cabeçalho em uma única linha, com nomes únicos e sem quebra de linha.
* Congele painéis em cabeçalhos e rótulos. Deixe o cursor em A1 e o mesmo zoom em todas as abas ao salvar.
* Linhas de grade desligadas no painel e nas abas de entrada; ligadas nas bases.

**Fórmulas**

* Curtas o bastante para serem lidas de uma vez. Se precisar rolar a barra de fórmulas, quebre em etapas.
* Evite SE aninhado em mais de dois níveis; prefira tabela de faixas com busca.
* Para buscas, use PROCX ou ÍNDICE com CORRESP, nunca PROCV com número de coluna fixo.
* Não esconda erros com SEERRO genérico. Trate só o caso esperado e deixe os demais aparecerem.
* Prefira referências diretas a células. Use nomes definidos apenas para os controles de cenário, liste-os na aba Instruções e não crie nomes para intervalos de cálculo.
* Adote uma convenção de sinal e registre-a: custos e fichas em uso como valores positivos, com o rótulo dizendo o que é.

**Formatos de número**

* Fichas como inteiros. Reais sem centavos nos agregados e com centavos só em valores por conta. Percentuais com uma casa decimal.
* Separador de milhar sempre. Zero exibido como traço. Negativos com sinal de menos e em vermelho.
* A unidade vai na coluna de unidade ou no cabeçalho, nunca digitada junto do número. Nenhum número guardado como texto.

**Tabelas e bases**

* Importe as bases como Tabelas do Excel com nomes claros, por exemplo `tbBaseB2C` e `tbBaseB2B`, sem linha de total dentro da tabela.
* Não altere os dados importados. Toda correção ou classificação entra em colunas auxiliares ao lado, identificadas como cálculo.

**Verificações visíveis**

* Cada teste da aba Testes devolve 1 quando passa e 0 quando falha, com a descrição ao lado.
* Uma célula de verificação geral soma as falhas. Mostre o resultado dela no topo de todas as abas, como "OK" ou "ERRO", para que um problema nunca passe despercebido.
* Inclua verificações estruturais: nenhuma célula mesclada, nenhuma célula com erro, nenhum vínculo externo, totais da população reconciliados.

**Documentação dentro do arquivo**

A aba Instruções traz: objetivo do modelo, como usar em três ou quatro passos, legenda de cores, lista das abas com o que cada uma faz, nomes definidos, convenções de sinal e unidade, versão, data, autor, registro de mudanças, pendências e limitações conhecidas.

**Painel**

Poucos gráficos, cada um com título que diz a conclusão, eixos rotulados e a fonte dos dados. Sem efeitos 3D. Paleta sóbria em preto, cinza e amarelo. Defina a área de impressão para caber em uma página em paisagem.

## Estrutura sugerida

Use abas para Instruções, Earn Referência, Earn Simulado, Calibração do Earn, Parâmetros da Vitrine, Simulador Individual, Base XP B2C, Base XP B2B, Cálculos da População, Resumo, Premissas de Custo e Testes. Acrescente a projeção de comportamento depois da validação da foto atual.

Organize os cálculos da população em blocos de colunas auxiliares. Se uma aba de cálculo por canal facilitar o desempenho e a manutenção, use essa estrutura.

Diferencie células editáveis, fórmulas e dados importados. Use português brasileiro, R$ para valores em reais e US$ para câmbio. Comece com o perfil individual zerado.

Reúna em um só lugar, na aba de Parâmetros da Vitrine, os **controles de cenário** descritos adiante: acesso ao Infinite (A ou B), Investback do One (com base ou só com fichas), Salas VIP (mínimo no cartão ou tudo por fichas), Corretagem zero (faixas ou corte único) e transição do Cofre XP.

## Regras de earn

Use o mesmo perfil para calcular Referência e Simulado. A Referência fica fixa. Os parâmetros do Simulado são editáveis.

### Três tipos de mecânica

Cada alavanca usa uma de três mecânicas. A aba de parâmetros mostra, para cada alavanca, só os campos da mecânica dela.

| Mecânica | Como funciona | Campos |
| --- | --- | --- |
| **Tem ou não tem** | O cliente tem a coisa, ou atinge um valor mínimo, e ganha um número fixo de fichas | Valor mínimo (quando houver), fichas |
| **A cada valor** | Ganha fichas a cada bloco completo de valor, acima de um ponto de partida, até um teto | A partir de, a cada, fichas por bloco, teto de fichas |
| **Por faixas** | O valor do cliente cai em uma faixa e cada faixa vale um número de fichas | Lista de faixas: de, até, fichas |

Não use os rótulos "passo" nem "piso ou gatilho". Use "a cada" para o tamanho do bloco, "a partir de" para o ponto de partida e "valor mínimo" para a mecânica "tem ou não tem".

### Desenho das abas de parâmetros de earn

Crie **duas abas com o mesmo layout**: `Earn Referência`, travada, e `Earn Simulado`, editável. O layout idêntico permite que as fórmulas das duas réguas sejam as mesmas, mudando só a aba de origem.

Em cada aba, **uma linha por alavanca**, nunca várias linhas genéricas por alavanca. Colunas, da esquerda para a direita:

1. Momento da jornada.
2. Alavanca.
3. Medida do cliente e unidade (por exemplo, "AUC, R$" ou "Open Finance ativo, sim ou não").
4. Ligada, sim ou não. É aqui que se decide se a alavanca entra na régua.
5. Mecânica, escolhida em lista: tem ou não tem, a cada valor, por faixas.
6. Bloco "Tem ou não tem": valor mínimo, fichas.
7. Bloco "A cada valor": a partir de, a cada, fichas por bloco, teto de fichas.
8. Máximo de fichas da alavanca, calculado.
9. Observação.

As faixas ficam em uma **tabela separada na mesma aba**, logo abaixo, em formato longo: alavanca, número da faixa, de (exclusivo), até (inclusivo), fichas. Reserve até seis faixas por alavanca; faixas em branco são ignoradas. A última faixa preenchida pode ter "até" vazio, significando sem limite.

Os campos que não pertencem à mecânica escolhida ficam esmaecidos por formatação condicional e não entram no cálculo. Na aba `Earn Simulado`, acrescente uma coluna "Difere da Referência", sim ou não, e mantenha ao lado de cada entrada o valor inicial, para poder voltar atrás.

No cálculo, cada alavanca tem três colunas auxiliares, uma por mecânica, e uma quarta que escolhe o resultado conforme a mecânica selecionada e zera quando a alavanca está desligada. Assim, trocar a mecânica de uma alavanca não exige reescrever fórmula.

### Alavancas e configuração inicial

| Momento | Alavanca | Medida do cliente | Mecânica inicial | Referência | Simulado |
| --- | --- | --- | --- | --- | --- |
| Planeje sua vida financeira | Open Finance | Ativo, sim ou não | Tem ou não tem | 1 ficha | 1 ficha |
| Planeje sua vida financeira | Planejamento financeiro | Atualizado, sim ou não | Tem ou não tem | Desligada | Desligada; fichas a definir |
| Planeje sua vida financeira | PFM 3.0 | Ativado, sim ou não | Tem ou não tem | Desligada | Desligada; fichas a definir |
| Comece a poupar | AUC | Saldo em R$ | A cada valor | A partir de R$ 0, a cada R$ 5.000, 1 ficha, teto 10 | A partir de R$ 30.000, a cada R$ 5.000, 1 ficha, teto 10 |
| Comece a poupar | Aporte recorrente | Valor aportado no mês, R$ | Por faixas | Qualquer valor acima de zero: 5 fichas | Igual à Referência; faixas a definir |
| Comece a poupar | Previdência | Saldo em R$ | Tem ou não tem | Valor mínimo R$ 100, 1 ficha | Igual |
| Otimize seu dia a dia | TPV no cartão | Gasto mensal, R$ | A cada valor | A cada R$ 500, 1 ficha, teto 15 | Igual |
| Otimize seu dia a dia | Boletos | Valor pago no mês, R$ | Tem ou não tem | Valor mínimo R$ 5.000, 2 fichas | Igual |
| Otimize seu dia a dia | Salário portado | Salário mensal, R$ | Por faixas | Até R$ 5.000: 0; acima de R$ 5.000 até R$ 10.000: 2; acima de R$ 10.000: 5 | Igual |
| Otimize seu dia a dia | Câmbio | Valor da remessa no mês, US$ | A cada valor | Desligada | A cada US$ 2.000, 1 ficha, teto 10 |
| Acelere e proteja seus planos | Crédito | Valor do crédito, R$ | A cada valor | A cada R$ 10.000, 1 ficha, teto 20 | Igual |
| Acelere e proteja seus planos | Consórcio | Valor da carta, R$ | A cada valor | A cada R$ 10.000, 1 ficha, teto 20 | Igual |
| Acelere e proteja seus planos | Seguro de vida | Valor do PA, R$ | Tem ou não tem | Valor mínimo R$ 100, 5 fichas | Igual |
| Acelere e proteja seus planos | Seguro Conta e Cartão | Apólice ativa, sim ou não | Tem ou não tem | Desligada | Desligada; fichas a definir |

Observações sobre a tabela:

* **Aporte recorrente** passa a ser medido pelo valor aportado, e não só por sim ou não. A configuração inicial reproduz a regra anterior (qualquer aporte vale 5 fichas). Deixe prontas, em branco, faixas como R$ 500 a R$ 1.000, R$ 1.000 a R$ 1.500 e acima de R$ 1.500, para serem preenchidas quando a quantidade de faixas for decidida. Se a base só trouxer a marca de sim ou não, registre a limitação.
* **Salário portado** começa por faixas, mas a mecânica pode ser trocada para "tem ou não tem" na lista. Mantenha a sensibilidade de 1 ficha entre R$ 3.000 e R$ 5.000 como uma faixa adicional desligada.
* **Seguro de vida** começa como "tem ou não tem" pelo valor do PA e pode virar "por faixas".
* Ainda não está decidido se todas as alavancas entram no programa. A coluna "Ligada" existe para isso; mostre no painel quantas estão ligadas em cada régua.

Nas regras "a cada valor", arredonde a quantidade de blocos para baixo e aplique o teto da alavanca. Nas regras "por faixas", o limite inferior é exclusivo e o superior é inclusivo, e as faixas não podem se sobrepor: inclua uma verificação que acuse sobreposição ou lacuna.

Mostre soma bruta, teto total, pontuação final e redução pelo teto. O teto total inicial é zero, significando sem teto. Classifique as fichas finais nas faixas 0, 1–4, 5–9, 10–14, 15–29, 30–49, 50–59 e 60 ou mais.

Mostre também o **máximo de fichas possível** em cada régua, somando o máximo das alavancas ligadas. A experiência exibe ao cliente "N fichas de M possíveis", então M precisa sair do modelo.

### Calibração das fichas por alavanca

A quantidade de fichas de cada alavanca ainda será discutida e precisa de um critério, e não de palpite. Crie uma aba `Calibração do Earn` que, para cada alavanca do Simulado e usando a base de outubro, mostre lado a lado:

* Quantas contas pontuam na alavanca e que percentual da população representam.
* Fichas médias por conta que pontua, e fichas totais geradas.
* Participação da alavanca no total de fichas do programa.
* Quanto esforço do cliente uma ficha exige naquela alavanca, na unidade da medida (por exemplo, R$ de gasto por ficha).
* Margem de contribuição estimada do comportamento, como entrada pendente, e as **fichas por R$ de margem**.

O último indicador coloca todas as alavancas na mesma base: mostra quais estão pagando fichas demais ou de menos em relação ao valor que o comportamento traz. Inclua ainda, por alavanca, o efeito de ligar ou desligar: quantas contas mudam de faixa de fichas e quantas passam a alcançar, ou deixam de alcançar, a oferta mais barata.

## Cartões e cenários de acesso

O corte patrimonial do Infinite é de R$ 30.000 de AUC. Abaixo dele, o cartão é o XP One. Deixe os parâmetros editáveis.

Compare duas rotas de acesso ao Infinite:

* Cenário A. Infinite elegível a partir do corte patrimonial.
* Cenário B. Mantém a rota patrimonial e permite escolher o Infinite com fichas abaixo do corte. Use 10 fichas como hipótese inicial editável.

Para comparar A e B, use a mesma régua de earn e os mesmos preços da prateleira. O controle Referência versus Simulado pertence à pontuação. O controle A versus B pertence ao acesso ao cartão.

O corte patrimonial do Infinite e o piso de AUC sem fichas são parâmetros independentes. No B, atingir as fichas necessárias torna a oferta elegível. O cartão com fichas precisa ser escolhido para afetar o saldo.

Na experiência, quem vê a opção de pedir o Infinite já está pré-aprovado e o cartão é emitido na hora do pedido. Para o modelo, trate "elegível" e "escolheu" como estados distintos e assuma que a escolha tem efeito imediato. **[a confirmar]** A partir de quando os benefícios do Infinite passam a valer: no pedido ou na entrega do cartão.

Use fichas travadas como modo inicial. Ao atingir o corte patrimonial, teste liberar as fichas antes alocadas ao Infinite. O perfil abaixo do corte continua participando do programa e pode escolher outros benefícios.

### Investback de largada

Crie um controle com duas opções para o XP One:

* **One só com fichas** (opção inicial). O One não tem Investback de largada. Toda taxa do One é ativada com fichas, a partir de 0,8%.
* **One com base de fevereiro de 2027.** O One tem 0,8% de Investback com TPV mensal maior ou igual a R$ 2.500, sem usar fichas, e os turbos partem daí.

As duas opções se equivalem no ponto de entrada quando o preço de 0,8% é de 5 fichas: R$ 2.500 de TPV geram exatamente 5 fichas. Mostre no painel quantas contas atingem 0,8% em cada opção e quantas ficam sem fichas para outro benefício depois de ativá-lo.

O Infinite parte de 1% de Investback incluído, sem fichas e sem gasto mínimo. **[a confirmar]** Ausência de gasto mínimo no Infinite.

## Prateleira inicial de burn

Crie as ofertas abaixo com preços editáveis em fichas. Cada benefício é uma régua: um ponto de partida, que é o que o cliente tem sem fichas, e degraus ativados com fichas. O valor de cada degrau é o total do benefício, não um acréscimo.

**Cofre XP**

* Partida: 100% do CDI, incluído, sem fichas.
* Turbo: 110% do CDI por 10 fichas, 115% por 15 e 125% por 30.
* Ao desativar ou perder o turbo, o saldo volta a render 100% do CDI.

**Investback turbinado**

* One, no modo "só com fichas": 0,8% por 5 fichas, 1,0% por 10 e 1,1% por 15. **[a confirmar]** Preços ilustrativos; no prompt original, 1,0% custava 5 e 1,1% custava 10.
* One, no modo "com base de fevereiro de 2027": 0,8% incluído com TPV ≥ R$ 2.500; 1,0% por 5 fichas e 1,1% por 10.
* Infinite: 1% incluído; 1,2% por 10 fichas e 1,5% por 15.
* Mantenha, como atributo informativo de cada degrau, a equivalência em pontos de recompensa por US$ do cartão (1,0% ou 2 pontos; 1,2% ou 2,5; 1,5% ou 3). Esses pontos pertencem ao cartão e não se misturam com as fichas.

**Salas VIP**

Crie um controle com dois modos, com quantidades e preços editáveis. **[a confirmar]** Todos os números abaixo são ilustrativos.

* **Mínimo no cartão** (opção inicial). O Infinite inclui 4 acessos por ano, sem fichas, condicionados a gasto mínimo no cartão. Com fichas: 6 acessos por 10 fichas ou 8 por 15. O One não inclui acessos; com fichas: 2 acessos por 10 ou 4 por 15.
* **Tudo por fichas.** Nenhum cartão inclui acessos. Infinite: 4 acessos por 10 fichas ou 8 por 15. One: 2 por 10 ou 4 por 15.

**Corretagem zero**

* Faixas (opção inicial): 3 ordens por mês por 5 fichas, 6 por 10 e 9 por 15. Nenhuma ordem é incluída sem fichas. **[a confirmar]** No prompt original eram 3, 6 e 10 ordens por 15, 30 e 50.
* Alternativa de corte único, com preço e cobertura editáveis. Deixe-a desligada inicialmente e permita compará-la às faixas.

**Infinite com fichas**

* Disponível no cenário B abaixo do corte patrimonial, por 10 fichas.

Permita uma opção ativa por família. As famílias são Cofre XP, Investback, Salas VIP, Corretagem zero e, no B, Infinite com fichas. As opções de Investback e de Salas VIP dependem do cartão efetivo. Os preços são hipóteses de calibração.

No simulador individual, use listas para selecionar benefícios. Mostre fichas totais, em uso, disponíveis e déficit, quando houver. Na troca dentro da mesma família, libere a reserva anterior e aplique a nova. Se uma mudança de perfil tornar a escolha inválida, sinalize o motivo. Quando o cartão efetivo muda, as escolhas de Investback e de Salas VIP do cartão anterior ficam inválidas e suas fichas voltam ao saldo.

## Como tratar a base agregada de outubro

Vou fornecer os dados. Inspecione os cabeçalhos e documente o significado das colunas antes de criar referências.

Cada linha representa um grupo com marca, canal, arquétipo, combinação de faixas das alavancas, quantidade de contas e medidas somadas, como AUC, TPV, receita e custos atuais de benefícios. Esses custos podem incluir pontos do cartão, Turbo Conta e sala VIP. Verifique suas definições e se existe sobreposição.

Use quantidade de contas para ponderar os indicadores. Calcule médias por conta dividindo somas pela quantidade correspondente. Preserve as combinações observadas entre as alavancas.

Use a pontuação calculada no Databricks como conferência, se vier na extração. Recalcule uma regra no Excel quando os valores dentro da faixa receberem a mesma pontuação. Quando houver ambiguidade, sinalize as contas afetadas e a necessidade de uma faixa mais detalhada.

Uma faixa de R$ 30 mil a R$ 35 mil pode conter clientes com resultados diferentes se eu mudar o piso para R$ 32 mil. Nessa situação, o valor médio do grupo é insuficiente para determinar a elegibilidade exata.

Se faltar alguma alavanca na base, registre-a como indisponível e mostre a cobertura do cálculo. Dados pendentes devem permanecer identificados nos resultados. É provável que Planejamento financeiro e PFM 3.0 não existam na base de outubro; trate-os como indisponíveis na foto e só os use na projeção.

## Painel de calibração da foto atual

Mostre, por canal e arquétipo, quantidade de contas, distribuição de fichas, percentual com zero, percentual que pontua e continua sem oferta elegível e percentual com ao menos uma oferta elegível. Conte cada conta uma vez nesse último indicador. Considere "oferta elegível" apenas o que exige fichas; o que vem incluído (cartão, Cofre XP a 100%, Investback de largada, acessos incluídos) aparece à parte, como "já tem sem fichas".

Abra a elegibilidade por benefício e a origem das fichas quando a base permitir. Para A e B, mostre quantas contas abaixo do corte de AUC podem acessar o Infinite e qual saldo sobraria se o escolhessem.

Destaque dois pontos que apareceram no protótipo e precisam de número:

* No B, quem tem 15 fichas e escolhe o Infinite fica com 5. Mostre quantas contas ficam nessa situação e qual é o benefício mais barato que ainda alcançam.
* Quem tem cerca de R$ 40 mil de AUC e pouco uso dos demais produtos junta 2 fichas no Simulado. Mostre o tamanho desse grupo e a distância até a oferta mais barata.

Para o Cofre XP de janeiro, compare quem mantém, perde ou ganha acesso a cada faixa quando os indicadores comerciais estiverem disponíveis. As condições de trabalho são:

* 110% do CDI com TPV de pelo menos R$ 5 mil e Seguro Conta e Cartão ou portabilidade.
* 115% com Seguro Conta e Cartão ou portabilidade, combinado com crédito com garantia ou Term Life. O piso de R$ 10 mil para crédito é provisório.
* 125% com Seguro Conta e Cartão ou portabilidade, combinado com consórcio. O piso de R$ 100 mil da carta é provisório.

Registre essas condições como premissas a confirmar. A apólice ativa pode contar para elegibilidade comercial mesmo com zero ficha no earn.

Acrescente um controle de **transição do Cofre XP** para quem já tiver o benefício antes do programa, com três hipóteses: preservar a condição sem usar fichas; carência até uma data editável, depois da qual a condição passa a exigir fichas; migração imediata para fichas, voltando a 100% do CDI. Mostre, em cada hipótese, quantas contas manteriam a faixa atual com as fichas que têm.

## Premissas de custo e cenários de escolhas

Prepare uma tabela por benefício com fórmula de custo, unidade de uso, teto, duração, custo de referência, fonte e status de validação. Vou fornecer as premissas disponíveis. Mantenha valores ausentes identificados como pendentes.

* Investback depende do TPV elegível e da taxa.
* Cofre XP depende do saldo efetivamente remunerado, do teto e da diferença de custo de remuneração em relação aos 100% do CDI da partida.
* Corretagem depende das ordens que seriam cobradas e de custos variáveis adicionais onde houver dado.
* Salas VIP dependem dos acessos efetivamente usados e do custo por acesso. Como referência de partida, use a proxy de US$ 40 por acesso com o acréscimo de tributação usado pelo assessorado, identificada como pendente de validação.
* Infinite com fichas depende da diferença econômica frente ao pacote que o cliente teria.

Use a foto de outubro para estimar custo com comportamento observado. A referência econômica desejada é a mesma base recalculada pelas regras de fevereiro de 2027, ou seja, One com 0,8% de Investback a partir de R$ 2.500 de TPV e as regras de sala VIP já acordadas. Enquanto ela estiver pendente, identifique qual comparação está disponível.

Os controles de cenário mudam a linha de base, não só o custo dos turbos. Em particular, "One só com fichas" e "Salas VIP tudo por fichas" retiram custo que hoje é de largada e o condicionam à escolha do cliente. Mostre esse efeito em linha própria, separado do custo dos benefícios adicionais.

Para manter o Excel leve, comece com poucas combinações explícitas de benefícios, com fichas exigidas e custo calculados em uma tabela auxiliar. Com cinco famílias, o número de combinações cresce depressa; limite a tabela às combinações que cabem em até 30 fichas e documente o critério. Determine quais combinações cabem no saldo de cada grupo.

Simule um mix central editável, um mix de menor custo e um estresse com as combinações viáveis mais caras. Use o mesmo conjunto de combinações e adesão para comparar os mixes. Se o conjunto for parcial, identifique o estresse como o maior custo entre as combinações modeladas. Confira que os percentuais de escolhas somam 100%, incluindo quem adere e não ativa oferta, quando aplicável.

Mostre custo total, custo incremental e custo por conta participante. Compare custo por ficha exigida entre ofertas no mesmo período. Esse indicador pode variar com o perfil e o uso. No modo travado, destaque custo por conta ativa por mês.

## Etapas de entrega

Primeiro, construa parâmetros, simulador individual e testes. Depois conecte a base agregada e valide população, fichas e elegibilidade. Na sequência, conecte as premissas econômicas e os cenários de escolha.

Depois que a foto de outubro estiver validada, prepare a projeção futura. Ela deve permitir informar público potencial, conversão incremental, intensidade da mudança, duração e margem de contribuição por comportamento. Recalcule fichas, acesso e custo a partir dessas mudanças.

Use ARPAC histórico por perfil como referência de plausibilidade. Para o retorno atribuído ao programa, use hipóteses próprias de margem incremental. Calcule margem adicional dos comportamentos induzidos menos custo incremental dos benefícios e da operação. Inclua o custo de premiar quem já se qualificaria e verifique se algum custo já foi descontado na margem fornecida.

## Decisões ainda em aberto

Registre na aba de Instruções, como pendências do modelo:

* Periodicidade de apuração das fichas, validade e vigência mínima de um benefício. O protótipo assume apuração mensal, com saldo recalculado a cada mês, sem acúmulo.
* Política de perda de elegibilidade quando as fichas caem abaixo do que está em uso, e quando o AUC cai abaixo do corte com Infinite ativo.
* Escolha entre os cenários A e B, e entre os modos de Investback do One, de Salas VIP e de Corretagem zero.
* Limite de saldo, duração e renovação do Cofre XP turbinado.

## Testes mínimos

Com os parâmetros iniciais e todos os demais campos zerados:

* Perfil zerado gera zero ficha em Referência e Simulado.
* Perfil zerado tem, sem fichas: cartão XP One, Cofre XP a 100% do CDI, nenhum Investback (no modo "One só com fichas"), nenhum acesso a sala VIP e nenhuma ordem com corretagem zero.
* Open Finance ativo gera 1 ficha nas duas réguas.
* Aporte recorrente de R$ 300 no mês gera 5 fichas com a faixa inicial. Ao preencher faixas de R$ 500 a R$ 1.000 e acima, o mesmo aporte passa a seguir a nova tabela.
* Trocar a mecânica do Salário portado de "por faixas" para "tem ou não tem", com 2 fichas, faz R$ 4.000 de salário gerar 2 fichas, sem alterar nenhuma fórmula.
* Desligar uma alavanca na coluna "Ligada" zera as fichas dela e reduz o máximo possível da régua no mesmo valor.
* Faixas sobrepostas ou com lacuna disparam a verificação de erro.
* Planejamento financeiro e PFM 3.0 ativos geram zero ficha enquanto as alavancas estiverem desligadas.
* AUC de R$ 25 mil e TPV de R$ 7.500 geram 20 fichas na Referência e 15 no Simulado.
* No A, esse perfil tem o One como cartão efetivo e 15 fichas para a prateleira. Combinações que cabem exatamente: Cofre XP 115%; Investback One 1,1%; Cofre XP 110% com Investback One 0,8%; Corretagem zero 9 ordens.
* No B, escolher Infinite por 10 fichas deixa 5 disponíveis. Com o Infinite como cartão efetivo, as opções de Investback passam a ser as do Infinite, e nenhuma cabe em 5 fichas.
* Ao elevar o AUC para R$ 30 mil, mantendo TPV de R$ 7.500, o Simulado continua com 15 fichas. A rota patrimonial libera as 10 fichas antes alocadas ao Infinite.
* AUC de R$ 35 mil e TPV de R$ 7.500 geram 16 fichas no Simulado.
* TPV de R$ 2.500, sozinho, gera 5 fichas e torna elegível o Investback One de 0,8%. TPV de R$ 2.499 gera 4 e não torna.
* No modo "One com base de fevereiro de 2027", TPV de R$ 2.500 dá 0,8% sem usar fichas e as 5 fichas ficam livres.
* Na portabilidade inicial, R$ 5.000 geram zero, R$ 5.001 geram 2, R$ 10.000 geram 2 e R$ 10.001 geram 5.
* Boletos de R$ 10 mil geram 2 fichas fixas.
* Câmbio de US$ 4 mil gera zero na Referência e 2 no Simulado.
* Seguro Conta e Cartão ativo gera zero ficha enquanto a alavanca estiver desligada.
* Salas VIP no modo "mínimo no cartão": perfil com Infinite tem 4 acessos sem fichas. No modo "tudo por fichas", tem zero.
* Trocar Cofre XP de 110% para 115% libera 10 fichas e aloca 15: o saldo disponível cai 5.
* Com Cofre XP 115% ativo (15 fichas em uso), reduzir o TPV para R$ 4.000 leva o total a 8 fichas e gera déficit de 7, sinalizado.
* O máximo de fichas possível no Simulado, com os parâmetros iniciais, é a soma dos tetos das alavancas ligadas; confira o valor contra a soma manual.
* Os totais da população devem reconciliar com as contagens e controles importados.
* Verificações estruturais: nenhuma célula mesclada, nenhuma célula com erro, nenhum vínculo externo e nenhuma constante numérica dentro de fórmula.

Ao final de cada etapa, mostre o que foi construído, os testes realizados e os insumos pendentes. Mantenha o cálculo organizado em passos curtos, com prioridade para desempenho, rastreabilidade e clareza.

# Protótipo · Benefícios e Loyalty Digital

Protótipo navegável da experiência de benefícios e fichas no app, para apresentação no iPad.
É um único arquivo, sem build nem dependências: abra `index.html` no navegador.

- **Paisagem (iPad):** painel da demonstração à esquerda, telefone à direita.
- **Retrato ou telas estreitas:** o painel abre pelo botão **Demo**.

Inspirado nas telas do time de Design (recebidas como fotos de tela). Delas vieram o visual escuro com CTA em
pílula amarela e o vocabulário: fichas, Em uso / Disponíveis, Juntar / Usar, desafios e trilha para desbloquear.
Mudanças em relação a elas: o cartão e o que já vale sem fichas aparecem primeiro (aba Resumo); os benefícios são
agrupados por família, com uma opção ativa por vez; a barra "15 de 181" deu lugar à composição em uso / disponíveis;
confirmação, troca, perda de elegibilidade e transição dos R$ 30 mil ganharam telas próprias.

## Organização da experiência

| Área | O que responde |
| --- | --- |
| **Meu cartão** | O que já está valendo no meu cartão, como chegar ao próximo pacote, em que etapa está o meu pedido |
| **Usar** | Qual é o meu cartão, o que posso ativar com fichas, quanto custa, o que cabe no meu saldo |
| **Detalhe do benefício** | Escolha da opção, efeito no saldo, confirmação, troca, desativação |
| **Juntar** | Minha trilha, o que é recomendado para mim e meu avanço em cada grupo de desafios |

## Painel da demonstração

- **Cenário A / B** de acesso ao Infinite. Trocar o cenário reinicia a jornada do perfil.
- **Perfis:** Marina (R$ 25 mil, R$ 7.500/mês no cartão, 15 fichas), Rafael (R$ 40 mil, 2 fichas), Jô (R$ 8 mil, zero ficha).
- **Simular comportamento:** patrimônio, gasto no cartão e cada desafio (Open Finance, aporte, salário...) recalculam fichas, elegibilidade e alertas na hora.
- **Ir direto a um estado:** boas-vindas, zero ficha, fichas insuficientes, disponível, em processamento, ativo, troca,
  perda de elegibilidade, queda de patrimônio, Infinite por fichas, chegada a R$ 30 mil em A e em B, Cofre XP já ativo.
- **Cofre XP antes do Loyalty:** três hipóteses de transição (preservar, carência, migrar já).
- **Premissas editáveis:** preços em fichas, corte patrimonial, textos de sala VIP e de cobertura da corretagem.

Dentro do app, o botão tracejado "Demo · simular ação concluída" marca um comportamento como feito.
Quando há um pedido do Infinite em análise, o painel mostra o botão para simular a aprovação.

## Régua e preços usados

Informados no briefing: cartão (1 ficha a cada R$ 500, até 15), patrimônio (1 ficha a cada R$ 5 mil completos
acima de R$ 30 mil, até 10), preços da prateleira e Infinite por 10 fichas.

Ilustrativos, criados para o protótipo: Open Finance 3, aporte recorrente 3, previdência 3, pagamentos 2,
portabilidade de salário 5, câmbio 1, crédito 2, consórcio 2, seguros 2, Seguro Conta e Cartão 1;
condição de lançamento do Cofre XP a 110% do CDI; carência até 30/04/2027.

## Hipóteses adotadas

- **Pacotes.** Dois pacotes, XP One e XP Infinite, sem nomes de nível ou segmento. Na tela, a palavra é sempre "cartão": o do cliente aparece como "Incluído · não usa fichas", com a razão (cliente XP Digital, ou R$ 30 mil ou mais investidos).
- **Pacotes.** No One, o Investback vem só de fichas: 0,8%, 1,0% ou 1,1% por 5, 10 ou 15 fichas. Não há mais gasto mínimo de R$ 2.500: gastar R$ 2.500 no cartão rende as 5 fichas do 0,8%. No Infinite, 1% já vem incluído.
- **Pacotes.** Quem tem o XP One vê o Infinite ao lado, em carrossel. Quem já tem o Infinite vê só o Infinite. Quem está longe do corte (abaixo de 60%) não vê barra de "faltam R$": só a regra, sem cobrança.
- **Sala VIP.** Dois modos no painel. Mínimo no cartão: o Infinite inclui 4 acessos por ano e chega a 6 ou 8 com 10 ou 15 fichas. Tudo por fichas: nenhum cartão inclui, e o Infinite tem 4 ou 8 acessos por 10 ou 15 fichas. Nos dois modos o One tem 2 acessos por 10 fichas. Quantidades e preços são ilustrativos.
- **Sala VIP.** Como no Investback, o número escolhido é o total de acessos do ano, não um extra.
- **Pacotes.** O cartão mostra o que já vale e, logo abaixo, até onde dá para chegar com fichas (ex.: Investback 1%, até 1,5% com fichas).
- **Pacotes.** Abaixo do corte, o Infinite aparece bloqueado no carrossel, com o que falta para desbloquear.
- **Pacotes.** Atingir o corte libera o pedido do Infinite. O cartão só muda depois de pedido, análise e ativação: três estados separados na tela.
- **Fichas.** Cartão: 1 ficha a cada R$ 500 de gasto no mês, até 15. Patrimônio: 0 ficha até R$ 30 mil e 1 ficha a cada R$ 5 mil completos acima disso, até 10.
- **Fichas.** Demais comportamentos com pontuação ilustrativa: Open Finance 3, aporte recorrente 3, previdência 3, pagamentos 2, salário 5, câmbio 1, crédito 2, consórcio 2, seguros 2, Seguro Conta e Cartão 1.
- **Fichas.** Apuração mensal: o saldo total é recalculado a cada ciclo conforme o comportamento. Não há acúmulo nem validade no protótipo.
- **Saldo.** O medidor mostra as fichas do cliente contra o total possível (48 na régua ilustrativa): em uso, disponíveis e a conquistar. O total é a soma dos tetos de todos os desafios e muda com a calibração.
- **Saldo.** Fichas travadas: ficam em uso enquanto o benefício está ativo e voltam ao desativar. Uma opção ativa por família.
- **Saldo.** Na troca dentro da família, as fichas da opção atual são liberadas e as da nova entram em uso, em um só passo.
- **Prateleira.** Cofre XP Turbo 110/115/125% do CDI por 10/15/30 fichas. Não existe Cofre XP sem Turbo.
- **Prateleira.** Investback turbinado é a taxa total do cartão. One: 0,8%, 1,0% ou 1,1% por 5, 10 ou 15 (os preços de 1,0% e 1,1% subiram 5 fichas para abrir espaço ao 0,8%). Infinite: 1,2% ou 1,5% por 10 ou 15.
- **Prateleira.** Corretagem zero em corte único por 15 fichas, com cobertura parametrizável.
- **Prateleira.** Investback turbinado pertence ao cartão. Se o cartão muda, a opção é encerrada e as fichas voltam ao saldo.
- **Cenário B.** Infinite por 10 fichas abaixo do corte. As fichas ficam reservadas desde o pedido.
- **Cenário B.** Ao atingir R$ 30 mil, as fichas do cartão são liberadas automaticamente e o acesso passa a ser por patrimônio.
- **Elegibilidade.** Queda de fichas: nada muda até o fim do ciclo. O cliente recupera as fichas ou escolhe o que manter.
- **Elegibilidade.** Queda de patrimônio com Infinite ativo: o cartão segue ativo, com aviso prévio antes de qualquer mudança. No B, pode manter com fichas.
- **Cofre XP.** Quem já tinha Cofre XP antes do Loyalty entra com 110% do CDI. Três alternativas de transição: preservar sem fichas, carência até 30/04/2027, ou migração imediata para fichas.
- **Recomendação.** A ordem das sugestões é definida por perfil. Crédito e consórcio nunca aparecem como sugestão: só no catálogo, com a necessidade antes e as condições à vista.
- **Trilha.** O cliente pode seguir a trilha de um benefício e acompanhar no resumo quanto falta e quais desafios sugeridos levam até lá.
- **Vocabulário.** Das telas de Design: fichas (evita confusão com os pontos do cartão), Em uso e Disponíveis, Juntar e Usar, desafios, trilha para desbloquear.
- **Vocabulário.** Mantidos do briefing e diferentes das telas: taxas 110/115/125% e preços 10/15/30 (telas: 110% por 5 e 120% por 15), Infinite por 10 fichas (telas: 15), quatro contextos de earn (telas: seis).

## Decisões de produto em aberto

- **Acesso ao Infinite.** Cenário A ou B. No B, com 15 fichas, quem pega o Infinite fica com 5 e não alcança nenhum adicional (o menor custa 10). Vale rever o preço do cartão ou o piso do Investback Infinite.
- **Acesso ao Infinite.** Mostrar os dois pacotes para todos (adotado) ou segmentar, com cada cliente vendo só o seu. Risco de mostrar: frustrar quem não tem como chegar a R$ 30 mil.
- **Acesso ao Infinite.** Jornada operacional ao atingir o corte: pedido novo, migração do One, análise de crédito, prazo e o que acontece com o cartão antigo.
- **Acesso ao Infinite.** No B: confirmar a liberação automática das fichas no corte e se o cliente pode devolver o Infinite para reaver as fichas.
- **Elegibilidade.** Política de perda por queda de fichas: carência, ordem de desativação quando o cliente não escolhe, e comunicação.
- **Elegibilidade.** Política de perda do Infinite por queda de patrimônio: tolerância, rebaixamento ou manutenção.
- **Ciclo.** Periodicidade de apuração, validade das fichas e regra de manutenção dos benefícios.
- **Ciclo.** Vigência mínima de um benefício e prazo para as fichas voltarem após desativar ou trocar.
- **Régua.** Pontuação dos comportamentos fora de cartão e patrimônio. Inclusão e fichas do Seguro Conta e Cartão.
- **Régua.** Nesta régua, o cliente de R$ 40 mil com pouco uso tem 2 fichas e fica a 8 do benefício mais barato. Avaliar se há algo alcançável mais cedo.
- **Prateleira.** Corretagem zero: corte único ou franquias de 3, 6 e 10 ordens. Cobertura por mercado e canal.
- **Prateleira.** Cofre XP: limite de saldo, duração e renovação. Como não há versão sem Turbo, definir o que acontece com o dinheiro guardado quando o benefício é desativado ou perdido.
- **Prateleira.** Investback do One abaixo de R$ 2.500 de gasto: o turbinado pode ser vendido a quem não atinge o mínimo? O protótipo permite e informa a condição.
- **Prateleira.** Troca de cartão com Investback turbinado ativo: encerrar e devolver fichas (adotado) ou converter para a opção equivalente.
- **Sala VIP.** Mínimo incluído no cartão ou tudo por fichas. Quantidade de acessos por opção, preço em fichas, gasto mínimo, e se o One pode ter sala VIP com fichas.
- **Pacotes.** Lista completa de benefícios de cada cartão.
- **Cofre XP.** Regra de transição para quem ativar o Cofre XP entre janeiro e o início do Loyalty, e preço de upgrade para quem tem condição preservada.
- **Recomendação.** Critérios de adequação: quais sinais de capacidade e necessidade definem o que sugerir a cada cliente.

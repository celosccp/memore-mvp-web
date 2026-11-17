# Protótipo · Benefícios e Loyalty Digital

Protótipo navegável da experiência de benefícios e pontos no app, para apresentação no iPad.
É um único arquivo, sem build nem dependências: abra `index.html` no navegador.

- **Paisagem (iPad):** painel da demonstração à esquerda, telefone à direita.
- **Retrato ou telas estreitas:** o painel abre pelo botão **Demo**.

As telas de referência do time de Design ainda não foram incorporadas. A direção visual é a provisória
(amarelo, preto e cinza) e os componentes são genéricos.

## Organização da experiência

| Área | O que responde |
| --- | --- |
| **Benefícios** (central) | Quantos pontos tenho, qual é o meu cartão, o que escolhi, qual é o meu próximo passo |
| **Meu pacote** | O que já está valendo no meu cartão, como chegar ao próximo pacote, em que etapa está o meu pedido |
| **Escolher** (prateleira) | O que posso ativar com pontos, quanto custa, o que cabe no meu saldo |
| **Detalhe do benefício** | Escolha da opção, efeito no saldo, confirmação, troca, desativação |
| **Pontos** | De onde vieram meus pontos, o que é recomendado para mim, todas as formas de ganhar |

## Painel da demonstração

- **Cenário A / B** de acesso ao Infinite. Trocar o cenário reinicia a jornada do perfil.
- **Perfis:** Marina (R$ 25 mil, R$ 7.500/mês no cartão, 15 pontos), Rafael (R$ 40 mil, 2 pontos), Jô (R$ 8 mil, zero ponto).
- **Simular comportamento:** patrimônio e gasto no cartão recalculam pontos, elegibilidade e alertas na hora.
- **Ir direto a um estado:** zero ponto, pontos insuficientes, disponível, em processamento, ativo, troca,
  perda de elegibilidade, queda de patrimônio, Infinite por pontos, chegada a R$ 30 mil em A e em B, Cofrinho já ativo.
- **Cofrinho antes do Loyalty:** três hipóteses de transição (preservar, carência, migrar já).
- **Premissas editáveis:** preços em pontos, corte patrimonial, textos de sala VIP e de cobertura da corretagem.
- Abas **Hipóteses** e **Decisões** com as listas completas.

Dentro do app, o botão tracejado "Demo · simular ação concluída" marca um comportamento como feito.
Quando há um pedido do Infinite em análise, o painel mostra o botão para simular a aprovação.

## Régua e preços usados

Informados no briefing: cartão (1 ponto a cada R$ 500, até 15), patrimônio (1 ponto a cada R$ 5 mil completos
acima de R$ 30 mil, até 10), preços da prateleira e Infinite por 10 pontos.

Ilustrativos, criados para o protótipo: Open Finance 3, aporte recorrente 3, previdência 3, pagamentos 2,
portabilidade de salário 5, câmbio 1, crédito 2, consórcio 2, seguros 2, Seguro Conta e Cartão 1;
Cofrinho sem Turbo a 100% do CDI; condição de lançamento do Cofrinho a 110% do CDI; carência até 30/04/2027.

Hipóteses e decisões de produto em aberto estão nas abas do painel (`HIPOTESES` e `DECISOES` em `index.html`).

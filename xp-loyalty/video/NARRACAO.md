# Narração do vídeo Jornada XP — ponto em que paramos

## Objetivo

Colocar narração em **português do Brasil** no vídeo de teste da Jornada XP (47 s, 1920×1080), usando uma voz brasileira da **ElevenLabs**.

## O que já foi tentado e descartado

- Vozes prontas da API do Runway (ElevenLabs com locutores em inglês): saiu com sotaque de Portugal.
- Kokoro local (`hyperframes tts`, vozes `pf_dora` e `pm_alex`): brasileira, mas robótica.
- Abertura filmada gerada no Runway: descartada, ficou ruim.
- Primeiro roteiro: descartado porque a voz lia o que já estava escrito na tela.

Quem avalia a voz é o usuário, de ouvido. Antes de narrar tudo, gerar **uma frase** em duas ou três vozes brasileiras e pedir para ele escolher.

## Roteiro aprovado em linha geral (a voz não lê a tela)

Tom: a XP fala como guia ("a gente"). Ideias centrais: a jornada leva o cliente ao sucesso financeiro, a XP orienta os momentos e as ações, e o cliente escolhe o benefício que faz sentido em cada momento. A voz não usa "fichas", "turbinar" nem "passo".

| Cena | Início | Duração | Na tela | Voz |
|---|---|---|---|---|
| s1 abertura | 0,0 s | 2,8 s | Jornada XP | Sucesso financeiro não acontece de uma vez. |
| s3 momentos | 2,8 s | 6,2 s | Mais perto dos seus objetivos a cada avanço. | Por isso a gente criou uma jornada, e caminha com você: mostrando por onde começar e o que fazer em cada momento. |
| s4 fichas | 9,0 s | 6,9 s | Cada avanço na sua jornada vira fichas. | Cada coisa que você faz pela sua vida financeira é reconhecida, e volta para você. |
| s5 turbinar | 15,9 s | 10,0 s | Com fichas, você escolhe o que turbinar. | E o que volta, quem escolhe é você: o benefício que faz mais sentido para o seu momento. Render mais, pagar menos, viajar melhor. |
| s6 trocar | 25,9 s | 6,3 s | Troque quando quiser. As fichas voltam. | Seu momento mudou? Suas escolhas mudam junto. |
| s7 app | 32,2 s | 10,4 s | Tudo no app · Simples. Personalizada. Interativa. | E você acompanha de perto: onde está, o que já conquistou e para onde ir agora. |
| s8 fecho | 42,6 s | 4,6 s | Jornada XP · Comece a sua. | Seu sucesso financeiro, uma conquista de cada vez. |

O usuário ainda não confirmou este texto palavra por palavra; perguntar se quer ajustar antes de gerar a versão final.

## Como montar

1. O vídeo sem voz é o projeto HyperFrames desta pasta. Renderizar com a CLI (`render -o renders/jornada-xp-base.mp4`); os renders não ficam no repositório.
2. Gerar um arquivo de áudio por frase.
3. Encaixar cada frase cerca de 0,2 a 0,5 s depois do início da cena. Se uma frase for maior que a cena, ajustar a duração da cena no gerador (`gerar-cenas.py`) em vez de acelerar a voz.
4. Baixar os efeitos sonoros para uns 35% do volume sob a voz e normalizar o áudio final em torno de −16 LUFS.
5. Ainda não há música.

## Pendências relacionadas

- A fala da cena do app promete "para onde ir agora"; a gravação atual (`assets/app-demo.mp4`) mostra mais a aba Usar. Avaliar regravar passando pela trilha recomendada (aba Juntar).
- Melhorias de imagem levantadas e ainda não aplicadas: variar transições e entradas de título, tirar laços pulsantes da cena da órbita, fecho com chamada (botão "Começar minha jornada").
- A conta do Runway tem cerca de 800 créditos e a chave está salva no ambiente; não gastar sem o usuário pedir.

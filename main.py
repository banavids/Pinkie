# Importa a função randint do módulo random, o módulo paygame e algumas classes personalizadas.
from random import randint
import pygame   # Importa o módulo pygame.
from configs import *    # Importa todas as constantes e configurações de "configs.py".
from player import Player   # Importa a classe Player do módulo player.
from rock import Rock   # Importa a classe Rock do módulo rock.

# Inicializa a biblioteca paygame.
pygame.init()
# Inicializa a variavel "count" com valor 0.
count = 0
# Cria uma instância do jogador (classe Player) chamada "p1".
p1 = Player()

# Inicia um loop principal que continua enquanto a variável "gameOver" for False.
while not gameOver:
    # Incrementa a variável "count" em 1 a cada iteração.
    count += 1
    # Define o intervalo de tempo (dt) e limita a taxa de quadros (frames) a 60 por segundo
    # (para controlar a velocidade do jogo).
    dt = clock.tick(50)

    # Itera sobre eventos pygame na fila de eventos.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Se o evento for QUIT (fechar a janela), define gameOver como True para encerrar o loop.
            gameOver = True
            break
        elif event.type == pygame.KEYDOWN:
            # Se o evento for KEYDOWM (tecla pressionada), verifica se a tecla é a barra de espaço.
            if event.key == pygame.K_SPACE:
                # Define a variável "jump" como True para executar um salto.
                jump = True

    # Preenche a tela com a cor branca.
    screen.fill('white')
    # Desenha a imagem de fundo na tela.
    screen.blit(imgBg, (0, 0))

    # Verifica se o jogador está sem vidas.
    if not p1.getLifes():
        # Se o jogador está sem vidas, exibe uma mensagem na tela e atualiza a tela.
        text = fontRoboto50.render(f'Morreu!!!', True, 'green', 'blue')
        # Obtém um retângulo que envolve o texto.
        textRect = text.get_rect()
        # Desenha o texto na tela.
        screen.blit(text, textRect)
        # Atualiza a tela.
        pygame.display.update()
        # Pula o restante do loop e continua para a próxima iteração
        continue

    # Chama o método "drawME()" do objeto "p1" para desenhar o jogador.
    p1.drawME()

    # Desenha as vidas do jogador na tela.
    for life in p1.getLifes():
        # Chama o método "drawMe()" de cada vida para desenhá-las.
        life.drawMe()

    # Chama o método "validateKeys()" de "p1" para validar as teclas pressionadas.
    p1.validateKeys(pygame.key.get_pressed())

    
    if jump:
        jump = p1.jump()   # Chama o método "jump()" de "p1" para realizar um salto
    
    if  count % 100 == 0:
        # Adiciona uma nova instância da classe "Rock" à lista "rocks" da classe "Rock".
        Rock.rocks.append(Rock())

    # Itera sobre as rochas na lista "rocks" da classe "Rock".
    for rock in Rock.rocks:
        # Verifica se o jogador colidiu com a rocha.
        if p1.colides(rock):
            # Remove a rocha da lista.
            Rock.rocks.remove(rock)
            # Chama o método "loseLife()" de "p1" para fazer o jogador perder uma vida.
            p1.loseLife()
        # Chama o método "move()" de cada rocha para movê-las.
        rock.move()
        # Verifica se a rocha deve ser removida.
        if rock.remove():
            Rock.rocks.remove(rock)
        # Chama o método "drawMe()" de cada rocha para desenhá-las.
        rock.drawMe()


    pygame.display.update()


pygame.quit()    # Encerra a biblioteca pygame e fecha a janela do jogo.
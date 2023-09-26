# Código responsável pela configuração inicial do jogo, incluindo a criação da janela de exibição
# a inicialização do relógio do jogo, o carregamento de recursos como a imagem de fundo, a definição
# de variáveis importantes para o funcionamento do jogo.

import pygame

###### Display ######
screenW = 613    # Representa a largura da tela.
screenH = 256    # Representa a altura da tela.
# Cria a janela de exibição do paygame com as dimenções definidas.
screen = pygame.display.set_mode((screenW, screenH))

###### Clock ######
clock = pygame.time.Clock()   # Cria um objeto "Clock" do paygame, controla a taxa de quadros por segundo (FPS)
                              # do jogo, mantem a jogabilidade suave.

###### Image Background ####### 
imgBg = pygame.image.load("imgs/bg.png") # Imagem do plano de fundo da tela de jogo.

###### Font ######   Inicializa o módulo de fontes do paygame e cria um objeto de fonte chamado de "fontRoboto50"
pygame.font.init()
fontRoboto50 = pygame.font.SysFont("fonts/Roboto-Regular.ttf", 50)

###### Gameover ######  Indica que o jogo não terminou, variável que é usada mais tarde para controlar o loop
gameOver = False     #  principal do jogo.

###### Music ######
pygame.mixer.init()

###### Variables ######  "jump" variável usada para controlar se o jogador salta no jogo, é definida como 'True'
jump = False          #  quando é pressionada a tecla de espaço para saltar.
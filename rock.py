# classe Rock representa pedras no jogo. Mantém a posição, a imagem e fornece métodos para desenhar,
# mover e verificar se as pedras devem ser removidas do jogo. As pedras são criadas com coordenadas iniciais
# fora da tela e movem-se para a esquerda até saírem completamente da tela, momento em que são removidas do jogo.

from configs import screenW   # importa a variável "screenW" do módulo 'configs'.
from random import choice, randint
import pygame

class Rock:
    imgRock1 = pygame.image.load("imgs/rock1.png")
    imgRock2 = pygame.image.load("imgs/rock2.png")
    rocks = []

    def __init__(self):   # método construtor da classe 'Rock'.
        self.__x = screenW    # A coordenada x é definida como a largura da tela (screenW), o que coloca a pedra fora da tela no início.
        self.__y = randint(165, 191)   # A coordenada y é definida aleatoriamente dentro de um intervalo entre 165 e 191 pixels,
                                       # coloca as pedras em diferentes alturas verticalmente na tela.
        self.__img = choice([Rock.imgRock1, Rock.imgRock2])    # (self.__img) é escolhida aleatoriamente entre as duas
                                                               # imagens de pedra carregadas anteriormente.
    
    def drawMe(self):    # método responsável por desenhar a pedra na tela.
        pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))

    def move(self):    # método responsável por mover a pedra.
        self.__x -= 5
    
    def remove(self):    # método que verifica se a pedra deve ser removida do jogo.
        if self.__x <= 0:    # coordenada x da pedra, se for menor ou igual a 0, isso significa que a pedra saiu
            return True      # completamente da tela para a esquerda e não é mais visível.
                             # Nesse caso, o método retorna True, indicando que a pedra deve ser removida.

    def getBounds(self):    # método que retorna os limites (caixa delimitadora) da pedra, representados como um objeto Rect do pygame.
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())
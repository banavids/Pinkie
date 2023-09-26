import pygame
from Direction import Direction

class Lifes:
    imgLife = pygame.image.load("imgs/heart.png")

    def __init__(self, x):
        # Inicializa a classe Lifes com uma posição x.
        self.__x = x
        self.__y = 0
        self.__img = Lifes.imgLife

    def drawMe(self):
        # Desenha a imagem do coração na tela nas coordenadas (x, y).
        pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))

class Player:
    def __init__(self):
        # Inicializa a classe Player com atributos como posição, imagem e vidas.
        self.__x = 10
        self.__y = 160
        self.__img = pygame.image.load('imgs/pinkie.png')
        self.__up = True
        self.__lifes = []
        # Cria três instâncias da classe Lifes para representar as vidas do jogador.
        for x in range(3):
            if x == 0:
                self.__lifes.append(Lifes(x))
            else:
                self.__lifes.append(Lifes(Lifes.imgLife.get_width() * x))
    
    def getLifes(self):
        # Retorna a lista de vidas do jogador.
        if len(self.__lifes) <= 0:
            return False
            
        return self.__lifes
    
    def loseLife(self):
        # Remove uma vida da lista de vidas do jogador.
        self.__lifes.pop()
    
    def drawME(self):
        # Desenha a imagem do jogador na tela nas coordenadas (x, y).
        pygame.display.get_surface().blit(self.__img, (self.__x, self.__y))

    def move(self, dir):
        # Move o jogador na direção especificada (esquerda ou direita) com limites.
        if dir == Direction.LEFT and self.__x > 5:
            self.__x -= 5
        elif dir == Direction.RIGHT and self.__x < 639 - self.__img.get_width():
            self.__x += 5

    def validateKeys(self, keys):
        # Valida as teclas pressionadas e move o jogador com base nas teclas
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(Direction.UP)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(Direction.DOWN)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move(Direction.RIGHT)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move(Direction.LEFT)
    
    def jump(self):
        # Implementa uma lógica de salto para o jogador.
        if self.__y == 100:
            self.__up = False
        
        if self.__up:
            self.__y -= 5
        elif not self.__up:
            self.__y += 5
        
        if self.__y == 160:
            self.__up = True
            return False
        else:
            return True
        
    def getBounds(self):
        # Obtém os limites do retângulo em torno do jogador.
        return pygame.Rect(self.__x, self.__y, self.__img.get_width(), self.__img.get_height())

    def colides(self, who):
        # Verifica se o jogador colidiu com outro objeto (geralmente uma rocha)
        return self.getBounds().colliderect(who.getBounds())
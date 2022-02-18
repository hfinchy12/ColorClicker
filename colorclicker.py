import pygame
import random
import time

pygame.init()
pygame.display.set_caption('Color Clicker')
screen = pygame.display.set_mode((800,800))
running = True
score = 0
randnum = random.randint(0, 3)
basic_square = pygame.Rect(10, 10, 380, 380)
c1 = random.randint(0,255)
c2 = random.randint(0,255)
c3 = random.randint(0,255)
num_of_squares = 25

def square(color, Rect):
    pygame.draw.rect(screen, color, Rect)
startX = 15
startY = 15
#square_points = [(15, 15), (405, 15), (15, 405), (405, 405)]
square_points = []
for i in range(5): # makes grid
    for j in range(5):
        #startX += 150
        point = (startX, startY)
        square_points.append(point)
        startX += 155
    startX = 15
    startY += 155


squares = []
plots = []
colors = []

score_value = 0
font = pygame.font.Font('balloons.ttf', 32)


def thingy(): # makes the grid
    for i in range(25):
        squares.append(pygame.Rect(square_points[i], (150, 150)))
    for i in range(25):
        plots.append(square(colors[i], squares[i]))

def show_score(x, y): # scoreboard
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

while running:
    screen.fill((255, 255, 255))
    colors = []
    for i in range(25): # changes one of the squares by a few shades
        if i == randnum:
            if c1 < 60:
                c_alt = c1 + 30
            else:
                c_alt = c1 - 30
            c = (c_alt, c2, c3)
            colors.append(c)
        else:
            c = (c1, c2, c3)
            colors.append(c)

    thingy()


    for event in pygame.event.get():
        mouseX, mouseY = pygame.mouse.get_pos()
        if event.type == pygame.QUIT: # quits the game
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # checks to see if user clicked correct square
            if pygame.Rect.collidepoint(squares[randnum], (mouseX, mouseY)):
                print('hit')
                randnum = random.randint(0, 24)
                c1 = random.randint(0, 255)
                c2 = random.randint(0, 255)
                c3 = random.randint(0, 255)
                score_value += 1
            else:
                print('miss')

    show_score(350,20) # shows scoreboard
    pygame.display.update()
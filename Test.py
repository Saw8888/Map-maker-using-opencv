import sys
import pygame
import cv2

pygame.init()

screen = pygame.display.set_mode((388, 404))

lib = ['Map1.png']

Read = list(cv2.imread(lib[0]))

clock = pygame.time.Clock()
while True:
    screen.fill((0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(len(Read)):  # y coords
        for j in range(len(Read[i])):  # x coords
            blue = list(Read[i][j])[0]
            green = list(Read[i][j])[0]
            red = list(Read[i][j])[0]
            pygame.draw.rect(screen, (red,green,blue), pygame.Rect(j, i, 32, 32))

    pygame.display.update()
    clock.tick(30)
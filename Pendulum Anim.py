import pygame
import sys
from pygame.locals import *
pygame.init()
import math

screen_w = 720
screen_h = 480
screen = pygame.display.set_mode((screen_w, screen_h))
clock = pygame.time.Clock()
fps = 60
run = True

gravity = 1
origin = pygame.Vector2(screen_w/2, 80)
bob = pygame.Vector2()
length = 100
angle = math.pi/4
angV = 0
angA = 0

bob2 = pygame.Vector2()
length2 = 100
angle2 = math.pi / 2
angV2 = 0
angA2 = 0

mass1 = 30
mass2 = 30

while run:
    screen.fill(pygame.Color("black"))
    num1 = -gravity*(2*mass1+mass2)*math.sin(angle)
    num2 = -mass2*gravity*math.sin(angle-2*angle2)
    num3 = -2*math.sin(angle-angle2)*mass2*((angV2**2)*length2+(angV**2)*length + (angV**2)*length*math.cos(angle-angle2))
    den = length*(2*mass1+mass2-mass2*math.cos(2*angle-2*angle2))
    angA = (num1+num2+num3)/den

    nm1 = 2*math.sin(angle-angle2)*((angV**2)*length*(mass1+mass2)+gravity*(mass1 + mass2)*math.cos(angle)+(angV2**2)*length2*mass2*math.cos(angle-angle2))
    den2 = length2*(2*mass1 + mass2 - mass2*math.cos(2*angle-2*angle2))
    angA2 = nm1/den2

    # pendulum 1
    # fp = -(math.sin(angle) * gravity) / length
    # angA = fp
    angV += angA
    angle += angV

    bob.x = length * math.sin(angle) + origin.x
    bob.y = length * math.cos(angle) + origin.y

    pygame.draw.line(screen, pygame.Color("white"), origin, bob, 4)
    pygame.draw.circle(screen, pygame.Color("white"), bob, 20)
    pygame.draw.circle(screen, pygame.Color("grey"), bob, 15)

    # pendulum 2
    # origin2 = bob

    # fp2 = -(math.sin(angle2) * gravity) / length2
    # angA2 = fp2
    angV2 += angA2
    angle2 += angV2

    bob2.x = length2 * math.sin(angle2) + bob.x
    bob2.y = length2 * math.cos(angle2) + bob.y

    pygame.draw.line(screen, pygame.Color("white"), bob, bob2, 4)
    pygame.draw.circle(screen, pygame.Color("white"), bob2, 20)
    pygame.draw.circle(screen, pygame.Color("grey"), bob2, 15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(fps)
    pygame.display.update()

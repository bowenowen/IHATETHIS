from ConstructMap import *
import pygame


x = Line (100, 100, 100, 200, "first", True)
y = Line (100, 200, 200, 200, "second")
z = Line (200, 200, 200, 300, "third")
a = Line (300, 200, 100, 200, "fourth")

print a

m = Maze ([x,y,z, a], 50)
m.Parse()

print m

m.Traverse()

pygame.init()

clock = pygame.time.Clock()

black    = (   0,   0,   0,  255)
white    = ( 255, 255, 255,  255)
red      = ( 255,   0,   0,  255)
green    = (   0, 255,   0,  255)

screen = pygame.display.set_mode((640, 480))

for l in m.paths:
	print l
	pygame.draw.line(screen, white, l.startNode, l.endNode, 2)

while True:
    clock.tick (60)
    pygame.event.clear()
    key = pygame.key.get_pressed ()
    if key[pygame.K_ESCAPE]:
        break

    pygame.display.flip()

pygame.quit()
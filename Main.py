from myro import *
import time, pygame
from Vector2 import *
from ConstructMap import *

init ("COM19")
setIRPower(135)
IR = []
closeFront = 0
closeLeft = 0

rightMotor = 0.5
leftMotor = 0.5
START_SPEED = 0.5

def Median (IR):
    sorts = sorted(IR)
    length = len(sorts)
    if not length % 2:
        return (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
    return sorts[length / 2]  


def Detect ():
    setIRPower(135)
    IR = []    
    for count in range (10):
        pygame.event.clear()
        IR.append (getObstacle())
    return IR

def DetectFront (IR):
    data = []
    for ir in IR:
        data.append (ir[1])
    return Median (data)

def DetectLeft (IR):
    data = []
    for ir in IR:
        data.append (ir[0])
    return Median (data)

def DetectRight (IR):
    data = []
    for ir in IR:
        data.append (ir[2])
    return Median (data)


def Check(IR):
        if DetectFront(IR) > 1100:
            return 1
        else:
            return 0

def LineFromVectors(v1, v2, startPath = False):
    return Line (v1.x, v1.y, v1.x + v2.x, v1.y + v2.y, "Pathname", startPath)

def DrawLine (l):
    pygame.draw.line (screen, white, (l.x1, screen.get_height() - l.y1), (l.x2, screen.get_height() - l.y2), 3)

def Dijkstra (paths):
    start_path = paths[0]
    open_paths = start_path.exitPaths
    closed_paths = []
    while True:
        print start_path.name
        if (start_path.name == "End"):
            print "Found end"
            break
        shortest_distance = ()
        shortest_path = None
        for p in open_paths:
            if p.magnitude < shortest_distance and p not in closed_paths:
                shortest_distance = p.magnitude
                shortest_path = p
        closed_paths.append (start_path)
        start_path = shortest_path
        open_paths.extend (start_path.exitPaths)
    
FACTOR = 20
directions = {2:Vector2(1,0), 1:Vector2(0,1), 0:Vector2(-1,0), 3:Vector2(0,-1)}
currentDirection = directions[1]
currentDirectionNo = 1
currentTurns = 0
currentPosition = Vector2(400,100)
paths = []

t = time.clock()

pygame.init()

clock = pygame.time.Clock()

black    = (   0,   0,   0,  255)
white    = ( 255, 255, 255,  255)
red      = ( 255,   0,   0,  255)
green    = (   0, 255,   0,  255)

screen = pygame.display.set_mode((640, 480))
position_clock = time.clock()

while True:
    pygame.event.clear()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_q]:
        break
    while (time.clock() - t < 3):
        motors (leftMotor, rightMotor)
        readings =  Detect()
        if DetectFront(readings) >0:
            break
        if DetectLeft (readings) > 0:
            rightMotor -= 0.1
            print "Iceberg ahead!"
        if DetectLeft (readings) > 0:
            rightMotor += 0.1
            print "Iceberg ahead!"

    motors (0,0)
    current_path_time = time.clock() - position_clock

    if (currentTurns == 0):
        paths.append (LineFromVectors (currentPosition, currentDirection*current_path_time*FACTOR, True))
        currentTurns = 1
    else:
        paths.append (LineFromVectors (currentPosition, currentDirection*current_path_time*FACTOR, False))
    paths[-1].name = str (len(paths))
    DrawLine (paths[-1])
    currentPosition += currentDirection*current_path_time*FACTOR
    turnLeft (1, 0.8325)
    currentDirectionNo += 3
    currentDirection = directions[currentDirectionNo % 4]
    readings =  Detect()
    while Check(readings):
        turnRight (1, 0.7525)
        currentDirectionNo += 1
        currentDirection = directions[currentDirectionNo % 4]
        readings =  Detect()
    print currentDirection
    t = time.clock()
    position_clock = time.clock()
    pygame.display.update()

paths[-1].name = "End"
maze = Maze (paths, 100)
maze.Parse()
Dijkstra (paths)

for l in maze.paths:
    DrawLine(l)
    
while True:
    clock.tick (60)
    pygame.event.clear()
    key = pygame.key.get_pressed ()
    if key[pygame.K_ESCAPE]:
        break
    pygame.display.flip()

pygame.quit()    

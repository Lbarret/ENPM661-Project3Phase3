import os
from time import time
from AStar import AStar
from Mechanism import Environment

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from math import sin, cos, radians

multiplier = 5
height, width = 102 * multiplier, 102 * multiplier
count = 0

# Get input from user
radius = int(float(input("Enter radius: "))*10)
clearance = int(float(input("Enter Clearance: "))*10)
clearance += radius
coordinates = []
env = Environment([0, 0], clearance)
startBool = True
goalBool = True
# Get start position
startPos = [0, 0, 0]
while startBool:
    print("Enter start position: ")
    startPos[0] = input("x: ")
    startPos[1] = input("y: ")
    startPos[2] = input("theta: ")
    # Check to see if input is valid
    if env.possiblePostion([int(float(startPos[0])*10), int(float(startPos[1])*10)]):
        coordinates.append([int(float(startPos[0])*10) * multiplier, (102 - int(float(startPos[1])*10)) * multiplier, int(startPos[2])])
        count += 1
        startBool = False
    else:
        print("Invalid position.")
# Get goal position
goalPos = [0, 0]
while goalBool:
    print("Enter goal position: ")
    goalPos[0] = input("x: ")
    goalPos[1] = input("y: ")

    # Check to see if input is valid
    if env.possiblePostion([int(float(goalPos[0])*10), int(float(goalPos[1])*10)]):
        coordinates.append([int(float(goalPos[0])*10) * multiplier, (102 - int(float(goalPos[1])*10)) * multiplier])
        count += 1
        goalBool = False
    else:
        print("Invalid position.")
# Get step size
stepSize = [0,0]
print("Enter RPM size: ")
stepSize[0] = int(input("RPM1: "))
stepSize[1] = int(input("RPM2: "))

# Initialize AStar object
aStar = AStar([int(coordinates[0][0] / multiplier), int(102 - coordinates[0][1] / multiplier), coordinates[0][2]],
              [int(coordinates[1][0] / multiplier), int(102 - coordinates[1][1] / multiplier)], clearance, stepSize)
start = time()
# Compute solution
print("Computing...")
solution = aStar.solve()
end = time()
print(end - start)

# Initialize pygame
pygame.init()
display = pygame.display.set_mode((width, height))
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 10 * multiplier)
ticks = 40
clock = pygame.time.Clock()




# Draw environment
def drawEnv():
    global count

    pygame.draw.circle(display, (138, 132, 226), (51 * multiplier, height - 51 * multiplier), 10 * multiplier)
    pygame.draw.circle(display, (138, 132, 226), (31 * multiplier, height - 21 * multiplier), 10 * multiplier)
    pygame.draw.circle(display, (138, 132, 226), (71 * multiplier, height - 21 * multiplier), 10 * multiplier)
    pygame.draw.circle(display, (138, 132, 226), (71 * multiplier, height - 81 * multiplier), 10 * multiplier)
    pygame.draw.rect(display, (138, 132, 226),
                     pygame.Rect(23.5 * multiplier, height - 88.5 * multiplier, 15 * multiplier, 15 * multiplier))
    pygame.draw.rect(display, (138, 132, 226),
                     pygame.Rect(3.5 * multiplier, height - 58.5 * multiplier, 15 * multiplier, 15 * multiplier))
    pygame.draw.rect(display, (138, 132, 226),
                     pygame.Rect(83.5 * multiplier, height - 58.5 * multiplier, 15 * multiplier, 15 * multiplier))
    pygame.draw.rect(display, (138, 132, 226),
                     pygame.Rect(0 * multiplier, height - 1 * multiplier, 102 * multiplier, 1 * multiplier))
    pygame.draw.rect(display, (138, 132, 226),
                     pygame.Rect(0 * multiplier, height - 102 * multiplier, 102 * multiplier, 1 * multiplier))
    pygame.draw.rect(display, (138, 132, 226),
                     pygame.Rect(0 * multiplier, height - 102 * multiplier, 1 * multiplier, 102 * multiplier))
    pygame.draw.rect(display, (138, 132, 226),
                     pygame.Rect(101 * multiplier, height - 102 * multiplier, 1 * multiplier, 102 * multiplier))
    if count > 0:
        env = Environment(coordinates[0], clearance)
        if env.possiblePostion([int(coordinates[0][0] / multiplier), int(102 - coordinates[0][1] / multiplier)]):
            if radius != 0:
                pygame.draw.circle(display, (0, 0, 255), (coordinates[0][0], coordinates[0][1]), radius * multiplier, 1)
            pygame.draw.rect(display, (0, 0, 255),
                             pygame.Rect(coordinates[0][0], coordinates[0][1], multiplier, multiplier))

            textsurface = myfont.render("Initial Postion", False, (255, 0, 0))
            if height - coordinates[0][1] > 40:
                display.blit(textsurface, (coordinates[0][0] - 10 * multiplier, coordinates[0][1] + multiplier))
            else:
                display.blit(textsurface, (coordinates[0][0] - 10 * multiplier, coordinates[0][1] + multiplier - 40))
        else:
            print("Invalid position")
            count = 0
            coordinates.pop(0)

    if count > 1:
        env = Environment(coordinates[1], clearance)
        if env.possiblePostion([int(coordinates[1][0] / multiplier), int(102 - coordinates[1][1] / multiplier)]):
            if radius != 0:
                pygame.draw.circle(display, (0, 0, 255), (coordinates[1][0], coordinates[1][1]), radius * multiplier, 1)
            pygame.draw.rect(display, (0, 0, 255),
                             pygame.Rect(coordinates[1][0], coordinates[1][1], multiplier, multiplier))

            textsurface = myfont.render("Goal Postion", False, (255, 0, 0))
            if height - coordinates[1][1] > 40:
                display.blit(textsurface, (coordinates[1][0] - 10 * multiplier, coordinates[1][1] + multiplier))
            else:
                display.blit(textsurface, (coordinates[1][0] - 10 * multiplier, coordinates[1][1] + multiplier - 40))
        else:
            print("Invalid position")
            count = 1
            coordinates.pop(1)
    pygame.display.flip()
    clock.tick(ticks)

r = 0.033
l = 0.160


def drawPoint(x, y, color, size):
    pygame.draw.rect(display, color, pygame.Rect([x, height - y, size,size]))

def draw(x, y, theta, rpm1, rpm2, color, stroke):
    rpm1 /= 10
    rpm2 /= 10
    for _ in range(100):
        x += r / 2 * (rpm1 + rpm2) * cos(radians(theta))
        y += r / 2 * (rpm1 + rpm2) * sin(radians(theta))
        theta += r / l * (rpm1 - rpm2)
        drawPoint(x * multiplier, y * multiplier, color, stroke)
    return x, y, theta

# Draw arrow
def drawCurve(i, color, list, stroke):

    if list[i+1].action == "1":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],0, stepSize[1], color, stroke)
    if list[i+1].action == "2":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],stepSize[0], stepSize[1], color, stroke)
    if list[i+1].action == "3":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],stepSize[1], stepSize[1], color, stroke)
    if list[i+1].action == "4":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],stepSize[1], stepSize[0], color, stroke)
    if list[i+1].action == "5":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],stepSize[1], 0, color, stroke)
    if list[i+1].action == "6":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],0, stepSize[0], color, stroke)
    if list[i+1].action == "7":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],stepSize[0], stepSize[0], color, stroke)
    if list[i+1].action == "8":
        draw(list[i].env[0], list[i].env[1], list[i].env[2],stepSize[0], 0, color, stroke)



if len(solution) == 3:
    print("Unreachable goal.")
    for i in range(1, len(solution[2])):
        drawCurve(i, (255, 255, 255), solution[2], 2)
    drawEnv()
    pygame.display.flip()
else:
    path, search = solution[0], solution[1]
    path, search = solution[0], solution[1]
    # for i in range(1, len(search)):
    #     drawArrow(i, (255, 255, 255), search, 1)
    # draw()
    # pygame.display.flip()
    for i in range(0, len(search) - 1):
        pygame.event.get()
        drawCurve(i, (255, 255, 255), search, 2)
        # pygame.display.flip()
        # clock.tick(ticks)
    drawEnv()
    pygame.display.flip()
    for i in range(0, len(path) - 1):
        pygame.event.get()
        drawCurve(i, (255, 0, 255), path, 5)
        drawEnv()
        pygame.display.flip()
        clock.tick(ticks)

drawEnv()

temp = input("Enter something to exit.")
pygame.quit()
exit()

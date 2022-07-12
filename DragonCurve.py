import pygame
import math

pygame.init()
screenWidth = 1280
screenHeight = 1024
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Dragon")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def radian(grades: float):
    return grades * math.pi / 180


def rotate_point(point: list, rotatePoint: list, angle_: float):
    x0_ = rotatePoint[0]
    y0_ = rotatePoint[1]
    x_ = point[0]
    y_ = point[1]

    xn = (x_ - x0_) * math.cos(angle_) + (y_ - y0_) * math.sin(angle_) + x0_
    yn = -(x_ - x0_) * math.sin(angle_) + (y_ - y0_) * math.cos(angle_) + y0_
    new_point = [xn, yn]
    return new_point


def rotate_line(line_: list, rotatePoint_: list, angle_: float):
    x0_ = rotatePoint_[0]
    y0_ = rotatePoint_[1]

    newStartPoint = rotate_point(line_[0], rotatePoint_, angle_)
    newEndPoint = rotate_point(line_[1], rotatePoint_, angle_)

    new_line = [newStartPoint, newEndPoint]
    return new_line


def rotate_lines(lines_: list, rotatePoint_: list, angle_: float):
    x0_ = rotatePoint_[0]
    y0_ = rotatePoint_[1]

    new_lines_ = []
    for line_ in lines_:
        newStartPoint = rotate_point(line_[0], rotatePoint_, angle_)
        newEndPoint = rotate_point(line_[1], rotatePoint_, angle_)
        new_line_ = [newStartPoint, newEndPoint]
        new_lines_.append(new_line_)

    return new_lines_






clock = pygame.time.Clock()
timer = 0
corePoint = [screenWidth / 2, screenHeight / 2 - 50]
initLine = [corePoint, [screenWidth / 2, screenHeight / 2 + 50]]
lines = [initLine]
stages = [radian(alpha) for alpha in range(0, 90, 2)]
stageIter = 0
scale = 1


running = True
stop = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        stop = True
    if key[pygame.K_RIGHT]:
        stop = False
    if stop:
        continue

    screen.fill(WHITE)
    clock.tick(60)
    angle = radian(90)
    scale *= 0.995
    w_shift = -(scale - 1) * (screenWidth / 2)
    h_shift = -(scale - 1) * (screenHeight / 2)

    for line in lines:
        pygame.draw.line(screen, BLACK,
                         [line[0][0] * scale + w_shift, line[0][1] * scale + h_shift],
                         [line[1][0] * scale + w_shift, line[1][1] * scale + h_shift])

    timer = pygame.time.get_ticks()
    tempLines = rotate_lines(lines, corePoint, stages[stageIter])
    for line in tempLines:
        pygame.draw.line(screen, GREEN,
                         [line[0][0] * scale + w_shift, line[0][1] * scale + h_shift],
                         [line[1][0] * scale + w_shift, line[1][1] * scale + h_shift])
    stageIter += 1


    if stageIter >= len(stages) - 1:                              # if pygame.time.get_ticks() - timer > 2000:
        stageIter = 0
        timer = pygame.time.get_ticks()
        newLines = rotate_lines(lines, corePoint, angle)
        for newLine in reversed(newLines):
            lines.append(newLine)
        corePoint = lines[-1][1]






    pygame.display.update()







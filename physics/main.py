import pygame
#from numba import njit
from random import randint

# global variables
height = 600
width = 1200
half_height = height // 2
half_width = width // 2
fps = 60
g = -9.81
h = -half_height
w = half_width
v, vw = randint(-100, 100), randint(-100, 100)
dt = 0.2
rad = 10
material = 1.05
innersion = 0.25
console_pos = (0, 0)
c_par = (400, 500)
c_visualisate = False
atschot = False
atschott = 0


def text():
    font = pygame.font.SysFont('Arial', 12, bold = True)
    apply = font.render('Press fn + F1, to acsess console', 0, (0, 0, 0))
    sc.blit(apply, (width - 190, 5))
    apply = font.render('Press fn + F1, to acsess console', 0, (0, 0, 0))
    sc.blit(apply, (width - 190, 5))

class Console:
    def __init__(self, sc):
        self.sc = sc

    def visual(self, cv):
        if cv:
            pygame.draw.rect(self.sc, (0, 0, 0), (console_pos, c_par))

#@njit(fastmath=True)
def Ft(h, v, w, vw):
    v += g * dt
    h = h + v * dt
    if vw >= innersion * dt:
        vw += -innersion * dt
    elif vw <= -innersion * dt:
        vw += innersion * dt
    else:
        vw = 0
    w += vw * dt
    return h, v, w, vw


#@njit(fastmath=True)
def obj_collision(h, v, w, vw):
    if int(h) >= 0 - rad and v >= 0 or int(h) <= -height + rad and v <= 0:
        v = -(v / material)
    if int(-h) >= height - rad and abs(v) <= 1 or int(-h) <= 0 + rad and abs(v) <= 1:
        h, v = (-height + rad, 0) if int(-h) >= height - rad else (0 - rad, 0)
    if int(w) <= 0 + rad and vw <= 0 or int(w) >= width - rad and vw >= 0:
        vw = -(vw / material)
    return h, v, w, vw


pygame.init()
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
console = Console(sc)
pygame.mouse.set_visible(False)
pygame.display.set_caption('physics')


while True:
    sc.fill((220, 220, 220))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    h, v, w, vw = Ft(h, v, w, vw)

    h, v, w, vw = obj_collision(h, v, w, vw)

    pygame.draw.circle(sc, (220, 0, 0), (int(w), int(-h)), rad)

    if keys[pygame.K_F1] and atschot == False:
        c_visualisate = c_visualisate == False
        atschot = True

    console.visual(c_visualisate)

    text()

    if atschot:
        if atschott == 30:
            atschot = False
            atschott = 0
        else:
            atschott += 1

    pygame.display.flip()
    clock.tick(fps)

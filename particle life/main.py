import pygame
import sys
import time
import datetime
from random import randrange, choice


# Initialize Pygame
pygame.init()
stop_distance=10
number_particles=100
speed = 1
max_velocity=100
FPS = 60 * speed
DT=1/FPS
# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Pygame Window")
clock = pygame.time.Clock()
# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.Font(None, 30)
decode_color = {
    1: "red",
    2: "blue",
    # 3: "green",4:'yellow'
}


properties = {1: {1: -1, 2: 0}, 2: {1: 0, 2: 1}}


class particle:
    def __init__(
        self,
        color: int,
        pos: list[int, int],
        screen: pygame.display,
        mass=1,
        velocity: list[int, int] = [0, 0],
        acceleration: list[int, int] = [0, 0],
    ):
        self.pos = pos
        self.old_pos = pos
        self.velocity = velocity

        self.acceleration = acceleration
        self.color = color
        self.screen = screen
        self.mass = mass
        self.time = time.time()

    def draw(self):

        DT = (time.time() - self.time) * speed
        self.time = time.time()
        self.old_pos = self.pos
        self.velocity[0] += self.acceleration[0] * DT
        self.velocity[1] += self.acceleration[1] * DT
        self.velocity[0] = get_sign(self.velocity[0]) * min(max_velocity, abs(self.velocity[0]))
        self.velocity[1] = get_sign(self.velocity[1]) * min(max_velocity, abs(self.velocity[1]))
        self.pos[0] += self.velocity[0] * DT
        self.pos[1] += self.velocity[1] * DT
        if self.pos[0] > WIDTH:
            self.pos[0] = WIDTH
            self.velocity[0]=-self.velocity[0]
        elif self.pos[0] < 0:
            self.pos[0] = 0
            self.velocity[0]=-self.velocity[0]
        if self.pos[1] > HEIGHT:
            self.pos[1] = HEIGHT
            self.velocity[1]=-self.velocity[1]
        elif self.pos[1] < 0:
            self.velocity[1]=-self.velocity[1]
            self.pos[1] = 0
        pygame.draw.circle(
            self.screen,
            decode_color[self.color],
            self.pos,
            stop_distance//2,
        )
        print(self.acceleration, self.velocity, self.acceleration[1] * DT, self.pos)


def display_time(screen):
    now = datetime.datetime.now()
    text = font.render(str(now.time()), True, BLACK)
    text_rect = text.get_rect(center=(90, 15))
    screen.blit(text, text_rect)


particles = []
# make particles
for i in range(number_particles):
    particles.append(
        particle(
            choice([1]),
            [randrange(0, WIDTH), randrange(0, HEIGHT)],
            screen,
            1,
            # [randrange(-30, 30), randrange(-30, 30)],
            # [randrange(-10, 10), randrange(-10, 10)],
        )
    )

# particles.append(
#     particle(
#         1,
#         [110, 200],
#         screen,
#         1,
#     )
# )
# particles.append(
#     particle(
#         1,
#         [100, 210],
#         screen,
#         1,
#     )
# )


def square_distance(pos1, pos2):
    return ((pos1[0] - pos2[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 1


force_constant = 1000


def get_sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def draw(screen):
    display_time(screen)
    print(particles)
    for i in particles:
        i.acceleration = [0, 0]
        for j in particles:
            # print(i.color,j.color)
            # print(properties[i.color][j.color],(j.old_pos[1] - i.old_pos[1]))

            if (
                square_distance(i.old_pos, j.old_pos) != 0
                and square_distance(i.old_pos, j.old_pos) > 10
            ):
                i.acceleration[0] += (
                    force_constant
                    * properties[i.color][j.color]
                    * get_sign(j.old_pos[0] - i.old_pos[0])
                ) / square_distance(i.old_pos, j.old_pos)
                i.acceleration[1] += (
                    force_constant
                    * properties[i.color][j.color]
                    * get_sign(j.old_pos[1] - i.old_pos[1])
                ) / square_distance(i.old_pos, j.old_pos)
            if (
                square_distance(i.old_pos, j.old_pos) != 0
                and square_distance(i.old_pos, j.old_pos) < stop_distance
            ):
                i.acceleration[0] += (
                    force_constant
                    * -10
                    * get_sign(j.old_pos[0] - i.old_pos[0])
                    * properties[i.color][j.color]
                ) / square_distance(i.old_pos, j.old_pos)
                i.acceleration[1] += (
                    force_constant
                    * -10
                    * get_sign(j.old_pos[1] - i.old_pos[1])
                    * properties[i.color][j.color]
                ) / square_distance(i.old_pos, j.old_pos)

        i.draw()
        # print(i.acceleration)


# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw something (e.g., a black rectangle)
    draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
# Quit Pygame
pygame.quit()
sys.exit()

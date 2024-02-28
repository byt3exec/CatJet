import pygame
import random

pygame.init()

# Game Variables
screen_width = 400
screen_height = 600
floor_height = 100
gravity = 0.5
Cat_movement = 0
game_active = True

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

Cat_surface = pygame.image.load('assets/Cat.png').convert_alpha()
Cat_rect = Cat_surface.get_rect(center=(100, screen_height // 2))

bg_surface = pygame.image.load('assets/background.png').convert()
floor_surface = pygame.Surface((screen_width, floor_height))
floor_surface.fill((255, 255, 255))

pipe_surface = pygame.image.load('assets/pipe.png').convert()
pipe_list = []
PIPE_SPAWN = pygame.USEREVENT
pygame.time.set_timer(PIPE_SPAWN, 1200)
pipe_height = [200, 300, 400]

# Main Game Loop
def main():
    global Cat_movement, game_active
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    Cat_movement = 0
                    Cat_movement -= 10
                if event.key == pygame.K_SPACE and not game_active:
                    game_active = True
                    pipe_list.clear()
                    Cat_rect.center = (100, screen_height // 2)
                    Cat_movement = 0

            if event.type == PIPE_SPAWN:
                pipe_list.extend(create_pipe())

        # Game Mechanics
        screen.blit(bg_surface, (0, 0))
        if game_active:
            # Cat
            Cat_movement += gravity
            Cat_rect.centery += Cat_movement
            screen.blit(Cat_surface, Cat_rect)
            game_active = check_collision(pipe_list)

            # Pipes
            pipe_list = move_pipes(pipe_list)
            draw_pipes(pipe_list)
        else:
            pass

        # Floor
        screen.blit(floor_surface, (0, screen_height - floor_height))

        pygame.display.update()
        clock.tick(120)

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(500, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return [pipe for pipe in pipes if pipe.right > -50]

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if Cat_rect.colliderect(pipe):
            return False
    return True

if __name__ == '__main__':
    main()
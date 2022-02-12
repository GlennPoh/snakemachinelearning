import pygame
import random
import time

def update_speed(direction):
    global x, y
    if direction == "up":
        y -= vel
        x += 0
    elif direction == "right":
        x += vel
        y += 0
    elif direction == "down":
        y += vel
        x += 0
    elif direction == "left":
        x -= vel
        y += 0

if __name__ == '__main__':
    pygame.init()
    run = True

    x = 300
    y = 450
    screen_width = 600
    screen_height = 900

    clock = pygame.time.Clock()
    vel = 5
    direction = "right"

    font_style = pygame.font.SysFont(None, 50)
    score = 0

    foodx = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0

    def show_message(msg, color, pos):
        message = font_style.render(msg, True, color)
        screen.blit(message, pos)

    while run:
        screen = pygame.display.set_mode((600, 900), 0, 0, 0, 0)
        pygame.display.set_caption('First Snake Game')
        rect = pygame.Rect(10, 10, 590, 890)
        pygame.draw.rect(screen, (255, 0, 0), (5, 5, 590, 890), 1)
        snake = pygame.draw.rect(screen, (0, 255, 0), [x, y, 20, 20])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # y -= 10
                    direction = "up"
                if event.key == pygame.K_RIGHT:
                    # x += 10
                    direction = "right"
                if event.key == pygame.K_DOWN:
                    # y += 10
                    direction = "down"
                if event.key == pygame.K_LEFT:
                    # x -= 10
                    direction = "left"
            else:
                update_speed(direction)

        if x + 20 >= 590 or x + 20 <= 5 or y + 20 >= 890 or y + 20 <= 5:
            run = False

        pygame.draw.rect(screen, (255, 255, 255), [foodx, foody, 20, 20])
        pygame.draw.rect(screen, (0, 255, 0), [x, y, 20, 20])
        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
            score += 1
        # game will run at max 30 fps
        clock.tick(30)


show_message('Game Over', (255,255,255), [200, 50])
score_msg = "Score: " + str(score)
show_message(score_msg, (255,255,255), [200, 100])
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()
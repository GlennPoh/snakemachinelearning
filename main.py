import pygame
import random
import time


def show_message(msg, color, pos):
    message = font_style.render(msg, True, color)
    screen.blit(message, pos)


def update_speed():
    global x, y, direction
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

    font_style = pygame.font.SysFont("Times", 50)
    score = 0

    food_x = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0

    snake_List = []
    snake_length = 1

    def draw_snake(snake_list, snake_block):
        for coordinate in snake_list:
            pygame.draw.rect(screen, [0, 255, 0], [coordinate[0], coordinate[1], snake_block, snake_block])

    while run:
        screen = pygame.display.set_mode((600, 900), 0, 0, 0, 0)
        pygame.display.set_caption('First Snake Game')
        rect = pygame.Rect(10, 10, 590, 890)
        pygame.draw.rect(screen, (255, 0, 0), (5, 5, 590, 890), 1)
        # snake = pygame.draw.rect(screen, (0, 255, 0), [x, y, 20, 20])

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
                update_speed()

        if x + 20 >= 590 or x + 20 <= 5 or y + 20 >= 890 or y + 20 <= 5:
            run = False

        snake_head = [x, y]
        snake_List.append(snake_head)
        if len(snake_List) > snake_length:
            del snake_List[0]

        for i in snake_List[:-1]:
            if i == snake_head:
                game_close = True

        draw_snake(snake_List, 30)
        pygame.draw.rect(screen, (255, 255, 255), [food_x, food_y, 20, 20])
        # pygame.draw.rect(screen, (0, 255, 0), [x, y, 20, 20])
        pygame.display.update()

        if y - 25 < food_y < y + 25:
            if x + 25 > food_x > x - 25:
                food_x = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
                food_y = round(random.randrange(0, screen_width - 20) / 10.0) * 10.0
                snake_length += 1
                vel += 1
                score += 1

        # game will run at max 30 fps
        clock.tick(30)


show_message('Game Over', (255, 255, 255), [200, 50])
score_msg = "Score: " + str(score)
show_message(score_msg, (255, 255, 255), [200, 100])
pygame.display.update()
time.sleep(3)

pygame.quit()
quit()

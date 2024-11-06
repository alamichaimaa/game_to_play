import pygame
import random

pygame.init()

main_width, main_height = 600, 400

game_width, game_height = 400, 300
game_x, game_y = 100, 80  


background_color = (230, 230, 230)    # Main window background
score_area_color = (200, 220, 250)     # Score area background
game_area_color = (180, 180, 180)      # Game area background
text_color = (0, 0, 0)                 # Text color
snake_color = (34, 139, 34)            # Snake color
food_color = (255, 69, 0)              # Food color


dis = pygame.display.set_mode((main_width, main_height))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont(None, 30)

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()


def display_score(score):
    score_text = font.render("Score: " + str(score), True, text_color)
    dis.blit(score_text, (20, 20))  


def draw_game_area():
    pygame.draw.rect(dis, game_area_color, (game_x, game_y, game_width, game_height))


def message(msg, color, y_offset):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [main_width / 6, main_height / 3 + y_offset])

def gameLoop():
    game_over = False
    game_close = False

    x1 = game_x + game_width / 2
    y1 = game_y + game_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(game_x, game_x + game_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(game_y, game_y + game_height - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over:
        while game_close:
            dis.fill(background_color)
            message("You Lost! Press C to Play Again or Q to Quit", text_color, 0)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= game_x + game_width or x1 < game_x or y1 >= game_y + game_height or y1 < game_y:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(background_color)  

        pygame.draw.rect(dis, score_area_color, (0, 0, main_width, 50))
        display_score(score)  


        draw_game_area()

        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True


        for segment in snake_list:
            pygame.draw.rect(dis, snake_color, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()


        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(game_x, game_x + game_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(game_y, game_y + game_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 1 

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
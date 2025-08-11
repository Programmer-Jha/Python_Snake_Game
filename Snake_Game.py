# Developed by: Aniket Kumar Jha

import pygame
import time
import random
import os

# Initialize
pygame.init()

# Window setup
width, height = 1200, 760
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Game")

# Colors
white = (255, 255, 255)
food_color = (255, 140, 0)  # Bright orange for normal food
green = (0, 255, 0)
black = (0, 0, 0)
blue = (50, 153, 213)
yellow = (255, 255, 102)
special_food_color = (255, 0, 255)  # Purple for special big ball
red = (255, 0, 0)

# Fonts
font_style = pygame.font.SysFont("comicsansms", 24)
score_font = pygame.font.SysFont("comicsansms", 20)

# Game variables
snake_block = 10
snake_speed = 13
clock = pygame.time.Clock()

# High score file
HIGH_SCORE_FILE = "highscore.txt"

# Function to get player's name via input box
def get_player_name():
    input_box = pygame.Rect(width//3, height//3, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.strip() != '':
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 15:
                            text += event.unicode
        
        win.fill(black)
        msg = font_style.render("Enter your name:", True, white)
        win.blit(msg, (width//3, height//3 - 30))

        txt_surface = font_style.render(text, True, color)
        width_box = max(200, txt_surface.get_width()+10)
        input_box.w = width_box
        win.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(win, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

    return text.strip()

# Load high score with name
def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'r') as f:
            line = f.readline().strip()
            if ':' in line:
                name, score = line.split(':')
                return name.strip(), int(score.strip())
    return "NoName", 0

# Save high score with name
def save_high_score(name, score):
    with open(HIGH_SCORE_FILE, 'w') as f:
        f.write(f"{name}: {score}")

# Show score and high score with name
def your_score(score, high_score, high_score_name):
    val = score_font.render(f"Score: {score}   High Score: {high_score} ({high_score_name})", True, yellow)
    win.blit(val, [10, 10])

# Draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

# Show message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

# Generate food position not on snake
def generate_food(snake_list):
    while True:
        foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
        if [foodx, foody] not in snake_list:
            return foodx, foody

# Game loop
def game_loop():
    player_name = get_player_name()
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx, foody = generate_food(snake_List)

    high_score_name, high_score = load_high_score()

    score = 0
    food_eaten = 0

    special_food = None
    special_food_timer = 0
    special_food_value = 0

    while not game_over:
        while game_close:
            win.fill(black)
            message("You crashed! Press C to Play Again or Q to Quit", red)
            your_score(score, high_score, high_score_name)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        game_loop()
                        return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        win.fill(blue)

        # Draw normal food (orange square)
        pygame.draw.rect(win, food_color, [foodx, foody, snake_block, snake_block])

        # Draw special food (big purple ball) if active
        if special_food:
            pygame.draw.circle(win, special_food_color, (special_food[0] + snake_block // 2, special_food[1] + snake_block // 2), 12)

            # Timer countdown
            special_food_timer -= 1 / snake_speed
            if special_food_timer <= 0:
                special_food = None
            else:
                special_food_value = max(1, int(special_food_timer))

            # Render timer text centered inside special food ball
            timer_text = font_style.render(str(special_food_value), True, white)
            text_rect = timer_text.get_rect(center=(special_food[0] + snake_block // 2, special_food[1] + snake_block // 2))
            win.blit(timer_text, text_rect)

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check collision with self
        for segment in snake_List[:-1]:
            if segment == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)

        # Check if snake eats normal food
        if x1 == foodx and y1 == foody:
            Length_of_snake += 1
            score += 1
            food_eaten += 1
            foodx, foody = generate_food(snake_List)

            # Spawn special food every 5 normal foods eaten
            if food_eaten % 5 == 0:
                special_food = generate_food(snake_List)
                special_food_timer = 11  # seconds
                special_food_value = 11

        # Check if snake eats special food (distance based collision)
        if special_food:
            snake_center_x = x1 + snake_block / 2
            snake_center_y = y1 + snake_block / 2
            food_center_x = special_food[0] + snake_block / 2
            food_center_y = special_food[1] + snake_block / 2

            distance = ((snake_center_x - food_center_x) ** 2 + (snake_center_y - food_center_y) ** 2) ** 0.5
            snake_half_diag = (2 * (snake_block / 2) ** 2) ** 0.5  # approx half diagonal of snake block
            special_ball_radius = 12

            if distance < snake_half_diag + special_ball_radius:
                Length_of_snake += 1
                score += special_food_value
                special_food = None

        # Update high score
        if score > high_score:
            high_score = score
            high_score_name = player_name
            save_high_score(high_score_name, high_score)

        your_score(score, high_score, high_score_name)
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
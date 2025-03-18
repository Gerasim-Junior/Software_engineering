import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Размеры окна
WIDTH = 600
HEIGHT = 400

# Создание окна
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра "Змейка"')

# Настройки игры
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Шрифты
font_style = pygame.font.SysFont('Times', 25)
score_font = pygame.font.SysFont('Times', 35)

# Функция отображения счета
def display_score(score):
    value = score_font.render('Счёт: ' + str(score), True, WHITE)
    game_window.blit(value, [20, 10])

# Отрисовка змейки
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(game_window, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Вывод сообщения
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_window.blit(mesg, [WIDTH // 6, HEIGHT // 3])

# Экран окончания игры
def game_over_screen(score):
    game_window.fill(BLACK)
    message = font_style.render(f"Игра окончена! Ваш счёт: {score}", True, RED)
    game_window.blit(message, [WIDTH // 6, HEIGHT // 3])
    message2 = font_style.render("Нажмите R для рестарта или Q для выхода.", True, RED)
    game_window.blit(message2, [WIDTH // 6, HEIGHT // 2])
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_r:
                    game_loop()  # Перезапуск игры
                    waiting = False  # Выход из цикла ожидания

# Основной игровой цикл
def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Проверка на запрет противоположных направлений
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = BLOCK_SIZE
                    x_change = 0

                # Проверка на движение в противоположном направлении
                # Если змейка двигается вправо, она не может сразу двигаться влево
                if event.key == pygame.K_LEFT and x_change == BLOCK_SIZE:
                    game_over_screen(snake_length - 1)  # Если это противоположное направление, игра заканчивается
                    return
                if event.key == pygame.K_RIGHT and x_change == -BLOCK_SIZE:
                    game_over_screen(snake_length - 1)
                    return
                if event.key == pygame.K_UP and y_change == BLOCK_SIZE:
                    game_over_screen(snake_length - 1)
                    return
                if event.key == pygame.K_DOWN and y_change == -BLOCK_SIZE:
                    game_over_screen(snake_length - 1)
                    return

        # Движение змейки
        x += x_change
        y += y_change

        # Проход через стены
        if x >= WIDTH:
            x = 0
        elif x < 0:
            x = WIDTH - BLOCK_SIZE
        if y >= HEIGHT:
            y = 0
        elif y < 0:
            y = HEIGHT - BLOCK_SIZE

        game_window.fill(BLACK)
        pygame.draw.rect(game_window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Создание змейки
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Проверка столкновения с собой
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over_screen(snake_length - 1)
                return  # Выход из game_loop()

        draw_snake(snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        # Поедание еды
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        pygame.time.Clock().tick(SNAKE_SPEED)

# Главная функция
def main():
    game_loop()

main()

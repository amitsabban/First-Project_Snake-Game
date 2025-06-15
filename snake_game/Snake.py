import pygame
import random
import pandas as pd


# classes
class Player:
    global screen_size_x
    global screen_size_y

    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = 100
        self.y = 40
        self.move = 10
        self.direction = 5
        self.speed = 100

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] \
                and self.y >= self.height \
                and self.direction != 1\
                and self.direction != 6:
            self.direction = 0
        elif keys[pygame.K_DOWN] \
                and self.y <= screen_size_y - 2 * self.height \
                and self.direction != 0\
                and self.direction != 6:
            self.direction = 1
        elif keys[pygame.K_LEFT] \
                and self.x >= self.width \
                and self.direction != 3\
                and self.direction != 6:
            self.direction = 2
        elif keys[pygame.K_RIGHT] \
                and self.x <= screen_size_x - 2 * self.width \
                and self.direction != 2\
                and self.direction != 6:
            self.direction = 3

        if self.direction == 0 \
                and self.y >= self.height:
            self.y -= self.move
        elif self.direction == 1 \
                and self.y <= screen_size_y - 2 * self.height:
            self.y += self.move
        elif self.direction == 2 \
                and self.x >= self.width:
            self.x -= self.move
        elif self.direction == 3 \
                and self.x <= screen_size_x - 2 * self.width:
            self.x += self.move

    def snake_head(self):
        pygame.draw.rect(screen, black,
                         (self.x, self.y, snake.width, snake.height))


class Food:
    def __init__(self):
        self.x = random.randrange(1, 47) * 10
        self.y = random.randrange(1, 47) * 10
        self.width = 10
        self.height = 10
        self.image = pygame.image.load("pictures\\apple.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def display_food(self):
        screen.blit(self.image, (self.x, self.y))


class Tail:
    def __init__(self):
        self.x = 10
        self.y = 10

    def new_tail(self):
        for i in game.snake_lst:
            pygame.draw.rect(screen, snake_body_color,
                             (i[0], i[1], self.x, self.y))


class Game:
    global screen_size_x
    global screen_size_y

    def __init__(self):
        self.score_count = 0
        self.snake_lst = []
        self.snake_len = 0
        self.running = True
        self.snake_head = []
        self.flag = 0

    def menu(self):
        while self.running:
            pygame.time.delay(100)
            screen.fill(white)
            menu_page()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()

    def exit_game(self):
        self.flag = 0
        self.running = False
        score_board()

    def restart(self):
        self.flag = 0
        self.running = True
        score_board()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            snake.speed = 100
            self.score_count = 0
            self.snake_lst = []
            self.snake_len = 0
            self.snake_head = []
            game.gameloop()
            pygame.display.update()

    def gameloop(self):
        snake.x = 140
        snake.y = 60
        snake.direction = 5
        while self.running:
            screen.fill(black)
            screen.blit(back_ground_game, (0, 0))
            pygame.time.delay(snake.speed)
            tail.new_tail()
            snake.snake_head()
            food.display_food()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screen.fill(black)
                    self.running = False

            pygame.time.get_ticks()
            self.snake_head = [snake.x, snake.y]
            self.snake_lst.append(self.snake_head)
            snake.movement()

            if snake.x == food.x \
                    and snake.y == food.y:
                food.x = random.randrange(1, 47) * 10
                food.y = random.randrange(1, 47) * 10
                snake.speed -= 1
                self.score_count += 1
                self.snake_len += 1
                if self.snake_len % 5 == 0:
                    snake.speed -= 2
            value = main_font.render("Score: " + str(self.score_count), True, grey)
            screen.blit(value, [10, 0])

            if len(self.snake_lst) > self.snake_len:
                del self.snake_lst[0]

            # game over for those terms:
            for i in self.snake_lst[1:]:
                if self.snake_lst[0] == i:
                    game_over()
                    snake.direction = 6

            if snake.x == 0 \
                    or snake.y == 0 \
                    or snake.x == screen_size_x - 10 \
                    or snake.y == screen_size_y - 10:
                game_over()
            pygame.display.update()


def score_board_menu():
    score_board_df()
    global high_score
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        pygame.mouse.set_visible(True)
        screen.fill(white)
        screen.blit(score_board_back_ground, (0, 125))
        score_board_font = font_over.render("Score Board", False, black)
        screen.blit(score_board_font, (71, 40))
        first_name = high_score.iloc[0][0]
        second_name = high_score.iloc[1][0]
        third_name = high_score.iloc[2][0]
        first_score = str(high_score.iloc[0][1])
        second_score = str(high_score.iloc[1][1])
        third_score = str(high_score.iloc[2][1])
        first = main_font.render(first_name, False, white)
        screen.blit(first, (215, 320))
        second = main_font.render(second_name, False, white)
        screen.blit(second, (65, 380))
        third = main_font.render(third_name, False, white)
        screen.blit(third, (370, 390))
        first = main_font.render(first_score, False, white)
        screen.blit(first, (230, 360))
        second = main_font.render(second_score, False, white)
        screen.blit(second, (85, 420))
        third = main_font.render(third_score, False, white)
        screen.blit(third, (390, 435))
        button(blue, light_blue, 15, 3, 20, 0, 75, 40,  "Back", "back_to_menu")
        button(light_red, red, 420, 3, 425, 0, 75, 40, "Quit", "exit")
        pygame.display.update()


def score_board_game_over():
    score_board_df()
    global high_score
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
        pygame.mouse.set_visible(True)
        screen.fill(white)
        screen.blit(score_board_back_ground, (0, 125))
        score_board_font = font_over.render("Score Board", False, black)
        screen.blit(score_board_font, (71, 40))
        first_name = high_score.iloc[0][0]
        second_name = high_score.iloc[1][0]
        third_name = high_score.iloc[2][0]
        first_score = str(high_score.iloc[0][1])
        second_score = str(high_score.iloc[1][1])
        third_score = str(high_score.iloc[2][1])
        first = main_font.render(first_name, False, white)
        screen.blit(first, (215, 320))
        second = main_font.render(second_name, False, white)
        screen.blit(second, (65, 380))
        third = main_font.render(third_name, False, white)
        screen.blit(third, (370, 390))
        first = main_font.render(first_score, False, white)
        screen.blit(first, (230, 360))
        second = main_font.render(second_score, False, white)
        screen.blit(second, (90, 410))
        third = main_font.render(third_score, False, white)
        screen.blit(third, (390, 435))
        button(blue, light_blue, 15, 3, 20, 0, 115, 40, "Restart", "restart")
        button(light_red, red, 420, 3, 425, 0, 75, 40, "Quit", "exit")
        pygame.display.update()


def game_over():
    if game.flag == 0:
        score_board()
        score_board_df()
        game.flag = 1
    screen.fill(white)
    pygame.mouse.set_visible(True)
    screen.blit(back_ground_end, (-40, -10))
    game_over_font = font_over.render("GameOver", False, black)
    screen.blit(game_over_font, (180, 275))
    name = score_font.render(str(player_name) + "'s", False, black)
    screen.blit(name, (265, 0))
    score = score_font.render("Score: " + str(game.score_count), False, black)
    screen.blit(score, (235, 45))
    author = small_font.render("Amit Sabban", False, light_red)
    screen.blit(author, (30, 470))
    button(light_grey, grey, 247, 140, 255, 140, 190, 50, "Score-Board", "score_board_game_over")
    button(light_green, green, 280, 200, 285, 195, 115, 40, "Restart", "restart")
    button(light_red, red, 300, 250, 305, 245, 75, 35, "Quit", "exit")


def menu_page():
    score_board_df()
    pygame.mouse.set_visible(True)
    screen.blit(back_ground_menu, (0, 0))
    game_name = font_name.render("Snake", False, black)
    screen.blit(game_name, (220, 10))
    author = small_font.render("Amit Sabban", False, light_red)
    screen.blit(author, (30, 470))
    button(light_green, green, 272, 140, 278, 140, 145, 44, "Play game", "name_box")
    button(light_grey, grey, 250, 220, 255, 220, 190, 50, "Score-Board", "score_board_menu")
    button(light_red, red, 300, 300, 310, 300, 85, 50, "Quit", "exit")
    pygame.display.update()


def button(color1, color2, x, y, x_loc, y_loc, width, height, text='', action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, color2, (x, y, width, height))
        if click[0] == 1 and action is not None:
            if action == "exit":
                action = None
                game.exit_game()
            if action == "name_box":
                action = None
                name_box()
            if action == "restart":
                action = None
                game.restart()
            if action == "back_to_menu":
                action = None
                game.menu()
            if action == "score_board_menu":
                action = None
                score_board_menu()
            if action == "score_board_game_over":
                action = None
                score_board_game_over()
    else:
        pygame.draw.rect(screen, color1, (x, y, width, height))
    text = main_font.render(text, False, black)
    screen.blit(text, (x_loc, y_loc))


def name_box():
    global player_name
    name_screen = pygame.display.set_mode((screen_size_x, screen_size_y))
    input_box = pygame.Rect(150, 90, 140, 40)
    color = black
    active = True
    text = ''
    done = False
    while not done:
        for event in pygame.event.get():
            pygame.mouse.set_visible(False)
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text == "":
                            player_name_2 = main_font.render("Please Enter Your Name:", False, red)
                            name_screen.blit(player_name_2, (80, 30))
                            pygame.display.update()
                            pygame.time.wait(500)
                        else:
                            player_name = text.capitalize()
                            done = True
                            game.gameloop()
                            text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        name_screen.blit(rules_back_ground, (0, 0))
        text_surface = main_font.render(text, False, color)
        width = max(200, text_surface.get_width() + 10)
        input_box.w = width
        name_screen.blit(text_surface, (input_box.x + 5, input_box.y - 8))
        pygame.draw.rect(name_screen, color, input_box, 2)
        player_name = main_font.render("Please Enter Your Name:", False, black)
        name_screen.blit(player_name, (80, 30))
        submit_name = name_font.render("Press Enter To Start Playing", False, black)
        name_screen.blit(submit_name, (110, 160))
        rules = main_font.render("Rules:", False, black)
        name_screen.blit(rules, (60, 210))
        pygame.display.update()


# data frame:
def score_board():
    try:
        with open("Score_Board.csv", 'a') as s_b_csv:
            s_b_csv.write(player_name + ',' + str(game.score_count) + '\n')
    except:
        print("File not Found")

def score_board_df():
    global high_score
    df = pd.read_csv("Score_Board.csv", delimiter=',')
    score_board_sorted = df.sort_values("Score", ascending=False).drop_duplicates()
    high_score = score_board_sorted.head(3)


# init
pygame.init()

# classes objects
game = Game()
snake = Player()
food = Food()
tail = Tail()

# variables
player_name = ""
high_score = []

# screen
screen_size_x = 500
screen_size_y = 500

# colors
snake_head_color = (93, 116, 4)
snake_body_color = (215, 138, 75)
white = (255, 255, 255)
light_red = (255, 0, 0)
red = (200, 0, 0)
light_green = (0, 255, 0)
green = (150, 208, 47)
black = (0, 0, 0)
light_grey = (220, 220, 220)
grey = (200, 200, 200)
light_blue = (0, 0, 255)
blue = (149, 202, 255)

# fonts
font_name = pygame.font.SysFont("Comic Sans MS", 85)
font_over = pygame.font.SysFont("Comic Sans MS", 65)
score_font = pygame.font.SysFont("Comic Sans MS", 50)
main_font = pygame.font.SysFont("Comic Sans MS", 30)
name_font = pygame.font.SysFont("Comic Sans MS", 20)
small_font = pygame.font.SysFont("Comic Sans MS", 18)

# game screen
screen = pygame.display.set_mode((screen_size_x, screen_size_y))
pygame.display.set_caption("Snake")
over_screen = pygame.display.set_mode((screen_size_x, screen_size_y))
pygame.display.set_caption("Snake")

# pictures
icon = pygame.image.load("pictures\\snake_icon.png")
pygame.display.set_icon(icon)
back_ground_menu = pygame.image.load("pictures\\snake_bg_menu.png")
back_ground_end = pygame.image.load("pictures\\snake_bg_end.png")
back_ground_game = pygame.image.load("pictures\\grass_bg.png")
rules_back_ground = pygame.image.load("pictures\\rules_bg.png")
score_board_back_ground = pygame.image.load("pictures\\score_board_bg.png")
apple_image = pygame.image.load("pictures\\apple.png")

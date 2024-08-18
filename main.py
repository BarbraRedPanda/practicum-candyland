import pygame
import random

pygame.init()


screen = pygame.display.set_mode((800,600))

bg_image = pygame.transform.scale(pygame.image.load('bg.png'), (800,600))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

tile_positions = [
   (0,0), (473, 589), (342, 109), (175, 392), (783, 520), (150, 219), (670, 295), (302, 510), (119, 548), (774, 167), (406, 396), 
(425, 97), (619, 483), (564, 325), (253, 251), (617, 193), (596, 438), (63, 247), (185, 367), (530, 82), (689, 295), 
(305, 537), (721, 420), (488, 453), (405, 587), (197, 118), (741, 290), (567, 183), (304, 407), (690, 577), (488, 140), 
(49, 398), (121, 522), (782, 284), (307, 171), (469, 580), (149, 268), (546, 326), (412, 217), (637, 453), (174, 167), 
(735, 482), (198, 279), (452, 224), (583, 592), (121, 374), (697, 136), (399, 213), (568, 408), (370, 569), (646, 207), 
(289, 426), (778, 152), (120, 450), (559, 540), (423, 309), (658, 348), (240, 139), (483, 389), (142, 165), (749, 425), 
(220, 272), (305, 293), (663, 248), (125, 209), (438, 504), (361, 311), (274, 174), (676, 547), (543, 232), (184, 569), 
(735, 363), (489, 178), (219, 485), (276, 321), (633, 191), (78, 509), (310, 348), (129, 449), (385, 489), (698, 163), 
(143, 347), (457, 205), (710, 452), (229, 382), (511, 594), (66, 279), (154, 568), (308, 434), (699, 143), (596, 225), 
(334, 526), (582, 410), (385, 99), (423, 126), (618, 373), (462, 564), (155, 387), (645, 277), (282, 143), (711, 564)

]

class Player:
    def __init__(self, color):
        self.color = color;
        self.currentTile = 0;
        self.rect = pygame.Rect(tile_positions[0], (30,30))

    def move(self, newTile):
        self.currentTile = newTile % len(tile_positions)
        self.rect.topleft = tile_positions[self.currentTile]
 

    def movePlayer(self, distance):
        self.rect.move(distance*5, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


def home_screen():
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    players = 0

    while True:
        screen.fill(black)

        title_text = font.render("Select Number of Players", True, white)
        screen.blit(title_text, (100, 100))

        # Display options for number of players
        two_players_text = small_font.render("2 Players", True, red)
        three_players_text = small_font.render("3 Players", True, blue)
        four_players_text = small_font.render("4 Players", True, green)

        screen.blit(two_players_text, (100, 300))
        screen.blit(three_players_text, (300, 300))
        screen.blit(four_players_text, (500, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    players = 2
                elif event.key == pygame.K_3:
                    players = 3
                elif event.key == pygame.K_4:
                    players = 4
        if players:
            return players

def main_game(num_players):
    colors = [red, blue, green, yellow] 
    players = [Player(colors[i]) for i in range(num_players)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Example movement for player 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    roll = random.randint(1, 6)
                    players[0].move(players[0].currentTile + roll) 


        screen.fill(white)

        screen.blit(bg_image, (0,0))

        # Draw all players
        for player in players:
            player.draw(screen)

        # Update display
        pygame.display.flip()

    pygame.quit()

# Run the game
num_players = home_screen()
main_game(num_players)
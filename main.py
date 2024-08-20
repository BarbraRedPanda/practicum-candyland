import pygame
import random
import time
import math

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
(205, 536), 
(227, 525), 
(246, 513), 
(262, 492), 
(277, 473), 
(301, 461), 
(326, 457), 
(357, 460), 
(382, 477), 
(402, 492), 
(425, 513), 
(449, 532), 
(477, 543), 
(505, 549), 
(534, 549), 
(558, 546), 
(584, 536), 
(598, 509), 
(587, 485), 
(560, 469), 
(529, 468), 
(501, 467), 
(473, 468), 
(444, 462), 
(417, 445), 
(410, 416), 
(416, 396), 
(442, 382), 
(469, 391), 
(497, 402), 
(522, 420), 
(544, 430), 
(571, 440), 
(605, 446), 
(633, 445), 
(657, 442), 
(682, 437), 
(698, 422), 
(711, 393), 
(710, 370), 
(697, 349), 
(681, 334), 
(652, 330), 
(630, 332), 
(605, 334), 
(583, 345), 
(552, 357), 
(526, 351), 
(496, 342), 
(473, 333), 
(444, 321), 
(414, 313), 
(385, 314), 
(361, 324), 
(333, 336), 
(310, 354), 
(287, 376), 
(260, 390), 
(234, 400), 
(203, 412), 
(186, 416), 
(154, 419), 
(125, 410), 
(105, 401), 
(86, 383), 
(79, 358), 
(94, 330), 
(119, 319), 
(147, 325), 
(165, 328), 
(194, 336), 
(218, 341), 
(244, 339), 
(259, 324), 
(250, 297), 
(233, 281), 
(213, 265), 
(202, 248), 
(210, 220), 
(226, 206), 
(257, 203), 
(282, 209), 
(305, 222), 
(326, 236), 
(349, 250), 
(374, 261), 
(395, 268), 
(421, 275), 
(449, 281), 
(473, 285), 
(501, 290), 
(522, 290), 
(552, 293), 
(578, 293), 
(601, 288), 
(630, 286), 
(656, 271), 
(673, 254), 
(677, 230), 
(675, 202), 
(654, 188), 
(628, 184), 
(607, 164), 
(590, 145), 
(581, 124), 
(559, 110), 
(531, 114), 
(507, 126), 
(490, 141), 
(472, 166), 
(459, 186), 
(435, 197), 
(407, 206), 
(384, 198), 
(360, 186), 
(335, 177), 
(314, 165), 
(291, 153), 
(262, 154), 
(233, 158), 
(210, 164), 
(179, 166), 
(157, 158), 
(135, 150), 
(114, 128), 
(111, 106), 
(121, 77), 
(137, 62), 
(163, 57), 
(191, 56), 
(215, 62), 
(231, 84), 
(254, 100), 
(280, 109)
]

class Player:
    def __init__(self, color):
        self.color = color;
        self.currentTile = 0;
        self.rect = pygame.Rect(tile_positions[0], (15,15))
        self.multiplier = 1.0 # creates a move distance multiplier

    def move(self, newTile):
        if newTile < 0: newTile = 0     # tile position must be greater than zero
        if newTile > 150: # keeps the player in place if they don't get exactly to the finish 
            newTile = self.currentTile   
            print("You must get exactly to the finish!")
        self.currentTile = newTile % len(tile_positions)
        self.rect.center = tile_positions[self.currentTile]


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


def home_screen():
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    players = 0

    specialMode = False

    while True:
        screen.fill(white)

        title_text = font.render("Select Number of Players", True, black)
        screen.blit(title_text, (100, 100))

        switch_rect = pygame.Rect(650, 500, 120, 40)  # Creates a special mode option

        # Display options for number of players
        two_players_text = small_font.render("2 Players", True, red)
        three_players_text = small_font.render("3 Players", True, blue)
        four_players_text = small_font.render("4 Players", True, green)

        screen.blit(two_players_text, (100, 300))
        screen.blit(three_players_text, (300, 300))
        screen.blit(four_players_text, (500, 300))

        # Sets switch color
        switch_color = green if specialMode else yellow
        pygame.draw.rect(screen, switch_color, switch_rect)
        switch_text = small_font.render("Special", True, black)
        screen.blit(switch_text, (switch_rect.x + 10, switch_rect.y + 5))


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

            if event.type == pygame.MOUSEBUTTONDOWN:
                if switch_rect.collidepoint(event.pos):
                    specialMode = not specialMode

        if players:
            return players, specialMode

def main_game(num_players, specialMode):
    colors = [red, blue, green, yellow] 
    players = [Player(colors[i]) for i in range(num_players)]

    turn = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Example movement for player 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    player = players[turn]
                    roll = math.ceil(random.randint(1, 6)*player.multiplier)  # multiplies a random roll by a player's multiplier
                    newTile = player.currentTile + roll 
                    if newTile % 5 == 0 and specialMode:
                        rand = random.randrange(-1,1)                       # either -1, 0, or 1
                        player.multiplier = player.multiplier + rand*0.2    # changes the multiplier by -0.2, 0, or +0.2   
                        player.move(newTile) # moves to new tile 
                        newTile = newTile+rand*10
                        time.sleep(1)       # waits 1 second to move it to the boosted tile
                    player.move(newTile) 
                    turn = (turn+1) % len(players)        # changes turn to next player, loops back to player 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(str(pygame.mouse.get_pos()) + ", ")


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
main_game(num_players[0], num_players[1])
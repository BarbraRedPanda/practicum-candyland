import pygame
import random
import time
import math

pygame.init()
movementMP3 = './sounds/movement.mp3'
sounds = {
    "movement": "./sounds/movement.mp3",
    "victory": "./sounds/victory.mp3",
    "button_main": "./sounds/button_main.mp3",
    "button_deeper": "./sounds/button_deeper.mp3",
    "spinning": "./sounds/spinning.mp3",
    "bg_sound": "./sounds/bg_sound.mp3"
}
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((800,600))

bg = pygame.transform.scale(pygame.image.load('bg.png'), (800,600))
#dice = pygame.transform.scale(pygame.image.load('bg.jpg'), (30,30))
specialBG = pygame.transform.scale(pygame.image.load('specialBG.png'), (800,600))

diceIcons = [pygame.transform.scale(pygame.image.load(f"./dice-icons/Dice0{n}.png"), (60,60)) for n in range(1,7)]
trophy = pygame.transform.scale(pygame.image.load('trophy.png'), (150,300))


icons = {
    "Lolipop": pygame.transform.scale(pygame.image.load("./icons/lolipop.png"), (30,30)),
    "Mint": pygame.transform.scale(pygame.image.load('./icons/mint.png'), (30,30)),
    "Cake": pygame.transform.scale(pygame.image.load('./icons/cake.png'), (30,30)),
    "Goat": pygame.transform.scale(pygame.image.load('bg.jpg'), (30,30))
} 

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (148, 255, 33)
yellow = (255, 255, 0)
gray = (188, 194, 204)
bg_color = (188, 206, 235)

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

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
    def __init__(self, iconKey):
        self.currentTile = 0
        self.rect = pygame.Rect(tile_positions[0], (15,15))
        self.multiplier = 1.0 # creates a move distance multiplier
        self.iconKey = iconKey
        

    def move(self, newTile):
        if newTile < 0: newTile = 0     # tile position must be greater than zero
        if newTile > 133: # keeps the player in place if they don't get exactly to the finish 
            newTile = self.currentTile   
            print("You must get exactly to the finish!")
        if newTile == 133:
            winner(self)

        playSound("movement")
        self.currentTile = newTile % len(tile_positions)
        self.rect.bottomright = tile_positions[self.currentTile]


    def draw(self, screen):
        screen.blit(icons[self.iconKey], self.rect)


def home_screen():
    
    players = 0

    specialMode = False

    while True:
        screen.fill(bg_color)

        title_text = font.render("Select Number of Players", True, black)
        screen.blit(title_text, (90, 100))

        switch_rect = pygame.Rect(600, 500, 180, 40)  # Creates a special mode option


        # Display options for number of players
        two_players_text = small_font.render("2 Players", True, black)
        three_players_text = small_font.render("3 Players", True, black)
        four_players_text = small_font.render("4 Players", True, black)

        two_players_rect = pygame.Rect(120,300,130,35)
        three_players_rect = pygame.Rect(320,300,130, 35)
        four_players_rect = pygame.Rect(520,300,130,35)
        pygame.draw.rect(screen, white, two_players_rect)
        pygame.draw.rect(screen, white, three_players_rect)
        pygame.draw.rect(screen, white, four_players_rect)

        screen.blit(two_players_text, (two_players_rect.x+10, two_players_rect.y+5))
        screen.blit(three_players_text, (three_players_rect.x+10, three_players_rect.y+5))
        screen.blit(four_players_text, (four_players_rect.x+10, four_players_rect.y+5))

        # Sets switch color
        switch_color = green if specialMode else gray
        pygame.draw.rect(screen, switch_color, switch_rect)
        switch_text = small_font.render("Special Mode", True, black)
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
                    playSound("button_deeper")
                elif two_players_rect.collidepoint(event.pos):
                    players = 2
                    playSound("button_main")
                elif three_players_rect.collidepoint(event.pos):
                    players = 3
                    playSound("button_main")
                elif four_players_rect.collidepoint(event.pos):
                    players = 4
                    playSound("button_main")

        if players:
            return players, specialMode

def main_game(num_players, specialMode):
    pygame.mixer.Channel(1).play(pygame.mixer.Sound(sounds["bg_sound"]))
    players = [Player(list(icons.keys())[i]) for i in range(num_players)]
    turn = 0
    roll = 0
    latestEvent = ""

    dice_rect = diceIcons[roll-1].get_rect(topleft=(730, 530))  
    running = True
    while running:
        screen.fill(bg_color)

        player = players[turn]
        prevPlayer = players[(turn+len(players)-1)%(len(players))]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if dice_rect.collidepoint(event.pos):  # Check if the dice was clicked
                    roll = math.ceil(random.randint(1, 6)*player.multiplier)  # multiplies a random roll by a player's multiplier
                    newTile = player.currentTile + roll 
                    if (newTile+1) % 7 == 0 and specialMode:
                        rand = random.randrange(-1,1,2)                       # either -1 or 1
                        player.multiplier = (player.multiplier*10 + 2*rand)/10    # changes the multiplier by -0.2 or +0.2 
                        player.move(newTile) # moves to new tile 
                        newTile = newTile+rand*10
                        latestEvent = f"{player.iconKey}'s multiplier is now {player.multiplier}. They also teleport {random.randrange(-1,1,2)*10} spaces."  
                        time.sleep(0.4)       # waits 1 second to move it to the boosted tile
                    player.move(newTile) 
                    latestEvent =""
                    turn = (turn+1) % len(players)        # changes turn to next player, loops back to player 0

        screen.blit(diceIcons[roll-1], dice_rect.topleft)

        # Changes background depending if it's special mode
        if specialMode: 
            screen.blit(specialBG, (0,0))
            screen.blit(small_font.render(latestEvent, True, black), (20,300))
            screen.blit(small_font.render("Multipliers", True, black), (20,500))
            for i in range(len(players)):
                screen.blit(small_font.render(f"{players[i].iconKey}: {players[i].multiplier}", True, black), (20, 520+(20*i)))
        else : screen.blit(bg, (0,0))

        # Draw all players
        for playera in players:
            playera.draw(screen)

        if prevPlayer.currentTile != 0:
            screen.blit(small_font.render(f"{str(prevPlayer.iconKey)} moved to {str(prevPlayer.currentTile+1)} ", True, black), (20, 15))

        screen.blit(small_font.render(f"{str(player.iconKey)}\'s turn!", True, black), (600,15))

       # Update display
        pygame.display.flip()

    pygame.quit()

def winner(player):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    newGame()
        playSound("victory")
        screen.fill(bg_color)
        screen.blit(font.render(f"{str(player.iconKey)} wins!", True, black), (250,100))
        screen.blit(small_font.render("Press space to restart", True, black), (275,170))
        screen.blit(pygame.transform.scale(icons[player.iconKey], (100,100)), (350,225))
        screen.blit(trophy, (325,300))

        pygame.display.flip()

    pygame.quit()

# sound - key to sounds dictionary
def playSound(sound):
    #pygame.mixer.music.load(sounds[sound])
    #pygame.mixer.music.play()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound(sounds[sound]))

# Run the game
def newGame():
    pygame.mixer.stop()
    num_players = home_screen()
    main_game(num_players[0], num_players[1])

newGame()
import pygame #Importing The Pygame Module
import sys
import random #WE USE RANDOM TO GENERATE ENEMY POSITION
pygame.init() #intitialise pygame

#Screen Size
WIDTH = 800 #Width Variable 
HEIGHT = 600 #Height Variable
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # A Tuple List To Set Screen Size


#RGB Variable
RED = (255,0,0)
BACKGROUND_COLOUR = (0,0,0) #Background Colour 
BLUE = (153,255,255)
GREEN = (13,239,66)
myFont = pygame.font.SysFont("monospace", 35)


player_position = [400,530] #Position Of The Player 
player_size = 50 #Player Size

enemy_size = 30 #Enemy Size
enemy_position = [random.randint(0,WIDTH-enemy_size), 0] #RANDOM ENEMY POSITION
enemy_list = [enemy_position]

#Speed of game
SPEED = 10
score = 0

game_over = False #condition

clock = pygame.time.Clock()

#Spawning Enemies Function
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) <10 and delay < 0.2: #Add 10 enemies with a delay
        x_pos = random.randint(0,WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

#Draw Multiple Enemies
def draw_enemies(enemy_list):
    for enemy_position in enemy_list:
        pygame.draw.rect(screen, RED, (enemy_position[0], enemy_position[1], enemy_size, enemy_size))
        
#
def update_enemy_positions(enemy_list, score):
    for idx, enemy_position in enumerate(enemy_list):
        if enemy_position[1] >=0 and enemy_position[1] < HEIGHT: #Check if enemy is shown on screen
            enemy_position[1] += SPEED
        else:
            enemy_list.pop(idx) #Pop of enemy when not on screen
            score += 1
    return score

#Using detect collision function to check for collision (2)
def collision_check(enemy_list, player_position):
    for enemy_position in enemy_list:
        if detect_collision(enemy_position, player_position):
            return True

    return False

#Function To Detect Collision (1)
def detect_collision(player_position, enemy_position):
    player_x = player_position[0] # X Axis of Player Position
    player_y = player_position[1] # Y Axis of Player Position

    enemy_x = enemy_position[0]  # Axis of enemy position
    enemy_y = enemy_position[1]

#Possible Collisions Between Enemy and Player
    if (enemy_x >= player_x and enemy_x < (player_x + player_size)) or (player_x >= enemy_x and player_x < (enemy_x+enemy_size)):
        if (enemy_y >= player_y and enemy_y < (player_y + player_size)) or (player_y >= enemy_y and player_y < (enemy_y+enemy_size)):
            return True

    return False    


#While loop
while not game_over: #while loop that keeps running untill the condition is met
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # An event is anything the user inputs, so key input or mouse input
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: 
            # Grabs X and Y coordinates of player position
            x = player_position[0] #X axis of player position
            y = player_position[1] # y axis up/down

           #if key left is pressed, shift the x value by player size 50
            if event.key == pygame.K_LEFT: # Moves the player left 
                x -= player_size 
           
            elif event.key == pygame.K_RIGHT:
            
                x += player_size #changing x coordinate in our position

            player_position = [x,y] #New values of x and y

    screen.fill(BACKGROUND_COLOUR) #stops the red from being tracked and replaces it with black

    drop_enemies(enemy_list)

    score = update_enemy_positions(enemy_list,score)

    text = "Score:" + str(score)
    label = myFont.render(text, 1, GREEN)
    screen.blit(label, (WIDTH-200, HEIGHT-40))
    

    #(2)
    if collision_check(enemy_list, player_position):
        game_over = True #if collision is true end game
        break

    draw_enemies(enemy_list)

    #DRAWS AND PRINTS PLAYER ONTO THE SCREEN
    #rect(Surface, colour, Rect, width=0) -> Rect
    pygame.draw.rect(screen, BLUE, (player_position[0], player_position[1], player_size, player_size))
    
    clock.tick(30) # sets speed of the game to 30 seconds

    pygame.display.update()
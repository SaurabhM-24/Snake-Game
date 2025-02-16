import pygame
import random

pygame.init()


# set variables for color
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,155,0)

#display variables
display_width = 800
display_height = 600

AppleThickness = 20         # size of apple and drawing it
#1 block size of snake
block_size = 20

#Display colored box for background and game caption
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')

icon = pygame.image.load('snakehead.png')
pygame.display.set_icon(icon)

#image of snake
img = pygame.image.load('snakehead.png')
#image of apple
apple_img = pygame.image.load('apple.png')

clock = pygame.time.Clock()

FPS = 10            # Frames per second
direction = 'up'    # direction of snake

# Different size of fonts for message to screen
smallfont = pygame.font.SysFont('comicsansms', 25)
medfont = pygame.font.SysFont('comicsansms', 50)
largefont = pygame.font.SysFont('comicsansms', 80)


# function for pausing the game
def pause():
    paused = True
    
    message_to_screen('Paused', red, -100, size = 'large')
    message_to_screen('Press A to continue, C to restart and Q to quit.', black)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                elif event.key == pygame.K_c:
                    gameLoop()

        #gameDisplay.fill(green)
                clock.tick(5)


# function to display score
def score(score):
    text = smallfont.render('Score: '+str(score), True, black)
    gameDisplay.blit(text, [0,0])

#Function for apple's location
def randApple():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))
    randAppleY = round(random.randrange(0, display_height-AppleThickness))

    return randAppleX, randAppleY

randAppleX, randAppleY = randApple()

# Function for the beginning of the game
def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(white)
        message_to_screen('Welcome to Snake Game!!', green, -110, 'medium')
        message_to_screen('The objective of the game is to eat red apples.', black, -60)
        message_to_screen('The more apples you eat, the longer you get.', black, -20)
        message_to_screen('If you run into yourself, or the edges, you die!', black, 20)
        message_to_screen('Press C to play or Q to quit.', black, 100)
        message_to_screen('You can pause the game by pressing P.', black, 140)

        pygame.display.update()
        clock.tick(10)

#Function for snakes movement and initial display
def snake(block_size, snakeList):

    if direction == 'right':
        head = pygame.transform.rotate(img, 270)

    if direction == 'left':
        head = pygame.transform.rotate(img, 90)

    if direction == 'up':
        head = img

    if direction == 'down':
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

# Function to display box text
def text_objects(text, color, size):
    if size == 'small':
        textSurf = smallfont.render(text, True, color)
    elif size == 'medium':
        textSurf = medfont.render(text, True, color)
    elif size == 'large':
        textSurf = largefont.render(text, True, color)
        
    return textSurf, textSurf.get_rect()

# Function to display text
def message_to_screen (msg,color,y_displace=0, size = 'small'):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width//2),((display_height//2) + y_displace)
    gameDisplay.blit(textSurf, textRect)

# main game function
def gameLoop():
    global direction
    direction = 'up'
    gameExit = False
    gameOver = False

    lead_x = display_width // 2
    lead_y = display_height // 2
    
    lead_x_change = 0
    lead_y_change = -10

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randApple()

#While gameExit is False. Actual game loop
    while not gameExit:

        # game over functionality 
        if gameOver == True:
            message_to_screen('Game over!!!!', red, y_displace = -50, size = 'large')
            message_to_screen( 'Press C to play again or Q to quit', black, 50, size = 'medium')
            pygame.display.update()

        while gameOver == True:
            #gameDisplay.fill(white)
            
            # loop to quit the game by clicking on the cross in top right
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False

                # commands to quit or restart the game    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #game controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                    
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

        #command for hitting the boundaries
        if lead_x >= display_width  or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        #Colour of the background
        gameDisplay.fill(white)

        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY,AppleThickness,AppleThickness])
        #displaying the apple
        gameDisplay.blit(apple_img, (randAppleX, randAppleY))

        # movement of snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
            
        snake(block_size, snakeList)

        score(snakeLength - 1)
        
        pygame.display.update()

        #changing the positon 
        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness or lead_x + block_size >= randAppleX and lead_x + block_size <= randAppleX + AppleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness or lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + AppleThickness:
                randAppleX, randAppleY = randApple()
                pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY,AppleThickness,AppleThickness])
                snakeLength += 1


        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()

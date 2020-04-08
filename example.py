# import game library
# import to generate random numbers
import pygame 
import random

# Initialize the pygame modules to get everything started.
pygame.init()

width = 1040 # Width of the screen
height = 680 # Height of the screen
screen = pygame.display.set_mode((width, height))# This creates the screen and gives it the width and height specified as a 2 item sequence.

# Creates the player and enemies also gives it the image found in this folder.
player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy1 = pygame.image.load("monster.jpg")
enemy2 = pygame.image.load("player.jpg")
prize =  pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection for enemies and player.
image_height = player.get_height()
image_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

prize_height = player.get_height()
prize_width = player.get_width()
                           

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

print("This is the height of the player image: " +str(enemy_height))
print("This is the width of the player image: " +str(enemy_width))

print("This is the height of the player image: " +str(enemy1_height))
print("This is the width of the player image: " +str(enemy1_width))

print("This is the height of the player image: " +str(enemy2_height))
print("This is the width of the player image: " +str(enemy2_width))

print("This is the height of the player image: " +str(prize_height))
print("This is the width of the player image: " +str(prize_width))


pygame.display.set_caption("First Game") #Display a caption on the top of the screen window.

# Stored the position of the player as a variable so that you can change them later. 
x = 100
y = 50

# Make the enemy start off screen and at a random y position.
enemyX =  width
enemyY =  random.randint(0, height - enemy_height)

# Make the enemy start off screen and at a random y position.
enemy1_X = height
enemy1_Y = random.randint(0, width - enemy1_width)

# Make the enemy move from the top to bottom of the screen.
enemy2_X = width - 350
enemy2_Y = height - 680

# Make the enemy move from the left to the rigth of the screen.
prize_X = height - 380
prize_Y = width - 1000

# Declared a variable called run and set to boolean data type True.
run = True

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while run:
   
    
    screen.fill(0) # Clears the screen.
    screen.blit(player, (x, y))# This draws the player and enemy images to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyX, enemyY))
    screen.blit(enemy1, (enemy1_Y, enemy1_X))
    screen.blit(enemy2,(enemy2_X,enemy2_Y))
    screen.blit(prize, (prize_Y, prize_X))
    
    pygame.display.flip() # This updates the screen.
    
    # This loops through events in the game.
    for event in pygame.event.get():
        
        # This event checks if the user quits the program, then if so it exits the program. 
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False #if player quits then run is changes to false and loop stops.
            
    # Declared a variable called keys and used the get_pressed() method to detemine if a key was pressed or not.        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 1: # Checks if the left arrow key was pressed variable x is decremented by 1 and this allows the player to move left, X > 1 stops the player from moving pass the screen.
        x -= 1

    if keys[pygame.K_RIGHT] and x < width - image_width - 1 : # Checks if the right arrow key was pressed variable x is incremented by 1 and this allows the player to move right, X < width - image_width - 1 and stops the player from moving pass the screen.
        x += 1

    if keys[pygame.K_UP] and y > 1:# Checks if the up arrow key was pressed variable y is decremented by 1 and this allows the player to move up, y > 1 stops the player from moving pass the screen.
        y -= 1

    if keys[pygame.K_DOWN]and y < height - image_height - 1 : # Checks if the down arrow key was pressed variable y is incremented by 1 and this allows the player to move down, y < width - image_heigt - 1, stops the player from moving pass the screen.
        y += 1

    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemies.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    # Bounding box for the player and enemies
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = y
    playerBox.left = x

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyY
    enemyBox.left = enemyX

    enemyBox1 = pygame.Rect(enemy.get_rect())
    enemyBox1.top = enemy1_X
    enemyBox1.left = enemy1_Y

    enemyBox2 = pygame.Rect(enemy.get_rect())
    enemyBox2.top = enemy2_Y
    enemyBox2.left = enemy2_X

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prize_X
    prizeBox.left = prize_Y
    
    # Test collision of the boxes:
    if playerBox.colliderect(enemyBox):
        
        # Display losing status to the user:
        print("You lose!")
        
        # Quite game and exit window:
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    if enemyX < 0 - enemy_width :

        # Display winning status to the user:
        print("You win!")
        
        #Quite game and exit window.
        pygame.quit()
        exit(0)

    enemyX -= 0.30 #set speed and direction of enemey

    # Test collision of the boxes:
    if playerBox.colliderect(enemyBox1):

        # Display losing status to the user:
        print("You lose!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    # If the enemy is off the screen the user wins the game:
    if enemy1_X < 0 - enemy1_height :
        
        # Display winning status to the user:
        print("You win!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)   
    
    enemy1_X -= 0.25 #set speed and direction of enemey

    # Test collision of the boxes:
    if playerBox.colliderect(enemyBox2):
        
        # Display losing status to the user:
        print("You lose!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    if enemy2_Y > 680  + enemy2_height:
        
        # Display winning status to the user:
        print("you win!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)

    enemy2_Y += 0.20 #set speed and direction of enemey

    # Test collision of the boxes:
    if playerBox.colliderect(prizeBox):
        
        # Display winning status to the user:
        print("You Win!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)
        
    # If the enemy is off the screen the user wins the game:
    if prize_Y > 1040 + prize_width:
        
        # Display winning status to the user:
        print("You Win!")

        # Quite game and exit window:
        pygame.quit()
        exit(0)
        
    prize_Y += 0.15 #set speed and direction of enemey






  

import cv2
import numpy as np
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge Game")

# Set up the player
player_x = screen_width // 2
player_y = screen_height - 50
player_width = 30
player_height = 30
player_color = (255, 0, 0)
player_speed = 8

# Set up the obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_color = (0, 255, 0)
obstacles = []
obstacle_num = 3
obstacle_speed = 8

# Set up the camera
camera = cv2.VideoCapture(0)

# Set up game variables
game_over = False
score = 0
level = 1
obstacle_speed = 8


flag = 0
# Set up the clock
clock = pygame.time.Clock()

while not game_over:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Capture a frame from the camera
    ret, frame = camera.read()

    frame = cv2.flip(frame, 1)
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Determine the direction of movement based on the position of the face
    for (x, y, w, h) in faces:
        if x + w/2 < player_x:
            player_x -= 5
        elif x + w/2 > player_x + player_width:
            player_x += 5

    # Move the obstacles
    for i in range(len(obstacles)):
        obstacles[i][1] += obstacle_speed * level
        if obstacles[i][1] > screen_height:
            obstacles[i][0] = random.randint(0, screen_width - obstacle_width)
            obstacles[i][1] = 0
            score += 1

        # Check for collisions with the player
        if player_x < obstacles[i][0] + obstacle_width and \
           player_x + player_width > obstacles[i][0] and \
           player_y < obstacles[i][1] + obstacle_height and \
           player_y + player_height > obstacles[i][1]:
            game_over = True

    # Add a new obstacle if necessary
    if len(obstacles) < obstacle_num:
        x = random.randint(0, screen_width - obstacle_width)
        y = random.randint(-screen_height, 0)
        obstacles.append([x, y])

    # Increase the difficulty level based on the score
    if score > 0 and (score % 10 == 5 or score%10==0) and flag==0:
        level += 1
        obstacle_num += 1
        player_width -= 1
        player_height -= 1
        obstacle_width -= 1
        obstacle_height -= 1
        player_speed += 1
        obstacle_speed += 0.5
        flag = 1
        
    if score%10==6 or score%10==1:
        flag=0

    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    text = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(text, (10, 40))
    pygame.display.update()

    cv2.imshow('Face Direction', frame)
    # Set the frame rate
    clock.tick(60)
    
print("Your Score:",score)
print("Max level achieved:",level)
camera.release()
pygame.quit()

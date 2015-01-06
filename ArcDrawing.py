import serial
import Tkinter
import time
import sys
import pygame
import math

###################### SET UP PYGAME #######################

pygame.init()

window = pygame.display.set_mode((640,480))

# First, clear the screen to white. Don't put other drawing commands
# above this, or they will be erased with this command.
window.fill((255,255,255))

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

###################### SET UP SERIAL BAUD RATE ####################

usbport = 'COM4'
ser = serial.Serial(usbport, 9600, timeout=1)

###################### INITIALIZE VARIABLES #######################

radius = 0
deltaR =1
distString= ""
dist = 0
angle=0
deltaA =5;
angleString =""

# -------- Main Program Loop -----------

while not done:

    #---------------------- GET THE DISTANCE FROM THE ARDUINO ------------------

    distString =""
    angleString=""
    comma = False
    for line in ser.readline():
    #    print line
        if line.isdigit():
            distString+=line
    for line in ser.readline():
    #    print line
        if line.isdigit():
            angleString+=line
    if distString.isdigit():
        dist = float(distString)
    if angleString.isdigit():
        angle = float(angleString)
    print 'angle'
    print angle
    print 'dist'
    print dist
        
    
    # --- Main event loop -------------------------------
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            pygame.quit()
            done = True
 
    # --- Game logic should go here

    radius = dist*3
   # radius =75
   # print dist
    angle+=deltaA
    if angle>=180 or angle<=0:
        deltaA*=-1
        if not done:
            window.fill((255,255,255))
 
    # --- Drawing code should go here
    

    #pygame.draw.circle(window, (255,0,255), (310, 230), (int)(radius))4
    
    if dist<12:
        x = 60 * math.cos(math.radians(angle))
        y = 60 * math.sin(math.radians(angle))
        pygame.draw.circle(window, (0,255,255), (int(310+x), int(230-y)), (3))
   
  
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(50)


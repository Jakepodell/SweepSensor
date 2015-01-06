import serial
import Tkinter
import time
import sys
import pygame

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
dist =- 0

# -------- Main Program Loop -----------

while not done:

    #---------------------- GET THE DISTANCE FROM THE ARDUINO ------------------

    distString =""
    for line in ser.readline():
        if line.isdigit():
            distString+=line
    if distString.isdigit():
        dist = float(distString)
    
    # --- Main event loop -------------------------------
    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            pygame.quit()
            done = True
 
    # --- Game logic should go here

    radius = dist*3
    print dist
 
    # --- Drawing code should go here
    if not done:
        window.fill((255,255,255))

    pygame.draw.circle(window, (255,0,255), (310, 230), (int)(radius))
  
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(50)


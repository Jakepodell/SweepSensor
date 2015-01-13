import serial
import Tkinter
import time
import sys
import pygame
import math
import Obstacle

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
start =0;
highest=0
obstacles=[]
sweepCount=0
angles =0
endCounter =0
inish = False
counter=0;


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
    if dist > 20:
        print 'angle'
        print angle
        print 'dist'
        print dist
    obstacles.append(Obstacle.Obstacle(angle, dist))
        
    
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
   # angle+=deltaA
    if inish == False:
        inish=True
      #  print "now its true"
    elif angle>=180 or angle<=0:
        deltaA*=-1
        start=0
        endCounter+=1
        print endCounter
        if not done and endCounter==2:
            window.fill((255,255,255))
            endCounter=0
        if endCounter==1:
            for obs in obstacles:
            #  pygame.draw.circle(window, (0,0,255), (int(220+obs.angle), int(230-obs.distance)), 3)
                if obs.distance > highest:
                    highest = obs.distance
                    highIndex = counter
                    counter+=1
         #   print "Recommended Angle :"
         #   print obstacles[highIndex].angle
            del obstacles[:]
            highest=0
            counter =0
            highIndex =0
        
    if start == 0:
        start = dist
 
    # --- Drawing code should go here
    

    #pygame.draw.circle(window, (255,0,255), (310, 230), (int)(radius))4
    
    #if dist<12:
    x = angle
    y = dist
    '''if y>start/10:
        pygame.draw.circle(window, (0,255,0), (int(220+x), int(230-y)), (3))
    elif y<start/10:
        pygame.draw.circle(window, (255,0,0), (int(220+x), int(230-y)), (3))
    else:'''
    pygame.draw.circle(window, (0,0,255), (int(220+x), int(230-y)), (3))
   
  
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(50)


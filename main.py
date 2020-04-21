"""<<In Sha Allah, First Game in Python 2.7 with Pygame Coupled>>
Specially Thanking Allah for intellectuality , interest and kept my motivated..

Version : 4.12
#Copyright 2018 Zahid Khan.

# Brief: Shooter game to depict the anger against genocide.
#  \author Zahid Khan.
#  \version 3.42
Bugs : Unoptimised yet plus some options not working  (Incomplete) & Unsupportable to many OS."""
#HIGHSCORE  WORKING
#RESUME ()WORKING)
#MUSIC NOT WORKING WELL
#EXIT NOT WORKING WELL..

import pygame, time
import pygame, time
from screen import Background                                                                   #Once necessary modules are imported
from game import Game, Aircraft 
pygame.init()

#The running variable is little tricky as it indicate the status of the game, if the game is running(background) it returns True if crash it returns false.
running = False

def main():
            global running
            #DECLARATIONS
            white = (255,255,255)
            DisplayX  , DisplayY = 550,  300
            FontSize = 30
            backgroundImage = "images/background_homepage.jpg"
            #CODE START
            gameObj = Game()
            pygame.mouse.set_visible(False)
            gameDisplay = pygame.display.set_mode(  (1350,690) )       #Size of the Window(width,height)
            bg = Background("                                                                                                                                                               The Anonymous Shooter[XEE]                                             ","images/icon.png");                  #Calling constructor(TItle, Status Bar IconPath)                                          
            #BACKGROUND CLASS DISPLAYS THE BACKGROUND IMAGE AND THE SOUND FOR PLAY>>
            username = bg.User()                                                                #This is responsible for getting the username from the user,.
            bg.screen(backgroundImage,gameDisplay)
            bg.music("Music/background_home.mp3")
            #Writes Options Text on Screen with starting X = 20;
            
            #THIS LOOP IS CONTINOUS WAITING FOR USER REPLIES
            #running = True
            cmenu1 = (
                                   "Start BloodShed.",
                                   " High Score.",
                                   "Settings",
                                   "About Developer.",
                                   "Quit!"
                           )            
            cmenu2 = (
                                   "Start BloodShed.",
                                  "Resume" ,
                                   " High Score.",
                                   "Settings",
                                   "About Developer.",
                                   "Quit!"
                           )

            cmenu = cmenu1
            bg.text(gameDisplay, "comicsansms", FontSize, cmenu, white, DisplayX ,  DisplayY)
            while True:
                        if running == False:
                                                                        cmenu = cmenu1
                        else:
                                                                     cmenu = cmenu2
                        pygame.init()
                        for event in pygame.event.get():
                                    if  event.type == pygame.QUIT:                               
                                                                        running = False
                                                                        time.sleep(1)
                                                                        pygame.quit()
                                    if event.type == pygame.KEYDOWN:              
                                                if event.key == pygame.K_DOWN:                                                                  #IF DOWN KEY IS PRESSED ON CHOICE MENU
                                                            bg.screen(backgroundImage,gameDisplay)  
                                                            bg.selectedDown(gameDisplay, cmenu, white, DisplayX, DisplayY)                      # (parameter, .. . . .. , 1 = RESET)
                                                elif event.key == pygame.K_UP:                                                                              #IF UP KEY IS PRESSED ON CHOICE MENU
                                                            bg.screen(backgroundImage,gameDisplay)  
                                                            bg.selectedUp(gameDisplay, cmenu, white, DisplayX, DisplayY)          
                                                elif event.key == pygame.K_ESCAPE:                                                                          #IF ESCAPE KEY IS PRESSED ON CHOICE MENU
                                                            quit()
                                                elif event.key == pygame.K_RETURN:
                                                            if bg.CursorIndex() == 1:                
                                                                        gameObj.destructor() 
                                                                        pygame.mixer.music.pause()
                                                                        bg.music("Music/background_game.mp3")
                                                                        GameScreen( gameObj ,username)                             #Calling game module to display game 
                                                                        bg.screen(backgroundImage,gameDisplay)                      #Returning and showing default screen.
                                                                        bg.music("Music/background_home.wav")
                                                                        if running == False:
                                                                                cmenu = cmenu1
                                                                        else:
                                                                                cmenu = cmenu2
                                                                        bg.text(gameDisplay, "comicsansms", FontSize, cmenu, white, DisplayX ,  DisplayY)                               #IF ANY OF THE OPTION ARE Selected through enter key..      
                                                                        bg = Background("                                                                                                                                                               The Anonymous Shooter[XEE]                                             ","images/icon.png");                  #Calling constructor(TItle, Status Bar IconPath)                                          
                                                            elif bg.CursorIndex() == 2 and running == False:
                                                                        bg.highscore(gameDisplay)  
                                                                        bg.screen(backgroundImage,gameDisplay)                      #Returning and showing default screen.
                                                                        bg.text(gameDisplay, "comicsansms", FontSize, cmenu, white, DisplayX ,  DisplayY)                               #IF ANY OF THE OPTION ARE Selected through enter key..      
                                                            elif bg.CursorIndex() == 3 and running == True:                                                                             #HighScore Option Selected.
                                                                        bg.highscore(gameDisplay)  
                                                                        bg.screen(backgroundImage,gameDisplay)                      #Returning and showing default screen.
                                                                        bg.text(gameDisplay, "comicsansms", FontSize, cmenu, white, DisplayX ,  DisplayY)                               #IF ANY OF THE OPTION ARE Selected through enter key..      
                                                            elif bg.CursorIndex() == 2:                                                                                                                             #Executes if game is running, it displays resume option.
                                                                        bg.music("Music/background_game.wav")
                                                                        GameScreen( gameObj ,username)                                                                                                                  #Calling game module to display game 
                                                                        bg.screen(backgroundImage,gameDisplay)                                                                          #Returning and showing default screen.
                                                                        if running == False:
                                                                                cmenu = cmenu1
                                                                        else:
                                                                                cmenu = cmenu2
                                                                        bg.text(gameDisplay, "comicsansms", FontSize, cmenu, white, DisplayX ,  DisplayY)                               #IF ANY OF THE OPTION ARE Selected through enter key..      
                                                            elif bg.CursorIndex() == len(cmenu)  :                                                               #Exit code, Exit is always at the last option:
                                                                        bg.Quit() 
                                                                        gameObj.Quit() 
                                                                        pygame.quit()
                                                                        quit()


#This is for the game screen mode only if user selects the Game option here is the coding for that . .. 
def GameScreen( gameObj , username):
                                    plane =  Aircraft()
                                    global  running 
                                    running = True
                                    bulletstate = 0
                                    directionstate =0
                                    gameObj.screen(username);                                                        #Blanks screen with white color and also put the aeroplane at its place.
                                    bulletinterval = 0                                                                  #Indicates the delay between the two bullets
                                    while running:
                                                pygame.init()
                                                gameObj.screen( username );                                                                    #Blanks screen with white color and also put the aeroplane at its place.
                                                for event in pygame.event.get():
                                                            if  event.type == pygame.QUIT:                               #If user has exit through the exit bclick on the top of window.
                                                                        pygame.display.quit()
                                                                        quit()
                                                            elif event.type == pygame.KEYDOWN :                         # USER HAS PRESSED ANY KEY
                                                                        if event.key == pygame.K_RIGHT:                                                              
                                                                                    directionstate = 1
                                                                        elif event.key == pygame.K_ESCAPE:
                                                                                    running = True
                                                                                    return  0                                                                        #This pauses the game for some time being                                                                        
                                                                        elif event.key == pygame.K_LEFT:
                                                                                   directionstate = 3
                                                                        elif event.key == pygame.K_UP:
                                                                                   directionstate = 4
                                                                        elif event.key == pygame.K_DOWN:
                                                                                   directionstate = 5
                                                                        if event.key == pygame.K_s :                              #FIRING TO THE ENEMY BY SPECIFIC KEY
                                                                                    bulletstate = 6
                                                                                    bullet = 0

                                                            elif event.type == pygame.KEYUP:                                        #USER HAS TAKEN FINGER UP KEY
                                                                        if event.key == pygame.K_RIGHT:                                                              
                                                                                    directionstate = 0
                                                                        elif event.key == pygame.K_LEFT:
                                                                                   directionstate = 0
                                                                        elif event.key == pygame.K_UP:
                                                                                   directionstate = 0
                                                                        elif event.key == pygame.K_DOWN:
                                                                                   directionstate = 0
                                                                        if event.key == pygame.K_s :                              #FIRING TO THE ENEMY BY SPECIFIC KEY
                                                                                    bulletstate = 0
                                                                                    bullet = 0
                                                if directionstate == 1:
                                                           plane.right();
                                                elif directionstate == 3:
                                                            plane.left()
                                                elif directionstate == 4 :
                                                            plane.up()
                                                elif directionstate == 5:
                                                            plane.down()
                                                if bulletstate == 6 and bulletinterval <=0:
                                                            bulletinterval = 10
                                                            plane.firing()
                                                if not gameObj.runningstatus():                                                                                #IF Aircraft crashed with enemy it will show the menu
                                                            running = False
                                                bulletinterval -=1
##____________________________ [ The Python Execution Stats From Here! ] ___________________________________
if __name__ == '__main__':                                                                   #Ensures that the main modules stats first
                                    main()
#_______________________[ END oF Main FILE ]--------------------------------------------------
#BUGS : UNOPTIMISED 
import pygame
from  random import randint

#Bullets Stuff.
bulletarray = [  ]                              #It contains the list of all the bullets on the screen
bulletspeed = 10                                 #It is the speed at which bullets are moving on screen.change also in the firing class

#Enemies related stuff.
enemyarray = [ ]                       #It contains the enemies on screen.
crasharray= []
enemyspeed = 3                      #It is the speed at which enemies are moving on screen
enemyinterval = 30                  
kills = 0                                             #It defines enemies got killed.
stage = 0


#Airplane Related Stuff.
airplaneSpeed = 12                                                                                                      #It gets added to axis makes appearance of motion.
x_location = 100                                                                                                                      #Default Location of the Airplane
y_location = 550                                                                                                                     #Default Location of Airplane
damaged = 0

#Creating a game surface for the use rather than sending same screen as parameters.
gameDisplay = pygame.display.set_mode(  (1350,690) )       #Size of the Window(width,height)
pygame.init()


#Images loading from slow memory HDD...
airplane = pygame.image.load("Images/FighterPlane/airplane.png").convert_alpha()
background= pygame.image.load("images/stages/stage1.jpg").convert()
bullet = pygame.image.load("images/game_fire.png").convert_alpha()
bullet2 =pygame.image.load("images/game_fire2.png").convert_alpha()
enemy = pygame.image.load("images/enemy.png").convert_alpha()
boom = pygame.image.load("images/crasheffect.png").convert_alpha()
gameover = pygame.image.load("images/gameover.jpg").convert_alpha()


#<<<<<<<<<<<<<<<<<<<<<<CLASSES START FROM HERE>>>>>>>>>>>
#The Aircraft class is responsible for causing motion to the aircraft (LEFT, RIGHT, UP, DOWN) , Showing the aircraft , Shooting the bullets , and updating those 
#bullets on the screen as well as destroying those bullets out of scope.
class Aircraft:
                        def show(self):
                                    global airplane, background
                                    gameDisplay.blit(pygame.transform.scale( background ,(1360,700)), (0 ,0))
                                    gameDisplay.blit(pygame.transform.scale( airplane,( 150,150 )), ( x_location , y_location ) )
                                    
                        def update_showbullet(self):
                                                global x_location, bulletspeed,bullet,bullet2                                    
                                                loop = 0
                                                while loop < len(bulletarray):                   
                                                            bulletx = bulletarray[loop]
                                                            bullety =  bulletarray[loop+1]
                                                            if bullety < 10:
                                                                        del(bulletarray[loop] )              #deleting X CoOrdinate of bullet.
                                                                        del(bulletarray[loop])             #deleting Y CoOrdinate of bullet. since Y would have at X places now.
                                                                        loop=-2
                                                            else:
                                                                        bulletarray[loop+1]  = bullety - bulletspeed
                                                                        if  bullety%2 == 0:
                                                                                    gameDisplay.blit(pygame.transform.scale(bullet,(100,100)), (bulletx , bullety) )
                                                                        elif bullety%2 ==1:
                                                                                    gameDisplay.blit(pygame.transform.scale(bullet2,(100,100)), (bulletx , bullety) )
                                                            loop += 2                           #As we are assigning X as well as Y location in the bulletarray...

                        def right(self):
                                    global x_location
                                    if x_location <=1150: 
                                                x_location = x_location + airplaneSpeed
                        def left(self):
                                    global x_location
                                    if x_location> 10: 
                                                x_location = x_location - airplaneSpeed
                        def up(self):
                                    global y_location
                                    if y_location > 40: 
                                                y_location = y_location - airplaneSpeed
                        def down(self):
                                    global y_location
                                    if y_location < 550: 
                                                y_location = y_location + airplaneSpeed
                        
                        def firing(self):
                                                global x_location, y_location 
                                                if pygame.mixer.get_busy != True:
                                                            #pygame.mixer.music.load("music/fire.mp3")
                                                            #pygame.mixer.music.play()
                                                                                    sound =pygame.mixer.Sound("music/fire.wav")
                                                                                    sound.play()
                                                                                    pygame.mixer.Sound.set_volume(sound,0.1)
                                                                                    
                                                bulletarray.append( x_location+13 )                         #So firing from 13 location to the left of the airplane.
                                                bulletarray.append( y_location-10 )
#                                        <<END OF THE CLASS AIRCRAFT>>
#                                        <<END OF THE CLASS AIRCRAFT>>
#                                        <<END OF THE CLASS AIRCRAFT>>


class Enemy:
            def update_display(self):
                                                loop = 0
                                                while loop < len(enemyarray):                   
                                                            enemyx = enemyarray[loop]
                                                            enemyy =  enemyarray[loop+1]
                                                            if enemyy > 690:
                                                                        del(enemyarray[loop] )              #deleting X CoOrdinate of bullet.
                                                                        del(enemyarray[loop])             #deleting Y CoOrdinate of bullet. since Y would have at X places now.
                                                                        loop=-2
                                                            else:
                                                                        enemyarray[loop+1]  = enemyy + enemyspeed
                                                                        gameDisplay.blit(pygame.transform.scale(enemy,(100,100)), (enemyx , enemyy) )
                                                            loop += 2                           #As we are assigning X as well as Y location in the enemyarray...

            def generate(self):
                                    global enemyinterval
                                    if enemyinterval<=0:
                                                number = randint(1,5)                     #Determines number of enemies on a single row..
                                                while number > 0:
                                                            temp = randint(0,12)
                                                            temp *= 100
                                                            enemyarray.append(temp+10)
                                                            enemyarray.append(-20)
                                                            number-=1
                                                            enemyinterval = 40
                                    enemyinterval -= 1

                                    #This function ensures that if a bullet strikes the airplane that happens a collision and airplane burns.
            def checkCrash( self , username ):
                                                             global damaged  , airplane, x_location , y_location , gameover , gameDisplay
                                                             loop = 0
                                                             while loop <  len(enemyarray):                   
                                                                        hit = False                                                       #This indicates if an enemy is hit or not.
                                                                        bloop = 0
                                                                        enemyx = enemyarray[loop]                 
                                                                        enemyy =  enemyarray[loop+1]
                                                                        #The below ensures that there is no crashed between aircrafts
                                                                        if (x_location <= enemyx and x_location+70 >= enemyx and enemyy<= y_location and enemyy+30 >= y_location ) or (x_location+20 >= enemyx and enemyx+70 >= x_location and  enemyy<= y_location and enemyy+30 >= y_location):
                                                                              sound =pygame.mixer.Sound( "Music/crash.wav")
                                                                              sound.play( )
                                                                              damaged += 5
                                                                              if damaged>=10 and damaged<=30:
                                                                                    airplane = pygame.image.load("Images/FighterPlane/damaged10.png").convert_alpha()
                                                                              elif damaged>=30 and damaged<=70:
                                                                                    airplane = pygame.image.load("Images/FighterPlane/damaged50.png").convert_alpha()
                                                                              elif damaged>=70 and damaged<=95:
                                                                                    airplane = pygame.image.load("Images/FighterPlane/damaged100.png").convert_alpha()
                                                                              if damaged >= 100:                              #IF GAME ENDS BY CRASHED PLANE
                                                                                    Filelines = 0
                                                                                    file = open("Scores.txt","r+")            #READING FROM FILE
                                                                                    lines = file.readlines()                        #STORING EXISTING DATA IN LINES
                                                                                    file.close()
                                                                                    file = open("Scores.txt","w+")            #WRITING IN FILE NEW DATA
                                                                                    file.write( username.ljust(55) + "Stage = " + str(stage) + str(". \n") )
                                                                                    for line in lines:                        #APPENDINg NEw Data
                                                                                                file.write(line)
                                                                                                Filelines += 1
                                                                                                if Filelines > 9:
                                                                                                      break
                                                                                    file.close()
                                                                                    gameDisplay.blit(pygame.transform.scale( gameover ,(1360,700)), (0 ,0))
                                                                                    pygame.display.flip();
                                                                                    while True:
                                                                                          pygame.init()
                                                                                          for event in pygame.event.get():
                                                                                                if event.type == pygame.KEYDOWN:              
                                                                                                            if event.key == pygame.K_ESCAPE:                
                                                                                                                  return False


                                                                        while bloop<len(bulletarray) and hit == False:              #continues checking if any bullet hit prespecified enemy.
                                                                                    global kills
                                                                                    bulletx = bulletarray[bloop]
                                                                                    bullety =  bulletarray[bloop+1]
                                                                                    if (bulletx <= enemyx and bulletx+80 >=enemyx and bullety+100 <=enemyy+100) or  (bulletx >= enemyx and bulletx <= enemyx+80 and bullety <= enemyy+100):
                                                                                                del(enemyarray[loop] )             #deleting X CoOrdinate of bullet.
                                                                                                del(enemyarray[loop])             #deleting Y CoOrdinate of bullet. since Y would have at X places now.
                                                                                                crasharray.append(enemyx)
                                                                                                crasharray.append(enemyy)
                                                                                                crasharray.append(10)                     #Time to display the effect of crash
                                                                                                kills +=1
                                                                                                loop -=2
                                                                                                hit = True
                                                                                    bloop +=2
                                                                        loop += 2                           #As we are assigning X as well as Y location in the enemyarray...
                                                             return True                        

            def showcrash(self):
                                                            loop = 0
                                                            while loop <  len(crasharray):                   
                                                                        crashx = crasharray[loop]
                                                                        crashy =  crasharray[loop+1]
                                                                        times = crasharray[loop+2]
                                                                        if times <  0:
                                                                                                del(crasharray[loop] )             #deleting X CoOrdinate of bullet.
                                                                                                del(crasharray[loop])             #deleting Y CoOrdinate of bullet. since Y would have at X places now.
                                                                                                del(crasharray[loop] )             #deleting X CoOrdinate of bullet.
                                                                                                loop-=3
                                                                        else:
                                                                                                effectx = randint(80,150)
                                                                                                effecty = randint(70,120)
                                                                                                crasharray[loop+2] = crasharray[loop+2] - 1
                                                                                                gameDisplay.blit(pygame.transform.scale(boom,(effectx,effecty)), (crashx , crashy) )                           
                                                                        loop +=3


#<<THE GAME Class is overall responsible for the sequencial execution of other modules.. 
class Game:                     
            RunningGame = True;
            airplane = Aircraft()
            enemy = Enemy()

            def stageadjustment(self):
                 global enemyspeed,airplaneSpeed, bulletspeed, stage, background
                 if stage <3:
                              background= pygame.image.load("images/stages/stage1.jpg").convert()
                 elif stage <5:
                              background= pygame.image.load("images/stages/stage2.jpg").convert()
                 else:
                              background= pygame.image.load("images/stages/stage3.jpg").convert()
                 if enemyspeed < 15:
                              enemyspeed += 1
                 if airplaneSpeed <=18:
                              airplaneSpeed += 1
                 if bulletspeed <=30:
                              bulletspeed += 3
                 sound =pygame.mixer.Sound( "Music/levelcompleted.wav")
                 sound.play( )



            def destructor(self):                                       #New game rather then restart
                  global bulletarray,enemyarray,crasharray,bulletspeed,enemyspeed,x_location,y_location,kills,stage                              #It contains the list of all the bullets on the screen
                  bulletarray = [  ]
                  bulletspeed = 10                                 #It is the speed at which bullets are moving on screen.
                  #Enemies related stuff.
                  enemyarray = [ ]                       #It contains the enemies on screen.
                  crasharray= []
                  enemyspeed = 3                      #It is the speed at which enemies are moving on screen
                  enemyinterval = 30                  
                  kills = 0                                             #It defines enemies got killed.
                                    #Airplane Related Stuff.
                  airplaneSpeed = 12                                                                                                      #It gets added to axis makes appearance of motion.
                  x_location = 100                                                                                                                      #Default Location of the Airplane
                  y_location = 550                                                                                                                     #Default Location of Airplane
                  kills =0
                  stage = 0

            def screen( self , username ):                                                                                         
                        global kills,stage
                        self.airplane.show()                                                                      
                        self.enemy.generate()
                        self.enemy.update_display()
                        self.airplane.update_showbullet()
                        self.RunningGame = self.enemy.checkCrash( username )                             #It sets GameRunning to False if a crash happen to airplane.
                        self.enemy.showcrash(  )

                        if kills > 50:
                                          font = pygame.font.SysFont("comicsansms", 50)
                                          text = font.render(  "Level Cleared. Get Ready!"  , True, (255,255,255))
                                          gameDisplay.blit( text,  [300,80] )
                                          pygame.display.flip();
                                          pygame.time.delay(1200)
                                          self.stageadjustment()
                                          stage += 1
                                          kills = 0
                                          pygame.display.set_caption("              Current stage                     ======              " + str(stage)  )                                      #Title 
                        pygame.display.flip();
                        
            def runningstatus(self):
                        return self.RunningGame
            
            def Quit(self):
                  self.destructor()
                  pygame.quit()
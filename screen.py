import os , pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10,30)                  #X AND Y AXIS TO THE MAIN SCREEN OF GAME>>
pygame.init( )
class Background:
            count = 0                           
            SelectedOption = 0
            def __init__( self, WindowTitle,IconPath ):
                        pygame.display.set_caption( WindowTitle )                                      #Title 
                        icon = pygame.image.load( IconPath )
                        pygame.display.set_icon( icon )
                        pygame.init( )

            def screen( self,name,gameDisplay ):
                        img = pygame.image.load( name )                   #<<BACKGROUND IMAGE>>
                        gameDisplay.blit( (img), (0,0) )
                        pygame.display.flip( )
            
            def music( self, FileName, times=0 ):
                        pygame.mixer.music.load( FileName )
                        pygame.mixer.music.play( )

            def sound(self, FileName):
                        sound =pygame.mixer.Sound( FileName )
                        sound.play( )

            def text(self, gameDisplay,  FontName, Size, menu,  color, x, y,reset=0):
                        for loop in range( 0 ,  len(menu) ):
                                    font = pygame.font.SysFont(FontName, Size)
                                    text = font.render( str(loop+1) + str(". ") +  menu[loop]  , True, color )
                                    y = y + self.count
                                    gameDisplay.blit( text,  [x, y] )
                                    self.count =  40                                                                         #Spacing between text
                        pygame.display.update()
                        

            def  selectedDown(self , gameDisplay, cmenu, white, DisplayX, DisplayY ):
                        self.sound("music/buttondown.wav")
                        FontSize = 20
                        FontName = "comicsansms"
                        self.count =  0                                                                         #Spacing between text
                        beauty = ' > '
                        if len(cmenu) > self.SelectedOption:
                                    self.SelectedOption +=  1
                        for loop in range(0, len(cmenu)):
                                    font = pygame.font.SysFont(FontName, FontSize)
                                    text = font.render( str(loop+1) + str(". ") + cmenu[loop], True, (255,255,255) )
                                    if self.SelectedOption == loop+1:                                        #If this is selected option . . .
                                                font = pygame.font.SysFont(FontName, FontSize+10)
                                                text = font.render(str(beauty) + cmenu[loop], True, (255,255,255) )
                                    DisplayY = DisplayY + self.count
                                    gameDisplay.blit( text,  [DisplayX, DisplayY] )
                                    self.count =  40                                                                         #Spacing between text
                        pygame.display.update()



            def  selectedUp(self , gameDisplay, cmenu, white, DisplayX, DisplayY ):
                        self.sound("music/buttonup.wav")
                        FontSize = 20
                        FontName = "comicsansms"
                        self.count =  0                                                                         #Spacing between text
                        beauty = ' > '
                        if self.SelectedOption > 1:
                                    self.SelectedOption -=  1
                        for loop in range(0, len(cmenu)):
                                    font = pygame.font.SysFont(FontName, FontSize)
                                    text = font.render(str(loop+1) + str(". ") +  cmenu[loop], True, (255,255,255) )
                                    if self.SelectedOption == loop+1:                                                                                            #If this is selected option . . .
                                                font = pygame.font.SysFont("Comic Sans MS", FontSize+10)
                                                text = font.render(beauty + cmenu[loop], True, (255,255,255) )
                                    DisplayY = DisplayY + self.count
                                    gameDisplay.blit( text,  [ DisplayX , DisplayY ] )
                                    self.count =  40                                                                         #Spacing between text
                        pygame.display.update()


            def CursorIndex( self ):                                                  #returns selected menu item.
                        return int( self.SelectedOption )

            def highscore(self,screen):
                                    x  ,  y  = 200  ,  100                                                               #It specifies the X-Location and Y-Location for the starting of the scores.
                                    gameDisplay = pygame.display.set_mode(  (1350,690) )       #Size of the Window(width,height
                                    font = pygame.font.SysFont("BrowalliaUPC", 70)
                                    text = font.render( ".HIGH SCORE. "  , True, (255,255,255))
                                    gameDisplay.fill((0,0,130))
                                    gameDisplay.blit( text,  [450 , 10  ] )
                                    #gameDisplay.blit(pygame.transform.scale(bg,(1320,650)), (10 ,10))
                                    try:
                                                file = open("Scores.txt","r+")
                                    except IOError:
                                                font = pygame.font.SysFont("comicsansms", 30)
                                                text = font.render( "NO LASTSCORE RECORDED YET!" , True, (255,255,255))
                                                gameDisplay.blit( text , [400, 500] )
                                                pygame.display.flip( )
                                                while True:
                                                     for event in pygame.event.get():
                                                            if  event.type == pygame.QUIT:                               
                                                                        pygame.quit()
                                                            if event.type == pygame.KEYDOWN:              
                                                                         if event.key == pygame.K_ESCAPE:            
                                                                                     return 0
                                                return
                                    pygame.draw.rect(gameDisplay,(40,30,150) ,(20,100,1300,450))                                   #Draws a rectangle and fills it with the Color              
                                    i = 0
                                    for loop in file:
                                                i+=1
                                                font = pygame.font.SysFont("comicsansms", 30)
                                                text = font.render(  str(i).ljust(4) +  loop[0:-1]  , True, (255,255,255))
                                                y = y + 35
                                                gameDisplay.blit( text,  [x, y] )
                                                pygame.time.delay(20)
                                                pygame.display.flip( )
                                    font = pygame.font.SysFont("comicsansms", 20)
                                    msg = " ~ You can move back to homescreen by pressing Escape Key[ Esc ]."
                                    text = font.render(  msg  , True, (255,255,255))
                                    gameDisplay.blit( text,  [80,570] )
                                    pygame.display.flip( )

                                    #In order to exit successfully from the highscore wait till the escape
                                    while True:
                                                for event in pygame.event.get():
                                                            if  event.type == pygame.QUIT:                               
                                                                        pygame.quit()
                                                            if event.type == pygame.KEYDOWN:              
                                                                         if event.key == pygame.K_ESCAPE:            
                                                                                    file.close()
                                                                                    return 0

            def Quit(self):
                                    pygame.quit()
                                    quit()

            def User(self):                                                                                 #The first Screen The User sees responsible for the input as well as the output
                                                pygame.init()
                                                gameDisplay = pygame.display.set_mode(  (1350,690) )       #Size of the Window(width,height
                                                gameDisplay.fill((0,0,130))
                                                temp = ""
                                                font = pygame.font.SysFont("comicsansms", 20)
                                                msg = " Player Name [Max 10 Alphabets]: "
                                                text = font.render(  msg  , True, (255,255,255))
                                                gameDisplay.blit( text,  [80,170] )
                                                msg = " Player Name : "                                                             #THis message will be printed after the user keydown
                                                #RECTANGLE SURFACE FROM HERE . .  .
                                                pygame.draw.rect( gameDisplay , (40,30,150) ,( 420,170         ,         500,40) )                                   #Draws a rectangle and fills it with the Color                                                  
                                                pygame.display.flip( )
                                                while True:
                                                            pygame.init()
                                                            for event in pygame.event.get():
                                                                        if  event.type == pygame.QUIT:                               
                                                                                     pygame.quit()
                                                                        if event.type == pygame.KEYDOWN:              
                                                                                    if event.key == pygame.K_ESCAPE:            
                                                                                                temp = "Anonymous"
                                                                                                return temp
                                                                                    if event.key >= 97 and event.key<=122 and len(temp)<10:
                                                                                                temp += chr(event.key)
                                                                                    if event.key ==8:                               #BACKSPACE
                                                                                                temp = temp[0:-1]
                                                                                    if event.key == 13:                             #Enter pressed
                                                                                                if len(temp)>0:
                                                                                                            return temp
                                                                                    gameDisplay.fill((0,0,130))
                                                                                    text = font.render(  msg  , True, (255,255,255))
                                                                                    gameDisplay.blit( text,  [80,170] )
                                                                                    #RECTANGLE SURFACE FROM HERE . .  .
                                                                                    pygame.draw.rect( gameDisplay , (40,30,150) ,( 260,170         ,         500,40) )                                   #Draws a rectangle and fills it with the Color                                                  
                                                                                    text = font.render(  temp  , True, (255,255,255))
                                                                                    gameDisplay.blit( text,  [290,170] )
                                                                                    press ="~You can continue by hit [Enter]."
                                                                                    text = font.render(  press  , True, (225,255,255))
                                                                                    gameDisplay.blit( text,  [290,270] )
                                                                                    pygame.display.flip( )
#----------------------------------------------VERSION---->>(2.2)----------------------------------------------------------------------------------------








#ALL THE CONCEPT,CODE AND ARTWORK IS OWNED BY VIGNESH BALAJI S
#Image source: Google
#EMAIL:    vigneshbalaji.rajan@gmail.com (for details)
#THIS IS A PYTHON PROJECT FOR THE ACADEMIC YEAR 2018-2019(CLASS 11)
#PRODUCT OF 20 HOURS OF CODING WITH LOVE.
#YOU'LL ENJOY IT FOR SURE!!!!
#What are you waiting for???
#HIT THE F5 AND START PLAYING :P


#------------------------------CodeStartsHere---------------------------------------------------------------------
import pygame
import random
import time

#-----------------------------initialising pygame----------------------------------------------------------------------------------
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
gameDisplay = pygame.display.set_mode((1366, 768),pygame.FULLSCREEN)                                     
pygame.display.set_caption('FLAP IN SPACE')
clock = pygame.time.Clock()
#------------------------------definingColors-------------------------------------------------------------------------------
black = (0,0,0)
white = (255,255,255)
purple = (255,10,246)
skyblue = (0,215,255)
lightPurple = (245,150,240)
green = (0,200,30)
green1 = (0,200,100)
homeButtonL=(0,55,255)
homeButtonR=(0,55,255)
red = (200,0,0)
#------------------------------loadingImages-----------------------------------------------------------------
bulletImg1 = pygame.image.load('bulletImg.png')
rockImg = pygame.transform.scale(pygame.image.load('rock.png'), (100,100))

coverImg1 = pygame.image.load('coverImg.jpg')
coverImg = pygame.transform.scale(coverImg1, (1040, 400))

bgImg1 = pygame.image.load('bgImg.png')
bgImg = pygame.transform.scale(bgImg1, (1366, 768))

intro1 = pygame.transform.scale(pygame.image.load('intro1.jpg'), (1366, 768))
intro2 = pygame.transform.scale(pygame.image.load('intro2.jpg'), (1366, 768)) 
vigbalityImg1 = pygame.transform.scale(pygame.image.load('vigbality1.jpg'), (1366, 768))
vigbalityImg2 = pygame.transform.scale(pygame.image.load('vigbality2.jpg'), (1366, 768))
vigbalityImg3 = pygame.transform.scale(pygame.image.load('vigbality3.jpg'), (1366, 768))
vigbalityImg4 = pygame.transform.scale(pygame.image.load('vigbality4.jpg'), (1366, 768))


vigneshImg = pygame.transform.scale(pygame.image.load('vignesh.png'), (500,800))
anupamImg = pygame.transform.scale(pygame.image.load('anupam.png'), (500,800))
farazImg = pygame.transform.scale(pygame.image.load('faraz.png'), (500,800))
kuralImg = pygame.transform.scale(pygame.image.load('kural.png'), (500,800))
saiImg = pygame.transform.scale(pygame.image.load('sai.png'), (500,800))

vigneshImgC = pygame.transform.scale(pygame.image.load('vignesh.png'), (350,600))
anupamImgC = pygame.transform.scale(pygame.image.load('anupam.png'), (275,600))
farazImgC = pygame.transform.scale(pygame.image.load('faraz.png'), (275,600))
kuralImgC = pygame.transform.scale(pygame.image.load('kural.png'), (350,600))
saiImgC = pygame.transform.scale(pygame.image.load('sai.png'), (350,600))

vigneshImgF = pygame.transform.scale(pygame.image.load('vignesh.png'), (115, 145))
anupamImgF = pygame.transform.scale(pygame.image.load('anupam.png'), (115, 145))
farazImgF = pygame.transform.scale(pygame.image.load('faraz.png'), (115, 145))
kuralImgF = pygame.transform.scale(pygame.image.load('kural.png'),(115, 145))
saiImgF = pygame.transform.scale(pygame.image.load('sai.png'),(115, 145))




bgImgHome1 = pygame.image.load('bgImgHome.png')
bgImgHome = pygame.transform.scale(bgImgHome1, (1366, 768))
#--------------------------------def starts here--------------------------------------------------------------
def charDecider(number):
    if number==1:
        return kuralImgF
    if number==2:
        return saiImgF
    if number==3:
        return vigneshImgF
    if number==4:
        return anupamImgF
    if number==5:
        return farazImgF
def charChose():
    gameDisplay.blit(bgImgHome,(0,0))
    gameDisplay.blit(kuralImgC,(-40,80))
    gameDisplay.blit(saiImgC,(245,80))
    gameDisplay.blit(vigneshImgC,(520,80))
    gameDisplay.blit(anupamImgC,(825,80))
    gameDisplay.blit(farazImgC,(1100,80))
    pygame.display.update()
    colorDict = {1:red,2:black,3:black,4:black,5:black}
    x = 1
    char = 0
    done = False
    while not done:
        
       
       for event in pygame.event.get():
        
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 if x==0:
                     colorDict[5] = black
                 colorDict[x+1] = red
                 if x != 0 and x<5:
                     colorDict[x] = black
                 if x<5:    
                     x+=1
                 if x==5:
                     x=0
                     colorDict[5] = red
             if event.key == pygame.K_RETURN :
                 for i in colorDict.keys():
                     if colorDict[i]==red:
                         char = i
                         done = True
                
       pygame.draw.rect(gameDisplay,colorDict[1],[0,80,275,600],5)
    
       pygame.draw.rect(gameDisplay,colorDict[2],[275,80,275,600],5)
    
       pygame.draw.rect(gameDisplay,colorDict[3],[550,80,275,600],5)
    
       pygame.draw.rect(gameDisplay,colorDict[4],[825,80,275,600],5)
   
       pygame.draw.rect(gameDisplay,colorDict[5],[1100,80,265,600],5)
    
       pygame.display.update()
    return char  
def init():
    vigChoice = [vigbalityImg1,vigbalityImg2,vigbalityImg3,vigbalityImg4]
    for i in range (6):
      for vig in vigChoice:
        gameDisplay.blit(vig, (0,0))
        pygame.display.flip()
        time.sleep(1/4)
    
    y1 = -400
    y2 = 1500
    while y1 < 1466:
        gameDisplay.blit(bgImgHome,(0,0))
        gameDisplay.blit(vigneshImg, (430,y1))
        gameDisplay.blit(farazImg, (150,y2))
        gameDisplay.blit(anupamImg, (800,y2))
        gameDisplay.blit(kuralImg, (940,y1))
        gameDisplay.blit(saiImg, (-100,y1))
        pygame.display.update()
        y1+=12
        y2-=12
    gameDisplay.blit(intro1, (0,0))
    pygame.display.update()
    time.sleep(5)
    gameDisplay.blit(intro2, (0,0))
    pygame.display.update()
    time.sleep(5)
    
    
    
    
    
       
def face(x,y,char):#main hero
    gameDisplay.blit(char, (x,y))
def ublock(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, lightPurple, [blockx, blocky, blockw, blockh])
    pygame.draw.rect(gameDisplay, color, [blockx+75, blocky, 50, blockh])
def dblock(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, lightPurple, [blockx, blocky, blockw, blockh])
    pygame.draw.rect(gameDisplay, color, [blockx+75, blocky, 50, blockh])
def showText(text,sleep,color,fontSize,center):
    Font = pygame.font.Font('AllerDisplay.ttf',fontSize)
    textSurf = Font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = center#(663,495)
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
    time.sleep(sleep)
def showScore(count):
    font = pygame.font.SysFont(None, 35)
    text = font.render("SCORE: "+str(count), True, skyblue)
    gameDisplay.blit(text,(1180,0))
def countDown():
    gameDisplay.fill(white)
    showText('3',1,black,300,(663,495))
    gameDisplay.fill(white)
    showText('2',1,black,300,(663,495))
    gameDisplay.fill(white)
    showText('1',1,black,300,(663,495))
def bullet(x,y):
    x+=100
    y+=20
    h = 35
    bulletImg = pygame.transform.scale(bulletImg1,(100,h))
    while x < 1280:
       gameDisplay.blit(bulletImg,(x,y))
       pygame.display.update()
       bulletImg = pygame.transform.scale(bulletImg1,(100,h))    
       x+=40
       h+=10
def bootUp(text):
    gameDisplay.fill((134,115,154))
    pygame.draw.rect(gameDisplay, black, [295, 400, 800,65])
    x = 1
    Font = pygame.font.Font('AllerDisplay.ttf',85)
    textSurf = Font.render(text, True, black)
    textRect = textSurf.get_rect()
    textRect.center = (700,350)
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
    
    while x < 800:
      pygame.draw.rect(gameDisplay, (90,250,22), [295, 400, x,65])
      x+=(1/2)
      pygame.display.flip()
def mainGame(char):#THE GAME LOOP
 score=0
 speedScore=0
 speedup=500
 x=450
 y=200
 yChange=0
 chosenChar=char
 face(x,y,char)
 gravity=8
  

 blockSpeed = 15 #initial value

 ublockStartx =2400                                                  
 ublockWidth = 200 
 ublockHeight = 400

 dblockStartx =1200                                                  
 dblockWidth = 200 
 dblockHeight = 400


 ublockStarty =-180#0#-350
 dblockStarty = 550#700#375

 rx = 1600
 ry = random.randrange(0,768)



 crashed = False
 blockStart=[(1200,2400),(2400,1200),(1200,2000),(2000,1200)]
 ublockStartx,dblockStartx= random.choice(blockStart)
 colorList = [(5,48,112),(199,3,22),(3,56,12)]
 color = random.choice(colorList)
 #-------------LoopOfGame-------------------------------------------------------------------------------------------------
 while not crashed:#gameloopstarts
     clock.tick(640)
 #---------------EventHandeling--------------------------------------------------------------------------------------------     
     for event in pygame.event.get():
        
         if event.type == pygame.KEYDOWN:
             x=500
             gravity=7
             if event.key == pygame.K_UP:
                yChange = 17#our effort in moving up
             if event.key == pygame.K_DOWN:
                yChange = -17#our effort in moving up
             if event.key == pygame.K_SPACE :
                bullet(x,y)
                if x<rx<(x+500) and y<ry<(y+100):
                    rx = 1600
                    ry = random.randrange(0,768)
                    score+=100
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_UP :
                yChange = 0
             if event.key == pygame.K_DOWN :
                yChange = 0    
         if event.type == pygame.QUIT:
             crashed = True
  #---------------FrameShiftLogic-----------------------------------------------------
     if rx < 0:
         rx = 1600
         ry = random.randrange(0,768)
         
     if ublockStartx < dblockStartx:
         if (dblockStartx+100)  < 0:    #calling the next pair of blocks into the screen
            blockStart=[(1200,2400),(2400,1200),(1200,2000),(2000,1200)]#the three combination of blocks
            ublockStartx,dblockStartx= random.choice(blockStart)
            blockpair=[(-180,550),(0,700),(-350,375)]
            ublockStarty,dblockStarty= random.choice(blockpair)
            color = random.choice(colorList)
     elif (ublockStartx+100)  < 0: 
         blockStart=[(1200,2400),(2400,1200),(1200,2000),(2000,1200)]#the three combination of blocks
         ublockStartx,dblockStartx= random.choice(blockStart)
         blockpair=[(-180,550),(0,700),(-350,375)]
         ublockStarty,dblockStarty= random.choice(blockpair)
         color = random.choice(colorList)
  #-----------CallingTheNextFrame----------------------------------------------------------------------------------     
     gameDisplay.blit(bgImg,(0,0))
     gameDisplay.blit(rockImg,(rx,ry))
     rx-=8 #rockSpeed
     ublock(ublockStartx, ublockStarty, ublockWidth, ublockHeight, color)
     ublockStartx -= blockSpeed #accelerator
     dblock(dblockStartx, dblockStarty, dblockWidth, dblockHeight, color)
     dblockStartx -= blockSpeed#accelerator
     face(x,y,char)
     showScore(score) #updating score
  #------FrameMover-------------------------------------------------------------------------------------------------
     y-=yChange
     y+=gravity
     score+=1
  #-----------------CRASH LOGIC-----------------------------------------------------------------------------------------------
     if ((ublockStartx+200)> (x+50) > ublockStartx) and ((y+20) < (ublockStarty+400)):
         crashed= True  #UpBlock
     if ((dblockStartx+200)> (x+50) > dblockStartx) and ((y+135) > dblockStarty):
         crashed= True#DownBlock
     if ((y+10) < -20) or (y+145)>788:
         crashed= True  
  #----------------DifficultyRaiser----------------------------------------------------------------------------     
     if score == speedup:#speed increase
         blockSpeed+=2
         gravity+=10
         yChange+=15
         speedup+=500 
         speedScore+=5
   
  #-------------------------------------------GameLoopEnds-----------------------------------------------------------------------------
       
    
     pygame.display.update()
     
     
          
 #--------------gameover final note ----------------------------- 
 Font = pygame.font.Font('AllerDisplay.ttf',115)
 pygame.mixer.music.pause()
 textSurf = Font.render('YOUR SCORE:'+ str(score), True, green1)
 textRect = textSurf.get_rect()
 textRect.center = (683,393)
 gameDisplay.blit(textSurf,textRect)
 pygame.display.update()
 time.sleep(3)
 
#-----------------------------------------------Def_EndsHere------------------------------------------------------------








#---------------------------------------------HomeScreenSetup--------------------------------------------------------------------
run=True
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
init()
while run:
   #-------------------------------------------HomeSrnNote&Button-----------------------------------------------------
   
   gameDisplay.blit(bgImgHome,(0,0))
   gameDisplay.blit(coverImg,(150,115))
   Font = pygame.font.Font('AllerDisplay.ttf',150)
   
   textRectL = pygame.draw.rect(gameDisplay, homeButtonL, [150, 520, 516, 170])
   textRectR = pygame.draw.rect(gameDisplay, homeButtonR, [675, 520, 513, 170])
   
   textSurfL = Font.render('  PLAY', True, black)
   textSurfR = Font.render('  QUIT', True, black)
   
   gameDisplay.blit(textSurfL,textRectL)
   gameDisplay.blit(textSurfR,textRectR)
  
   pygame.display.update()
   #--------------------------------------------HomeSrnEvent--------------------------------------------------------------
   for event in pygame.event.get():
           if event.type == pygame.MOUSEMOTION:#for button color change
                  xm,ym = event.pos
                  if (666 > xm > 150) and (690 > ym >520):
                      homeButtonL = (200,30,30)
               
                  elif (1188 > xm > 675) and (690 > ym >520):
                      homeButtonR = (200,30,30)
                  else:
                      homeButtonL,homeButtonR = (0,55,255),(0,55,255)    
           if event.type == pygame.MOUSEBUTTONUP:#for button clicking
                  pos = pygame.mouse.get_pos()
                  xClick,yClick = pos
                  if(666 > xClick > 150) and (690 >yClick >520):
                      
                      char = charDecider(charChose())
                      bootUp('GET READY!!!')
                      countDown() 
                      mainGame(char)
                      showText('Try Again!!!',2,skyblue,115,(663,495))
                      pygame.mixer.music.unpause()
                  if (1188 > xm > 675) and (690 > ym >520):
                      run=False    
           if event.type == pygame.KEYDOWN:#universal quiting option escape
                  if event.key == pygame.K_ESCAPE :
                      run=False
       
pygame.quit()
quit()


#----------------------------------------------------CodeEndsHere------------------------------------------------------













#-----------------------------------------------------THANK YOU---------------------------------------------------------------------------------------------------

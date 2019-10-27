import Giraffe2D



Running = True
myGame = Giraffe2D.App()
fps = 60

screenWidth = 640
screenHeight = 480

myGame.RenderWindow(screenWidth, screenHeight)
myGame.SetTitle("RPG GAME")


mySprite = Giraffe2D.Draw()
mySound = Giraffe2D.Sound("")

vel = 5
color = (11, 34, 65)

xPos = 100
yPos = 200


while(Running):
    myGame.FPS(fps)
    myEvent = Giraffe2D.Event()
    
    if myEvent.close:
        myGame.quit()
    keyboard = Giraffe2D.Keyboard()
    
    
        
    mySprite.DrawRect(color, 64, 64, xPos, yPos)
   
    
    if keyboard.moveRight:
        xPos += vel
    elif keyboard.moveLeft:
        xPos -= vel
    elif keyboard.moveUp:
        yPos -= vel
    elif keyboard.moveDown:
        yPos += vel
    
            
    
    
    myGame.Update()
    myGame.Fill((0,205,205))
   


   

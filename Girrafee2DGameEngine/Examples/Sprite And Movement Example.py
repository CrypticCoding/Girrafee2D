import Giraffe2D





Running = True
myGame = Giraffe2D.App()
fps = 60
screenWidth = 640
screenHeight = 480
myGame.RenderWindow(screenWidth, screenHeight)
myGame.SetTitle("RPG GAME")


mySprite = Giraffe2D.Sprite()

vel = 5


xPos = 100
yPos = 200


while(Running):
    myGame.FPS(fps)
    myEvent = Giraffe2D.Event()
    if myEvent.close:
        myGame.quit()
    keyboard = Giraffe2D.Keyboard()
    
    
        
    mySprite.DrawRect((0,225,0), 64, 64, xPos, yPos)
    mySprite.LookAtMouse()
    
    if keyboard.moveRight:
        xPos += vel
    if keyboard.moveLeft:
        xPos -= vel
    if keyboard.moveUp:
        yPos -= vel
    if keyboard.moveDown:
        yPos += vel 
            
    
    
    myGame.Update()
    myGame.Fill((0,205,205))
   


   

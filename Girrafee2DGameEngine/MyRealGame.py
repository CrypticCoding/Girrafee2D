import Giraffe2D



Running = True
myGame = Giraffe2D.App()
fps = 60
myGame.RenderWindow(640, 480)
myGame.SetTitle("MyWindowIsTHis")

myEvent = Giraffe2D.Event()
mySprite = Giraffe2D.Sprite()

keys = Giraffe2D.Keyboard()




while(Running):
    myGame.FPS(fps)
    if (myEvent.type("QUIT")):
        myGame.close()
    mySprite.DrawRect((0,225,0), 64, 64, 100, 200)
    
    if keys.checkForInput("left"):
        print("ass")
    
    myGame.Update()
    myGame.Fill((0,205,205))
   


   

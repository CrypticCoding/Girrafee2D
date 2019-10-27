import Giraffe2D
myGame = Giraffe2D.App()

myGame.RenderWindow(640,480)
myGame.SetTitle("Giraffe2D")


mySprite = Giraffe2D.Draw()

Running = True

while Running:
    myGame.FPS(60)
    myEvent = Giraffe2D.Event()
    
    if myEvent.close:
        myGame.quit()
    
    mySprite.DrawCircle(100, 100, (5,60,64), 20)
    
    
    myGame.Update()
    myGame.Fill((2,23,235))

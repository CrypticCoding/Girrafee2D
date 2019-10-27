import Giraffe2D

myGame = Giraffe2D.App()

myGame.RenderWindow(640,480)
myGame.SetTitle("WindowTitle")


mySprite = Giraffe2D.Draw()

Running = True

while Running:
    myGame.FPS(60)
    myEvent = Giraffe2D.Event()
    
    if myEvent.close:
        myGame.quit()
    mySprite.DrawRect((32,32,32),64, 64, 100,200)
    
    myGame.Update()
    myGame.Fill((2,23,235))

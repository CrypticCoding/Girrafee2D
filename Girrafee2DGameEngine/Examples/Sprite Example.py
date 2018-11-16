import Giraffe2D

myGame = Giraffe2D.App()

myGame.RenderWindow(640,480)
myGame.SetTitle("WindowTitle")


Running = True

while Running:
    myGame.FPS(60)
    myEvent = Giraffe2D.Event()
    if myEvent.close:
        myGame.quit()
    
    myGame.Update()

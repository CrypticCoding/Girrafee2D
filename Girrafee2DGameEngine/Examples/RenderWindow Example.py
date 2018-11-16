import Girrafee2D

myGame = Girrafee2D.App()
myGame.RenderWindow(640,480)
myGame.SetTitle("Slither")

fps = 30

myEvent = Girrafee2D.Event()

while True:
    myGame.FPS(fps)
    if myEvent.type("QUIT"):
        myGame.close()
    
myGame.run()

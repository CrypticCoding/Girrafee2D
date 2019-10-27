import Giraffe2D

myGame = Giraffe2D.App()
myGame.RenderWindow(640,480)
myGame.SetTitle("Slither")



fps = 30



while True:
    myGame.FPS(fps)
    myEvent = Giraffe2D.Event()
    if myEvent.close:
        myGame.quit()

    myGame.Update()

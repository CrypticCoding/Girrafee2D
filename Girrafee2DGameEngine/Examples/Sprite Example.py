import Giraffe2D

myGame = Giraffe2D.App()
myGame.RenderWindow(640,480)
myGame.SetTitle("This Is A Title")

mySprite = Giraffe2D.Sprite('..\Sprites\icon.png')


Running = True



while Running:
    myGame.FPS(30)
    mySprite.PlaceImage(20,20)
    Event = Giraffe2D.Event()

    if Event.close:
        myGame.quit()
    myGame.Update()
    
    

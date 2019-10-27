import Giraffe2D

myGame = Giraffe2D.App()
myGame.RenderWindow(640,480)
myGame.SetTitle("This Is A Title")
# New
myGame.SetIcon('Sprites/anotherIcon.png')

Running = True

while Running:
    myGame.FPS(30)
    
    Event = Giraffe2D.Event()

    if Event.close:
        myGame.quit()
    myGame.Update()
    
    

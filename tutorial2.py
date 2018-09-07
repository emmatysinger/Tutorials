from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 0.5)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 0.5)
black = Color(0x000000, 0.5)

thinline = LineStyle(1, black)
mycircle1 = CircleAsset(5, thinline, blue)
mycircle2 = CircleAsset(5, thinline, red)
xcoordinates = range(100, 600, 10)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle1, (x, x*0.5 + 100)) for x in range(100, 600, 10)]
sprites = [Sprite(mycircle2, (x, x*0.5 +100)) for x in range(100, 600, 10)]

myapp = App()
myapp.run()

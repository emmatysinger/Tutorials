from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)

ellipse = EllipseAsset(30, 20, thinline, blue)
polygon = PolygonAsset([(0,0),(60,0),(80,50),(0,40),(0,0)],thinline, red)

Sprite(polygon, (80,30))
Sprite(ellipse, (80,30))

# A graphics asset that represents a rectangle
rectangle = RectangleAsset(50, 20, thinline, blue)

# Now display a rectangle
Sprite(rectangle)

myapp=App()
myapp.run()

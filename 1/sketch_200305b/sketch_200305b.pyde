def setup():
    rectMode(CORNERS)
    size(400,600) 
def draw():
    if mousePressed:
        ellipse(mouseX, mouseY, 10, 10)

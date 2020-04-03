def setup():
    rectMode(CORNERS)
    size(400,600) 
def draw():
    if mousePressed:
        ellipse(mouseX, mouseY, width/40, width/40) # lepiej stosować wielkości zależne
        
# zabrakło mi jeszcze else w konstrukcji, miało się też coś zadziać gdy nie klikamy
# 1,5 pkt

global color1
global colorB
global colorK
color1 = color(255)
colorB = color(20, 60, 200)
colorK = color(150, 240, 30)

def setup():
    size(600, 600)
    textSize(400)
def draw():
    clear()
    text ("B", width/7-50, height/1.4)
    text ("K", width/2-20, height/1.4)
    print mouseX, mouseY
    
    if mouseX>=72 and mouseX<=240 and mouseY>142 and mouseY<=430:
         clear()
         fill(colorB)
         text ("B", width/7-50, height/1.4)
         fill(color1)
         text ("K", width/2-20, height/1.4)
    elif keyPressed:
        if key=="K" or key=="k":
            clear()
            fill(color1)
            text ("B", width/7-50, height/1.4)
            fill(colorK)
            text ("K", width/2-20, height/1.4)
            
    elif key == CODED:
        if keyCode == LEFT:
            clear()
            fill(colorB)
            text ("B", width/7-50, height/1.4)
            fill(color1)
            text ("K", width/2-20, height/1.4)
        elif keyCode == RIGHT:
            clear()
            fill(color1)
            text ("B", width/7-50, height/1.4)
            fill(colorK)
            text ("K", width/2-20, height/1.4)
            
    a = createShape()
    a.beginShape() 
    a.fill(20, 60, 200,255) 
    a.stroke(20, 60, 200)
    a.vertex(40, 400) 
    a.vertex(300, 400)
    a.vertex(260, 430)
    a.vertex(550, 430)
    a.endShape(CLOSE) 
    shape(a, 10, 80)

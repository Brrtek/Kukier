import random 
add_library('pdf') 

def setup():
    global img 
    size(492, 633) 
    img = loadImage("Zdjdowod.jpg")
    beginRecord(PDF, "Zdjdowod.pdf") 
    print(random.random()) 
    print(type(img)) 
def draw():
    global img
    image(img, 0, 0) 
    endRecord()
    if key == CODED:
        if keyCode == LEFT:
            img = loadImage("Zdjdowod.jpg")
            image(img, 0, 0)
            img = loadImage("glasses.png")
            image(img, 50, 240, height/1.6, width/3)
        elif keyCode == RIGHT:
            img = loadImage("Zdjdowod.jpg")
            image(img, 0, 0)
            img = loadImage("cap.png")
            image(img, 40, 0, height/1.5, width/1.5)

       
def mousePressed():
    endRecord()
    exit()

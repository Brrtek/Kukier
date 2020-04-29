import random 
add_library('pdf') 

def setup():
    global img, img2, img3
    size(492, 633) 
    img = loadImage("Zdjdowod.jpg")
    img2 = loadImage("glasses.png") # lepiej załadować raz na początku niż co klatkę
    img3 = loadImage("cap.png")
    beginRecord(PDF, "Zdjdowod.pdf") 
    print(random.random()) 
    print(type(img)) 
def draw():
    global img, img2, img3
    image(img, 0, 0, width, height) # warto uwzględnić skalowanie
    if key == CODED:
        if keyCode == LEFT:
            image(img2, 50, 240, height/1.6, width/3) # teraz tylko rysujemy co klatkę jeśli strzałka kliknięta
        elif keyCode == RIGHT:
            image(img3, 40, 0, height/1.5, width/1.5)

       
def mousePressed():
    endRecord()
    exit()
    
# 1,5p

class Mustang():
    
    def obraz(self, img):
        self.img = img
        image(loadImage(self.img), 60, 60, 500, 292)
        
        
    def ramka(self, x1, x2, x3, x4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        rect(self.x1, self.x2, self.x3, self.x4)
        
    def ramkaKolor(self, y1, y2, y3):
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        fill(y1, y2, y3)
        
    def ramkaSrodek(self, z1, z2, z3, z4):
        self.z1 = z1
        self.z2 = z2
        self.z3 = z3
        self.z4 = z4
        rect(self.z1, self.z2, self.z3, self.z4)
        
def setup():
    textSize(20)
    size(600, 400)
    global mustang, a
    a = "mustang.png"
    mustang = Mustang()
    
    try:
        mustang.ramka (40, 40, 520, 300)
        mustang.ramkaKolor(10,200,255)
        mustang.ramkaSrodek(50, 50, 500, 280)
        mustang.obraz(a)
        text("Wyswietlono obraz", width/2-80, height -10)
        
    except:
        
        mustang.ramkaKolor(255,0,0)
        text("Nie ma tego obrazka", width/2-100, height -10)
        mustang.ramka (40, 40, 520, 300)
        mustang.ramkaKolor(255,255,255)
        mustang.ramkaSrodek(50, 50, 500, 280)

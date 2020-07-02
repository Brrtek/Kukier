class szafka():
    def __init__(self, arg_x, arg_y):
        self.x = arg_x 
        self.y = arg_y
    def rys(self):
        rect( self.x, self.y,300,100,)
        
    

        
class uchwyt():
    uchwyt_click = 0
    def __init__(self, arg_x, arg_y):
        self.wcisniety = False
        self.x = arg_x 
        self.y = arg_y
    
    def przycisnij (self):
        uchwyt.uchwyt_click +=1
        self.wcisniety = not self.wcisniety
        if self.wcisniety:
            fill(255,0,0)
        else:
            fill(0,0,255)
            
    def rys(self):
        circle( self.x, self.y,20)

        
def setup():
    size(500,300)
    global Pozycja_szafka
    Pozycja_szafka = szafka(100,100)
    global Pozycja_uchwyt
    Pozycja_uchwyt = uchwyt(250,150)
def mouseClicked():
    Pozycja_uchwyt.przycisnij()
    
    
def draw():
    background(100,100,100)
    Pozycja_szafka.rys()
    Pozycja_uchwyt.rys()
    print(uchwyt.uchwyt_click)
    
# 1,75pkt

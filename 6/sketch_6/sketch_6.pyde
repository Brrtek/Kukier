class Kwadrat():
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y) 
        space = self.bok/paski 
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KolkowyKwadrat(Kwadrat):
    def sketchKolkowy(self, x, y, kolka):
        Kwadrat.sketch(self, x, y)
        przerwa =self.bok/kolka
        _xKolka_ = 0
        for kolko in range(0, kolka-1):
            _xKolka_+=przerwa
            circle(x+_xKolka_, y+_xKolka_, self.bok/kolka)
                    
def setup():
    size(500, 500)

    malyKolkowyKwadrat = KolkowyKwadrat(50.0)
    malyKolkowyKwadrat.sketchKolkowy(50,50,20)
    duzyKolkowyKwadrat = KolkowyKwadrat(300.0)
    duzyKolkowyKwadrat.sketchKolkowy(100,150,20)
    
# dosyć mocna kalka metody
# 1,5pkt

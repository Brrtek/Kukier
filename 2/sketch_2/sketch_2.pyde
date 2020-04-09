def setup():
    size(600, 600)
    frameRate(100)
    global x, y, o, p # aby mieć pewność, że te zmienne zainicjaliują się na początku przy otwarciu programu, powinny znaleźć się w tej funkcji
    x = float(300)
    y = float(0)
    o = float(1)
    p = float(1)                   
    global slownik_kolorow                            
    slownik_kolorow = {"biały":(255,255,255,80), "czarny":(0,0,0,100)} 
    global lista_kolorow
    lista_kolorow = []                    
    for klucz, wartosc in slownik_kolorow.items(): 
        lista_kolorow.append(wartosc) 
    global iteracja_programu
    iteracja_programu = 0             
def draw():                           
    global iteracja_programu
    global x, y, o, p
    iteracja_programu +=1                                                   
    stroke(*slownik_kolorow["biały"]) 
    fill(*lista_kolorow[iteracja_programu%len(lista_kolorow)])
    ellipse(x,y,60,60);
    x=x+o;
    y=y+p;

    if x>width:
        x=width
        o=-o
    if x<0:
        x=0
        o=-o
    if y>height:
        y=height
        p=-p
    if y<o:
        y=0
        p=-p
    if mousePressed:
        exit()
        
# 2 pkt
    

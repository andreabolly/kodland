#pgzero
#nuovo 1

WIDTH = 600
HEIGHT = 400

TITLE = "Tocca gli animali"
# vuol che chiamo in 1 secondo
# 30 volte le funzioni draw, update
FPS = 30

# Oggetti
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus1 = Actor("bonus", (450, 100))
bonus2 = Actor("bonus", (450, 200))
play = Actor("play", (300, 100))
shop = Actor("shop", (300, 200))
col = Actor("collection", (300, 300))
crocodile = Actor("crocodile", (100, 200))
hippo = Actor("hippo", (300, 200))
x = Actor("cross", (560, 30))

negozio = ["crocodile", "hippo"] 
collezione = []

# Variabili
count = 0
mode = "menu"


# NOSTRE FUNZIONI
def bonus_1():
    global count
    count = count + 2


def bonus_2():
    global count
    count = count + 10


def disegna_game():
    global count
    background.draw()
    animal.draw()
    screen.draw.text(count, center=(150, 100), color="white", fontsize=96)
    bonus1.draw()
    screen.draw.text("+2 ogni 5s", center=(450, 85), color="black", fontsize=17)
    screen.draw.text("prezzo: 5", center=(450, 105), color="black", fontsize=17)
    bonus2.draw()
    screen.draw.text("+10 ogni 5s", center=(450, 180), color="black", fontsize=17)
    screen.draw.text("prezzo: 15", center=(450, 200), color="black", fontsize=17)
    x.draw()

def mouse_game(button, pos):
    global count
    global mode
    if button == mouse.LEFT:
        if animal.collidepoint(pos):
            count = count + 1
            animal.y = 200
            animate(animal, tween="bounce_end", duration=0.5, y=250)
        elif bonus1.collidepoint(pos):
            # dobbiamo avere 5 punti
            if count >= 5:
                count = count - 5
                schedule_interval(bonus_1, 5)
        elif bonus2.collidepoint(pos):
            # dobbiamo avere 15 punti
            if count >= 15:
                count = count - 15
                schedule_interval(bonus_2, 5)
        elif x.collidepoint(pos):
            mode = "menu"
            

def mouse_shop(button, pos):
    global count
    global mode
    global negozio, collezione
    if button == mouse.LEFT:
        if x.collidepoint(pos):
            mode = "menu"
        elif crocodile.collidepoint(pos):
            if count >= 50:
                count -= 50
                #hai almeno 50 punti puoi comprare il coccodrillo
                negozio.remove("crocodile")
                collezione.append("crocodile")
        elif hippo.collidepoint(pos):
            if count >= 75:
                count -= 75
                #hai almeno 50 punti puoi comprare il coccodrillo
                negozio.remove("hippo")
                collezione.append("hippo")


def mouse_menu(button, pos):
    global mode
    if button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = "game"
        elif shop.collidepoint(pos):
            mode = "shop"


def disegna_menu():
    global count
    background.draw()
    screen.draw.text(count, topleft=(30, 30), color="white", fontsize=45)
    play.draw()
    shop.draw()
    col.draw()


def disegna_shop():
    global count
    global negozio, collezione
    
    background.draw()
    screen.draw.text(count, topleft=(30, 30), color="white", fontsize=45)
    
    if "crocodile" in negozio:
        crocodile.draw()
        screen.draw.text("500 €", topleft=(70, 300), color="white", fontsize=35)
    
    if "hippo" in negozio:
        hippo.draw()
        screen.draw.text("2500 €", topleft=(250, 300), color="white", fontsize=35)
    
    x.draw()

# FUNZIONI DI PYGAMEZERO
def draw():
    global mode
    if mode == "game":
        disegna_game()
    elif mode == "menu":
        disegna_menu()
    elif mode == "shop":
        disegna_shop()


def on_mouse_down(button, pos):
    global count
    global mode
    if mode == "game":
        mouse_game(button, pos)
    elif mode == "menu":
        mouse_menu(button, pos)
    elif mode == "shop":
        mouse_shop(button, pos)
        
        
        
        
        

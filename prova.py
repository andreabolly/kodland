#pgzero

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


def mouse_menu(button, pos):
    global mode
    if button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = "game"


def disegna_menu():
    global count
    background.draw()
    screen.draw.text(count, topleft=(30, 30), color="white", fontsize=45)
    play.draw()


# FUNZIONI DI PYGAMEZERO
def draw():
    global mode
    if mode == "game":
        disegna_game()
    elif mode == "menu":
        disegna_menu()


def on_mouse_down(button, pos):
    global count
    global mode
    if mode == "game":
        mouse_game(button, pos)
    elif mode == "menu":
        mouse_menu(button, pos)

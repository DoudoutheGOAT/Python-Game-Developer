import pgzrun
import random
WIDTH=1000
HEIGHT=750
gorilla=Actor("removed background gorilla.png")
freshlol=Actor("freshlol.png")
noob=Actor("netherite_noob.png")
gorilla.x=100
gorilla.y=300
freshlol.x=100
freshlol.y=100
noob.x=100
noob.y=500
def draw():
    screen.fill("gold")
    gorilla.draw()
    freshlol.draw()
    noob.draw()
def update():
    if keyboard.s:
        noob.y+=5
    if keyboard.w:
        noob.y-=5
    if keyboard.d:
        noob.x+=5
    if keyboard.a:
        noob.x-=5
pgzrun.go()
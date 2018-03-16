from Graphics import *
import time
from Building import *
from Base import *
win = GraphWin("City",1900,1000)
land = City(win)
land.backdrop()
b1 = Building(100, 350, "gray", win, "black", "white")
b2 = House(600, 350, color_rgb(219, 215, 177), win, "white", color_rgb(81, 45, 45))
b3 = Townhouse(1200, 350, color_rgb(102, 51, 0), win, "white", color_rgb(79, 36, 18))
land.drawBox()
win.getMouse()
y = 0
vlc.MediaPlayer("siren.wav").play()
while y <= 600:
    nuke = Nuke(win, 950, y)
    y += 100
    time.sleep(1)
nuke.explode()
win.getMouse()
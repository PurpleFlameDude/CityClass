from Graphics import *
import vlc
class City(object):
    def __init__(self,window):
        self.window = window

    def drawBox(self):
        counter = 0
        x = 150
        y = 650
        while counter != 4:
            base = Rectangle(Point(x,y),Point(x+30,y+100))
            side = Polygon(Point(x+30,y+100),Point(x+45,y+85),Point(x+45,y),Point(x+30,y))
            box = Rectangle(Point(x-10,y-30),Point(x+40,y))
            boxTop = Arc(Point(x-10,y-50),Point(x+40,y-10),0,180)
            boxSide = Rectangle(Point(x,y-30),Point(x+50,y))
            boxTopB = Arc(Point(x, y - 50), Point(x + 50, y - 10), 0, 180)
            doorHand = Rectangle(Point(x,y-20),Point(x+25,y-10))
            flag = Rectangle(Point(x+41,y-38),Point(x+49,y-28))
            stem = Rectangle(Point(x+41,y-38),Point(x+45,y-18))
            boxSide.setFill("white")
            boxSide.draw(self.window)
            boxTopB.setFill("white")
            boxTopB.draw(self.window)
            boxTop.setFill("white")
            boxTop.draw(self.window)
            box.setFill("white")
            box.draw(self.window)
            side.setFill("white")
            side.draw(self.window)
            base.setFill("white")
            base.draw(self.window)
            doorHand.setFill("white")
            doorHand.draw(self.window)
            stem.setFill("red")
            stem.draw(self.window)
            flag.setFill("red")
            flag.draw(self.window)
            counter += 1
            x += 450
            y += 11.5


    def backdrop(self):
        back = Image(Point(950,200),"easytotype.png")
        back.draw(self.window)
        ground = Polygon(Point(0,400),Point(1900,450),Point(1900,1000),Point(0,1000))
        street = Polygon(Point(0,750),Point(1900,800),Point(1900,1000),Point(0,1000))
        road = Polygon(Point(0,800),Point(1900,850),Point(1900,1000),Point(0,1000))
        road.setFill("black")
        street.setFill("light grey")
        ground.setFill("green")
        ground.draw(self.window)
        street.draw(self.window)
        x = 0
        y = 50
        z = 25
        v = 75
        p = 750
        while x <= 1900:
            tile = Polygon(Point(x, p), Point(z,1000),Point(v, 1000),Point(y,p))
            tile.setFill('light grey')
            tile.draw(self.window)
            x += 50
            y += 50
            z += 50
            v += 50
            p += 1.25
        road.draw(self.window)
        x = 0
        y = 75
        z = 25
        v = 100
        p = 925
        counter = 0
        while x <= 1900:
            if counter % 6 == 1:
                strip = Polygon(Point(x, p), Point(z, p + 25), Point(v, p + 25), Point(y, p))
                strip.setFill('yellow')
                strip.draw(self.window)
            x += 50
            y += 50
            z += 50
            v += 50
            p += 2
            counter += 1
class Nuke(object):
    def __init__(self,window,x,y):
        self.window = window
        self.x = x
        self.y = y
        self.drawNuke(window)

    def drawNuke(self,window):
        tail = Polygon(Point(self.x,self.y),Point(self.x+5,self.y),Point(self.x+10,self.y+10),Point(self.x+5,self.y+10))
        base = Oval(Point(self.x+5,self.y+10),Point(self.x+30,self.y+60))
        tailO = Polygon(Point(self.x+35,self.y),Point(self.x+30,self.y),Point(self.x+25,self.y+10),Point(self.x+30,self.y+10))
        tail.setFill("black")
        base.setFill("black")
        tailO.setFill("black")
        tail.draw(self.window)
        base.draw(self.window)
        tailO.draw(self.window)
    def explode(self):
        cloud1 = Polygon(Point(125,500),Point(50,400),Point(225,350),Point(25,275),Point(200,175),Point(100,50),Point(250,100),Point(375,25),Point(450,100),Point(550,25),Point(600,125),Point(750,25),Point(800,125),Point(950,75),Point(1900-800,125),Point(1900-750,25),Point(1900-600,125),Point(1900-550,25),Point(1900-450,100),Point(1900-375,25),Point(1900-375,25),Point(1900-250,100),Point(1900-100,50),Point(1900-200,175),Point(1900-25,275),Point(1900-125,1000-500),Point(1900-50,1000-400),Point(1900-225,1000-350),Point(1900-25,1000-275),Point(1900-200,1000-175),Point(1900-100,1000-50),Point(1900-250,1000-100),Point(1900-375,1000-25),Point(1900-450,1000-100),Point(1900-550,1000-25),Point(1900-600,1000-125),Point(1900-750,1000-25),Point(1900-800,1000-125),Point(1900-950,1000-75),Point(800,1000-125),Point(750,1000-25),Point(600,1000-125),Point(550,1000-25),Point(450,1000-100),Point(375,1000-25),Point(375,1000-25),Point(250,1000-100),Point(100,1000-50),Point(200,1000-175),Point(25,1000-275))
        cloud1.setFill("orange")
        cloud1.draw(self.window)
        vlc.MediaPlayer("bomb+1.wav").play()
        back = Image(Point(950, 500), "Mr.bae.png")
        back.draw(self.window)
        #back = Image(Point(950,200),"capture.png")
        #back.draw(self.window)
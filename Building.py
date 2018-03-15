from graphics import *

class Building(object):

    def __init__(self, x, y, color, win, color1, color2):
        """creates a building"""
        self.x = x
        self.y = y
        self.color = color
        self.drawBuilding(x, y, color ,win)
        self.drawDoor(win, color1, color2)

    def drawBuilding(self, x, y, color, win):
        building = Rectangle(Point(x, y), Point(x + 300, y + 300))
        top = Polygon(Point(x + 100, y - 200), Point(x + 400,y - 200), Point(x + 300, y), Point(x,y))
        side = Polygon(Point(x + 300,y ), Point(x + 400, y - 200 ), Point(x + 400,y + 100 ), Point(x + 300,y + 300 ))
        building.setFill(color)
        top.setFill(color)
        side.setFill(color)
        top.draw(win)
        side.draw(win)
        building.draw(win)

    def drawDoor(self, win, color1, color2):
        door = Rectangle(Point(self.x + 125, self.y + 230), Point(self.x + 175, self.y + 300))
        door.setFill(color1)
        door.draw(win)
        doorDesign = Polygon(Point(self.x + 125, self.y + 230), Point(self.x + 175, self.y + 230),Point(self.x + 125, self.y + 300), Point(self.x + 175, self.y + 300))
        doorDesign.setFill(color2)
        doorDesign.draw(win)
        #doorknob
        knob = Circle(Point(self.x + 130, self.y + 270), 2.5)
        knob.setFill("Gold")
        knob.draw(win)

class House(Building):
    def __init__(self, x, y, color, win, color1, color2):
        """Creates a house"""
        super(House,self).__init__(x, y, color, win, color1, color2)
        self.drawRoof(win)
        self.drawWindows(win)

    def drawRoof(self, win):
        """Draws the roof"""
        leftRoof = Polygon(Point(self.x, self.y), Point(self.x + 150, self.y - 150), Point(self.x + 250, self.y - 350), Point(self.x + 100, self.y - 200))
        leftRoof.setFill(color_rgb(96, 96, 96))
        leftRoof.draw(win)
        rightRoof = Polygon(Point(self.x + 300, self.y), Point(self.x + 150, self.y - 150), Point(self.x + 250, self.y - 350), Point(self.x + 400, self.y - 200))
        rightRoof.setFill(color_rgb(96, 96, 96))
        rightRoof.draw(win)
        middleRoof = Polygon(Point(self.x, self.y), Point(self.x + 150, self.y - 150), Point(self.x + 300, self.y))
        middleRoof.setFill(color_rgb(96, 96, 96))
        middleRoof.draw(win)

    def drawWindows(self, win):
        """Draws Identical Windows"""
        # window1
        rect1 = Rectangle(Point(self.x + 50, self.y + 50), Point(self.x + 100, self.y +100))
        line1 = Line(Point(self.x + 50, self.y + 75), Point(self.x + 100, self.y + 75))
        line2 = Line(Point(self.x + 75, self.y + 50), Point(self.x + 75, self.y + 100))
        shutter1 = Rectangle(Point(self.x + 25, self.y + 50), Point(self.x + 50, self.y + 100))
        shutter2 = Rectangle(Point(self.x + 100, self.y + 50), Point(self.x + 125, self.y + 100))
        rect1.draw(win)
        rect1.setFill("Light blue")
        line1.draw(win)
        line2.draw(win)
        shutter1.draw(win)
        shutter1.setFill("white")
        shutter2.draw(win)
        shutter2.setFill("white")
        # window2
        rect2 = Rectangle(Point(self.x + 200, self.y + 50), Point(self.x + 250, self.y + 100))
        line3 = Line(Point(self.x + 200, self.y + 75), Point(self.x + 250, self.y + 75))
        line4 = Line(Point(self.x + 225 ,self.y + 50), Point(self.x + 225, self.y + 100))
        shutter3 = Rectangle(Point(self.x + 175, self.y + 50), Point(self.x + 200, self.y + 100))
        shutter4 = Rectangle(Point(self.x + 250, self.y + 50), Point(self.x + 275, self.y + 100))
        rect2.draw(win)
        rect2.setFill("Light blue")
        line3.draw(win)
        line4.draw(win)
        shutter3.draw(win)
        shutter3.setFill("white")
        shutter4.draw(win)
        shutter4.setFill("white")

class Townhouse(House):

    def __init__(self, x, y, color, win, color1, color2):
        """Creates a townhouse"""
        counter = 0
        while counter != 2:
            super(Townhouse,self).__init__(x, y, color, win, color1, color2)
            self.drawChimney(win)
            if counter == 1:
                super(Townhouse, self).__init__(x + 300, y, color, win, color1, color2)
                self.drawChimney(win)
            counter += 1


    def drawChimney(self, win):
        """Creates a chimney"""
        frontChim = Rectangle(Point(self.x + 75, self.y - 275), Point(self.x + 125, self.y - 150))
        sideChim = Polygon(Point(self.x + 125, self.y - 150), Point(self.x + 125, self.y - 275), Point(self.x + 150, self.y - 325), Point(self.x + 150, self.y - 200))
        topChim = Polygon(Point(self.x + 75, self.y - 275), Point(self.x + 100, self.y - 325), Point(self.x + 150, self.y - 325), Point(self.x + 125, self.y - 275))
        #smokeChim = Oval(Point(self.x + 100, self.y - 325), Point(self.x + 125, self.y - 275))
        frontChim.draw(win)
        frontChim.setFill(color_rgb(124, 10, 2))
        sideChim.draw(win)
        sideChim.setFill(color_rgb(124, 10, 2))
        topChim.draw(win)
        topChim.setFill("black")
        #smokeChim.draw(win)
        #smokeChim.setFill("Black")



from Building import *

def main():
    win = GraphWin("TestWindow", 1900, 1000)
    b1 = Building(100, 400, "gray", win, "black", "white")
    b2 = House(600, 400, color_rgb(219, 215, 177), win, "white", color_rgb(81, 45, 45))
    b3 = Townhouse(1100, 400, color_rgb(102, 51, 0), win, "white", color_rgb(79, 36, 18))





    win.getMouse()
    win.close()


main()

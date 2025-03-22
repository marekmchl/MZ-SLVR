from window import Window
from drawing import Cell

def main():
    win = Window(800, 600)
    cell = Cell(10, 10, 250, 250, win)
    cell.draw("black")
    win.wait_for_close()

main()

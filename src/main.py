from window import Window
from drawing import Cell

def main():
    win = Window(800, 600)

    cell_1 = Cell(4, 4, 254, 254, win)
    cell_1.has_right_wall = False

    cell_2 = Cell(254, 4, 504, 254, win)
    cell_2.has_right_wall = False
    cell_2.has_left_wall = False

    cell_3 = Cell(504, 4, 754, 254, win)
    cell_3.has_left_wall = False

    cell_1.draw("black")
    cell_2.draw("black")
    cell_3.draw("black")

    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3, undo=True)

    win.wait_for_close()

main()

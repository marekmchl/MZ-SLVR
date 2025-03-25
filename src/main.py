from window import Window
from drawing import Maze

def main():
    win = Window(800, 600)
    start_x = 4
    start_y = start_x
    rows_x = 16
    rows_y = rows_x
    size_x = 100
    size_y = size_x
    maze = Maze(start_x, start_y, rows_x, rows_y, size_x, size_y, win)

    win.wait_for_close()

main()

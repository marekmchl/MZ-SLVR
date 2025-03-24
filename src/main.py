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
    for i in range(rows_x):
        for j in range(rows_y):
            maze._draw_cell(i, j)

    maze._break_walls_r(0, 0)

    maze._break_entrance_and_exit()

    win.wait_for_close()

main()

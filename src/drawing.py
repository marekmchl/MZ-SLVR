import random
from time import sleep

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell():
    def __init__(self, x1, y1, x2, y2, window):
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self.has_left_wall = True
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self._win = window
        self.visited = False

    def draw(self, fill_color):
        no_color = "#d9d9d9"
        if self.has_top_wall:
            wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            wall.draw(self._win.canvas, fill_color)
        else:
            wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            wall.draw(self._win.canvas, no_color)

        if self.has_bottom_wall:
            wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            wall.draw(self._win.canvas, fill_color)
        else:
            wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            wall.draw(self._win.canvas, no_color)

        if self.has_left_wall:
            wall = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            wall.draw(self._win.canvas, fill_color)
        else:
            wall = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            wall.draw(self._win.canvas, no_color)

        if self.has_right_wall:
            wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            wall.draw(self._win.canvas, fill_color)
        else:
            wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            wall.draw(self._win.canvas, no_color)

    def draw_move(self, to_cell, undo=False):
        center_1 = Point(
            (self.x2 + self.x1) / 2,
            (self.y1 + self.y2) / 2)

        center_2 = Point(
            (to_cell.x2 + to_cell.x1) / 2,
            (to_cell.y1 + to_cell.y2) / 2)

        path = Line(center_1, center_2)

        if not undo:
            path.draw(self._win.canvas, "red")
        else:
            path.draw(self._win.canvas, "gray")

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed != None:
            self.seed = random.seed(seed)
        self._create_cells()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._break_entrance_and_exit()

    def _create_cells(self):
        row = []
        x1 = self.x1
        for i in range(self.num_cols):
            col = []
            x2 = x1 + self.cell_size_x
            y1 = self.y1
            for j in range(self.num_rows):
                y2 = y1 + self.cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                col.append(cell)
                y1 = y2
            x1 = x2
            row.append(col)
        self._cells = row
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)



    def _draw_cell(self, i, j):
        self._cells[i][j].draw("black")
        self._animate()

    def _animate(self):
        win = self._win
        win.redraw()
        sleep(0.02)

    def _break_entrance_and_exit(self):
        if len(self._cells) != 0:
            self._cells[0][0].has_top_wall = False
            self._draw_cell(0, 0)

            if len(self._cells[0]) != 0:
                self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
                self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True

        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:                   # left
                to_visit.append((i-1, j))
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:   # right
                to_visit.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:                   # up
                to_visit.append((i, j-1))
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:   # down
                to_visit.append((i, j+1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            new_i, new_j = random.choice(to_visit)

            new_cell = self._cells[new_i][new_j]
            if new_i - i == 1:
                current_cell.has_right_wall = False
                new_cell.has_left_wall = False
            elif new_i - i == -1:
                current_cell.has_left_wall = False
                new_cell.has_right_wall = False
            elif new_j - j == 1:
                current_cell.has_bottom_wall = False
                new_cell.has_top_wall = False
            elif new_j - j == -1:
                current_cell.has_top_wall = False
                new_cell.has_bottom_wall = False

            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for cols in self._cells:
            for cell in cols:
                cell.visited = False

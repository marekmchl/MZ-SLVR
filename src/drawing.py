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

    def draw(self, fill_color):
        if self.has_top_wall:
            wall = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            wall.draw(self._win.canvas, fill_color)

        if self.has_bottom_wall:
            wall = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            wall.draw(self._win.canvas, fill_color)

        if self.has_left_wall:
            wall = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            wall.draw(self._win.canvas, fill_color)

        if self.has_right_wall:
            wall = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            wall.draw(self._win.canvas, fill_color)

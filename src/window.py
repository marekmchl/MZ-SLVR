from tkinter import Tk, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title("MZ-SLVR: The maze solver")
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.__root_widget.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root_widget)
        self.canvas.pack(anchor="center", fill="both", expand=True)
        self.window_is_running = False

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()

    def close(self):
        self.window_is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

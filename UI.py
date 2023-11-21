from tkinter import *
from main import Cell
import set1
import set2
root = Tk()
root.configure(bg="#69db7c")
root.geometry(f'{set1.WIDTH}x{set1.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)
top_frame = Frame(
    root,
    bg='#69db7c',
    width=set1.WIDTH,
    height=set2.height_prct(25)
)
top_frame.place(x=0, y=0)
game_title = Label(
    top_frame,
    bg='#69db7c',
    fg='black',
    text='Minesweeper Game',
    font=('', 48)
)
game_title.place(
    x=set2.width_prct(25), y=0
)
left_frame = Frame(
    root,
    bg='#69db7c',
    width=set2.width_prct(25),
    height=set2.height_prct(75)
)
left_frame.place(x=0, y=set2.height_prct(25))
center_frame = Frame(
    root,
    bg='#69db7c',
    width=set2.width_prct(75),
    height=set2.height_prct(75)
)
center_frame.place(
    x=set2.width_prct(25),
    y=set2.height_prct(25),
)
for x in range(set1.GRID_SIZE):
    for y in range(set1.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)
Cell.randomize_mines()
root.mainloop()

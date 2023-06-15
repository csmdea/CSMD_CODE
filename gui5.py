
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\TK\build\assets\frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.attributes('-fullscreen', True)
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    235.0,
    218.0,
    anchor="nw",
    text="방문해주셔서 감사합니다",
    fill="#000000",
    font=("OPTIBodoni Antiqua", 32 * -1)
)

canvas.create_text(
    303.0,
    262.0,
    anchor="nw",
    text="즐거운 쇼핑 시간 되세요",
    fill="#000000",
    font=("OPTIBodoni Antiqua", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=643.0,
    y=344.0,
    width=72.0,
    height=72.0
)
window.resizable(False, False)
window.mainloop()

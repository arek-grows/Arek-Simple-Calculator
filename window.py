from tkinter import *
import textwrap

ouput_text = ''  # input - updates on every button
memory_text = ''  # memory - updates on CE, operators, and =

global operators = ['÷', '×', '-', '+']
global previous_number = ''
global previous_operator = ''


def update_texts(inp, mem):
    output['state'] = 'normal'
    output.insert(1.0, inp)
    output['state'] = 'disabled'
    memory['text'] = textwrap.fill(mem, 16)


def btn_clicked():
    print("Button Clicked")


def btn4_clicked():
    previous_number += '4'


window = Tk()

window.geometry("170x334")
window.configure(bg="#000000")
canvas = Canvas(
    window,
    bg="#000000",
    height=334,
    width=170,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

img0 = PhotoImage(file=f"img0.png")
b4 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn4_clicked,
    relief="flat")

b4.place(
    x=2, y=208,
    width=40,
    height=40)

img1 = PhotoImage(file=f"img1.png")
b5 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b5.place(
    x=44, y=208,
    width=40,
    height=40)

img2 = PhotoImage(file=f"img2.png")
b6 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b6.place(
    x=86, y=208,
    width=40,
    height=40)

img3 = PhotoImage(file=f"img3.png")
bmin = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bmin.place(
    x=128, y=208,
    width=40,
    height=40)

img4 = PhotoImage(file=f"img4.png")
b1 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b1.place(
    x=2, y=250,
    width=40,
    height=40)

img5 = PhotoImage(file=f"img5.png")
b2 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b2.place(
    x=44, y=250,
    width=40,
    height=40)

img6 = PhotoImage(file=f"img6.png")
b3 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b3.place(
    x=86, y=250,
    width=40,
    height=40)

img7 = PhotoImage(file=f"img7.png")
bplus = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bplus.place(
    x=128, y=250,
    width=40,
    height=40)

img8 = PhotoImage(file=f"img8.png")
b0 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=2, y=292,
    width=124,
    height=40)

img9 = PhotoImage(file=f"img9.png")
bequ = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bequ.place(
    x=128, y=292,
    width=40,
    height=40)

img10 = PhotoImage(file=f"img10.png")
bCE = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bCE.place(
    x=2, y=124,
    width=40,
    height=40)

img11 = PhotoImage(file=f"img11.png")
b8 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b8.place(
    x=44, y=166,
    width=40,
    height=40)

img12 = PhotoImage(file=f"img12.png")
bC = Button(
    image=img12,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bC.place(
    x=44, y=124,
    width=40,
    height=40)

img13 = PhotoImage(file=f"img13.png")
bmul = Button(
    image=img13,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bmul.place(
    x=128, y=166,
    width=40,
    height=40)

img14 = PhotoImage(file=f"img14.png")
bneg = Button(
    image=img14,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bneg.place(
    x=86, y=124,
    width=40,
    height=40)

img15 = PhotoImage(file=f"img15.png")
b7 = Button(
    image=img15,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b7.place(
    x=2, y=166,
    width=40,
    height=40)

img16 = PhotoImage(file=f"img16.png")
bdiv = Button(
    image=img16,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

bdiv.place(
    x=128, y=124,
    width=40,
    height=40)

img17 = PhotoImage(file=f"img17.png")
b9 = Button(
    image=img17,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b9.place(
    x=86, y=166,
    width=40,
    height=40)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    85.0, 102.0,
    image=entry0_img)

output = Text(
    font="Consolas 28",
    bd=0,
    bg="#c4c4c4",
    highlightthickness=0,
    state='disabled')

output.place(
    x=2, y=82,
    width=166,
    height=38)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    85.0, 42.0,
    image=entry1_img)

# entry1 = Text(
#     bd=0,
#     bg="#c4c4c4",
#     highlightthickness=0,
#     font="Calibri 24")
#
# entry1.place(
#     x=2, y=2,
#     width=166,
#     height=78)

memory = Label(
    anchor=SE,
    justify='left',
    bd=0,
    bg="#c4c4c4",
    font="Consolas 14"
)

memory.place(
    x=2, y=2,
    width=166,
    height=78
)

window.resizable(False, False)
window.mainloop()

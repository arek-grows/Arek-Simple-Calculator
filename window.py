from tkinter import *
import textwrap

output_text = ''  # input - updates on every button

operating_list = []  # iterable for math when '=' pressed
# update this before calling update_memory() to change the memory text output

memory_text = ''  # memory - updates on CE, operators, and =

operators = ['÷', '×', '-', '+']
operated = False


def update_output():
    global output_text, operated
    if operated:
        output_text = output_text[-1]
        operated = False
    output['text'] = output_text


def update_memory():
    global memory_text, operating_list
    if operating_list:
        memory_text = ''.join(operating_list)
    else:
        memory_text = ''
    memory['text'] = textwrap.fill(memory_text, 16)


def btn0_clicked():
    global output_text
    output_text += '0'
    update_output()


def btn1_clicked():
    global output_text
    output_text += '1'
    update_output()


def btn2_clicked():
    global output_text
    output_text += '2'
    update_output()


def btn3_clicked():
    global output_text
    output_text += '3'
    update_output()


def btn4_clicked():
    global output_text
    output_text += '4'
    update_output()


def btn5_clicked():
    global output_text
    output_text += '5'
    update_output()


def btn6_clicked():
    global output_text
    output_text += '6'
    update_output()


def btn7_clicked():
    global output_text
    output_text += '7'
    update_output()


def btn8_clicked():
    global output_text
    output_text += '8'
    update_output()


def btn9_clicked():
    global output_text
    output_text += '9'
    update_output()


def operator_clicked(oper):
    global output_text, memory_text, operating_list

    if not memory_text and not output_text:  # None / None, do nothing
        return print('operator clicked with no memory or number input')
    elif output_text:  # (None / 100) or (100 - / 100), create (just append?) memory and delete input (output_text)
        if float(output_text) == 0.0:
            output_text = '0'
        operating_list.append(output_text)
        operating_list.append(oper)
        output_text = ''
        update_output()
        update_memory()
        return print('operator clicked with no memory but with number input')
    elif memory_text and not output_text:  # 100 - / None, change operator in memory
        operating_list[-1] = oper
        update_memory()
        return print('operator clicked with memory but no number input')
    return print('operator_clicked didn''t work')


def bmin_clicked():
    operator_clicked('-')


def bplus_clicked():
    operator_clicked('+')


def bdiv_clicked():
    operator_clicked('÷')


def bmul_clicked():
    operator_clicked('×')


def bneg_clicked():
    global output_text
    if '.' in  output_text:
        output_text = str(float(output_text)*-1)
    elif output_text:
        output_text = str(int(output_text)*-1)
    update_output()


def btnCE_clicked():
    global operating_list, output_text
    operating_list = []
    output_text = ''
    update_output()
    update_memory()
    return print('everything cleared')


def btnC_clicked():
    global output_text
    output_text = ''
    update_output()
    print('number input cleared')


def bequ_clicked():
    global operating_list, output_text, operators, operated
    if not operating_list:
        return print('equals pressed when nothing in operating_list')
    else:
        if output_text and float(output_text) == 0.0:
            output_text = '0'
        if output_text:
            operating_list.append(output_text)
        elif operating_list[-1] in operators:
            operating_list.pop(-1)
        update_memory()
        opl = operating_list
        total = float(operating_list[0])
        try:
            for i in range(1, len(operating_list), 2):
                if opl[i] == '÷':
                    total /= float(opl[i+1])
                elif opl[i] == '×':
                    total *= float(opl[i+1])
                elif opl[i] == '-':
                    total -= float(opl[i + 1])
                elif opl[i] == '+':
                    total += float(opl[i + 1])
                else:
                    return print('equals error')
        except:
            operating_list = []
            output_text = ''
            memory['text'] = 'error'
            update_output()
            return print('math error')
        del opl
        print(total)
        total_string = str(total)
        if int(total_string[total_string.index('.')+1:]) == 0:
            output_text = str(int(total))
            update_output()
        else:
            output_text = str(round(float(total), 2))
            update_output()
        del total
        operating_list = []
        operated = True


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

# output (bottom)
entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    85.0, 102.0,
    image=entry0_img)
output = Label(
    anchor=E,
    justify='left',
    bd=0,
    bg="#c4c4c4",
    font="Consolas 28")
output.place(
    x=2, y=82,
    width=166,
    height=38)

# memory (top)
entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    85.0, 42.0,
    image=entry1_img)
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

# 0
img8 = PhotoImage(file=f"img8.png")
b0 = Button(
    image=img8,
    borderwidth=0,
    highlightthickness=0,
    command=btn0_clicked,
    relief="flat")
b0.place(
    x=2, y=292,
    width=124,
    height=40)

# 1
img4 = PhotoImage(file=f"img4.png")
b1 = Button(
    image=img4,
    borderwidth=0,
    highlightthickness=0,
    command=btn1_clicked,
    relief="flat")
b1.place(
    x=2, y=250,
    width=40,
    height=40)

# 2
img5 = PhotoImage(file=f"img5.png")
b2 = Button(
    image=img5,
    borderwidth=0,
    highlightthickness=0,
    command=btn2_clicked,
    relief="flat")
b2.place(
    x=44, y=250,
    width=40,
    height=40)

# 3
img6 = PhotoImage(file=f"img6.png")
b3 = Button(
    image=img6,
    borderwidth=0,
    highlightthickness=0,
    command=btn3_clicked,
    relief="flat")
b3.place(
    x=86, y=250,
    width=40,
    height=40)

# 4
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

# 5
img1 = PhotoImage(file=f"img1.png")
b5 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn5_clicked,
    relief="flat")
b5.place(
    x=44, y=208,
    width=40,
    height=40)

# 6
img2 = PhotoImage(file=f"img2.png")
b6 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=btn6_clicked,
    relief="flat")
b6.place(
    x=86, y=208,
    width=40,
    height=40)

# 7
img15 = PhotoImage(file=f"img15.png")
b7 = Button(
    image=img15,
    borderwidth=0,
    highlightthickness=0,
    command=btn7_clicked,
    relief="flat")
b7.place(
    x=2, y=166,
    width=40,
    height=40)

# 8
img11 = PhotoImage(file=f"img11.png")
b8 = Button(
    image=img11,
    borderwidth=0,
    highlightthickness=0,
    command=btn8_clicked,
    relief="flat")
b8.place(
    x=44, y=166,
    width=40,
    height=40)

# 9
img17 = PhotoImage(file=f"img17.png")
b9 = Button(
    image=img17,
    borderwidth=0,
    highlightthickness=0,
    command=btn9_clicked,
    relief="flat")
b9.place(
    x=86, y=166,
    width=40,
    height=40)

# -
img3 = PhotoImage(file=f"img3.png")
bmin = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=bmin_clicked,
    relief="flat")
bmin.place(
    x=128, y=208,
    width=40,
    height=40)

# +
img7 = PhotoImage(file=f"img7.png")
bplus = Button(
    image=img7,
    borderwidth=0,
    highlightthickness=0,
    command=bplus_clicked,
    relief="flat")
bplus.place(
    x=128, y=250,
    width=40,
    height=40)

# /
img16 = PhotoImage(file=f"img16.png")
bdiv = Button(
    image=img16,
    borderwidth=0,
    highlightthickness=0,
    command=bdiv_clicked,
    relief="flat")
bdiv.place(
    x=128, y=124,
    width=40,
    height=40)

# x
img13 = PhotoImage(file=f"img13.png")
bmul = Button(
    image=img13,
    borderwidth=0,
    highlightthickness=0,
    command=bmul_clicked,
    relief="flat")
bmul.place(
    x=128, y=166,
    width=40,
    height=40)

# =
img9 = PhotoImage(file=f"img9.png")
bequ = Button(
    image=img9,
    borderwidth=0,
    highlightthickness=0,
    command=bequ_clicked,
    relief="flat")
bequ.place(
    x=128, y=292,
    width=40,
    height=40)

# CE
img10 = PhotoImage(file=f"img10.png")
bCE = Button(
    image=img10,
    borderwidth=0,
    highlightthickness=0,
    command=btnCE_clicked,
    relief="flat")
bCE.place(
    x=2, y=124,
    width=40,
    height=40)

# C
img12 = PhotoImage(file=f"img12.png")
bC = Button(
    image=img12,
    borderwidth=0,
    highlightthickness=0,
    command=btnC_clicked,
    relief="flat")
bC.place(
    x=44, y=124,
    width=40,
    height=40)

# +/-
img14 = PhotoImage(file=f"img14.png")
bneg = Button(
    image=img14,
    borderwidth=0,
    highlightthickness=0,
    command=bneg_clicked,
    relief="flat")
bneg.place(
    x=86, y=124,
    width=40,
    height=40)

window.resizable(False, False)
window.mainloop()

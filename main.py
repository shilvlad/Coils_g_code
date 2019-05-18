# n - количество витков
# l - длина катушки
# d - диаметр проволоки

# m - кол-во витков в этаже
# f - кол-во этажей
# k - просто какой-то счетчик


# disc - кол-во чух-чухов на 1 виток
# speed - скорость

from tkinter import *
from tkinter import scrolledtext

def g_code_header():
    header = 'G54 G21 G90 \nG28 X0\n'
    return header

def g_code_eof():
    eof = 'M02\n'
    return eof

def move_to_x(x, speed):
    pass
    return "G01 X%g F%d\n"%(x,speed)

def rotate_a_axis(angle, speed):
    pass
    return "G01 A%d F%d\n"%(angle, speed)


def generate_gcode(nn,ll,dd):

    n = int(nn)
    l = int(ll)
    d = float(dd)
    output = ''
    disc = 2
    speed = 100

    if l % d != 0:
        m = int(l / d) - 1
    else:
        m = int(l / d)

    if n % m != 0:
        f = int(n / m) + 1
    else:
        f = int(n / m)

    #print('Витков в слое: %d. Слоев: %d' % (m, f))

    output += g_code_header()

    i = 0
    counter = 0
    for layer in range(f):
        if counter == n:
            break
        for coil in range(m * disc):
            if counter == n:
                break
            if layer % 2 == 0:
                i = i + 1
            else:
                i = i - 1

            output += rotate_a_axis(360 / disc, speed)
            output += move_to_x(float(i * d / disc), speed)
            counter = counter + 1 / disc

    output += g_code_eof()
    return output


def clicked_btn():
    txt.delete(1.0, END)
    txt.insert(INSERT, generate_gcode(n.get(),l.get(),d.get()))



def clicked_btn1():

    file = open("output.gcode", "w")
    file.write(generate_gcode(n.get(),l.get(),d.get()))


if __name__ == '__main__':

    window = Tk()
    window.geometry('800x400')
    window.title("Рассчиташка")

    lbl1 = Label(window, text="Количество витков (шт, целое): ")
    lbl1.grid(column=0, row=0)
    n = Entry(window, width=10)
    n.grid(column=1, row=0)
    n.insert(INSERT, '1')


    lbl2 = Label(window, text="Длина намотки (мм, целое): ")
    lbl2.grid(column=0, row=1)
    l = Entry(window, width=10)
    l.grid(column=1, row=1)
    l.insert(INSERT, '1')

    lbl3 = Label(window, text="Диаметр проволоки (мм, ХХ.ХХ): ")
    lbl3.grid(column=0, row=2)
    d = Entry(window, width=10)
    d.grid(column=1, row=2)
    d.insert(INSERT, '0.5')


    txt = scrolledtext.ScrolledText(window, width=40, height=10)
    txt.grid(column=3, row=5)

    btn = Button(window, text="Захуячить!", command=clicked_btn)
    btn.grid(column=0, row=3)

    btn1 = Button(window, text="Заебашить в файл 'output.gcode'!", command=clicked_btn1)
    btn1.grid(column=0, row=4)

    window.mainloop()







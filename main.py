# n - количество витков
# l - длина катушки
# d - диаметр проволоки

# m - кол-во витков в этаже
# f - кол-во этажей
# k - просто какой-то счетчик


# disc - кол-во чух-чухов на 1 виток
# speed - скорость

from tkinter import *


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

if __name__ == '__main__':

    window = Tk()
    window.title("Добро пожаловать в приложение PythonRu")
    window.mainloop()
    
    #n = int(input ('Введите кол-во витков, шт: '))
    #l = int(input ('Введите длину катушки, мм: '))
    #d = int(input('Введите диаметр проволоки, мм: '))
    n = 13
    l = 5
    d = 0.67845
    output = ''
    disc = 2
    speed = 100

    if l%d != 0 :
        m = int(l/d) -1
    else:
        m = int(l/d)

    if n%m != 0 :
        f = int(n/m)+1
    else:
        f = int(n/m)

    print ('Витков в слое: %d. Слоев: %d' % ( m,f))

    output += g_code_header()


    i = 0
    counter = 0
    for layer in range(f):
        if counter == n:
            break
        for coil in range(m*disc):
            if counter == n:
                break
            if layer % 2 == 0:
                i = i+1
            else:
                i=i-1

            output += rotate_a_axis(360 / disc, speed)
            output += move_to_x(float(i * d/disc), speed)
            counter = counter + 1/disc


    output += g_code_eof()

    print(output)
    file = open("output.gcode", "w")
    file.write(output)

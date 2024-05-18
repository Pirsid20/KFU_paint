from tkinter import *
from PIL import Image, ImageDraw, ImageTk
from random import randint
from tkinter import colorchooser, messagebox, filedialog


def open_image():
    filepath = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if filepath:
        image = Image.open(filepath)
        photo = ImageTk.PhotoImage(image)
        canvas.image = photo  # keep a reference!
        canvas.create_image(0, 0, image=photo, anchor='nw')


def draw(event):
    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=color, width=0)
    draw_img.ellipse((x1, y1, x2, y2), fill=color, width=0)


def chooseColor():
    global color
    (rgb, hx) = colorchooser.askcolor()
    color = hx
    color_lab['bg'] = hx


def select(value):
    global brush_size
    brush_size = int(value)


def pour():
    canvas.delete('all')
    canvas['bg'] = color
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)


def clear_canvas():
    canvas.delete('all')
    canvas['bg'] = 'white'
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill='white')


def save_img():
    filename = f'image_{randint(0, 10000)}.png'
    image1.save(filename)
    messagebox.showinfo('Coхранение', 'Cохранено под названием %s' % filename)


def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


def circle():
    canvas.create_oval(x, y, x + brush_size, y + brush_size, fill=color, width=0)
    draw_img.ellipse((x, y, x + brush_size, y + brush_size), fill=color)


def square():
    canvas.create_rectangle(x, y, x + brush_size, y + brush_size, fill=color, width=0)
    draw_img.polygon((x, y, x + brush_size, y, x + brush_size, y + brush_size, x, y + brush_size), fill=color)


x = 0
y = 0
root = Tk()
root.title('Paint')
root.geometry('1280x720')
root.resizable(0, 0)
brush_size = 10
color = 'black'
root.columnconfigure(6, weight=1)
root.rowconfigure(2, weight=1)
canvas = Canvas(root, bg='white')
canvas.grid(row=2, column=0, columnspan=7, padx=5, pady=5, sticky=E + W + S + N)
canvas.bind('<B1-Motion>', draw)
canvas.bind("<Button-3>", popup)

menu = Menu(tearoff=0)
menu.add_command(label="Квадрат", command=square)
menu.add_command(label="Круг", command=circle)
image1 = Image.new('RGB', (1280, 640), 'white')
draw_img = ImageDraw.Draw(image1)

Label(root, text='Параметры:').grid(row=0, column=0, padx=6)

Button(root, text='Выбрать цвет', width=11, command=chooseColor).grid(row=0, column=1, padx=6)

color_lab = Label(root, bg=color, width=10)
color_lab.grid(row=0, column=2, padx=6)

v = IntVar(value=10)
Scale(root, variable=v, from_=1, to=100, orient=HORIZONTAL, command=select).grid(row=0, column=3, padx=6)

Label(root, text='Действия: ').grid(row=1, column=0, padx=6)

Button(root, text='Заливка', width=10, command=pour).grid(row=1, column=1)

Button(root, text='Очистить', width=10, command=clear_canvas).grid(row=1, column=2)

Button(root, text='Coxpанить', width=10, command=save_img).grid(row=1, column=6)

# Добавьте эту строку в ваш код, чтобы создать кнопку "Открыть изображение"
Button(root, text='Открыть изображение', command=open_image).grid(row=1, column=3)


root.mainloop()
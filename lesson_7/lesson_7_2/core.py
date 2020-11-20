import tkinter as tk
from tkinter import messagebox
from clothes import Clothes

# константы для графического интерфейса
WIN_SIZE = '530x420'
WIN_TITLE = 'Расход ткани'
MAIN_FONT = 'arial 14'
ENTER_FONT = 'arial 16'


def add_position(name, value):
    """
    Добавляет позицию в список одежды
    """
    clothes.add_clothes(name, value)
    list_clothes.delete(0, 'end')

    for elem in clothes.clothes_list:
        list_clothes.insert('end', elem)


def delete_position():
    """
    Удаляет выделенную позицию из списка одежды
    """
    if list_clothes.curselection():
        idx = list_clothes.curselection()[0]
        clothes.clothes_list.remove(clothes.clothes_list[idx])
        list_clothes.delete(list_clothes.curselection())


def calculate():
    """
    Производит расчёт суммарного расхода ткани на все позиции из списка одежды и выводит сумму в метку
    """
    result = round(clothes.clothes_tissue_consumption(), 2)
    label_answer.configure(text=str(result))


def if_error(name, parameter):
    """
    Проверяет корректность введённых данных
    """
    try:
        size = float(parameter)
        add_position(name, size)
    except ValueError:
        messagebox.showerror('Ошибка ввода данных', 'Необходимо ввести размер или рост в виде числа!')
        parameter_text.delete(0, 'end')


# создание объекта класса, с которым и будет работать программа
clothes = Clothes()

# создание графического интерфейса
root = tk.Tk()
root.title(WIN_TITLE)
root.geometry(WIN_SIZE)
root.grid()

main_frame = tk.Frame(root, borderwidth=2)
main_frame.grid(padx=20, pady=20)

list_clothes = tk.Listbox(main_frame, width=20, font=MAIN_FONT)
list_clothes.grid(rowspan=4, column=0)

scrollbar = tk.Scrollbar(main_frame)
scrollbar.grid(row=0, rowspan=4, column=0, sticky='nse')
list_clothes.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_clothes.yview)

button_calc = tk.Button(main_frame, text='Рассчитать', width=20, font=MAIN_FONT, command=calculate)
button_calc.grid(row=4, column=0, pady=20)

label_answer = tk.Label(main_frame, text='0', font=MAIN_FONT, width=20, height=2, bd=2, relief='ridge')
label_answer.grid(row=5, column=0, pady=10)

label_text = tk.Label(main_frame, text='Добавить в список:', font=MAIN_FONT)
label_text.grid(row=0, column=1, columnspan=2, padx=20)

label_entry = tk.Label(main_frame, text='Размер/рост:', font=MAIN_FONT)
label_entry.grid(row=1, column=1, padx=10)

parameter_text = tk.Entry(main_frame, width=5, font=ENTER_FONT)
parameter_text.grid(row=1, column=2,  padx=10)

button_add_coat = tk.Button(main_frame, text='Пальто', width=20, font=MAIN_FONT,
                            command=lambda: if_error('coat', parameter_text.get()))
button_add_coat.grid(row=2, column=1, columnspan=2, padx=20)

button_add_suit = tk.Button(main_frame, text='Костюм', width=20, font=MAIN_FONT,
                            command=lambda: if_error('suit', parameter_text.get()))
button_add_suit.grid(row=3, column=1, columnspan=2, padx=20)

button_delete = tk.Button(main_frame, text='Удалить позицию', width=20, font=MAIN_FONT, command=delete_position)
button_delete.grid(row=5, column=1, columnspan=2, padx=20)

root.mainloop()

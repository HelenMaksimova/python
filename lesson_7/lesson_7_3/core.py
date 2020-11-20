import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import cells


# вспомогательные функции:
def renew_list_boxes():
    """
    Обновляет списки клеток в интерфейсе:
    очищает их и заново записывает в них значения из списка объектов
    """
    list_left.delete(0, 'end')
    list_right.delete(0, 'end')
    for elem in cell_list:
        list_left.insert('end', elem)
        list_right.insert('end', elem)


def get_idx(mode):
    """
    Возвращает индекс или индексы текущих выделенных элементов списков в интерфейсе:
    mode == 1: один индекс (первый выделенный элемент, слева направо)
    mode == 2: кортеж из двух индексов (выделенные элементы в обоих списках)
    """
    if mode == 1:
        idx = None
        if list_left.curselection():
            idx = list_left.curselection()[0]
        elif list_right.curselection():
            idx = list_right.curselection()[0]
        return idx
    elif mode == 2:
        if list_right.curselection() and list_left.curselection():
            idx_l = list_left.curselection()[0]
            idx_r = list_right.curselection()[0]
            return idx_l, idx_r


def delete_cell():
    """
    Удаляет эелемент из списка объектов и из списков интерфейса
    """
    idx = get_idx(1)
    if idx is not None:
        cell_list.remove(cell_list[idx])
        renew_list_boxes()


# основные функции:
def create_cell():
    """
    Создаёт новый эелемент "Клетка" и добавляет его в список объектов и списки интерфейса
    Параметр нового объекта запрашивается у пользователя
    """
    size = simpledialog.askinteger('Размер клетки', 'Введите размер клетки:')
    try:
        new_cell = cells.Cell(size)
        cell_list.append(new_cell)
        renew_list_boxes()
        messagebox.showinfo('Создание клетки', f'Создана новая клетка:\n{str(new_cell)}')
    except ValueError as e:
        messagebox.showerror('Ошибка', e)
    except TypeError:
        messagebox.showinfo('Отмена', 'Операция отменена')


def add_cells():
    """
    Создаёт новый эелемент "Клетка" путём сложения двух других эелементов
    и добавляет его в список объектов и списки интерфейса
    """
    if get_idx(2):
        idx_l, idx_r = get_idx(2)
        new_cell = cell_list[idx_l] + cell_list[idx_r]
        cell_list.append(new_cell)
        renew_list_boxes()
        messagebox.showinfo('Создание клетки', f'Создана новая клетка:\n{str(new_cell)}')


def mul_cells():
    """
    Создаёт новый эелемент "Клетка" путём перемножения двух других эелементов
    и добавляет его в список объектов и списки интерфейса
    """
    if get_idx(2):
        idx_l, idx_r = get_idx(2)
        new_cell = cell_list[idx_l] * cell_list[idx_r]
        cell_list.append(new_cell)
        renew_list_boxes()
        messagebox.showinfo('Создание клетки', f'Создана новая клетка:\n{str(new_cell)}')


def sub_cells():
    """
    Создаёт новый эелемент "Клетка" путём вычитания одного элемента из другого
    и добавляет его в список объектов и списки интерфейса
    """
    if get_idx(2):
        idx_l, idx_r = get_idx(2)
        try:
            new_cell = cell_list[idx_l] - cell_list[idx_r]
            cell_list.append(new_cell)
            renew_list_boxes()
            messagebox.showinfo('Создание клетки', f'Создана новая клетка:\n{str(new_cell)}')
        except cells.CellOperationError as e:
            messagebox.showerror('Ошибка', e)


def div_cells():
    """
    Создаёт новый эелемент "Клетка" путём деления одного элемента на другой
    и добавляет его в список объектов и списки интерфейса
    """
    if get_idx(2):
        idx_l, idx_r = get_idx(2)
        try:
            new_cell = cell_list[idx_l] / cell_list[idx_r]
            cell_list.append(new_cell)
            renew_list_boxes()
            messagebox.showinfo('Создание клетки', f'Создана новая клетка:\n{str(new_cell)}')
        except cells.CellOperationError as e:
            messagebox.showerror('Ошибка', e)
        except TypeError:
            messagebox.showinfo('Отмена', 'Операция отменена')


def make_cell_order():
    """
    Задаёт порядок ячеек в выбранном эелементе "Клетка"
    Количество ячеек в ряду запрашивается у пользователя
    """
    idx = get_idx(1)
    if idx is not None:
        nucleus = simpledialog.askinteger('Размер клетки', 'Введите число ячеек в ряду:')
        cell_list[idx].make_order(nucleus)
        result = f'{str(cell_list[idx])} имеет порядок:\n\n{cell_list[idx].order}'
        messagebox.showinfo('Порядок клетки', result)


def show_cell_order():
    """
    Показывает порядок ячеек в выбранном эелементе "Клетка"
    Выводит сообщение с отображением порядка ячеек или сообщает о том, что порядок в элементе не установлен
    """
    idx = get_idx(1)
    if idx is not None:
        if cell_list[idx].order:
            result = f'{str(cell_list[idx])} имеет порядок:\n\n{cell_list[idx].order}'
            messagebox.showinfo('Порядок клетки', result)
        else:
            messagebox.showinfo('Порядок клетки', 'Порядок клетки не задан')


cell_list = []  # создание списка объектов, с которым будет работать программа

# создание графического интерфейса
root = tk.Tk()
root.title('Клеточный калькулятор')
root.geometry('800x600')

main_frame = tk.Frame(root)
main_frame.grid()

list_left = tk.Listbox(main_frame, width=30, height=16, font='arial 14', exportselection=0)
list_left.grid(row=0, rowspan=4, column=0, padx=20, pady=20)

scrollbar_left = tk.Scrollbar(main_frame)
scrollbar_left.grid(row=0, rowspan=4, column=0, padx=20, pady=20, sticky='nse')
list_left.configure(yscrollcommand=scrollbar_left.set)
scrollbar_left.config(command=list_left.yview)

list_right = tk.Listbox(main_frame, width=30, height=16, font='arial 14', exportselection=0)
list_right.grid(row=0, rowspan=4, column=2, padx=20, pady=20)

scrollbar_right = tk.Scrollbar(main_frame)
scrollbar_right.grid(row=0, rowspan=4, column=2, padx=20, pady=20, sticky='nse')
list_right.configure(yscrollcommand=scrollbar_right.set)
scrollbar_right.config(command=list_right.yview)

button_add = tk.Button(main_frame, text='+', width=4, height=2, font='arial 14', command=add_cells)
button_add.grid(row=0, column=1, pady=10)

button_sub = tk.Button(main_frame, text='-', width=4, height=2, font='arial 14', command=sub_cells)
button_sub.grid(row=1, column=1, pady=10)

button_mul = tk.Button(main_frame, text='*', width=4, height=2, font='arial 14', command=mul_cells)
button_mul.grid(row=2, column=1, pady=10)

button_div = tk.Button(main_frame, text='/', width=4, height=2, font='arial 14', command=div_cells)
button_div.grid(row=3, column=1, pady=10)

button_make_order = tk.Button(main_frame, text='Задать порядок', width=20, height=2, font='arial 14',
                              command=make_cell_order)
button_make_order.grid(row=4, column=0, pady=10)

button_get_order = tk.Button(main_frame, text='Показать порядок', width=20, height=2, font='arial 14',
                             command=show_cell_order)
button_get_order.grid(row=4, column=2, pady=10)

button_add_cell = tk.Button(main_frame, text='Создать клетку', width=20, height=2, font='arial 14',
                            command=create_cell)
button_add_cell.grid(row=5, column=0, pady=10)

button_delete_cell = tk.Button(main_frame, text='Удалить клетку', width=20, height=2, font='arial 14',
                               command=delete_cell)
button_delete_cell.grid(row=5, column=2, pady=10)

root.mainloop()

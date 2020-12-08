import tkinter as tk
from tkinter import ttk
import warehouse


# Для удобства вывода сообщений (в стандартном messagebox в tkinter нельзя задать параметр шрифта)
class Message(tk.Toplevel):
    """
    Класс, объектом которого являеется окно с текстом и единственной кнопкой, закрывающей это окно
    """
    def __init__(self, title, text):
        super().__init__()
        self.title(title)
        tk.Label(self, text=text, font='arial 14').grid(padx=20, pady=20)
        tk.Button(self, text='Ok', font='arial 14', width=6, command=lambda: self.destroy()).grid(padx=20, pady=20)
        self.focus()


# Создаём структуры, с которыми будет работать программа
wh = warehouse.Warehouse()  # объект склада

wh_current_list = []  # список отображаемых в данный момент объектов в listbox-е склада
dep_current_list = []  # список отображаемых в данный момент объектов в listbox-е отделов

department_list = []  # список созданных отделов


# Функции, обновляющие содержимое listbox-ов и обеспечивающие связь между ними и списками объектов
def renew_wh_current_list(view_mod):
    """
    Обновляет список отображаемых объектов в listbox-е склада в зависимости от режима просмотра
    """
    wh_current_list.clear()
    if view_mod == 'Всё оборудование':
        wh_current_list.extend([elem for key in wh.equipment for elem in wh.equipment[key]])
    else:
        wh_current_list.extend([elem for elem in wh.equipment[view_mod]])


def renew_list_wh(view_mod):
    """
    Обновляет список элементов в listbox-е склада в зависимости от режима просмотра
    и выводит соответствующее количество и стоимость оборудования
    """
    renew_wh_current_list(view_mod)
    combo_warehouse.set(view_mod)
    list_warehouse.delete(0, 'end')
    for elem in wh_current_list:
        list_warehouse.insert('end', elem)
    if view_mod == 'Всё оборудование':
        label_wh_count.configure(text=f'{wh.equipment_count()}')
        label_wh_cost.configure(text=f'{wh.equipment_cost():.2f}')
    else:
        label_wh_count.configure(text=f'{wh.equipment_type_count(view_mod)}')
        label_wh_cost.configure(text=f'{wh.equipment_type_cost(view_mod):.2f}')


def renew_dep_current_list(view_mod, idx):
    """
    Обновляет список отображаемых объектов в listbox-е отделов в зависимости от режима просмотра
    """
    dep_current_list.clear()
    if view_mod == 'Все отделы':
        dep_current_list.extend([elem for el in department_list for key in el.equipment for elem in el.equipment[key]])
    else:
        dep_current_list.extend([elem for key in department_list[idx].equipment
                                 for elem in department_list[idx].equipment[key]])


def renew_list_dep(view_mod):
    """
    Обновляет список элементов в listbox-е отделов в зависимости от режима просмотра
    и выводит соответствующее количество и стоимость оборудования
    """
    combo_department.set(view_mod)
    idx = combo_department.current() - 1
    renew_dep_current_list(view_mod, idx)
    list_department.delete(0, 'end')
    for elem in dep_current_list:
        list_department.insert('end', elem)
    if view_mod == 'Все отделы':
        label_dep_count.configure(text=f'{sum(elem.equipment_count() for elem in department_list)}')
        label_dep_cost.configure(text=f'{sum(elem.equipment_cost() for elem in department_list):.2f}')
    else:
        label_dep_count.configure(text=f'{department_list[idx].equipment_count()}')
        label_dep_cost.configure(text=f'{department_list[idx].equipment_cost():.2f}')


# Функции, отвечающие за события при выборе элементов в combobox-ах основного окна:
# (По какой-то причине PyCharm не видит event и считает его неиспользуемой переменной,
# но без него не работает, я проверяла)
def event_renew_hw_list(event):
    """
    Запускает обновление списка в listbox-е склада при
    выборе пользователем режима просмотра в соответствующем combobox-е
    """
    cur_value = combo_warehouse.get()
    renew_list_wh(cur_value)


def event_renew_dep_list(event):
    """
    Запускает обновление списка в listbox-е отделов при
    выборе пользователем режима просмотра в соответствующем combobox-е
    """
    cur_value = combo_department.get()
    renew_list_dep(cur_value)


# Основные функции, обрабатывающие события при нажатии кнопок, а также создающие дочерние окна для ввода данных
def add_equipment(brand, oe_type, price, condition, *args):
    """
    Добавляет оборудование с заданными параметрами в объект склада и запускает обновление интерфейса
    """
    cond = True if condition == 'Исправен' else False
    wh.add_equipment(brand, oe_type, price, cond, *args)
    renew_list_wh(oe_type)


def delete_equipment():
    """
    Удаляет выбранное оборудование из соответствующих объектов склада или отдела и запускает обновление интерфейса
    """
    if list_warehouse.curselection() or list_department.curselection():
        idx = list_warehouse.curselection()[0] if list_warehouse.curselection() else list_department.curselection()[0]

        if list_warehouse.curselection():
            delete_elem = wh_current_list[idx]
            view_mod = combo_warehouse.get()
            for key in wh.equipment:
                for elem in wh.equipment[key]:
                    if elem == delete_elem:
                        wh.equipment[key].remove(elem)
                        renew_list_wh(view_mod)
                        break

        if list_department.curselection():
            delete_elem = dep_current_list[idx]
            view_mod = combo_department.get()
            for element in department_list:
                for key in element.equipment:
                    for elem in element.equipment[key]:
                        if elem == delete_elem:
                            element.equipment[key].remove(elem)
                            renew_list_dep(view_mod)
                            break


def transfer_equipment(from_place, to_place, oe_type, count):
    """
    Производит перемещение оборудования между объектами склада и отделов, запускает обновление интерфейса
    """
    from_place.transfer_equipment(to_place, oe_type, int(count))
    renew_list_wh('Всё оборудование')
    renew_list_dep('Все отделы')


def get_info():
    """
    Выводит на экран информацию о выбранном оборудовании в отдельном окне
    """
    if list_warehouse.curselection() or list_department.curselection():
        idx = list_warehouse.curselection()[0] if list_warehouse.curselection() else list_department.curselection()[0]
        mess = wh_current_list[idx].get_info() if list_warehouse.curselection() else dep_current_list[idx].get_info()
        Message('Информация об оборудовании', mess)


def dialog():
    """
    Создаёт диалоговое окно для ввода информации о новом отделе
    """

    def give_value():
        """
        Вызывает функцию создания нового отдела и функцию уничтожения окна
        """
        add_department(entry.get())
        destroy_dialog()

    def destroy_dialog():
        """
        Уничтожает окно
        """
        win_data.destroy()

    # графический интерфейс дочернего окна
    win_data = tk.Toplevel(root)
    win_data.title('Создание отдела')
    tk.Label(win_data, text='Введите название отдела:', font='arial 14').grid(padx=20, pady=10)
    entry = tk.Entry(win_data, font='arial 14', width=20)
    entry.grid(padx=10, pady=10)
    tk.Button(win_data, text='Ok', font='arial 14', width=6, command=give_value).grid(padx=10, pady=10)
    win_data.focus()


def add_department(name):
    """
    Создаёт новый объект отдела, добавляет его в список отделов и запускает обновление интерфейса
    """
    name = name.strip()
    if name in [elem.name for elem in department_list]:
        Message('Ошибка ввода данных', 'Такой отдел уже есть!')
    if name and name not in [elem.name for elem in department_list]:
        new_dep = warehouse.Department(name)
        department_list.append(new_dep)
        combo_department.configure(values=['Все отделы'] + [elem.name for elem in department_list])
        combo_department.set(name)
        renew_list_dep(name)


def data_enter():
    """
    Создаёт окно для ввода данных при добавлении нового оборудования, обрабатывает данные
    и передаёт их в функцию, добавляющую оборудование в объект склада
    """

    def event_equipment_type(event):
        """
        Обрабатывает событие выбора типа оборудования
        """
        eq_type = combo_eo_type.get()
        if eq_type == 'Принтер':
            label_print_type.configure(state='normal')
            combo_print_type.configure(state='normal')
        else:
            label_print_type.configure(state='disabled')
            combo_print_type.configure(state='disabled')

    def destroy_win():
        """
        Уничтожает окно
        """
        win_data.destroy()

    def data_add():
        """
        Добавляет новое оборудование на склад
        """
        try:
            if not entry_brand.get():
                raise ValueError
            if combo_eo_type.get() == 'Принтер':
                add_equipment(entry_brand.get(), combo_eo_type.get(), float(entry_price.get()), combo_condition.get(),
                              combo_format.get(), combo_print_type.get())
            else:
                add_equipment(entry_brand.get(), combo_eo_type.get(), float(entry_price.get()), combo_condition.get(),
                              combo_format.get())
            destroy_win()
        except ValueError:
            Message('Ошибка ввода', 'Необходимо указать производителя и стоимость!')
            win_data.focus()

    # графический интерфейс дочернего окна
    win_data = tk.Toplevel(root)
    win_data.title('Добавление оборудования')
    win_data.geometry('530x420')
    win_data.focus()

    tk.Label(win_data, text='Введите данные оборудования:', font='arial 14').grid(row=0, column=0, columnspan=2,
                                                                                  sticky='we', pady=10, padx=20)

    tk.Label(win_data, text='Производитель (бренд):', font='arial 14').grid(row=1, column=0,
                                                                            sticky='e', pady=10, padx=10)
    entry_brand = tk.Entry(win_data, font='arial 14')
    entry_brand.grid(row=1, column=1, sticky='we', pady=10, padx=10)

    tk.Label(win_data, text='Тип оборудования:', font='arial 14').grid(row=2, column=0,
                                                                       sticky='e', pady=10, padx=10)
    combo_eo_type = ttk.Combobox(win_data, state='readonly', values=[elem for elem in wh.EQUIPMENT_TYPES],
                                 font='arial 14')
    combo_eo_type.grid(row=2, column=1, sticky='we', pady=10, padx=10)
    combo_eo_type.bind('<<ComboboxSelected>>', event_equipment_type)
    combo_eo_type.current(0)

    tk.Label(win_data, text='Цена оборудования:', font='arial 14').grid(row=3, column=0,
                                                                        sticky='e', pady=10, padx=10)
    entry_price = tk.Entry(win_data, font='arial 14')
    entry_price.grid(row=3, column=1, sticky='we', pady=10, padx=10)

    tk.Label(win_data, text='Состояние оборудования:', font='arial 14').grid(row=4, column=0,
                                                                             sticky='e', pady=10, padx=10)
    combo_condition = ttk.Combobox(win_data, state='readonly', values=['Исправен', 'Неисправен'], font='arial 14')
    combo_condition.grid(row=4, column=1, sticky='we', pady=10, padx=10)
    combo_condition.current(0)

    tk.Label(win_data, text='Формат бумаги:', font='arial 14').grid(row=5, column=0,
                                                                    sticky='e', pady=10, padx=10)
    combo_format = ttk.Combobox(win_data, state='readonly', values=['A1', 'A2', 'A3', 'A4', 'A5'], font='arial 14')
    combo_format.grid(row=5, column=1, sticky='we', pady=10, padx=10)
    combo_format.current(3)

    label_print_type = tk.Label(win_data, text='Тип печати:', font='arial 14')
    label_print_type.grid(row=6, column=0, sticky='e', pady=10, padx=10)
    combo_print_type = ttk.Combobox(win_data, state='readonly', values=['Лазерный', 'Струйный'], font='arial 14')
    combo_print_type.grid(row=6, column=1, sticky='we', pady=10, padx=10)
    combo_print_type.current(0)

    button_add_data = tk.Button(win_data, text='Добавить', font='arial 14', command=data_add, width=20)
    button_add_data.grid(row=7, column=0, columnspan=2, pady=20, padx=10)


def transfer_data(mod):
    """
    Создаёт окно для ввода данных при перемещении оборудования, обрабатывает данные
    и передаёт их в функцию, перемещающую оборудование
    """

    def destroy_win():
        """
        Уничтожает окно
        """
        win_data.destroy()

    def validation_data():
        """
        Проверяет введённые данные, бросает соответствующие ошибки
        """
        if not len(department_list):
            raise IndexError
        if not combo_eo_type.get() in wh.EQUIPMENT_TYPES:
            raise warehouse.WarehouseEquipmentError
        if not entry_count.get().isdigit:
            raise ValueError

    def data_transfer_dep():
        """
        Проверяет данные (ловит ошибки) и передаёт в функцию перемещения при передаче оборудования в отдел
        """
        try:
            validation_data()
            transfer_equipment(wh, department_list[combo_dep_name.current()], combo_eo_type.get(), entry_count.get())
            destroy_win()
        except IndexError:
            Message('Ошибка ввода данных', 'Пока не создано ни одного отдела!')
        except warehouse.WarehouseEquipmentError as e:
            Message('Ошибка ввода данных', e)
        except warehouse.EquipmentCountError as e:
            Message('Ошибка ввода данных', e)
        except ValueError:
            Message('Ошибка ввода данных', 'Необходимо ввести количество в формате числа!')
        finally:
            if win_data.winfo_exists():
                win_data.focus()

    def data_transfer_wh():
        """
        Проверяет данные (ловит ошибки) и передаёт в функцию перемещения при передаче оборудования на склад
        """
        try:
            validation_data()
            transfer_equipment(department_list[combo_dep_name.current()], wh, combo_eo_type.get(), entry_count.get())
            destroy_win()
        except IndexError:
            Message('Ошибка ввода данных', 'Пока не создано ни одного отдела!')
        except warehouse.WarehouseEquipmentError as e:
            Message('Ошибка ввода данных', e)
        except warehouse.EquipmentCountError as e:
            Message('Ошибка ввода данных', e)
        except ValueError:
            Message('Ошибка ввода данных', 'Необходимо ввести количество в формате числа!')
        finally:
            if win_data.winfo_exists():
                win_data.focus()

    func = data_transfer_dep if mod == 'dep'else data_transfer_wh  # функция для кнопки "Передать"
    text_lbl = 'Передать в отдел:' if mod == 'dep' else 'Передать из отдела:'  # текст для метки

    # графический интерфейс дочернего окна
    win_data = tk.Toplevel(root)
    win_data.title('Передача оборудования')
    win_data.geometry('530x300')
    win_data.focus()

    tk.Label(win_data, text='Введите данные для передачи оборудования:',
             font='arial 14').grid(row=0, column=0, columnspan=2, sticky='we', pady=10, padx=20)

    tk.Label(win_data, text='Тип оборудования:', font='arial 14').grid(row=1, column=0,
                                                                       sticky='e', pady=10, padx=10)
    combo_eo_type = ttk.Combobox(win_data, state='readonly', values=[elem for elem in wh.EQUIPMENT_TYPES],
                                 font='arial 14')
    combo_eo_type.grid(row=1, column=1, sticky='we', pady=10, padx=10)
    combo_eo_type.current(0)

    tk.Label(win_data, text='Количество оборудования:', font='arial 14').grid(row=2, column=0,
                                                                              sticky='e', pady=10, padx=10)
    entry_count = tk.Entry(win_data, font='arial 14')
    entry_count.grid(row=2, column=1, sticky='we', pady=10, padx=10)

    tk.Label(win_data, text=text_lbl, font='arial 14').grid(row=3, column=0,
                                                            sticky='e', pady=10, padx=10)
    combo_dep_name = ttk.Combobox(win_data, state='readonly', values=[elem.name for elem in department_list],
                                  font='arial 14')
    combo_dep_name.grid(row=3, column=1, sticky='we', pady=10, padx=10)
    if len(department_list) > 0:
        combo_dep_name.current(0)

    button_transfer = tk.Button(win_data, text='Передать', font='arial 14', command=func, width=20)
    button_transfer.grid(row=4, column=0, columnspan=2, pady=20, padx=10)


# графический интерфейс корневого окна:
root = tk.Tk()
root.title('Склад оргтехники')
root.geometry('900x700')
root.option_add('*TCombobox*Listbox.font', 'arial 14')
root.option_add('*Dialog.msg.font', 'arial 14')

main_frame = tk.Frame(root)
main_frame.grid(padx=25, pady=25)

label_wh_equip = tk.Label(main_frame, text='Оборудование на складе', font='arial 14')
label_wh_equip.grid(row=0, column=0, columnspan=2, sticky='we')

list_warehouse = tk.Listbox(main_frame, height=13, width=30, font='arial 14')
list_warehouse.grid(row=1, column=0, rowspan=2, columnspan=2, sticky='we')

combo_warehouse = ttk.Combobox(main_frame, state='readonly', font='arial 14',
                               values=['Всё оборудование'] + [elem for elem in wh.EQUIPMENT_TYPES])
combo_warehouse.grid(row=3, column=0, columnspan=2, pady=10, sticky='we')
combo_warehouse.current(0)
combo_warehouse.bind('<<ComboboxSelected>>', event_renew_hw_list)

label_wh_count_txt = tk.Label(main_frame, text='Количество:', font='arial 14')
label_wh_count_txt.grid(row=4, column=0, padx=10)

label_wh_cost_txt = tk.Label(main_frame, text='Стоимость:', font='arial 14')
label_wh_cost_txt.grid(row=4, column=1, padx=10)

label_wh_count = tk.Label(main_frame, text='0', font='arial 14', bd=2, relief='ridge', height=2)
label_wh_count.grid(row=5, column=0, padx=10, pady=10, sticky='we')

label_wh_cost = tk.Label(main_frame, text='0.00', font='arial 14', bd=2, relief='ridge', height=2, width=20)
label_wh_cost.grid(row=5, column=1, padx=10, pady=10, sticky='we')

button_add_equip = tk.Button(main_frame, text='Добавить оборудование', font='arial 14', command=data_enter)
button_add_equip.grid(row=6, column=0, columnspan=2, pady=20, sticky='we')

button_transfer_dep = tk.Button(main_frame, text='>>>', font='arial 14', command=lambda: transfer_data('dep'))
button_transfer_dep.grid(row=1, column=2, padx=20)

button_transfer_wh = tk.Button(main_frame, text='<<<', font='arial 14', command=lambda: transfer_data('wh'))
button_transfer_wh.grid(row=2, column=2, padx=20)

label_dep_equip = tk.Label(main_frame, text='Оборудование в отделе', font='arial 14')
label_dep_equip.grid(row=0, column=3, columnspan=2, sticky='we')

list_department = tk.Listbox(main_frame, height=13, width=30, font='arial 14')
list_department.grid(row=1, column=3, rowspan=2, columnspan=2, sticky='we')

combo_department = ttk.Combobox(main_frame, state='readonly', font='arial 14',
                                values=['Все отделы'] + [elem.name for elem in department_list])
combo_department.grid(row=3, column=3, columnspan=2, pady=10, sticky='we')
combo_department.current(0)
combo_department.bind('<<ComboboxSelected>>', event_renew_dep_list)

label_dep_count_txt = tk.Label(main_frame, text='Количество:', font='arial 14')
label_dep_count_txt.grid(row=4, column=3, padx=10)

label_dep_cost_txt = tk.Label(main_frame, text='Стоимость:', font='arial 14')
label_dep_cost_txt.grid(row=4, column=4, padx=10)

label_dep_count = tk.Label(main_frame, text='0', font='arial 14', bd=2, relief='ridge', height=2)
label_dep_count.grid(row=5, column=3, padx=10, pady=10, sticky='we')

label_dep_cost = tk.Label(main_frame, text='0.00', font='arial 14', bd=2, relief='ridge', height=2, width=20)
label_dep_cost.grid(row=5, column=4, padx=10, pady=10, sticky='we')

button_add_dep = tk.Button(main_frame, text='Добавить отдел', font='arial 14', command=dialog)
button_add_dep.grid(row=6, column=3, columnspan=2, pady=20, sticky='we')

button_show_info = tk.Button(main_frame, text='Показать информацию', font='arial 14', command=get_info)
button_show_info.grid(row=7, column=0, columnspan=2, pady=20, sticky='we')

button_delete_equip = tk.Button(main_frame, text='Удалить оборудование', font='arial 14', command=delete_equipment)
button_delete_equip.grid(row=7, column=3, columnspan=2, pady=20, sticky='we')

root.mainloop()

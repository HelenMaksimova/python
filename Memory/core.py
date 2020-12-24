import tkinter as tk
from random import randint
from tkinter import ttk


class Timer(tk.Frame):
    """
    Класс таймера игры
    """

    def __init__(self, master, obj, seconds, font=('arial', 12)):
        super().__init__()
        self.start_flag = False
        self.obj = obj
        self.value = seconds
        self.label = tk.Label(master, text=f'{self.value // 60:02}:{self.value % 60:02}',
                              font=font, fg=FG, bd=2, relief='groove', width=9)
        self.label.grid(pady=10)

    def start(self):
        """
        Запускает таймер
        """
        self.start_flag = True
        self.update_clock()

    def stop(self):
        """
        Останавливает таймер
        """
        self.value = 1
        self.start_flag = False

    def update_clock(self):
        """
        Обновляет значение таймера, если таймер доходит до нуля, запускает функцию проигрыша игры
        """
        try:
            self.value -= 1
            text = f'{self.value // 60:02}:{self.value % 60:02}'
            self.label.configure(text=text)
            if self.start_flag:
                if self.value <= 0:
                    self.obj.looser_game()
                    return
                self.after(1000, self.update_clock)
        except Exception:
            pass


class ImageLabel(tk.Label):
    """
    Класс метки с картинкой для заполнения поля игры
    """

    def __init__(self, master, row, column, number, img_passive, img_active, game_field):
        super().__init__(master)
        self.field = game_field
        self.row = row
        self.column = column
        self.number = number
        self.img_passive = img_passive
        self.img_active = img_active
        self.configure(image=self.img_passive)
        self.available = True
        self.status_active = False
        self.bind('<Button-1>', self.click_label)
        self.grid(row=row, column=column)

    def show_active(self):
        """
        Показывает лицевую сторону метки
        """
        if self.available:
            self.configure(image=self.img_active)
            self.status_active = True

    def show_passive(self):
        """
        Показывает рубашку метки
        """
        if self.available:
            self.configure(image=self.img_passive)
            self.status_active = False

    def click_label(self, event):
        """
        Обработчик щелчка по метке
        """
        if not self.status_active and self.available:

            if self.field.first_click:
                self.field.previous_click = self.number
                self.field.previous_row = self.row
                self.field.previous_column = self.column
                self.show_active()
                self.field.first_click = False

            else:
                self.show_active()

                if self.field.previous_click == self.number:
                    self.available = False
                    self.field.labels[self.field.previous_row][self.field.previous_column].available = False
                    self.field.first_click = True
                    self.field.validation_list.remove(self.number)
                    self.field.validation_list.remove(self.field.labels[self.field.previous_row]
                                                      [self.field.previous_column].number)
                    self.field.validation_win()

                else:
                    self.field.labels[self.field.previous_row][self.field.previous_column].show_passive()
                    self.field.previous_click = self.number
                    self.field.previous_row = self.row
                    self.field.previous_column = self.column


class GameField:
    """
    Класс поля игры
    """
    def __init__(self, master, img_passive, images_active, size=10):
        self.first_click = True
        self.previous_click = 0
        self.previous_row = 0
        self.previous_column = 0
        self.labels = []
        for _ in range(size):
            self.labels.append([])
        self.images_dict = {elem+1: images_active[elem] for elem in range(len(images_active))}

        self.random_list = []
        for _ in range(size):
            self.random_list.append([randint(1, len(images_active)) for _ in range(size)])

        self.validation_list = [self.random_list[row][column] for row in range(size) for column in range(size)]

        for row in range(size):
            for column in range(size):
                img_active = self.images_dict[self.random_list[row][column]]
                self.labels[row].append(ImageLabel(master, row, column, self.random_list[row][column],
                                                   img_passive, img_active, self))

    def validation_win(self):
        """
        Проверяет, остались ли парные неоткрытые элементы, если не осталось, запускает функцию победы
        """
        global timer
        result = 0
        for key in self.images_dict:
            if self.validation_list.count(key) > 1:
                result += 1
        if not bool(result):
            self.field_block()
            timer.stop()
            self.winner_game()

    def field_block(self):
        """
        Открывает все метки на поле и блокирует их
        """
        for row in self.labels:
            for elem in row:
                elem.available = True
                elem.show_active()
                elem.available = False

    def winner_game(self):
        """
        Обработчик победы в игре
        """
        self.field_block()
        win_winner = tk.Toplevel(root)
        win_winner.title('Memory')
        win_winner.geometry('300x300')
        win_winner.resizable(width=False, height=False)
        win_winner.focus()
        win_winner.protocol("WM_DELETE_WINDOW", lambda: exit_message(win_winner))
        tk.Label(win_winner, image=img_start).place(anchor='center', relx=0.5, rely=0.1)
        tk.Label(win_winner, font=FONT, fg=FG, text='Вы выиграли!').place(anchor='center', relx=0.5, rely=0.4)
        tk.Button(win_winner, font=FONT, fg=FG, text='OK', width=8,
                  command=lambda: exit_message(win_winner)).place(anchor='center', relx=0.5, rely=0.6)
        tk.Label(win_winner, image=img_start).place(anchor='center', relx=0.5, rely=0.9)

    def looser_game(self):
        """
        Обработчик проигрыша в игре
        """
        self.field_block()
        win_looser = tk.Toplevel(win_game)
        win_looser.title('Memory')
        win_looser.geometry('300x300')
        win_looser.resizable(width=False, height=False)
        win_looser.focus()
        win_looser.protocol("WM_DELETE_WINDOW", lambda: exit_message(win_looser))
        tk.Label(win_looser, image=img_start).place(anchor='center', relx=0.5, rely=0.1)
        tk.Label(win_looser, font=FONT, fg=FG, text='Вы проиграли!').place(anchor='center', relx=0.5, rely=0.4)
        tk.Button(win_looser, font=FONT, fg=FG, text='OK', width=8,
                  command=lambda: exit_message(win_looser)).place(anchor='center', relx=0.5, rely=0.6)
        tk.Label(win_looser, image=img_start).place(anchor='center', relx=0.5, rely=0.9)


def return_main_window():
    """
    Восстанавливает главное окно и даёт ему фокус
    """
    root.deiconify()
    root.focus()


def return_game_window():
    """
    Восстанавливает окно игры и даёт ему фокус
    """
    win_game.deiconify()
    win_game.focus()


def exit_win(window):
    """
    Разрушает указанное окно и возвращает главное
    """
    return_main_window()
    window.destroy()


def exit_message(window):
    """
    Разрушает указанное окно и возвращает окно игры
    """
    return_game_window()
    window.destroy()


def new_game(size, difficulty):
    """
    Создаёт окно игры
    """
    global timer, win_game
    root.withdraw()

    win_game = tk.Toplevel(root)
    win_game.title('Memory: game')
    win_game.resizable(width=False, height=False)
    win_game.focus()
    win_game.protocol("WM_DELETE_WINDOW", lambda: exit_win(win_game))

    tk.Label(win_game, image=img_start).grid(row=0)

    frame = tk.Frame(win_game, bd=2, relief='groove')

    field = GameField(frame, img0, difficulty_dict[difficulty], size)  # создание игрового поля

    timer = Timer(win_game, field, 300,  font=('Comic Sans MS', 26))
    timer.start()
    timer.grid(row=1, pady=20)

    frame.grid(row=2, pady=20)

    tk.Label(win_game, image=img_start).grid(row=18)


# константы:
FONT = ('Comic Sans MS', 18)
FG = '#191970'

# глобальные переменные
timer = None  # таймер игры
win_game = None  # окно игры

# создание основного окна
root = tk.Tk()

# загрузка изображений
img0 = tk.PhotoImage(file='00.png')
img1 = tk.PhotoImage(file='01.png')
img2 = tk.PhotoImage(file='02.png')
img3 = tk.PhotoImage(file='03.png')
img4 = tk.PhotoImage(file='04.png')
img5 = tk.PhotoImage(file='05.png')
img6 = tk.PhotoImage(file='06.png')
img7 = tk.PhotoImage(file='07.png')
img8 = tk.PhotoImage(file='08.png')
img_start = tk.PhotoImage(file='start.png')

# словарь размеров поля:
size_dict = {'5 x 5': 5, '10 x 10': 10, '15 x 15': 15}
# словарь сложностей игры:
difficulty_dict = {'Просто': [img1, img2, img3],
                   'Нормально': [img1, img2, img3, img4, img5],
                   'Сложно': [img1, img2, img3, img4, img5, img6, img7, img8]}

root.title('MEMORY')
root.configure(bg='white')
root.geometry('600x500')
root.resizable(width=False, height=False)
root.option_add('*TCombobox*Listbox.font', FONT)
root.option_add('*TCombobox*Listbox.foreground', FG)

tk.Label(root, image=img_start).place(anchor='center', relx=0.5, rely=0.05)
tk.Label(root, image=img_start).place(anchor='center', relx=0.5, rely=0.95)

main_frame = tk.Frame(root, bg='white')
main_frame.place(anchor='center', relx=0.5, rely=0.4)

tk.Label(main_frame, text='Размер поля', font=FONT, bg='white', foreground=FG).grid(row=0, column=0,
                                                                                    padx=10, pady=20, sticky='w')
combo_size = ttk.Combobox(main_frame, font=FONT, state='readonly', width=10, justify='center', foreground=FG,
                          values=[key for key in size_dict])
combo_size.grid(row=0, column=1, padx=10, pady=20, sticky='w')
combo_size.set('10 x 10')

tk.Label(main_frame, text='Сложность', font=FONT, bg='white', foreground=FG).grid(row=1, column=0,
                                                                                  padx=10, pady=20, sticky='w')
combo_mod = ttk.Combobox(main_frame, font=FONT, state='readonly', width=10, justify='center', foreground=FG,
                         values=[elem for elem in difficulty_dict])
combo_mod.grid(row=1, column=1, padx=10, pady=20, sticky='w')
combo_mod.set('Нормально')

button_start = tk.Button(root, text='Начать игру', font=FONT, bg='white', foreground=FG, width=15,
                         command=lambda: new_game(size_dict[combo_size.get()], combo_mod.get()))
button_start.place(anchor='center', relx=0.5, rely=0.65)

root.mainloop()

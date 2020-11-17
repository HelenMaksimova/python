import tkinter as tk
from threading import Timer  # для таймеров перключения цветов


class TrafficLight(tk.Frame):

    def __init__(self, master):
        super(TrafficLight, self).__init__(master)

        # флаги для регулировки режимов объекта
        self.color_run = False  # запущен ли режим какого-либо света
        self.auto_run = False  # запущен ли режим автоматической смены цветов светофора

        # создание полотна
        self.canvas = tk.Canvas(self, width=200, height=600, background='black')
        self.canvas.grid(column=0, rowspan=4)

        # загрузка картинок из файлов в переменные
        self.img = tk.PhotoImage(file='gray.png')  # серый кружок
        self.img_red = tk.PhotoImage(file='red.png')   # красный кружок
        self.img_yellow = tk.PhotoImage(file='yellow.png')   # жёлтый кружок
        self.img_green = tk.PhotoImage(file='green.png')  # зелёный кружок

        # создание объектов-картинок на полотне
        self.img_up = self.canvas.create_image((100, 100), image=self.img)  # верхний кружок
        self.img_mid = self.canvas.create_image((100, 300), image=self.img)  # средний кружок
        self.img_dwn = self.canvas.create_image((100, 500), image=self.img)  # нижний кружок

        # создание кнопок для запуска режимов объекта
        self.button_red = tk.Button(self, font='Arial 14', width=15, height=3, text='Красный',
                                    command=self.red_light)
        self.button_red.grid(row=0, column=1)  # включить красный свет

        self.button_yellow = tk.Button(self, font='Arial 14', width=15, height=3, text='Жёлтый',
                                       command=self.yellow_light)
        self.button_yellow.grid(row=1, column=1)    # включить жёлтый свет

        self.button_green = tk.Button(self, font='Arial 14', width=15, height=3, text='Зелёный',
                                      command=self.green_light)
        self.button_green.grid(row=2, column=1)    # включить зелёный свет

        self.button_auto = tk.Button(self, font='Arial 14', width=15, height=3, text='АВТО', command=self.running)
        self.button_auto.grid(row=3, column=1)    # включить автоматическую смену цветов светофора

    def red_light(self):
        """
        Переключает светофор на красный свет, а через заданное время выключает
        """
        if not self.color_run:  # проверяем, не запущен ли какой-то другой режим (кроме автоматического)
            self.color_run = True  # устанавливаем флаг запуска режима в положение True
            self.buttons_unavailable()  # делаем кнопки недоступными
            # меняем цвета кружков
            self.canvas.itemconfig(self.img_up, image=self.img_red)  # красный
            self.canvas.itemconfig(self.img_mid, image=self.img)  # серый
            self.canvas.itemconfig(self.img_dwn, image=self.img)  # серый
            if not self.auto_run:  # проверяем, не запущен ли автоматический режим
                t = Timer(7, self.gray_light)  # через заданное время переходим к выключению светофора
                t.start()
            else:
                self.color_run = False  # устанавливаем флаг запуска режима в положение False, если авторежим запущен

    # для переключения на жёлтый и зелёный цвет методы аналогичны вешеописанному методу переключения на красный

    def yellow_light(self):
        """
        Переключает светофор на жёлтый свет, а через заданное время выключает
        """
        if not self.color_run:
            self.color_run = True
            self.buttons_unavailable()
            self.canvas.itemconfig(self.img_up, image=self.img)
            self.canvas.itemconfig(self.img_mid, image=self.img_yellow)
            self.canvas.itemconfig(self.img_dwn, image=self.img)
            if not self.auto_run:
                t = Timer(2, self.gray_light)
                t.start()
            else:
                self.color_run = False

    def green_light(self):
        """
        Переключает светофор на зелёный свет, а через заданное время выключает
        """
        if not self.color_run:
            self.color_run = True
            self.buttons_unavailable()
            self.canvas.itemconfig(self.img_up, image=self.img)
            self.canvas.itemconfig(self.img_mid, image=self.img)
            self.canvas.itemconfig(self.img_dwn, image=self.img_green)
            if not self.auto_run:
                t = Timer(5, self.gray_light)
                t.start()
            else:
                self.color_run = False

    def gray_light(self):
        """
        Выключает светофор
        """
        # меняем цвета всех кружков на серый
        self.canvas.itemconfig(self.img_up, image=self.img)
        self.canvas.itemconfig(self.img_mid, image=self.img)
        self.canvas.itemconfig(self.img_dwn, image=self.img)
        # делаем все кнопки доступными, а все флаги переводим в положение False
        self.buttons_available()
        self.color_run = False
        self.auto_run = False

    def buttons_unavailable(self):
        """
        Делает все кнопки недоступными
        """
        self.button_red.configure(state='disabled')
        self.button_yellow.configure(state='disabled')
        self.button_green.configure(state='disabled')
        self.button_auto.configure(state='disabled')

    def buttons_available(self):
        """
        Делает все кнопки доступными
        """
        self.button_red.configure(state='normal')
        self.button_yellow.configure(state='normal')
        self.button_green.configure(state='normal')
        self.button_auto.configure(state='normal')

    def running(self):
        """
        Включает автоматическое переключение цветов, затем выключает светофор
        """
        if not self.color_run:  # проверяем, не запущен ли другой режим
            self.auto_run = True  # устанавливаем флаг авторежима в положение True
            self.buttons_unavailable()  # делаем кнопки недоступными
            # по таймерам запускаем методы переключения цветов
            s = Timer(0, self.red_light)
            s.start()
            r = Timer(7, self.yellow_light)
            r.start()
            y = Timer(9, self.green_light)
            y.start()
            g = Timer(14, self.gray_light)
            g.start()


root = tk.Tk()
root.title('Светофор')
root.geometry('400x600')
root.grid()

traffic_light = TrafficLight(root)
traffic_light.grid()

root.mainloop()

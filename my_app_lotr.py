import tkinter as tk
from tkinter import ttk, font
import pytz
from datetime import datetime
from PIL import Image, ImageTk
import requests
import io


class LotrTimeConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвектор времени")
        self.root.geometry("800x600")

        # Загрузка фонового изображения
        self.setup_background()

        # Стиль для виджетов
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Настройка шрифтов
        self.setup_fonts()

        # Загрузка и настройка изображений
        self.setup_images()

        # Создание интерфейса
        self.create_ui()

        # Инициализация времени
        self.set_current_time()

    def setup_background(self):
        try:
            # Фоновое изображение (можно заменить на свое)
            bg_image_url = "https://avatars.mds.yandex.net/get-shedevrum/16891129/img_ee9be39e536211f092120e5d09438c79/orig"  # Замените на реальный URL
            response = requests.get(bg_image_url)
            self.bg_image = Image.open(io.BytesIO(response.content))
            self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((800, 600), Image.LANCZOS))

            # Создаем холст с фоновым изображением
            self.canvas = tk.Canvas(self.root, width=800, height=600, highlightthickness=0)
            self.canvas.pack(fill="both", expand=True)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        except Exception as e:
            print(f"Ошибка загрузки фона: {e}")
            # Запасной вариант - однотонный фон
            self.root.configure(bg='#f5e6c8')
            self.canvas = tk.Canvas(self.root, width=800, height=600, highlightthickness=0, bg='#f5e6c8')
            self.canvas.pack(fill="both", expand=True)

    def setup_fonts(self):
        try:
            # Попробуем использовать тематические шрифты
            self.title_font = font.Font(family="Ringbearer", size=28)
            self.normal_font = font.Font(family="Moria Citadel", size=14)
            self.time_font = font.Font(family="Aniron", size=18)
        except:
            # Запасные шрифты
            self.title_font = font.Font(family="Times New Roman", size=28, weight="bold")
            self.normal_font = font.Font(family="Times New Roman", size=14)
            self.time_font = font.Font(family="Times New Roman", size=18)

    def setup_images(self):

        # Иконка для программы
        try:
            ring_icon_url = "https://avatars.mds.yandex.net/get-shedevrum/16367318/img_db506efd536811f08e002a268bbce87d/orig"  # Замените на реальный URL
            response = requests.get(ring_icon_url)
            self.ring_icon = Image.open(io.BytesIO(response.content))
            self.ring_photo = ImageTk.PhotoImage(self.ring_icon)
            self.root.iconphoto(False, self.ring_photo)
        except:
            pass

    def create_ui(self):
        # Создаем полупрозрачную рамку для содержимого
        self.main_frame = tk.Frame(self.canvas, bg='#e8d9a5', bd=3, relief='ridge',
                                   highlightbackground='#d4af37', highlightthickness=2)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=700, height=500)

        # Создаем рамку в средневековом стиле с закругленными углами
        self.main_frame = tk.Frame(self.canvas, bg='#e8d9a5', bd=3, relief='ridge', highlightbackground='#d4af37',
                                   highlightthickness=2)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center', width=700, height=500)

        # Заголовок
        title_label = tk.Label(self.main_frame,
                               text="Конветрация времени",
                               font=self.title_font,
                               fg='#8b6914',
                               bg='#e8d9a5')
        title_label.pack(pady=25)

        # Стили для Combobox с увеличенной стрелкой
        self.style.configure('TCombobox',
                             fieldbackground='#f0e0a0',
                             background='#f0e0a0',
                             foreground='#5a4a20',
                             font=self.normal_font,
                             borderwidth=2,
                             relief='solid',
                             arrowsize=20)  # Увеличиваем размер стрелки

        self.style.map('TCombobox',
                       fieldbackground=[('readonly', '#f0e0a0')],
                       selectbackground=[('readonly', '#e8d9a5')],
                       selectforeground=[('readonly', '#5a4a20')],
                       background=[('readonly', '#f0e0a0')])

        # Первый город
        city1_frame = tk.Frame(self.main_frame, bg='#e8d9a5')
        city1_frame.pack(pady=10)

        tk.Label(city1_frame,
                 text="Первый город :",
                 font=self.normal_font,
                 fg='#8b6914',
                 bg='#e8d9a5').pack(side='left', padx=10)

        self.city1_var = tk.StringVar()
        self.city1_combobox = ttk.Combobox(city1_frame,
                                           textvariable=self.city1_var,
                                           values=list(self.get_russian_cities().keys()),
                                           font=self.normal_font,
                                           style='TCombobox')
        self.city1_combobox.pack(side='left', padx=5)
        self.city1_combobox.bind("<<ComboboxSelected>>", self.update_times)
        self.city1_combobox.current(0)

        # Время первого города
        time1_frame = tk.Frame(self.main_frame, bg='#e8d9a5')
        time1_frame.pack(pady=5)

        tk.Label(time1_frame,
                 text="Время:",
                 font=self.normal_font,
                 fg='#8b6914',
                 bg='#e8d9a5').pack(side='left', padx=10)

        self.time1_var = tk.StringVar()
        self.time1_entry = tk.Entry(time1_frame,
                                    textvariable=self.time1_var,
                                    font=self.time_font,
                                    bg='#f0e0a0',
                                    fg='#5a4a20',
                                    insertbackground='#5a4a20',
                                    relief='solid',
                                    bd=2,
                                    highlightbackground='#d4af37',
                                    highlightthickness=1,
                                    highlightcolor='#d4af37')
        self.time1_entry.pack(side='left', ipady=3)
        self.time1_var.trace("w", self.time1_changed)

        self.tz1_var = tk.StringVar()
        tk.Label(time1_frame,
                 textvariable=self.tz1_var,
                 font=self.normal_font,
                 fg='#8b6914',
                 bg='#e8d9a5').pack(side='left', padx=10)

        # Разделитель
        tk.Label(self.main_frame,
                 text="⚔",
                 font=("Arial", 28),
                 fg='#8b6914',
                 bg='#e8d9a5').pack(pady=10)

        # Второй город
        city2_frame = tk.Frame(self.main_frame, bg='#e8d9a5')
        city2_frame.pack(pady=10)

        tk.Label(city2_frame,
                 text="Второй город :",
                 font=self.normal_font,
                 fg='#8b6914',
                 bg='#e8d9a5').pack(side='left', padx=10)

        self.city2_var = tk.StringVar()
        self.city2_combobox = ttk.Combobox(city2_frame,
                                           textvariable=self.city2_var,
                                           values=list(self.get_russian_cities().keys()),
                                           font=self.normal_font,
                                           style='TCombobox')
        self.city2_combobox.pack(side='left', padx=5)
        self.city2_combobox.bind("<<ComboboxSelected>>", self.update_times)
        self.city2_combobox.current(2)

        # Время второго города
        time2_frame = tk.Frame(self.main_frame, bg='#e8d9a5')
        time2_frame.pack(pady=5)

        tk.Label(time2_frame,
                 text="Время:",
                 font=self.normal_font,
                 fg='#8b6914',
                 bg='#e8d9a5').pack(side='left', padx=10)

        self.time2_var = tk.StringVar()
        self.time2_entry = tk.Entry(time2_frame,
                                    textvariable=self.time2_var,
                                    font=self.time_font,
                                    bg='#f0e0a0',
                                    fg='#5a4a20',
                                    insertbackground='#5a4a20',
                                    relief='solid',
                                    bd=2,
                                    highlightbackground='#d4af37',
                                    highlightthickness=1,
                                    highlightcolor='#d4af37')
        self.time2_entry.pack(side='left', ipady=3)
        self.time2_var.trace("w", self.time2_changed)

        self.tz2_var = tk.StringVar()
        tk.Label(time2_frame,
                 textvariable=self.tz2_var,
                 font=self.normal_font,
                 fg='#8b6914',
                 bg='#e8d9a5').pack(side='left', padx=10)

        # Кнопка текущего времени
        self.update_btn = tk.Button(self.main_frame,
                                    text="Указать текущее время",
                                    command=self.set_current_time,
                                    font=self.normal_font,
                                    bg='#d4af37',
                                    fg='#5a4a20',
                                    activebackground='#e8d9a5',
                                    activeforeground='#5a4a20',
                                    relief='raised',
                                    bd=3,
                                    padx=10,
                                    pady=5)
        self.update_btn.pack(pady=25)

        # Подпись внизу
        tk.Label(self.main_frame,
                 text="© iliaProject",
                 font=self.normal_font,
                 fg='#8b6914',
                 bg='#e8d9a5').pack(side='bottom', pady=15)

    def get_russian_cities(self):
        """Возвращает словарь городов России и их часовых поясов"""
        return {
            'Москва': 'Europe/Moscow',
            'Санкт-Петербург': 'Europe/Moscow',
            'Новосибирск': 'Asia/Novosibirsk',
            'Екатеринбург': 'Asia/Yekaterinburg',
            'Казань': 'Europe/Moscow',
            'Нижний Новгород': 'Europe/Moscow',
            'Челябинск': 'Asia/Yekaterinburg',
            'Самара': 'Europe/Samara',
            'Омск': 'Asia/Omsk',
            'Ростов-на-Дону': 'Europe/Moscow',
            'Уфа': 'Asia/Yekaterinburg',
            'Красноярск': 'Asia/Krasnoyarsk',
            'Пермь': 'Asia/Yekaterinburg',
            'Воронеж': 'Europe/Moscow',
            'Волгоград': 'Europe/Volgograd',
            'Краснодар': 'Europe/Moscow',
            'Саратов': 'Europe/Saratov',
            'Тюмень': 'Asia/Yekaterinburg',
            'Тольятти': 'Europe/Samara',
            'Ижевск': 'Europe/Samara',
            'Барнаул': 'Asia/Barnaul',
            'Иркутск': 'Asia/Irkutsk',
            'Хабаровск': 'Asia/Vladivostok',
            'Владивосток': 'Asia/Vladivostok',
            'Якутск': 'Asia/Yakutsk',
            'Магадан': 'Asia/Magadan',
            'Петропавловск-Камчатский': 'Asia/Kamchatka'
        }

    def set_current_time(self):
        """Устанавливает текущее время для выбранных городов"""
        now = datetime.now()
        city1 = self.city1_var.get().split(' (')[1][:-1] if '(' in self.city1_var.get() else self.city1_var.get()
        city2 = self.city2_var.get().split(' (')[1][:-1] if '(' in self.city2_var.get() else self.city2_var.get()

        if city1 and city2:
            tz1 = pytz.timezone(self.get_russian_cities()[self.city1_var.get()])
            tz2 = pytz.timezone(self.get_russian_cities()[self.city2_var.get()])

            time1 = now.astimezone(tz1).strftime("%H:%M")
            time2 = now.astimezone(tz2).strftime("%H:%M")

            self.time1_var.set(time1)
            self.time2_var.set(time2)

            self.update_timezone_info()

    def update_timezone_info(self):
        """Обновляет информацию о часовых поясах"""
        city1 = self.city1_var.get()
        city2 = self.city2_var.get()

        if city1 and city2:
            tz1 = pytz.timezone(self.get_russian_cities()[city1])
            tz2 = pytz.timezone(self.get_russian_cities()[city2])

            offset1 = datetime.now(tz1).strftime("%z")
            offset2 = datetime.now(tz2).strftime("%z")

            offset1_str = f"UTC{int(offset1[:3])}"
            offset2_str = f"UTC{int(offset2[:3])}"

            self.tz1_var.set(offset1_str)
            self.tz2_var.set(offset2_str)

    def update_times(self, event=None):
        """Обновляет время при изменении выбора города"""
        self.set_current_time()

    def time1_changed(self, *args):
        """Обработчик изменения времени для первого города"""
        self.convert_time(1)

    def time2_changed(self, *args):
        """Обработчик изменения времени для второго города"""
        self.convert_time(2)

    def convert_time(self, source):
        """Конвертирует время между городами"""
        try:
            city1_key = self.city1_var.get()
            city2_key = self.city2_var.get()

            if not city1_key or not city2_key:
                return

            city1 = city1_key.split(' (')[1][:-1] if '(' in city1_key else city1_key
            city2 = city2_key.split(' (')[1][:-1] if '(' in city2_key else city2_key

            tz1 = pytz.timezone(self.get_russian_cities()[city1_key])
            tz2 = pytz.timezone(self.get_russian_cities()[city2_key])

            if source == 1:  # Изменено время первого города
                time_str = self.time1_var.get()
                if not time_str:
                    return

                hours, minutes = map(int, time_str.split(':'))
                now = datetime.now()
                dt = datetime(now.year, now.month, now.day, hours, minutes)

                dt_tz1 = tz1.localize(dt)
                dt_tz2 = dt_tz1.astimezone(tz2)

                self.time2_var.set(dt_tz2.strftime("%H:%M"))

            elif source == 2:  # Изменено время второго города
                time_str = self.time2_var.get()
                if not time_str:
                    return

                hours, minutes = map(int, time_str.split(':'))
                now = datetime.now()
                dt = datetime(now.year, now.month, now.day, hours, minutes)

                dt_tz2 = tz2.localize(dt)
                dt_tz1 = dt_tz2.astimezone(tz1)

                self.time1_var.set(dt_tz1.strftime("%H:%M"))

            self.update_timezone_info()

        except Exception as e:
            print(f"Ошибка конвертации: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LotrTimeConverter(root)
    root.mainloop()
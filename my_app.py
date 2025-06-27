import tkinter as tk
from tkinter import ttk
import pytz
from datetime import datetime
import requests


class TimeZoneConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер времени для городов России")
        self.root.geometry("300x200")

        # Получаем список городов России с часовыми поясами
        self.cities = self.get_russian_cities()

        # Основные элементы интерфейса
        self.create_widgets()

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

    def create_widgets(self):
        # Первый город
        tk.Label(self.root, text="Город 1:").grid(row=0, column=0, padx=10, pady=5)
        self.city1_var = tk.StringVar()
        self.city1_combobox = ttk.Combobox(self.root, textvariable=self.city1_var, values=list(self.cities.keys()))
        self.city1_combobox.grid(row=0, column=1, padx=10, pady=5)
        self.city1_combobox.bind("<<ComboboxSelected>>", self.update_times)
        self.city1_combobox.current(0)  # Москва по умолчанию

        # Время для первого города
        tk.Label(self.root, text="Время:").grid(row=1, column=0, padx=10, pady=5)
        self.time1_var = tk.StringVar()
        self.time1_entry = tk.Entry(self.root, textvariable=self.time1_var)
        self.time1_entry.grid(row=1, column=1, padx=10, pady=5)
        self.time1_var.trace("w", self.time1_changed)

        # Часовой пояс первого города
        self.tz1_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.tz1_var).grid(row=1, column=2, padx=10, pady=5)

        # Второй город
        tk.Label(self.root, text="Город 2:").grid(row=2, column=0, padx=10, pady=5)
        self.city2_var = tk.StringVar()
        self.city2_combobox = ttk.Combobox(self.root, textvariable=self.city2_var, values=list(self.cities.keys()))
        self.city2_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.city2_combobox.bind("<<ComboboxSelected>>", self.update_times)
        self.city2_combobox.current(2)  # Новосибирск по умолчанию

        # Время для второго города
        tk.Label(self.root, text="Время:").grid(row=3, column=0, padx=10, pady=5)
        self.time2_var = tk.StringVar()
        self.time2_entry = tk.Entry(self.root, textvariable=self.time2_var)
        self.time2_entry.grid(row=3, column=1, padx=10, pady=5)
        self.time2_var.trace("w", self.time2_changed)

        # Часовой пояс второго города
        self.tz2_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.tz2_var).grid(row=3, column=2, padx=10, pady=5)

        # Кнопка для обновления текущего времени
        self.update_btn = tk.Button(self.root, text="Текущее время", command=self.set_current_time)
        self.update_btn.grid(row=4, column=1, pady=10)

        # Инициализация времени
        self.set_current_time()

    def set_current_time(self):
        """Устанавливает текущее время для выбранных городов"""
        now = datetime.now()
        city1 = self.city1_var.get()
        city2 = self.city2_var.get()

        if city1 and city2:
            tz1 = pytz.timezone(self.cities[city1])
            tz2 = pytz.timezone(self.cities[city2])

            time1 = now.astimezone(tz1).strftime("%H:%M")
            time2 = now.astimezone(tz2).strftime("%H:%M")

            self.time1_var.set(time1)
            self.time2_var.set(time2)

            # Обновляем информацию о часовых поясах
            self.update_timezone_info()

    def update_timezone_info(self):
        """Обновляет информацию о часовых поясах"""
        city1 = self.city1_var.get()
        city2 = self.city2_var.get()

        if city1 and city2:
            tz1 = pytz.timezone(self.cities[city1])
            tz2 = pytz.timezone(self.cities[city2])

            # Получаем смещение от UTC
            offset1 = datetime.now(tz1).strftime("%z")
            offset2 = datetime.now(tz2).strftime("%z")

            # Форматируем смещение (например, +0300 -> +3)
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
            city1 = self.city1_var.get()
            city2 = self.city2_var.get()

            if not city1 or not city2:
                return

            tz1 = pytz.timezone(self.cities[city1])
            tz2 = pytz.timezone(self.cities[city2])

            if source == 1:  # Изменено время первого города
                time_str = self.time1_var.get()
                if not time_str:
                    return

                # Парсим время
                hours, minutes = map(int, time_str.split(':'))
                now = datetime.now()
                dt = datetime(now.year, now.month, now.day, hours, minutes)

                # Конвертируем время
                dt_tz1 = tz1.localize(dt)
                dt_tz2 = dt_tz1.astimezone(tz2)

                # Обновляем время второго города
                self.time2_var.set(dt_tz2.strftime("%H:%M"))

            elif source == 2:  # Изменено время второго города
                time_str = self.time2_var.get()
                if not time_str:
                    return

                # Парсим время
                hours, minutes = map(int, time_str.split(':'))
                now = datetime.now()
                dt = datetime(now.year, now.month, now.day, hours, minutes)

                # Конвертируем время
                dt_tz2 = tz2.localize(dt)
                dt_tz1 = dt_tz2.astimezone(tz1)

                # Обновляем время первого города
                self.time1_var.set(dt_tz1.strftime("%H:%M"))

            self.update_timezone_info()

        except Exception as e:
            print(f"Ошибка конвертации: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimeZoneConverter(root)
    root.mainloop()
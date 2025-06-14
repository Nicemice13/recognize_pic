from random import choice
import time
import tkinter as tk
from tkinter import ttk

class Recognizer:
    LST_PIC = {
            "Васнецов": ["Иван Грозный", "Иван царевич и серый волк", "Богатыри"],
            "Шишкин": ["Утро в сосновом лесу", "Рожь", "Корабельная роща"],
            "Репин": ["Бурлаки на Волге", "Не ждали", "Запорожцы пишут письмо турецкому султану"]
    }


    def __init__(self, root):
        self.root = root
        self.root.title("Розовая мечта")
        self.root.geometry("400x500")
        self.root.configure(bg="#FFD1DC")

        for x, autor in enumerate(self.LST_PIC.keys(),1):

            self.radio1 = tk.Radiobutton(root, text=autor, variable="self.radio_var",
                                    value="1", bg="#FFD1DC")
            self.radio1.place(x=100*x, y=50)


def main(z=5):
    for _ in range(z):
        rmd_pic = choice(lst_pic)
        pic = choice(*rmd_pic.values())
        print(f"Кто автор картины {pic}?")

        while input("Введите имя автора: ") not in rmd_pic:
            print("Подумай еще!")

        print("Ты угадал")

        print(*rmd_pic)
        time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = Recognizer(root)
    root.mainloop()

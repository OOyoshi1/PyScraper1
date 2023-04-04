import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *
from tkinter import ttk
import re


def click():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
    }
    if cmb1.current() == 0:
        if cmb2.current() == 0:
            url = 'https://www.cifrus.ru/'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            categories = soup.find_all('a', class_='dropdown-toggle')
            result_listbox.delete(0, tk.END)

            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 1:
            url = 'https://www.cifrus.ru/catalog/1/'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['div', 'span'], class_=['name', 'price-new'])

            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 2:
            url = 'https://www.cifrus.ru/catalog/9'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['div', 'span'], class_=['name', 'price-new'])

            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1


        if cmb2.current() == 3:
            url = 'https://www.cifrus.ru/catalog/42'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['div', 'span'], class_=['name', 'price-new'])

            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 4:
            url = 'https://www.cifrus.ru/catalog2/3/nayshniki_i_bluetooth-garnityri'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['div', 'span'], class_=['name', 'price-new'])

            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1

        if cmb2.current() == 5:
            url = 'https://www.cifrus.ru/catalog/71'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['div', 'span'], class_=['name', 'price-new'])

            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1

    if cmb1.current() == 1:

        if cmb2.current() == 0:
            url = 'https://quke.ru/shop/smartfony'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all('a', class_='cat-nav__sec-list-link')
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1

        if cmb2.current() == 1:
            url = 'https://quke.ru/shop/smartfony'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'span'], class_=['b-card2-v2__name', 'b-card2-v2__price-val'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 2:
            url = 'https://quke.ru/shop/planshety'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'span'], class_=['b-card2-v2__name', 'b-card2-v2__price-val'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 3:
            url = 'https://quke.ru/shop/fitnes-chasy-i-braslety'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'span'], class_=['b-card2-v2__name', 'b-card2-v2__price-val'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 4:
            url = 'https://quke.ru/shop/naushniki-i-audiotehnika'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'span'], class_=['b-card2-v2__name', 'b-card2-v2__price-val'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 5:
            url = 'https://quke.ru/shop/tehnika-dlya-doma'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'span'], class_=['b-card2-v2__name', 'b-card2-v2__price-val'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
    if cmb1.current() == 2:

        if cmb2.current() == 0:
            url = 'https://biggeek.ru/'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all('a', class_='category-dropdown-header__link')
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1

        if cmb2.current() == 1:
            url = 'https://biggeek.ru/catalog/smartfony'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'b'], class_=['catalog-card__title cart-modal-title', 'cart-modal-count'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 2:
            url = 'https://biggeek.ru/catalog/planshety'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'b'], class_=['catalog-card__title cart-modal-title', 'cart-modal-count'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 3:
            url = 'https://biggeek.ru/catalog/chasy-i-elektronnye-braslety'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'b'], class_=['catalog-card__title cart-modal-title', 'cart-modal-count'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 4:
            url = 'https://biggeek.ru/catalog/kupit-nausniki'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'b'], class_=['catalog-card__title cart-modal-title', 'cart-modal-count'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 5:
            url = 'https://biggeek.ru/catalog/dlya-doma'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['a', 'b'], class_=['catalog-card__title cart-modal-title', 'cart-modal-count'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
    if cmb1.current() == 3:

        if cmb2.current() == 0:
            url = 'https://www.pleer.ru/'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all('span', class_='catalog-list__title')
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1

        if cmb2.current() == 1:
            url = 'https://www.pleer.ru/list_kpk-i-kommunikatory.html'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['span', 'span'], class_=['item_name', 'price_disk'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 2:
            url = 'https://www.pleer.ru/list_planshetnye-komputery.html'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['span', 'span'], class_=['item_name', 'price_disk'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1


        if cmb2.current() == 3:
            url = 'https://www.pleer.ru/list_umnye-chasy.html'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['span', 'span'], class_=['item_name', 'price_disk'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 4:
            url = 'https://www.pleer.ru/list_garnitury-s-odnim-naushnikom.html'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['span', 'span'], class_=['item_name', 'price_disk'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1
        if cmb2.current() == 5:
            url = 'https://www.pleer.ru/list_multivarki.html'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            result_listbox.delete(0, tk.END)

            categories = soup.find_all(['span', 'span'], class_=['item_name', 'price_disk'])
            for cat in categories:
                a = 0
                result_listbox.insert(a, cat.text)

                a += 1


win = tk.Tk()
win.title('Приложение')
win.geometry('800x600+500+300')
win.minsize(800, 600)
# photo = tk.PhotoImage(file='shopping.png')
# win.iconphoto(False, photo)
win.config(bg='#9db1cc')

Lable1 = tk.Label(win, text='Помошник выбора товара',
                  bg='#9db1cc',
                  fg='black',
                  font=('Aial', 20, 'bold'),
                  padx=20,
                  pady=20
                  )
Lable1.pack()

Lable2 = tk.Label(win, text='Выберите магазин',
                  bg='#9db1cc',
                  fg='black',
                  font=('Aial', 15),
                  padx=20,
                  pady=20
                  )
Lable2.pack()

shop = ['Cifrus.ru', 'Quke.ru', 'BigGeek.ru',
        'Pleer.ru']
cmb1 = ttk.Combobox(values=shop,
                    width=40,
                    font=10

                    )
cmb1.pack()

Lable3 = tk.Label(win, text='Выберите категорию',
                  bg='#9db1cc',
                  fg='black',
                  font=('Aial', 15,),
                  padx=20,
                  pady=20
                  )
Lable3.pack()

category = ['Названия категорий', 'Мобильные телефоны и цены', 'Планшеты, ноутбуки и цены',
            'Часы, умные браслеты и цены', 'Наушники и цены', 'Техника для дома и цены']
cmb2 = ttk.Combobox(values=category,
                    width=40,
                    font=10
                    )
cmb2.pack(padx=20)

btn1 = tk.Button(win, text='Искать',

                 command=click,
                 bg='#c8d6e6',
                 activebackground='#a2add0',
                 font=15
                 )

btn1.pack(pady=20)

result = []
result_var = Variable(value=result)

result_listbox = Listbox(listvariable=result_var,
                         bg='#c8d6e6',
                         font=8
                         )
result_listbox.pack(padx=10, pady=3, fill=tk.BOTH, expand=True)

win.mainloop()

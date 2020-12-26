import requests

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def get_download():
    """Скачать файл методом GET"""
    downloaded_file = requests.get(url.get(), auth=("admin", "pass"))
    if len(file_name.get()) > 0:
        open(path+str(file_name.get()), "wb").write(downloaded_file.content)
    else:
        messagebox.showinfo("Ошибка", "Введите название для файла")

def put_upload():
    """Загрузить файл на сервер по API методом PUT"""
    downloaded_file = requests.get(url.get(), auth=("admin", "pass"))
    if len(file_name.get()) > 0:
        requests.put(url+str(file_name.get()), data=downloaded_file, auth=("admin", "pass"))

def help_button():
    """Подсказки для работы со скриптом"""
    messagebox.showinfo("Помощь", "\tПункт 1\n\tПункт 2\n\tПункт 3")

def check_status():
    """Проверка статуса запрашиваемого URL"""
    response = requests.get(url.get())
    messagebox.showinfo("Статус", response.status_code)
    if response.status_code != 200:
        print(response.status_code)

def close_app():
    """Закрывает приложение"""
    exit()

root = Tk()
root.title("GET/PUT")
root.geometry("550x200+550+200")

style = ttk.Style()

path = "/Users/Downloads"
url = StringVar()
file_name = StringVar()

url_label = Label(text="Введите url: ")
file_name_label = Label(text="Введите название файла: ")

url_label.grid(row=0, column=0, sticky="w")
file_name_label.grid(row=1, column=0, sticky="w")

url_entry = Entry(textvariable=url, width=40)
file_name_entry = Entry(textvariable=file_name, width=40)

url_entry.insert(0, 'https://api.jokes.one/jod?category=knock-knock')

url_entry.grid(row=0, column=1, padx=5, pady=5)
file_name_entry.grid(row=1, column=1, padx=5, pady=5)

download_button = ttk.Button(text="Скачать", command=get_download)
download_button.place(relx=.85, rely=.5, anchor="c", width=110)

upload_button = ttk.Button(text="Загрузить", command=put_upload)
upload_button.place(relx=.15, rely=.5, anchor="c", width=110)

exit_button = ttk.Button(text="Выход", command=close_app)
exit_button.place(relx=.85, rely=.9, anchor="c", width=110)

help_button = ttk.Button(text="Помощь", command=help_button)
help_button.place(relx=.15, rely=.9, anchor="c", width=110)

check_button = ttk.Button(text="Проверить статус", command=check_status)
check_button.place(relx=.5, rely=.65, anchor="c", width=200)

root.mainloop()
import tkinter as tk
from tkinter import filedialog
import tkinter as tk
import threading
from Downloaders import *


url = ""
download_option = ""
directory = ""


def get_directory():
    global directory
    directory = filedialog.askdirectory()

def confirmar():
    global url, download_option
    url = url_entry.get()
    download_option = opcao_select.get()

    # Exibir o processo dos dados inseridos no textarea
    textarea.insert(tk.END, "Começando o Download...\n", "success")
    download_thread = threading.Thread(target=download_playlist, args=(url, download_option, directory))
    download_thread.start()


# Criar a janela principal
janela = tk.Tk()
janela.title('YoutubePlaylistDownloader')
janela['padx'] = 20
janela['pady'] = 20

# Criar os elementos da janela
url_label = tk.Label(janela, text="URL:")
url_label.pack(fill="x", pady=2)

url_entry = tk.Entry(janela)
url_entry.pack(fill="x", pady=5)

opcao_label = tk.Label(janela, text="Opção:")
opcao_label.pack(fill="x", pady=2)

opcao_select = tk.StringVar(janela)
opcao_select.set("MP4 (Alta Qualidade)")  # Definir a opção padrão

opcao_menu = tk.OptionMenu(janela, opcao_select, "MP4 (Alta Qualidade)", "MP4 (Baixa Qualidade)", "MPG")
opcao_menu.pack(fill="x", pady=5)

diretorio_button = tk.Button(janela, text="Selecionar diretório", command=get_directory)
diretorio_button.pack(fill="x", pady=5)

confirmar_button = tk.Button(janela, text="Confirmar", command=confirmar)
confirmar_button.pack(fill="x", pady=5)

textarea = tk.Text(janela)
textarea.pack(fill="y")

textarea.tag_config("success", foreground="green")
textarea.tag_config("failed", foreground="red")

# Iniciar a janela principal
janela.mainloop()

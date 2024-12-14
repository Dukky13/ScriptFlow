import tkinter as tk
from tkinter import filedialog


def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), 
                                                        ("Python Files", "*.py"), 
                                                        ("HTML Files", "*.html"), 
                                                        ("Markdown Files", "*.md"), 
                                                        ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))

def dark_back():
    root.configure(bg="#393E46")
    text_area.configure(bg="#23272A", fg="#FFFFFF")  # Alterar fundo e texto do editor
    
def light_back():
    root.configure(bg="#ffffff")
    text_area.configure(bg="#FFFFFF", fg="#000000")  # Alterar fundo e texto do editor

# Funções para o menu Editar
def undo_action():
    try:
        text_area.edit_undo()
    except:
        pass

def redo_action():
    try:
        text_area.edit_redo()
    except:
        pass

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(text_area.selection_get())

def paste_text():
    try:
        text_area.insert(tk.INSERT, root.clipboard_get())
    except:
        pass

def open_file():
    # Abre uma caixa de diálogo para escolher o arquivo
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:  # Se o caminho do arquivo não for vazio
        with open(file_path, 'r') as file:  # Abre o arquivo em modo leitura
            text_content = file.read()  # Lê o conteúdo do arquivo
            text_area.delete(1.0, tk.END)  # Apaga o conteúdo atual da área de texto
            text_area.insert(tk.END, text_content)  # Insere o conteúdo do arquivo na área de texto

# Configuração da janela principal
root = tk.Tk()
root.title("FlowEditor")

# Área de texto com suporte a undo/redo
text_area = tk.Text(root, wrap='word', undo=True)
text_area.pack(expand=1, fill='both')

# Menu
menu_bar = tk.Menu(root)
# Menu arquivo
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Novo", command=new_file)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Salvar", command=save_file)
file_menu.add_command(label="Abrir ficheiro" ,command=open_file)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)
# Menu temas
theme_menu = tk.Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Modo escuro", command=dark_back)
theme_menu.add_command(label="Modo claro", command=light_back)
menu_bar.add_cascade(label="Temas", menu=theme_menu)

menu_bar.add_command(label="Desfazer", command=undo_action)
menu_bar.add_command(label="Refazer", command=redo_action)
menu_bar.add_command(label="Copiar", command=copy_text)
menu_bar.add_command(label="Colar", command=paste_text)

root.config(menu=menu_bar)
root.mainloop()

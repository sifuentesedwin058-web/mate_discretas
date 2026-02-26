import tkinter as tk
from tkinter import messagebox

# -------- FUNCIONES -------- #

def limpiar_frames():
    for frame in (frame_bin, frame_hex, frame_oct):
        frame.pack_forget()

def mostrar(frame):
    limpiar_frames()
    frame.pack(fill="both", expand=True)

# BINARIO
def bin_a_hex():
    try:
        numero = entry_bin.get()
        decimal = int(numero, 2)
        resultado = hex(decimal)[2:].upper()
        lbl_resultado_bin.config(text="Hexadecimal: " + resultado)
    except:
        messagebox.showerror("Error", "Número binario inválido")

def bin_a_oct():
    try:
        numero = entry_bin.get()
        decimal = int(numero, 2)
        resultado = oct(decimal)[2:]
        lbl_resultado_bin.config(text="Octal: " + resultado)
    except:
        messagebox.showerror("Error", "Número binario inválido")

# HEXADECIMAL
def hex_a_bin():
    try:
        numero = entry_hex.get()
        decimal = int(numero, 16)
        resultado = bin(decimal)[2:]
        lbl_resultado_hex.config(text="Binario: " + resultado)
    except:
        messagebox.showerror("Error", "Número hexadecimal inválido")

# OCTAL
def oct_a_bin():
    try:
        numero = entry_oct.get()
        decimal = int(numero, 8)
        resultado = bin(decimal)[2:]
        lbl_resultado_oct.config(text="Binario: " + resultado)
    except:
        messagebox.showerror("Error", "Número octal inválido")

# -------- VENTANA PRINCIPAL -------- #

ventana = tk.Tk()
ventana.title("Conversor Binario - Hexadecimal - Octal")
ventana.geometry("400x300")
ventana.config(bg="lightgray")

# -------- MENU -------- #

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu=menu)
menu.add_command(label="Binario", command=lambda: mostrar(frame_bin))
menu.add_command(label="Hexadecimal", command=lambda: mostrar(frame_hex))
menu.add_command(label="Octal", command=lambda: mostrar(frame_oct))
menu.add_separator()
menu.add_command(label="Salir", command=ventana.quit)

# -------- FRAME BINARIO -------- #

frame_bin = tk.Frame(ventana, bg="white")

tk.Label(frame_bin, text="BINARIO", font=("Arial", 14), bg="white").pack(pady=10)

entry_bin = tk.Entry(frame_bin)
entry_bin.pack()

tk.Button(frame_bin, text="Convertir a Hexadecimal", command=bin_a_hex).pack(pady=5)
tk.Button(frame_bin, text="Convertir a Octal", command=bin_a_oct).pack(pady=5)

lbl_resultado_bin = tk.Label(frame_bin, text="Resultado:", bg="white")
lbl_resultado_bin.pack(pady=10)

tk.Button(frame_bin, text="Ir a Hexadecimal",
          command=lambda: mostrar(frame_hex)).pack()

# -------- FRAME HEXADECIMAL -------- #

frame_hex = tk.Frame(ventana, bg="white")

tk.Label(frame_hex, text="HEXADECIMAL", font=("Arial", 14), bg="white").pack(pady=10)

entry_hex = tk.Entry(frame_hex)
entry_hex.pack()

tk.Button(frame_hex, text="Convertir a Binario", command=hex_a_bin).pack(pady=5)

lbl_resultado_hex = tk.Label(frame_hex, text="Resultado:", bg="white")
lbl_resultado_hex.pack(pady=10)

tk.Button(frame_hex, text="Ir a Octal",
          command=lambda: mostrar(frame_oct)).pack()

# -------- FRAME OCTAL -------- #

frame_oct = tk.Frame(ventana, bg="white")

tk.Label(frame_oct, text="OCTAL", font=("Arial", 14), bg="white").pack(pady=10)

entry_oct = tk.Entry(frame_oct)
entry_oct.pack()

tk.Button(frame_oct, text="Convertir a Binario", command=oct_a_bin).pack(pady=5)

lbl_resultado_oct = tk.Label(frame_oct, text="Resultado:", bg="white")
lbl_resultado_oct.pack(pady=10)

tk.Button(frame_oct, text="Volver a Binario",
          command=lambda: mostrar(frame_bin)).pack()

# Mostrar primer frame
mostrar(frame_bin)

ventana.mainloop()

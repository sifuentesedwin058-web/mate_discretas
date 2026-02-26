import tkinter as tk
from tkinter import messagebox

# ---------------- FUNCIONES ---------------- #

def limpiar_frames():
    for frame in (frame1, frame2, frame3, frame4):
        frame.pack_forget()

def mostrar(frame):
    limpiar_frames()
    frame.pack(fill="both", expand=True)

def bin_a_dec():
    try:
        numero = entry_bin.get()
        resultado = int(numero, 2)
        lbl_res1.config(text="Resultado: " + str(resultado))
    except:
        messagebox.showerror("Error", "Número binario inválido")

def dec_a_bin():
    try:
        numero = int(entry_dec.get())
        resultado = bin(numero)[2:]
        lbl_res2.config(text="Resultado: " + resultado)
    except:
        messagebox.showerror("Error", "Número decimal inválido")

def hex_a_oct():
    try:
        numero = entry_hex.get()
        decimal = int(numero, 16)
        resultado = oct(decimal)[2:]
        lbl_res3.config(text="Resultado: " + resultado)
    except:
        messagebox.showerror("Error", "Número hexadecimal inválido")

def oct_a_hex():
    try:
        numero = entry_oct.get()
        decimal = int(numero, 8)
        resultado = hex(decimal)[2:].upper()
        lbl_res4.config(text="Resultado: " + resultado)
    except:
        messagebox.showerror("Error", "Número octal inválido")

# ---------------- VENTANA PRINCIPAL ---------------- #

ventana = tk.Tk()
ventana.title("APP DE CONVERSIONES")
ventana.geometry("400x300")
ventana.config(bg="lightblue")

# ---------------- MENU ---------------- #

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# ---------------- FRAME 1 ---------------- #

frame1 = tk.Frame(ventana, bg="white")

tk.Label(frame1, text="Binario a Decimal", bg="white", font=("Arial", 14)).pack(pady=10)
entry_bin = tk.Entry(frame1)
entry_bin.pack()

tk.Button(frame1, text="Convertir", command=bin_a_dec).pack(pady=5)
lbl_res1 = tk.Label(frame1, text="Resultado:", bg="white")
lbl_res1.pack(pady=5)

tk.Button(frame1, text="Ir a Decimal → Binario",
          command=lambda: mostrar(frame2)).pack(pady=10)

# ---------------- FRAME 2 ---------------- #

frame2 = tk.Frame(ventana, bg="white")

tk.Label(frame2, text="Decimal a Binario", bg="white", font=("Arial", 14)).pack(pady=10)
entry_dec = tk.Entry(frame2)
entry_dec.pack()

tk.Button(frame2, text="Convertir", command=dec_a_bin).pack(pady=5)
lbl_res2 = tk.Label(frame2, text="Resultado:", bg="white")
lbl_res2.pack(pady=5)

tk.Button(frame2, text="Ir a Hexadecimal → Octal",
          command=lambda: mostrar(frame3)).pack(pady=10)

# ---------------- FRAME 3 ---------------- #

frame3 = tk.Frame(ventana, bg="white")

tk.Label(frame3, text="Hexadecimal a Octal", bg="white", font=("Arial", 14)).pack(pady=10)
entry_hex = tk.Entry(frame3)
entry_hex.pack()

tk.Button(frame3, text="Convertir", command=hex_a_oct).pack(pady=5)
lbl_res3 = tk.Label(frame3, text="Resultado:", bg="white")
lbl_res3.pack(pady=5)

tk.Button(frame3, text="Ir a Octal → Hexadecimal",
          command=lambda: mostrar(frame4)).pack(pady=10)

# ---------------- FRAME 4 ---------------- #

frame4 = tk.Frame(ventana, bg="white")

tk.Label(frame4, text="Octal a Hexadecimal", bg="white", font=("Arial", 14)).pack(pady=10)
entry_oct = tk.Entry(frame4)
entry_oct.pack()

tk.Button(frame4, text="Convertir", command=oct_a_hex).pack(pady=5)
lbl_res4 = tk.Label(frame4, text="Resultado:", bg="white")
lbl_res4.pack(pady=5)

tk.Button(frame4, text="Volver al inicio",
          command=lambda: mostrar(frame1)).pack(pady=10)

# Mostrar primer frame
mostrar(frame1)

ventana.mainloop()

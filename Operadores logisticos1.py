import tkinter as tk

# Funciones lógicas
def AND(a,b):
    return int(a and b)

def OR(a,b):
    return int(a or b)

def NOT(a):
    return int(not a)

# Crear ventana
ventana = tk.Tk()
ventana.title("Tablas de verdad - Compuertas Lógicas")
ventana.geometry("400x300")

texto = tk.Text(ventana, font=("Consolas", 12))
texto.pack(pady=10)

# Tabla AND
texto.insert(tk.END, "Tabla de verdad AND\n")
texto.insert(tk.END, "A B | A AND B\n")
for A in [0,1]:
    for B in [0,1]:
        texto.insert(tk.END, f"{A} {B} | {AND(A,B)}\n")

texto.insert(tk.END, "\n")

# Tabla OR
texto.insert(tk.END, "Tabla de verdad OR\n")
texto.insert(tk.END, "A B | A OR B\n")
for A in [0,1]:
    for B in [0,1]:
        texto.insert(tk.END, f"{A} {B} | {OR(A,B)}\n")

texto.insert(tk.END, "\n")

# Tabla NOT
texto.insert(tk.END, "Tabla de verdad NOT\n")
texto.insert(tk.END, "A | NOT A\n")
for A in [0,1]:
    texto.insert(tk.END, f"{A} | {NOT(A)}\n")

ventana.mainloop()
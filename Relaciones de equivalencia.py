import tkinter as tk
from tkinter import messagebox

# Función principal para analizar la relación
def analizar_relacion():
    A = entrada_conjunto.get().split(",")
    A = [x.strip() for x in A if x.strip()]

    pares_texto = entrada_relacion.get().split(",")
    R = set()
    for p in pares_texto:
        if "-" in p:
            a,b = p.split("-")
            R.add((a.strip(), b.strip()))

    if not A or not R:
        messagebox.showwarning("Error", "Debes ingresar un conjunto y una relación válidos")
        return

    reflexiva = all((a,a) in R for a in A)
    simetrica = all((b,a) in R for (a,b) in R)
    transitiva = all((a,d) in R for (a,b) in R for (c,d) in R if b==c)

    # Preparar resultado con colores
    res_texto = ""
    res_texto += f"Reflexiva: {'✅' if reflexiva else '❌'}\n"
    res_texto += f"Simétrica: {'✅' if simetrica else '❌'}\n"
    res_texto += f"Transitiva: {'✅' if transitiva else '❌'}\n"
    res_texto += "\nEs relación de equivalencia ✅" if reflexiva and simetrica and transitiva else "\nNo es relación de equivalencia ❌"

    label_resultado.config(text=res_texto, fg="green" if reflexiva and simetrica and transitiva else "red")


# Ventana principal
ventana = tk.Tk()
ventana.title("Analizador de Relaciones de Equivalencia")
ventana.geometry("500x350")
ventana.configure(bg="#f0f0f0")

# Título
tk.Label(ventana, text="Relaciones de Equivalencia", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# Entradas
frame_entradas = tk.Frame(ventana, bg="#f0f0f0")
frame_entradas.pack(pady=10)

tk.Label(frame_entradas, text="Conjunto (ej: a,b,c)", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
entrada_conjunto = tk.Entry(frame_entradas, width=30, font=("Helvetica", 12))
entrada_conjunto.grid(row=0, column=1, pady=5)

tk.Label(frame_entradas, text="Relación (ej: a-a,b-b,c-c,a-b,b-a)", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
entrada_relacion = tk.Entry(frame_entradas, width=30, font=("Helvetica", 12))
entrada_relacion.grid(row=1, column=1, pady=5)

# Botón
tk.Button(ventana, text="Analizar Relación", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=20, command=analizar_relacion).pack(pady=15)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
label_resultado.pack(pady=10)

ventana.mainloop()
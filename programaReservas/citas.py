import tkinter as tk
from tkinter import messagebox
import json
import os

# Archivo donde se guardarán las citas
FILE_NAME = "citas_medicas.json"

# Cargar citas desde el archivo si existe
def cargar_citas():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Guardar citas en el archivo
def guardar_citas(citas):
    with open(FILE_NAME, "w") as file:
        json.dump(citas, file, indent=4)

# Añadir una nueva cita
def anadir_cita():
    nombre = entry_nombre.get()
    apellidos = entry_apellidos.get()
    dni = entry_dni.get()
    dia = entry_dia.get()
    hora = entry_hora.get()

    if not all([nombre, apellidos, dni, dia, hora]):
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    nueva_cita = {"nombre": nombre, "apellidos": apellidos, "dni": dni, "dia": dia, "hora": hora}
    citas.append(nueva_cita)
    guardar_citas(citas)

    messagebox.showinfo("Éxito", "Cita añadida correctamente")
    limpiar_campos()

# Visualizar citas
def visualizar_citas():
    ventana_visualizar = tk.Toplevel(ventana)
    ventana_visualizar.title("Citas médicas")
    ventana_visualizar.geometry("400x300")

    if not citas:
        tk.Label(ventana_visualizar, text="No hay citas registradas").pack()
        return

    for cita in citas:
        cita_texto = f"{cita['nombre']} {cita['apellidos']} - DNI: {cita['dni']} - {cita['dia']} a las {cita['hora']}"
        tk.Label(ventana_visualizar, text=cita_texto).pack()

# Eliminar cita
def eliminar_cita():
    dni = entry_dni.get()

    if not dni:
        messagebox.showwarning("Error", "Debe ingresar un DNI")
        return

    global citas
    citas = [cita for cita in citas if cita["dni"] != dni]
    guardar_citas(citas)

    messagebox.showinfo("Éxito", "Cita eliminada correctamente")

# Limpiar campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellidos.delete(0, tk.END)
    entry_dni.delete(0, tk.END)
    entry_dia.delete(0, tk.END)
    entry_hora.delete(0, tk.END)

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de citas médicas")
ventana.geometry("400x400")

# Variables y datos
citas = cargar_citas()

# Widgets de la interfaz
tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Apellidos").pack()
entry_apellidos = tk.Entry(ventana)
entry_apellidos.pack()

tk.Label(ventana, text="DNI").pack()
entry_dni = tk.Entry(ventana)
entry_dni.pack()

tk.Label(ventana, text="Día (dd/mm/yyyy)").pack()
entry_dia = tk.Entry(ventana)
entry_dia.pack()

tk.Label(ventana, text="Hora (HH:MM)").pack()
entry_hora = tk.Entry(ventana)
entry_hora.pack()

# Botones para funciones
tk.Button(ventana, text="Añadir Cita", command=anadir_cita).pack(pady=5)
tk.Button(ventana, text="Visualizar Citas", command=visualizar_citas).pack(pady=5)
tk.Button(ventana, text="Eliminar Cita", command=eliminar_cita).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=5)

ventana.mainloop()

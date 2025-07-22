import tkinter as tk
from tkinter import messagebox
import os
import sys

def obtener_ruta_recurso(nombre_archivo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nombre_archivo)
    return os.path.join(os.path.dirname(__file__), nombre_archivo)

def calcular_comision(bruto):
    return bruto * 0.054 + 0.30

def calcular_neto(bruto):
    return bruto - calcular_comision(bruto)

def calcular_bruto(neto_deseado):
    return (neto_deseado + 0.30) / (1 - 0.054)

# 🔍 Validación de entrada en tiempo real (solo dígitos y punto)
def validar_entrada(valor):
    if valor == "":
        return True
    try:
        float(valor)
        return True
    except ValueError:
        return False

def ejecutar_calculo():
    try:
        monto = float(entrada.get())
        if monto <= 0:
            raise ValueError

        if modo.get() == 1:
            comision = calcular_comision(monto)
            neto = calcular_neto(monto)
            resultado.config(text=f"Monto enviado: ${monto:.2f}\nComisión: ${comision:.2f}\nMonto recibido: ${neto:.2f}")
        else:
            bruto = calcular_bruto(monto)
            comision = calcular_comision(bruto)
            resultado.config(text=f"Monto a recibir deseado: ${monto:.2f}\nDebes enviar: ${bruto:.2f}\nComisión estimada: ${comision:.2f}")

        entrada.delete(0, tk.END)  # 🧼 Limpiar entrada luego de calcular

    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido y positivo.")

# 🎨 Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Comisión PayPal by KingWolfRaudi")
ventana.geometry("450x300")
ventana.resizable(False, False)

# 🖼️ Logotipo
tk.Label(ventana, text="CALCULADORA DE COMISIÓN PAYPAL", font=("Arial", 12, "bold")).pack(pady=10)

# 🎛️ Selector de modo
modo = tk.IntVar(value=1)
frame_opciones = tk.Frame(ventana)
tk.Radiobutton(frame_opciones, text="Desde monto enviado", variable=modo, value=1).pack(side="left", padx=10)
tk.Radiobutton(frame_opciones, text="Desde monto a recibir deseado", variable=modo, value=2).pack(side="left", padx=10)
frame_opciones.pack(pady=5)

# 🔢 Entrada con validación
vcmd = (ventana.register(validar_entrada), "%P")
entrada0 = tk.Label(ventana, text="Ejemplo: 5.20" , font=("Arial", 11), fg="blue")
entrada0.pack(pady=5)
entrada = tk.Entry(ventana, justify="center", font=("Arial", 12), validate="key", validatecommand=vcmd)
entrada.pack(pady=5)

# 🧠 Botón calcular
tk.Button(ventana, text="Calcular", command=ejecutar_calculo, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=10)

# 📋 Resultados
resultado = tk.Label(ventana, text="", font=("Times New Roman", 11), fg="blue")
resultado.pack(pady=10)

# Esto permite ubicar el icono en la misma carpeta que el archivo py
ruta_icono = obtener_ruta_recurso("calc.ico")
    # Asi se declara el icono si tienes un archivo .ico (windows)
ventana.iconbitmap(ruta_icono)

ventana.mainloop()

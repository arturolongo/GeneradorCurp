import re
import tkinter as tk
from tkinter import messagebox

ENTIDADES = {
    'AGUASCALIENTES': 'AS', 'BAJA CALIFORNIA': 'BC', 'BAJA CALIFORNIA SUR': 'BS',
    'CAMPECHE': 'CC', 'CHIAPAS': 'CS', 'CHIHUAHUA': 'CH', 'COAHUILA': 'CL',
    'COLIMA': 'CM', 'CIUDAD DE MÉXICO': 'DF', 'DURANGO': 'DG', 'GUANAJUATO': 'GT',
    'GUERRERO': 'GR', 'HIDALGO': 'HG', 'JALISCO': 'JC', 'MÉXICO': 'MC',
    'MICHOACÁN': 'MN', 'MORELOS': 'MS', 'NAYARIT': 'NT', 'NUEVO LEÓN': 'NL',
    'OAXACA': 'OC', 'PUEBLA': 'PL', 'QUERÉTARO': 'QT', 'QUINTANA ROO': 'QR',
    'SAN LUIS POTOSÍ': 'SP', 'SINALOA': 'SL', 'SONORA': 'SR', 'TABASCO': 'TC',
    'TAMAULIPAS': 'TS', 'TLAXCALA': 'TL', 'VERACRUZ': 'VZ', 'YUCATÁN': 'YN',
    'ZACATECAS': 'ZS'
}

def obtener_primer_vocal(apellido):
    """Devuelve la primera vocal interna de un apellido."""
    for letra in apellido[1:]:
        if letra in "AEIOU":
            return letra
    return 'X'

def obtener_consonante_interna(nombre):
    """Devuelve la primera consonante interna de un nombre."""
    for letra in nombre[1:]:
        if letra in "BCDFGHJKLMNPQRSTVWXYZ":
            return letra
    return 'X'

def generar_curp():
    """Genera la CURP a partir de los datos ingresados en la interfaz."""
    nombre = entrada_nombre.get().strip().upper()
    paterno = entrada_paterno.get().strip().upper()
    materno = entrada_materno.get().strip().upper()
    fecha = entrada_fecha.get().strip()
    sexo = entrada_sexo.get().strip().upper()
    entidad = entrada_entidad.get().strip().upper()

    if not re.match(r'\d{4}-\d{2}-\d{2}', fecha):
        messagebox.showerror("Error", "Fecha inválida. Usa el formato AAAA-MM-DD.")
        return

    anio, mes, dia = fecha.split('-')
    curp = (
        paterno[0] + obtener_primer_vocal(paterno) +
        materno[0] + nombre[0] +
        anio[-2:] + mes + dia +
        sexo +
        ENTIDADES.get(entidad, 'NE') +
        obtener_consonante_interna(paterno) +
        obtener_consonante_interna(materno) +
        obtener_consonante_interna(nombre) +
        '0'
    )

    messagebox.showinfo("CURP Generada", f"Tu CURP es: {curp}")

ventana = tk.Tk()
ventana.title("Generador de CURP")
ventana.geometry("400x400")
ventana.config(bg="#3E065F") 

titulo = tk.Label(ventana, text="Generador de CURP", font=("Josefin Sans", 20), bg="#3E065F", fg="white")
titulo.pack(pady=10)

def crear_entrada(label_text):
    """Crea una etiqueta y entrada centrada."""
    frame = tk.Frame(ventana, bg="#3E065F")
    frame.pack(pady=5)
    etiqueta = tk.Label(frame, text=label_text, font=("Josefin Sans", 12), bg="#3E065F", fg="white")
    etiqueta.pack(side=tk.LEFT)
    entrada = tk.Entry(frame, font=("Josefin Sans", 12))
    entrada.pack(side=tk.RIGHT)
    return entrada

entrada_nombre = crear_entrada("Nombre:")
entrada_paterno = crear_entrada("Apellido Paterno:")
entrada_materno = crear_entrada("Apellido Materno:")
entrada_fecha = crear_entrada("Fecha (AAAA-MM-DD):")
entrada_sexo = crear_entrada("Sexo (H/M):")
entrada_entidad = crear_entrada("Entidad Federativa:")

boton_generar = tk.Button(
    ventana, text="Generar CURP", font=("Josefin Sans", 14),
    bg="#7A0BC0", fg="white", command=generar_curp
)
boton_generar.pack(pady=20)

ventana.mainloop()

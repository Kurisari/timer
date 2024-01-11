import time
from datetime import datetime, timedelta
import winsound
import tkinter as tk
from tkinter import ttk

class Temporizador:
    def __init__(self, root):
        self.valor_predeterminado = "0"
        self.root = root
        self.setup_gui()
    
    def setup_gui(self):
        self.root.title("Temporizador")
        self.root.iconbitmap(r"temp\temporizador.ico")
        self.root.geometry("400x300")
        self.spinbox_hora = tk.StringVar()
        self.spinbox_hora.set(self.valor_predeterminado)
        self.spinbox_minuto = tk.StringVar()
        self.spinbox_minuto.set(self.valor_predeterminado)
        self.spinbox_segundo = tk.StringVar()
        self.spinbox_segundo.set(self.valor_predeterminado)
        self.hora = ttk.Spinbox(self.root, from_=0, to=255, state="readonly", textvariable=self.spinbox_hora)
        self.hora.place(x=30, y=30, width=70)
        self.etiqueta_hora = ttk.Label(self.root, text="Horas")
        self.etiqueta_hora.place(x=30, y=10)
        self.minuto = ttk.Spinbox(self.root, from_=0, to=255, state="readonly", textvariable=self.spinbox_minuto)
        self.minuto.place(x=160, y=30, width=70)
        self.etiqueta_minuto = ttk.Label(self.root, text="Minutos")
        self.etiqueta_minuto.place(x=160, y=10)
        self.segundo = ttk.Spinbox(self.root, from_=0, to=255, state="readonly", textvariable=self.spinbox_segundo)
        self.segundo.place(x=290, y=30, width=70)
        self.etiqueta_segundo = ttk.Label(self.root, text="Segundos")
        self.etiqueta_segundo.place(x=290, y=10)
        self.boton_comenzar = ttk.Button(self.root, text="Comenzar", command=self.iniciar_temporizador)
        self.boton_comenzar.place(x=160, y=100, width=70)
        
        self.etiqueta_tiempo_restante = ttk.Label(self.root, text="Tiempo restante: ")
        self.etiqueta_tiempo_restante.place(x=30, y=150)
        self.etiqueta_tiempo = ttk.Label(self.root, text="")
        self.etiqueta_tiempo.place(x=150, y=150)

    def iniciar_temporizador(self):
        tiempo = self.configurar_temporizador()
        self.actualizar_tiempo(tiempo)

    def actualizar_tiempo(self, tiempo):
        ahora = datetime.now()
        if ahora < tiempo:
            tiempo_restante = tiempo - ahora
            horas, segundos_restantes = divmod(tiempo_restante.seconds, 3600)
            minutos, segundos = divmod(segundos_restantes, 60)
            tiempo_formateado = "{:02}:{:02}:{:02}".format(horas, minutos, segundos)
            self.etiqueta_tiempo.config(text=tiempo_formateado)
            self.root.after(1000, lambda: self.actualizar_tiempo(tiempo))
        else:
            self.reproducir_sonido()
            self.mostrar_mensaje()


    def configurar_temporizador(self):
        horas = int(self.hora.get())
        minutos = int(self.minuto.get())
        segundos = int(self.segundo.get())
        
        tiempo = datetime.now() + timedelta(hours=horas, minutes=minutos, seconds=segundos)
        return tiempo

    def reproducir_sonido(self):
        winsound.Beep(1000, 1000)
        winsound.Beep(1000, 1000)

    def mostrar_mensaje(self):
        print("Tiempo terminado!")

if __name__ == '__main__':
    root = tk.Tk()
    app = Temporizador(root)
    root.mainloop()

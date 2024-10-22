# main.py
import tkinter as tk
from tkinter import messagebox

class ModularCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Modular")

        # Elementos de la interfaz gráfica
        self.label1 = tk.Label(root, text="Número 1:")
        self.label1.pack()

        self.num1 = tk.Entry(root)
        self.num1.pack()

        self.label2 = tk.Label(root, text="Número 2:")
        self.label2.pack()

        self.num2 = tk.Entry(root)
        self.num2.pack()

        self.label_p = tk.Label(root, text="Módulo p (primo):")
        self.label_p.pack()

        self.mod_p = tk.Entry(root)
        self.mod_p.pack()

        # Botones para operaciones
        self.add_button = tk.Button(root, text="Suma", command=self.add)
        self.add_button.pack()

        self.sub_button = tk.Button(root, text="Resta", command=self.subtract)
        self.sub_button.pack()

        self.mul_button = tk.Button(root, text="Multiplicación", command=self.multiply)
        self.mul_button.pack()

        self.div_button = tk.Button(root, text="División", command=self.divide)
        self.div_button.pack()

        self.pow_button = tk.Button(root, text="Potencia", command=self.power)
        self.pow_button.pack()

        self.result_label = tk.Label(root, text="Resultado:")
        self.result_label.pack()

        self.result = tk.Label(root, text="")
        self.result.pack()

    # Función para la suma modular
    def add(self):
        try:
            a = int(self.num1.get())
            b = int(self.num2.get())
            p = int(self.mod_p.get())
            if not self.is_prime(p):
                messagebox.showerror("Error", "p debe ser un número primo")
                return
            result = (a + b) % p
            self.result.config(text=str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada no válida")

    # Función para la resta modular
    def subtract(self):
        try:
            a = int(self.num1.get())
            b = int(self.num2.get())
            p = int(self.mod_p.get())
            if not self.is_prime(p):
                messagebox.showerror("Error", "p debe ser un número primo")
                return
            result = (a - b) % p
            self.result.config(text=str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada no válida")

    # Función para la multiplicación modular
    def multiply(self):
        try:
            a = int(self.num1.get())
            b = int(self.num2.get())
            p = int(self.mod_p.get())
            if not self.is_prime(p):
                messagebox.showerror("Error", "p debe ser un número primo")
                return
            result = (a * b) % p
            self.result.config(text=str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada no válida")

    # Función para la división modular
    def divide(self):
        try:
            a = int(self.num1.get())
            b = int(self.num2.get())
            p = int(self.mod_p.get())
            if not self.is_prime(p):
                messagebox.showerror("Error", "p debe ser un número primo")
                return
            result = (a * self.mod_inverse(b, p)) % p
            self.result.config(text=str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada no válida")
    
    # Función para calcular la potencia modular
    def power(self):
        try:
            a = int(self.num1.get())
            b = int(self.num2.get())
            p = int(self.mod_p.get())
            if not self.is_prime(p):
                messagebox.showerror("Error", "p debe ser un número primo")
                return
            result = pow(a, b, p)
            self.result.config(text=str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada no válida")

    # Función para calcular el inverso modular (usado en la división)
    def mod_inverse(self, b, p):
        return pow(b, p - 2, p)  # Usando el teorema de Fermat

    # Función para verificar si un número es primo
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ModularCalculatorApp(root)
    root.mainloop()

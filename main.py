import streamlit as st
import sympy as sp

# Clase para la calculadora modular basada en expresión
class ModularExpressionCalculatorApp:
    def __init__(self):
        st.title("Calculadora Modular con Expresiones")
        self.expression = st.text_input("Ingresa la expresión (ejemplo: (3*2)/2+(1-3)^2):", value="")
        self.mod_p = st.number_input("Módulo p (primo):", min_value=2, max_value=None, value=2, step=1)
        if st.button("Calcular"):
            self.calculate()

    def calculate(self):
        try:
            expr = self.expression.replace('^', '**')  # Reemplazar ^ con ** para operaciones de potencia
            a, p = sp.sympify(expr), self.mod_p

            if not self.is_prime(p):
                st.error("p debe ser un número primo")
                return

            result = a % p
            st.write(f"Resultado: {result}")
        except (sp.SympifyError, ValueError, ZeroDivisionError):
            st.error("Expresión o entrada no válida")

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Ejecutar la aplicación en Streamlit
if __name__ == "__main__":
    ModularExpressionCalculatorApp()
import math

#----------------------------------------------------
# Clientes
#----------------------------------------------------

# Parámetros del sistema
v0_param = 1.0   # Valor nominal de la moneda
k_param = 0.5    # Factor de ajuste de la depreciación
X0_param = 10    # Parámetro de escala para el saldo (ahora X0=10)

def effective_value(X, v0, k, X0):
    """
    Calcula el valor efectivo de cada moneda dado un saldo X.
    
    Parámetros:
    - X: saldo en la cuenta (número de monedas)
    - v0: valor nominal de la moneda (para saldo bajo)
    - k: factor de ajuste de la depreciación
    - X0: parámetro de escala para el saldo
    
    Retorna:
    - Valor efectivo por moneda.
    """
    return v0 / (1 + k * math.log(1 + X / X0))

# Lista de saldos para evaluar
saldos = [0, 100, 1000, 10000, 100000]

# Imprimir encabezado de la tabla
print("{:<10} {:<20}".format("Saldo (X)", "Valor Efectivo v(X)"))
print("-" * 32)

# Calcular y mostrar el valor efectivo para cada saldo usando los parámetros definidos
for X in saldos:
    v = effective_value(X, v0_param, k_param, X0_param)
    print("{:<10} {:<20.6f}".format(X, v))

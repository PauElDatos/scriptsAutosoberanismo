import math
import random

#----------------------------------------------------
# Productores
#----------------------------------------------------

# Parámetros del sistema
W0 = 0.0     # Riqueza inicial
k = 50.0     # Factor de escala para la recompensa
E0 = 10.0    # Energía base de referencia
beta = 0.1   # Factor que aumenta el coste energético con la riqueza

T0 = 0.1     # Target base para el PoW
gamma = 0.1 # Factor que aumenta la dificultad con la riqueza

# Simulación: en cada ronda, el usuario aporta una cantidad fija de energía
E_input = 100.0  # Energía aportada en cada ronda
num_rounds = 20

# Función de recompensa en función de la energía aportada y la riqueza actual.
def coin_reward(E, W, k, E0, beta):
    """
    Calcula la recompensa (incremento en la riqueza) usando:
    ΔW = k * ln(1 + E / (E0 + beta * W))
    """
    return k * math.log(1 + E / (E0 + beta * W))

# Función que simula el PoW: se requiere encontrar un número aleatorio
# en [0,1) menor que el target, el cual se reduce conforme aumenta W.
def pow_challenge(W, T0, gamma):
    """
    Simula un desafío PoW donde:
    - target = T0 / (1 + gamma * W)
    - Se cuentan los intentos necesarios hasta que un valor aleatorio < target.
    Retorna (número de intentos, target actual).
    """
    target = T0 / (1 + gamma * W)
    attempts = 0
    while True:
        attempts += 1
        # Simula un hash con un valor aleatorio entre 0 y 1
        if random.random() < target:
            break
    return attempts, target

W = W0
print("Ronda |  Riqueza  | Recompensa | Intentos PoW |   Target")
for r in range(1, num_rounds + 1):
    # Calcular la recompensa por aportar energía E_input
    reward = coin_reward(E_input, W, k, E0, beta)
    # Simular el desafío PoW para obtener la recompensa
    attempts, target = pow_challenge(W, T0, gamma)
    # Actualizar la riqueza acumulada
    W += reward
    print(f"{r:5d} | {W:9.2f} | {reward:10.2f} | {attempts:12d} | {target:8.4f}")

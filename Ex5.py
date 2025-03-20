import math
import matplotlib.pyplot as plt
import numpy as np


def get_float_input(message, default_value):
    try:
        return float(input(message))
    except ValueError:
        return default_value


print("Podaj parametry układu. Jeśli chcesz użyć wartości domyślnych - naciśnij Enter.")

# Wartościami domyślne
m_default = 1.0  # masa [kg]
b_default = 3.0  # współczynnik tłumienia [kg/s]
k_default = 1.0  # współczynnik sprężystości [N/m]
F0_default = 1.0  # siła [N]
x0_default = 0.0  # pozycja początkowa [m]
x_dot_0_default = 0.0  # prędkość początkowa [m/s]


m = get_float_input(f"Podaj masę (kg) [domyślnie {m_default}]: ", m_default)
b = get_float_input(f"Podaj współczynnik tłumienia (kg/s) [domyślnie {b_default}]: ", b_default)
k = get_float_input(f"Podaj współczynnik sprężystości (N/m) [domyślnie {k_default}]: ", k_default)
F0 = get_float_input(f"Podaj siłę (N) [domyślnie {F0_default}]: ", F0_default)
x0 = get_float_input(f"Podaj pozycję początkową - x (m) [domyślnie {x0_default}]: ", x0_default)
x_dot_0 = get_float_input(f"Podaj prędkość początkową - x' (m/s) [domyślnie {x_dot_0_default}]: ", x_dot_0_default)

delta = b**2 - 4 * m * k

if delta <= 0:
    print(f"Delta = {delta}.")
    print("Delta jest mniejsza lub równa zeru. Program kończy działanie.")
else:
    lambda_1 = (-b + math.sqrt(delta)) / (2 * m)
    lambda_2 = (-b - math.sqrt(delta)) / (2 * m)

    # Obliczanie rozwiązania ogólnego
    # x(t) = A_1 * exp(lambda_1 * t) + A_2 * exp(lambda_2 * t) + F0/k
    # math.exp(lambda_1 * 0) = math.exp(lambda_2 * 0) = 1
    A_1 = (k * lambda_2 * x0 - k * x_dot_0 - F0 * lambda_2) / (k * lambda_2 - k * lambda_1)
    A_2 = (x_dot_0 - A_1 * lambda_1) / lambda_2



    t_values = np.linspace(0, 10, 1000)  # Zakres czasowy od 0 do 10 sekund
    x_values = A_1 * np.exp(lambda_1 *  t_values) + A_2 * np.exp(lambda_2 *  t_values) + F0/k

    plt.plot(t_values, x_values, label="Pozycja x(t)")
    plt.title("Wykres położenia x(t) w czasie")
    plt.xlabel("Czas (t) [s]")
    plt.ylabel("Pozycja x(t) [m]")
    plt.legend()
    plt.grid(True)
    plt.show()

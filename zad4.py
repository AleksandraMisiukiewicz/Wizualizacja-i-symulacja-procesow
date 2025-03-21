import numpy as np
import matplotlib.pyplot as plt

# Parametry
m0 = 1  # Początkowa masa (można przyjąć 1, bo interesuje nas tylko stosunek)
lambda_ = np.log(2) / 5730  # Współczynnik rozpadu dla C-14 (w jednostkach 1/rok)
czas = np.linspace(0, 20000, 500)  # Czas od 0 do 20000 lat (w roku)

# Obliczanie masy w zależności od czasu
masa = m0 * np.exp(-lambda_ * czas)

# Rysowanie wykresu
plt.plot(czas, masa)
plt.title('Zmiana masy izotopu C-14 w czasie')
plt.xlabel('Czas (lata)')
plt.ylabel('Masa (jednostkowa)')
plt.grid(True)
plt.show()

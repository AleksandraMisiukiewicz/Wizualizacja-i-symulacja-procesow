import numpy as np
import matplotlib.pyplot as plt

# Funkcja obliczająca kąt obrotu robota
def obrot_robota(r, up, ul, czas):
    # Prędkość kątowa robota
    w = (up - ul) / r
    # Kąt obrotu robota w czasie (prosta całka, bo prędkość kątowa jest stała)
    theta = w * czas
    return theta

# Pobieranie danych od użytkownika
r = float(input("Podaj rozstaw kół (r): "))  # w metrach
up = float(input("Podaj prędkość liniową prawego koła (up): "))  # w metrach na sekundę
ul = float(input("Podaj prędkość liniową lewego koła (ul): "))  # w metrach na sekundę

# Czas (od 0 do 10 sekund)
czas = np.linspace(0, 10, 100)

# Obliczanie kąta obrotu robota w czasie
theta = obrot_robota(r, up, ul, czas)

# Wyświetlanie wykresu
plt.plot(czas, theta)
plt.title('Kąt obrotu robota w czasie')
plt.xlabel('Czas (s)')
plt.ylabel('Kąt obrotu (rad)')
plt.grid(True)
plt.show()

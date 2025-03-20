import numpy as np
import matplotlib.pyplot as plt

T = float(input("Podaj stałą czasową T: "))
k = float(input("Podaj wzmocnienie k: "))


t = np.linspace(0, 5*T, 500)


y_step = k * (t - T +T * np.exp(-t / T))
y_impulse = k * (1 - np.exp(-t / T))


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(t, y_step, label="Odpowiedź na skok jednostkowy", color='blue')
plt.xlabel("Czas [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, y_impulse, label="Odpowiedź na impuls Diraca", color='orange')
plt.xlabel("Czas [s]")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
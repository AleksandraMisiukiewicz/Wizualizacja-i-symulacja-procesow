import matplotlib.pyplot as plt
import numpy as np


x_start = float(input("Podaj początek przedziału x: "))
x_end = float(input("Podaj koniec przedziału x: "))
x = np.linspace(x_start, x_end, 1000)

_,ax = plt.subplots(figsize=(10, 5))

plot_x = input("Czy chcesz wyświetlić funkcję y=x? (y/n): ")
if plot_x.lower() == "y":
    color = input("Podaj kolor wykresu (np. 'red', 'blue', 'green'): ")
    ax.plot(x, x, color=color, label='y=x')

plot_sin = input("Czy chcesz wyświetlić funkcję y=sin(x)? (y/n): ")
if plot_sin.lower() == "y":
    color = input("Podaj kolor wykresu (np. 'red', 'blue', 'green'): ")
    ax.plot(x, np.sin(x), color=color, label='y=sin(x)', linestyle='--')

plot_cos = input("Czy chcesz wyświetlić funkcję y=cos(x)? (y/n): ")
if plot_cos.lower() == "y":
    color = input("Podaj kolor wykresu (np. 'red', 'blue', 'green'): ")
    ax.plot(x, np.cos(x), color=color, label='y=cos(x)', linestyle='-.')

plotx3 = input("Czy chcesz wyświetlić funkcję y=x³? (y/n): ")
if plotx3.lower() == "y":
    color = input("Podaj kolor wykresu (np. 'red', 'blue', 'green'): ")
    ax.plot(x, x**3, color=color, label='y=x³', linestyle=':')


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("Wykres funkcji")


ax.legend()


plt.show()
import numpy as np
import matplotlib.pyplot as plt


def simulate_robot_motion(phases, T, total_time):
    x1, x2, x3 = 0, 0, 0  # Początkowa pozycja i orientacja

    trajectory = [(x1, x2)]

    time = 0
    while time < total_time:
        for phase in phases:
            w1, w2, duration = phase
            steps = int(duration / T)

            for _ in range(steps):
                x1_new = x1 + T * w1 * np.cos(x3)
                x2_new = x2 + T * w1 * np.sin(x3)
                x3_new = x3 + T * w2

                x1, x2, x3 = x1_new, x2_new, x3_new
                trajectory.append((x1, x2))

                time += T
                if time >= total_time:
                    break

    return np.array(trajectory)


def plot_trajectory(trajectory, title="Robot trajectory"):
    plt.figure(figsize=(8, 6))
    plt.plot(trajectory[:, 0], trajectory[:, 1], marker='o', linestyle='-', markersize=3)
    plt.xlabel("x1 (position X)")
    plt.ylabel("x2 (position Y)")
    plt.title(title)
    plt.grid()
    plt.show()

T = float(input("Podaj krok dyskretyzacji (np. 0.1): "))
total_time = float(input("Podaj całkowity czas symulacji: "))
num_phases = int(input("Podaj liczbę faz ruchu: "))
phases = []
for i in range(num_phases):
    w1 = float(input(f"Podaj prędkość liniową dla fazy {i + 1}: "))
    w2 = float(input(f"Podaj prędkość obrotową dla fazy {i + 1}: "))
    duration = float(input(f"Podaj czas trwania fazy {i + 1}: "))
    phases.append((w1, w2, duration))

# Symulacja i wykres
trajectory = simulate_robot_motion(phases, T, total_time)
plot_trajectory(trajectory, "User-defined Motion")

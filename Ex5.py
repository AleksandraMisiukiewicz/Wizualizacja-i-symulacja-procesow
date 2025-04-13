import numpy as np
import matplotlib.pyplot as plt


def robot_dynamics(x1, x2, x3, w1, w2):
    dx1 = w1 * np.cos(x3)
    dx2 = w1 * np.sin(x3)
    dx3 = w2
    return np.array([dx1, dx2, dx3])


def rk2_step(x1, x2, x3, w1, w2, T):
    k1 = robot_dynamics(x1, x2, x3, w1, w2)
    k2 = robot_dynamics(x1 + T * k1[0] / 2, x2 + T * k1[1] / 2, x3 + T * k1[2] / 2, w1, w2)
    return np.array([x1, x2, x3]) + T * k2


def rk4_step(x1, x2, x3, w1, w2, T):
    k1 = robot_dynamics(x1, x2, x3, w1, w2)
    k2 = robot_dynamics(x1 + T * k1[0] / 2, x2 + T * k1[1] / 2, x3 + T * k1[2] / 2, w1, w2)
    k3 = robot_dynamics(x1 + T * k2[0] / 2, x2 + T * k2[1] / 2, x3 + T * k2[2] / 2, w1, w2)
    k4 = robot_dynamics(x1 + T * k3[0], x2 + T * k3[1], x3 + T * k3[2], w1, w2)
    return np.array([x1, x2, x3]) + T * (k1 + 2 * k2 + 2 * k3 + k4) / 6


def simulate_robot_motion_rk(phases, T, total_time, method):
    x1, x2, x3 = 0, 0, 0  # Początkowa pozycja i orientacja
    trajectory = [(x1, x2)]
    time = 0
    while time < total_time:
        for w1, w2, duration in phases:
            steps = int(duration / T)
            for _ in range(steps):
                if method == 'rk2':
                    x1, x2, x3 = rk2_step(x1, x2, x3, w1, w2, T)
                elif method == 'rk4':
                    x1, x2, x3 = rk4_step(x1, x2, x3, w1, w2, T)
                trajectory.append((x1, x2))
                time += T
                if time >= total_time:
                    break
    return np.array(trajectory)

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


def plot_trajectories(trajectory_rk2, trajectory_rk4):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].plot(trajectory_rk2[:, 0], trajectory_rk2[:, 1], marker='o', linestyle='-', markersize=3)
    axs[0].set_xlabel("x1 (position X)")
    axs[0].set_ylabel("x2 (position Y)")
    axs[0].set_title("Trajectory using RK-2")
    axs[0].grid()

    axs[1].plot(trajectory_rk4[:, 0], trajectory_rk4[:, 1], marker='o', linestyle='-', markersize=3)
    axs[1].set_xlabel("x1 (position X)")
    axs[1].set_ylabel("x2 (position Y)")
    axs[1].set_title("Trajectory using RK-4")
    axs[1].grid()

    plt.show()

def plot_all_trajectories(trajectory, trajectory_rk2, trajectory_rk4):
    plt.figure(figsize=(8, 6))
    plt.plot(trajectory[:, 0], trajectory[:, 1], color="black", marker='o', linestyle='-', markersize=3,
             label='Original')
    plt.plot(trajectory_rk2[:, 0], trajectory_rk2[:, 1], color="blue", marker='o', linestyle='-', markersize=3,
             label='RK2')
    plt.plot(trajectory_rk4[:, 0], trajectory_rk4[:, 1], color="red", marker='o', linestyle='-', markersize=3,
             label='RK4')
    plt.xlabel("x1 (position X)")
    plt.ylabel("x2 (position Y)")
    plt.title("Method comparison")
    plt.grid()
    plt.legend()
    plt.show()

T = float(input("Podaj krok dyskretyzacji (np. 0.1): "))
num_phases = int(input("Podaj liczbę faz ruchu: "))
phases = []
total_time = 0
for i in range(num_phases):
    w1 = float(input(f"Podaj prędkość liniową dla fazy {i + 1}: "))
    w2 = float(input(f"Podaj prędkość obrotową dla fazy {i + 1}: "))
    duration = float(input(f"Podaj czas trwania fazy {i + 1}: "))
    phases.append((w1, w2, duration))
    total_time += duration

trajectory_rk2 = simulate_robot_motion_rk(phases, T, total_time, 'rk2')
trajectory_rk4 = simulate_robot_motion_rk(phases, T, total_time, 'rk4')
plot_trajectories(trajectory_rk2, trajectory_rk4)
trajectory = simulate_robot_motion(phases, T, total_time)
plot_all_trajectories(trajectory, trajectory_rk2, trajectory_rk4)
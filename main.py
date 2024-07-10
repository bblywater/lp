import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Scale

a = 1
b = 1
n = 3
phi = np.pi / 4

theta = np.linspace(0, 2 * np.pi, 1000)

def compute_xy(a, b, n, phi, theta):
    x = a * np.sin(theta)
    y = b * np.sin(n * theta + phi)
    return x, y

x, y = compute_xy(a, b, n, phi, theta)

root = tk.Tk()
root.title("Lissajous and Sinusoidal Waves with Moving Points")

def on_closing():
    root.quit()
    root.destroy() 

root.protocol("WM_DELETE_WINDOW", on_closing)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
fig.suptitle('Lissajous and Sinusoidal Waves with Moving Points', fontsize=16)

ax1 = axs[0, 0]
line1, = ax1.plot([], [], color='green')
point1, = ax1.plot([], [], 'ro')
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 1.5)
ax1.set_title('Lissajous figure')
ax1.set_aspect('equal')

ax2 = axs[0, 1]
line2, = ax2.plot([], [], color='red')
point2, = ax2.plot([], [], 'ro')
ax2.set_xlim(0, 2 * np.pi)
ax2.set_ylim(-1.5, 1.5)
ax2.set_title('Sinusoidal Wave (y = b*sin(n*theta + phi))')

ax3 = axs[1, 0]
line3, = ax3.plot([], [], color='blue')
point3, = ax3.plot([], [], 'ro')
ax3.set_xlim(-1.5, 1.5)
ax3.set_ylim(0, 2 * np.pi)
ax3.set_title('Sinusoidal Wave (x = a*sin(theta))')
ax3.invert_yaxis()

axs[1, 1].remove()

def update_plot(val):
    a = a_slider.get()
    b = b_slider.get()
    n = n_slider.get()
    phi = phi_slider.get()

    global x, y
    x, y = compute_xy(a, b, n, phi, theta)

    ax1.set_xlim(-1.1 * a, 1.1 * a)
    ax1.set_ylim(-1.1 * b, 1.1 * b)
    ax2.set_ylim(-1.1 * b, 1.1 * b)
    ax3.set_xlim(-1.1 * a, 1.1 * a)

    canvas.draw()

a_slider = Scale(root, from_=0.1, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, label="a", command=update_plot)
a_slider.set(a)
a_slider.pack()

b_slider = Scale(root, from_=0.1, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, label="b", command=update_plot)
b_slider.set(b)
b_slider.pack()

n_slider = Scale(root, from_=1, to=10, resolution=0.1, orient=tk.HORIZONTAL, label="n", command=update_plot)
n_slider.set(n)
n_slider.pack()

phi_slider = Scale(root, from_=0, to=2*np.pi, resolution=0.1, orient=tk.HORIZONTAL, label="phi", command=update_plot)
phi_slider.set(phi)
phi_slider.pack()

def init():
    line1.set_data([], [])
    point1.set_data([], [])
    line2.set_data([], [])
    point2.set_data([], [])
    line3.set_data([], [])
    point3.set_data([], [])
    return line1, point1, line2, point2, line3, point3

def animate(i):
    i = i % len(theta)

    line1.set_data(x[:i], y[:i])
    point1.set_data([x[i]], [y[i]]) 
    line2.set_data(theta[:i], y[:i])
    point2.set_data([theta[i]], [y[i]]) 
    line3.set_data(x[:i], theta[:i])
    point3.set_data([x[i]], [theta[i]])
    
    return line1, point1, line2, point2, line3, point3

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(theta), interval=20, blit=True)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()

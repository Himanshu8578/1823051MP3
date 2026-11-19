
import numpy as np
import matplotlib.pyplot as plt
import math

L = 1
N = int(input("Enter number of points: "))

x = np.linspace(0, L, N)
h = x[1] - x[0]

A = np.zeros((N-1, N-1))
B = np.zeros(N-1)

for i in range(N-2):
    A[i, i] = -2 - h**2

    if i > 0:
        A[i, i-1] = 1

    A[i, i+1] = 1

B[0] = -1

A[-1, -1] = -2 - h**2
A[-1, -2] = 2

y = np.zeros(N)
y[0] = 1

y[1:] = np.linalg.solve(A, B)

print("Steady State Concentration:")
for i in range(N):
    print("x =", round(x[i], 3),
          "y =", round(y[i], 5))

plt.plot(x, y, 'o-')
plt.xlabel("Position x")
plt.ylabel("Concentration y(x)")
plt.title("Reaction-Diffusion Problem")
plt.grid()
plt.show()

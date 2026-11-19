
import numpy as np
import matplotlib.pyplot as plt
import math

L = float(input("Enter length of bar: "))
T0 = float(input("Enter temperature at left end: "))
TL = float(input("Enter temperature at right end: "))
N = int(input("Enter number of points: "))

x = np.linspace(0, L, N)
h = x[1] - x[0]

A = np.zeros((N-2, N-2))
B = np.zeros(N-2)

for i in range(N-2):
    A[i, i] = -2

    if i > 0:
        A[i, i-1] = 1

    if i < N-3:
        A[i, i+1] = 1

B[0] = -T0
B[-1] = -TL

T = np.zeros(N)
T[0] = T0
T[-1] = TL

T[1:-1] = np.linalg.solve(A, B)

print("Equilibrium Temperature:")
for i in range(N):
    print("x =", round(x[i], 3),
          "Temperature =", round(T[i], 3))

plt.plot(x, T, 'o-')
plt.xlabel("Length of Bar")
plt.ylabel("Temperature")
plt.title("Equilibrium Temperature of a Bar")
plt.grid()
plt.show()

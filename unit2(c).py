
import numpy as np
import matplotlib.pyplot as plt
import math

def f(t):
    if t >= 1:
        return 0
    x = t/(1-t)
    return math.exp(-x)/(1-t)**2

exact = 1.0

N = [4, 8, 16, 32, 64, 128]

error_nc = []
error_gauss = []

print("N       Newton Cotes       Gauss Quadrature")

for n in N:

    x = np.linspace(0, 1, n+1)
    y = np.array([f(i) for i in x])

    h = 1/n
    I1 = h*(y[0]/2 + sum(y[1:-1]) + y[-1]/2)

    error_nc.append(abs(exact-I1))

    z, w = np.polynomial.legendre.leggauss(n)
    z = (z+1)/2

    I2 = 0

    for i in range(n):
        I2 += w[i]*f(z[i])

    I2 = I2/2

    error_gauss.append(abs(exact-I2))

    print(n, "   ", round(I1, 8), "       ", round(I2, 8))

plt.plot(N, error_nc, 'o-', label="Newton Cotes")
plt.plot(N, error_gauss, 's-', label="Gauss Quadrature")

plt.xlabel("Number of Points")
plt.ylabel("Absolute Error")
plt.title("Comparison of Convergence")
plt.yscale("log")
plt.legend()
plt.grid()
plt.show()


import numpy as np
import matplotlib.pyplot as plt
import math

n = int(input("Enter number of points (2 or 3): "))

if n == 2:
    x1 = [0.585786, 3.414214]
    w1 = [0.853553, 0.146447]

    x2 = [-0.707107, 0.707107]
    w2 = [0.886227, 0.886227]

elif n == 3:
    x1 = [0.415775, 2.294280, 6.289945]
    w1 = [0.711093, 0.278518, 0.010389]

    x2 = [-1.224745, 0, 1.224745]
    w2 = [0.295409, 1.181636, 0.295409]

else:
    print("Enter only 2 or 3")
    exit()

I1 = 0
for i in range(n):
    I1 += w1[i] * x1[i]

I2 = 0
for i in range(n):
    I2 += w2[i] * x2[i]**2

print("Gauss Laguerre Integral =", I1)
print("Analytical Value =", 1)

print("Gauss Hermite Integral =", I2)
print("Analytical Value =", math.sqrt(math.pi)/2)

plt.figure(figsize=(10, 4))

x = np.linspace(0, 8, 100)
plt.subplot(1, 2, 1)
plt.plot(x, x*np.exp(-x))
plt.title("Gauss Laguerre")
plt.xlabel("x")
plt.ylabel("x exp(-x)")
plt.grid()

x = np.linspace(-4, 4, 100)
plt.subplot(1, 2, 2)
plt.plot(x, x**2*np.exp(-x**2))
plt.title("Gauss Hermite")
plt.xlabel("x")
plt.ylabel("x² exp(-x²)")
plt.grid()

plt.tight_layout()
plt.show()

import random
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import least_squares
from scipy.optimize import minimize
from scipy.optimize import differential_evolution
from scipy.optimize import dual_annealing

x_k = []
y_k = []

for i in range(0, 1001):
	d = np.random.normal(0, 1)
	temp_x = 3 * i / 1000
	fx = 1 / (temp_x**2 - 3 * temp_x + 2)
	temp_y = fx + d if abs(fx) <= 100 else 100 + d if fx > 100 else -100 + d
	x_k.append(temp_x)
	y_k.append(temp_y)

x_k = np.array(x_k)
y_k = np.array(y_k)

def f(x, a, b, c, d):
	return (a * x + b) / (x**2 + c * x + d)

def D(params):
	global x_k, y_k

	a, b, c, d = params

	return np.sum((f(x_k, a, b, c ,d) - y_k)**2)

def D_lm(params):
	global x_k, y_k

	a, b, c, d = params

	return f(x_k, a, b, c, d) - y_k

nm = minimize(D, [0, 0, 0, 0], method="Nelder-Mead", tol=0.001)

lm = least_squares(D_lm, [1, 1, 1, 1], method="lm", xtol=0.001, ftol=0.001)

de = differential_evolution(D, [(0, 1), (0, 1), (0, 1), (0, 1)], x0=[1, 1, 1, 1], tol=0.001, maxiter=1000)

da = dual_annealing(D, [(0, 1), (0, 1), (0, 1), (0, 1)], x0=[1, 1, 1, 1], maxiter=1000)

print("NELDER-MEAD")
print("Number of iterations: " + str(nm.nit))
print("Number of function calls: " + str(nm.nfev))
print("LM")
print("Number of function calls: " + str(lm.nfev))
print("DE")
print("Number of iterations: " + str(de.nit))
print("Number of function calls: " + str(de.nfev))
print("DA")
print("Number of iterations: " + str(da.nit))
print("Number of function calls: " + str(da.nfev))

plt.title("Rational approximant")
plt.scatter(x_k, y_k, label="Generated data", color='blue')
plt.plot(x_k, (nm.x[0] * x_k + nm.x[1]) / (x_k**2 + nm.x[2] * x_k + nm.x[3]), label="Nelder-Mead", color='red')
plt.plot(x_k, (lm.x[0] * x_k + lm.x[1]) / (x_k**2 + lm.x[2] * x_k + lm.x[3]), label="Levenberg-Marquardt method", color='green')
plt.plot(x_k, (de.x[0] * x_k + de.x[1]) / (x_k**2 + de.x[2] * x_k + de.x[3]), label="Differential evolution", color='purple')
plt.plot(x_k, (de.x[0] * x_k + de.x[1]) / (x_k**2 + de.x[2] * x_k + de.x[3]), label="Simulated annealing", color='yellow')
plt.grid()
plt.legend()
plt.show()
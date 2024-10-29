def newton_raphson(f, f_prime, x0, tol=1e-7, max_iter=1000): 
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_prime(x)
        x -= fx / fpx

f = lambda x: x**2 - 1
f_prime = lambda x: 2 * x


x0 = 0.7
root = newton_raphson(f, f_prime, x0)
print(f"{root}")
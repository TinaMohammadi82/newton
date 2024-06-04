x = [0, 1, 8, 27]
f = [0, 1, 2, 3 ]

xi = float(input(" Enter point: "))
n = len(x)

for j in range(1, n):
    for k in range(n - 1, j - 1, -1):
        f[k] = (f[k] - f[k - 1]) / (x[k] - x[k - j])

f_int = f[-1]
for l in range(n - 2, -1, -1):
    f_int = f_int * (xi - x[l]) + f[l]

print(" Result {x} is {y}.".format(x=xi, f=f_int))

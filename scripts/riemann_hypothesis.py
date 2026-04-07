from math import gcd

h = m = p = 0
d = f0 = f3 = n = q = 1
iteration = 0  # 记录迭代次数

while p**2 * (m - f0) < f3:
    d = 2 * n * d - 4 * (-1)**n * h
    n += 1
    g = gcd(n, q)
    q = n * q // g
    if g == 1:
        p += 1
    m = 0
    g = q
    while g > 1:
        g = g // 2
        m += d
    h = f0
    f0 = 2 * n * h
    f3 = (2 * n + 3) * f3

    # 每 10000 次迭代输出一次状态
    if iteration % 10000 == 0:
        print(f"Iteration: {iteration}, n: {n}, p: {p}, m: {m}, f0: {f0}, f3: {f3}")

# 如果程序运行到这里，说明黎曼猜想不成立！
print("程序已停机！黎曼猜想为假！")

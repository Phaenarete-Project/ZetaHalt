"""
极简马蒂亚谢维奇29寄存器机
输入: max_iter (最大迭代次数)
处理: 模拟机器运行，检测r是否变为负数
输出: 每次迭代的关键状态 (n, p, d, r)
"""

import math

def riemann_test(max_iter: int):
    # 初始化所有寄存器
    d = m = p = 0
    f0 = f1 = f3 = n = q = r = 1
    b = True

    for i in range(max_iter):
        # 核心指令序列
        d *= 2 * n
        d += -f1 if (b := not b) else f1
        n += 1

        g = math.gcd(n, q)
        q = (n * q) // g
        if g == 1:
            p += 1

        m = 0
        q2 = q
        while q2 > 1:
            q2 //= 2
            m += d

        f1 = 2 * f0
        f0 *= 2 * n
        f3 *= (2 * n + 3)

        r = f3 - p * p * (m - f0)

        # 输出：每1000步打印一次，避免刷屏
        if i % 1000 == 0:
            print(f"i={i:6d}, n={n:6d}, p={p:6d}, d={d:15d}, r={r:.6e}")

        # 停机条件：若r为负，立即停止
        if r < 0:
            print(f"\n程序停止于迭代 {i}: n={n}, p={p}, r={r}")
            return

    print(f"\n完成 {max_iter} 次迭代，未检测到停机。")

if __name__ == "__main__":
    # 输入：最大迭代次数（可根据需要调整）
    riemann_test(100000)
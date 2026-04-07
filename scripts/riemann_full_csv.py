"""
马蒂亚谢维奇29寄存器机 - 全状态记录到CSV
用于机器学习分析，寻找状态不变量
"""

import math
import csv

def run_riemann_full_csv(max_iter: int, csv_filename: str):
    """
    运行马氏寄存器机，将所有迭代的状态记录到CSV文件。

    参数:
        max_iter: 最大迭代步数（建议 50~200，数值会快速爆炸）
        csv_filename: 输出的CSV文件名
    """
    # 初始化所有寄存器（完全按照原始定义）
    d = 0          # 整数
    m = 0
    p = 0
    f0 = 1
    f1 = 1
    f3 = 1
    n = 1
    q = 1
    r = 1
    b = True

    # 打开CSV文件，写入列头
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # 定义列名（所有我们需要分析的状态）
        header = ['iter', 'n', 'p', 'd', 'm', 'f0', 'f1', 'f3', 'q', 'r', 'b']
        writer.writerow(header)

        for i in range(max_iter):
            # 记录当前迭代开始时的状态（也可以记录结束后的状态，这里记录更新前的状态）
            # 注意：第一次迭代时，n=1, p=0, d=0, ...
            writer.writerow([i, n, p, d, m, f0, f1, f3, q, r, int(b)])

            # 执行一条核心指令块（对应130条汇编指令）
            # 1. 更新 d
            d *= 2 * n
            if b:
                d += f1
            else:
                d -= f1
            b = not b   # 翻转标志

            # 2. n 递增
            n += 1

            # 3. 更新 q = lcm(1..n) 和素数计数 p
            g = math.gcd(n, q)
            q = (n * q) // g
            if g == 1:   # n是素数（或1，但n>=2）
                p += 1

            # 4. 计算 m = d * floor(log2(q))
            m_val = 0
            q2 = q
            while q2 > 1:
                q2 //= 2
                m_val += d
            m = m_val

            # 5. 更新阶乘变量
            f1 = 2 * f0
            f0 *= 2 * n
            f3 *= (2 * n + 3)

            # 6. 计算终止条件 r
            r = f3 - p * p * (m - f0)

            # 可选：如果 r < 0，记录最后状态并提前终止
            if r < 0:
                # 记录停止前的最后状态（此时迭代索引 i+1）
                writer.writerow([i+1, n, p, d, m, f0, f1, f3, q, r, int(b)])
                print(f"程序停机于迭代 {i+1}: n={n}, r={r}")
                break

        # 循环正常结束
        print(f"运行完成，共 {i+1} 次迭代，状态已保存到 {csv_filename}")

if __name__ == "__main__":
    # 可根据需要调整最大迭代次数（建议先小规模测试，如 50）
    run_riemann_full_csv(max_iter=100, csv_filename="riemann_states.csv")
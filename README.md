# ZetaHalt

黎曼猜想 ↔ 寄存器机停机问题的 Transformer 预测与不变量发现

## 核心等价性

Matiyasevich（2020）证明：黎曼猜想为真当且仅当一台显式给出的 29 寄存器机永不停机。

## 典故说明

ZetaHalt 融合 “Zeta”（黎曼 ζ 函数）与 “Halt”（停机问题），致敬：

- Matiyasevich 将黎曼猜想与寄存器机永不停机等价化
- Turing 提出停机问题，并在早期计算实践中推动了对 RH 零点的数值验证
- ZetaGrid 等分布式计算项目在临界线零点计算与验证方面的集体贡献
- 所有在临界线计算与零点验证中做出贡献的数学家

## 当前内容

- 原始论文 PDF：`papers/matiyasevich2020riemann.pdf`
- 整数版模拟脚本（可运行至 n=100）：`scripts/riemann_full_csv.py`
- 状态数据 CSV（n=1…100，r 始终为正）：`data/raw/riemann_states.csv`
- Lean 形式化代码（寄存器机）：[lean/MatiyasevichRHRegisterMachine.lean](lean/MatiyasevichRHRegisterMachine.lean)

其他已整理的历史脚本也位于 `scripts/` 目录下，供复现与对照使用。

## 如何运行

```bash
python scripts/riemann_full_csv.py --max-n 100
```

## 引用格式（BibTeX）

```bibtex
@article{Matiyasevich_2020,
  title = {The Riemann Hypothesis in computer science},
  author = {Matiyasevich, Yu.},
  journal = {Theoretical Computer Science},
  volume = {807},
  pages = {257--265},
  year = {2020},
  month = feb,
  doi = {10.1016/j.tcs.2019.07.028},
  url = {http://dx.doi.org/10.1016/j.tcs.2019.07.028},
  publisher = {Elsevier BV},
  language = {en}
}
```

## 空目录说明

以下目录为未来实验预留，目前不包含实现，仅用于保持标准化项目结构：

- `src/machine`（未来放模拟器）
- `src/model`（未来放 Transformer）
- `src/explain`（未来放可解释性工具）
- `data/processed`（未来放 Parquet 等派生数据）
- `notebooks`、`tests`、`.github/workflows`

为便于 Git 跟踪，空目录使用 `.gitkeep` 占位文件保留。

## 许可证

MIT License（见 `LICENSE`）。

-- 寄存器机状态类型
structure RiemannState where
  d  : Nat
  m  : Nat
  p  : Nat
  f0 : Nat
  f1 : Nat
  f3 : Nat
  n  : Nat
  q  : Nat
  r  : Int          -- 判别量可能为负，使用整数
  b  : Bool         -- 符号标志
  deriving Repr, Inhabited

-- 初始状态
def initialState : RiemannState where
  d  := 0
  m  := 0
  p  := 0
  f0 := 1
  f1 := 1
  f3 := 1
  n  := 1
  q  := 1
  r  := 1
  b  := true

-- 自定义 lcm 函数
def myLcm (a b : Nat) : Nat :=
  if a = 0 || b = 0 then 0
  else (a * b) / Nat.gcd a b

-- 手动实现 floor(log₂ x)
def log2Floor (x : Nat) : Nat :=
  if x ≤ 1 then 0
  else
    let rec loop (val : Nat) (acc : Nat) : Nat :=
      if val ≤ 1 then acc
      else loop (val / 2) (acc + 1)
    loop x 0

-- 单步状态转移
def step (s : RiemannState) : RiemannState :=
  let n := s.n
  -- 1. 更新 d：务必转换为 Int 再进行减法，避免 Neg Nat 错误
  let dInt := (s.d : Int) * (2 * n) + (if s.b then (s.f1 : Int) else -(s.f1 : Int))
  let dNew := if dInt ≥ 0 then dInt.toNat else 0   -- 实际永不为负

  -- 2. 翻转标志
  let bNew := !s.b

  -- 3. n 递增
  let nNew := n + 1

  -- 4. 更新 q 和 p
  let qNew := myLcm s.q nNew
  let pNew := if Nat.gcd s.q nNew = 1 then s.p + 1 else s.p

  -- 5. 计算 m = dNew * floor(log₂ qNew)
  let log2q := log2Floor qNew
  let mNew := dNew * log2q

  -- 6. 更新阶乘变量
  let f1New := 2 * s.f0
  let f0New := s.f0 * (2 * nNew)
  let f3New := s.f3 * (2 * nNew + 3)

  -- 7. 计算判别量 r
  let rNew := (f3New : Int) - (pNew : Int)^2 * ((mNew : Int) - (f0New : Int))

  { d  := dNew,
    m  := mNew,
    p  := pNew,
    f0 := f0New,
    f1 := f1New,
    f3 := f3New,
    n  := nNew,
    q  := qNew,
    r  := rNew,
    b  := bNew }

-- 模拟前 maxSteps 步，返回状态列表（含初始状态）
def simulate (maxSteps : Nat) : List RiemannState :=
  let rec loop (s : RiemannState) (stepsLeft : Nat) : List RiemannState :=
    if stepsLeft = 0 then [s]
    else s :: loop (step s) (stepsLeft - 1)
  loop initialState maxSteps

-- 检查是否有反例（r < 0）
def foundCounterexample (states : List RiemannState) : Bool :=
  states.any (fun s => s.r < 0)

-- 打印前 n 步状态
def showFirstN (n : Nat) : IO Unit := do
  let states := simulate n
  for s in states do
    IO.println s!"n={s.n}, p={s.p}, d={s.d}, m={s.m}, f0={s.f0}, f1={s.f1}, f3={s.f3}, q={s.q}, r={s.r}"

-- 运行前 10 步
#eval showFirstN 1
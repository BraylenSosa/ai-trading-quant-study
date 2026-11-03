import pandas as pd

df = pd.read_csv("csi300.csv", parse_dates=["date"]).set_index("date").sort_index()

# ① 形状:多少行、多少列
print("① 形状:", df.shape)

# ② 缺失值:每列有多少空洞
print("② 缺失值:\n", df.isna().sum())

# ③ 重复:同一天出现两次?
print("③ 重复日期:", df.index.duplicated().sum())

# ④ 日期间隔:相邻两根K线隔了几天
gap = df.index.to_series().diff().dt.days
print("④ 最大间隔:", gap.max(), "天,出现在", gap.idxmax().date())

# ⑤ 极端涨跌:单日涨跌超过6%的日子
ret = df["close"].pct_change()
big = ret[ret.abs() > 0.06]
print("⑤ 单日涨跌>6%:", len(big), "天;最猛一天:",
      big.abs().idxmax().date(), round(big[big.abs().idxmax()] * 100, 2), "%")

# ⑥ 可疑的零:成交量为0的天数
zero = df[df["volume"] == 0]
print("⑥ 零成交量:", len(zero), "天",
      "" if zero.empty else f"({zero.index.min().date()} → {zero.index.max().date()})")
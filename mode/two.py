import akshare as ak
import pandas as pd

# 拉取沪深300指数全部日线(新浪源)
# df = ak.stock_zh_index_daily(symbol="sh000300")
# df["date"] = pd.to_datetime(df["date"])
# df = df.set_index("date").sort_index()
#
# print(df.shape)        # 行数、列数
# print(df.tail(3))      # 最近 3 天
# df.to_csv("csi300.csv")  # 存下来,后面几节都用它


# 前复权(qfq)与不复权(空字符串)各拉一份
adj = ak.stock_zh_a_daily(symbol="sz000001", start_date="20200101",
                          end_date="20260729", adjust="qfq")
raw = ak.stock_zh_a_daily(symbol="sz000001", start_date="20200101",
                          end_date="20260729", adjust="hfq")
raw = ak.stock_zh_a_daily(symbol="sz000001", start_date="20200101",
                          end_date="20260729", adjust="")

print("前复权 2020-01-02 收盘:", round(float(adj.iloc[0]["close"]), 2))
print("后复权 2020-01-02 收盘:", round(float(adj.iloc[0]["close"]), 2))
print("不复权 2020-01-02 收盘:", round(float(raw.iloc[0]["close"]), 2))
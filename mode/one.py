import sys
import akshare as ak
import pandas as pd
import mplfinance
import backtrader as bt

print("Python:", sys.version.split()[0])
print("akshare:", ak.__version__)
print("pandas:", pd.__version__)
print("backtrader:", bt.__version__)
print("✅ 工作台就绪")


def func_test(a, *, b, c: str | None = "bb"):
    print(c)
    return 1


print(func_test(1, b=1))

import pandas as pd

data = pd.read_csv("/data/snp500_ohlcv.csv")
sym = set(data.symbol.to_list())
print(len(sym))
for s in sym:
    print(s)
    output = data[data.symbol == s]
    output.to_csv("/home/pthnhan/Desktop/khtn/ds_khtn_kr/data/{}.csv".format(s), index=False)

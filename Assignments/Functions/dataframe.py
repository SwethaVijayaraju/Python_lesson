import pandas as pd

ser = pd.Series([1, 2, 4, 56, 46, 57])
print(ser)
mod = ser.apply(lambda x: x ** 2)
print(mod)
mod = ser.apply(lambda x: x ** 2).where(lambda x: x < 100).dropna()
print(mod)
whe = ser.where(lambda x: x < 10)
print(whe)
whe = ser.where(lambda x: x < 10).dropna()
print(whe)

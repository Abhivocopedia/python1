import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl

df=pd.read_csv("data.csv")
months = df['Month'].to_numpy()
mm = df['Rainfall_mm'].to_numpy()

mpl.figure(figsize=(10,10))
mpl.bar(months,mm)
mpl.grid(axis='y',linestyle='--',alpha=0.4)
mpl.xticks(rotation=90)
mpl.show()

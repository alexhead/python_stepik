import csv
import re
import pandas as pd
from pathlib import Path

def read_them_all(files, **kwargs):
    return pd.concat([pd.read_csv(f, **kwargs) for f in files], ignore_index=True)

p = Path(r'../files')

phones = [2383482]
df = read_them_all(p.glob('Crimes.csv'))
print(df.query("A in @phones"))

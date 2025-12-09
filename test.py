import pandas as pd
import json

with open("data/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame([data])

print(df.head())
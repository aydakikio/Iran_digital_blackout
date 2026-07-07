import pandas as pd

df = pd.read_csv('data.csv', encoding='utf-8')

col = 'sender_name'

df[col] = df[col].astype(str).str.split('،', n=1).str[1].str.strip()

df.to_csv('data_raw.csv', index=False, encoding='utf-8')
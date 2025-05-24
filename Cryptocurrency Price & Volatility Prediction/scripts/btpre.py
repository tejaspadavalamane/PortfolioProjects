import pandas as pd
input_file_path = 'BTCUSDT.csv'

df = pd.read_csv(input_file_path)
df['d'] = pd.to_datetime(df['d'], unit='ms')  # assuming the timestamp is in milliseconds
df['d'] = df['d'].dt.strftime('%d-%m-%Y')
df['d'] = pd.to_datetime(df['d'], format='%d-%m-%Y')

last_entry_per_day.to_csv('Preprocess.csv', index=False)


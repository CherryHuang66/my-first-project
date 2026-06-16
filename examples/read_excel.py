import pandas as pd
from pathlib import Path

sample_file = Path('input.xlsx')

if not sample_file.exists():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
    df.to_excel(sample_file, index=False)
    print(f'Created sample {sample_file}')

df = pd.read_excel(sample_file)
print('Read dataframe:')
print(df)

out = Path('output.xlsx')
df.to_excel(out, index=False)
print(f'Wrote {out}')

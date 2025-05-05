import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('balanced_by_region.tsv', sep='\t')

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

train_val, test_df = train_test_split(
    df,
    test_size=0.10,
    stratify=df['region'],
    shuffle=True,
    random_state=42
)

val_frac = 0.10 / 0.90  
train_df, val_df = train_test_split(
    train_val,
    test_size=val_frac,
    stratify=train_val['region'],
    shuffle=True,
    random_state=42
)

train_df.to_csv('train.tsv', sep='\t', index=False)
val_df.to_csv('val.tsv',   sep='\t', index=False)
test_df.to_csv('test.tsv',  sep='\t', index=False)

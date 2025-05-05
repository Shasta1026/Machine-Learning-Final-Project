import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Load your pre-mapped, balanced dataset
df = pd.read_csv('balanced_by_region.tsv', sep='\t')

# 2. Shuffle the rows
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# 3. Split off 10% for test
train_val, test_df = train_test_split(
    df,
    test_size=0.10,
    stratify=df['region'],
    shuffle=True,
    random_state=42
)

# 4. From the remaining 90%, carve out 10% of the original for val
val_frac = 0.10 / 0.90  # ≃0.1111
train_df, val_df = train_test_split(
    train_val,
    test_size=val_frac,
    stratify=train_val['region'],
    shuffle=True,
    random_state=42
)

# 5. Write splits to disk
train_df.to_csv('train.tsv', sep='\t', index=False)
val_df.to_csv('val.tsv',   sep='\t', index=False)
test_df.to_csv('test.tsv',  sep='\t', index=False)

# 6. Sanity checks
print(f"✔️  Sizes ▶️ Train: {len(train_df)}, Val: {len(val_df)}, Test: {len(test_df)}")
print("✔️  Region distribution in train:")
print(train_df['region'].value_counts())


#creates a new dataset to group countries by region and makes sure that each region has the same amount of samples
import pandas as pd

df = pd.read_csv('balanced_by_country_dataset.tsv', sep='\t')

# 2. Map regions
region_map = {
    # South America
    'AR':'South America','BO':'South America','CL':'South America',
    'CO':'South America','EC':'South America','PE':'South America',
    'PY':'South America','UY':'South America','VE':'South America',
    # North America
    'US':'North America','MX':'North America',
    # Caribbean
    'CU':'Caribbean','DO':'Caribbean','PR':'Caribbean',
    # Central America
    'GT':'Central America','HN':'Central America','NI':'Central America',
    'CR':'Central America','PA':'Central America','SV':'Central America',

    'ES':'Europe'
}
df['region'] = df['condition'].map(region_map)

# 3. find smallest region
counts = df['region'].value_counts()
min_count = counts.min()

# 4. Down‐sample each region to min_count
balanced_df = (
    df.groupby('region', group_keys=False).apply(lambda grp: grp.sample(n=min_count,random_state=42)).reset_index(drop=True)
)

balanced_df.to_csv('balanced_by_region.tsv', sep='\t', index=False)


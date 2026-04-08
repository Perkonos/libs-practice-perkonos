import kagglehub
import pandas as pd

# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026", output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())

# depression = df[["depression_pct", 'country']]
# mask = (df['region'] == 'Europe') & (df['depression_pct'] >= 5)
# europe_depression = df[mask]
# print(europe_depression[['country', 'suicide_rate_per100k', 'depression_pct']])
# print(europe_depression[['country', 'suicide_rate_per100k']])
# df['millions_rate'] = df["suicide_rate_per100k"]*df['population_millions']*10
# print(df[['country', 'millions_rate']])


mask = (df['gdp_per_capita_usd'] >= 40000) & (df['mh_system_score'] < 5)
df["lack_of_care_mln"] = df["population_millions"]*df["treatment_gap_pct"]/100
hiu = df[mask]
print(hiu[['lack_of_care_mln', 'country']])




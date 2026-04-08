import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

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


# mask = (df['gdp_per_capita_usd'] >= 40000) & (df['mh_system_score'] < 5)
# df["lack_of_care_mln"] = df["population_millions"]*df["treatment_gap_pct"]/100
# hiu = df[mask]
# print(hiu[['lack_of_care_mln', 'country']])


# top5 = df.nlargest(5, 'depression_pct')
# plt.figure(figsize=(6,7))
# plt.plot(top5['country'], top5['depression_pct'],
# marker='o', label='depression', linewidth=2)
# plt.plot(top5['country'], top5['anxiety_pct'], marker='s', label='anxiety')
# plt.title('anxiety vs depression (%)')
# plt.xlabel('countrys')
# plt.ylabel('%')
# plt.legend()
#
#
# plt.show()
plt.figure(figsize=(7,6))
plt.title("mh vs sm")
plt.xlabel("hr in sm")
plt.ylabel("mh")
plt.scatter(df["social_media_hours_daily"], df["youth_mh_crisis_score"],
            marker="o", s=100, color='red', alpha=0.5)
plt.show()


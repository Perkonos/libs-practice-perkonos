# Setup
import numpy as np
import pandas as pd
import kagglehub

# Live Coding 1
views = np.array([15000, 32000, 8500, 45000])
likes = np.array([1200, 3000, 800, 4100])
comments = np.array([150, 400, 50, 600])

# TODO:
total_interaction =likes + comments
engagement_rate = (total_interaction / views) *100
print(f"...:{np.round(engagement_rate)}")


# Guided Practice 1
rpm = np.array([1.5, 2.0, 0.8, 2.5])
production_cost = np.array([10, 30, 5, 50])

# TODO:
money = views//1000 * rpm - production_cost
print(np.max(money))


# Live Coding 2
cpu_load = np.array([
    [45, 50, 55, 40, 48],  # Server 1
    [88, 92, 95, 89, 94],  # Server 2
    [20, 25, 22, 18, 30]   # Server 3
])

# TODO:
mean_load = np.mean(cpu_load, axis=1)
print("mean load", mean_load)
absolute_max_server = np.max(cpu_load, axis = 1)
print(absolute_max_server)
critical_loads = cpu_load[cpu_load > 50]
print(critical_loads)
print(critical_loads.size)



# Guided Practice 2
pings = np.array([
    [45, 50, 48, 55],       # Server 1
    [120, 115, 210, 130],   # Server 2
    [300, 250, 310, 280],   # Server 3
    [15, 20, 18, 22]        # Server 4
])

# TODO:
min_time = np.min(pings, axis=1)
print(min_time)
print(np.mean(pings))
big_ping = pings[pings>200]
print(big_ping)
print(big_ping.size)
print(big_ping.size/pings.size*100)







# Live Coding 3
kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026",
                                  output_dir="datasets", force_download=True)
df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
print(df.head())

# TODO:
"""
Project: Jet Engine Performance and Vibration Analysis Model  
Aurthor: Aayan Mahmood 
Date: January 2026
Description:    This script analyses static fire test data from 
a turbojet engine. It ingests raw sensor telemetry to calculate 
critical performance metrics and identify safety anomalies. 
Dependancies:
- Pandas 
- NumPy
- MatPlotLib

"""


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Load raw data from the test bench 

df = pd.read_csv("Engine_Data.csv")


# Prints data and checks for data types and null values 
print ("__ENGINE DATA HEAD__")
print(df.head())

print ("\n__DATA INFO__")
print(df.info())

# Physics Calculations 

# Thrust is proportional to RPM^3.5 for gas turbines 
# using 4e-11 to model roughly a small business jet (around 8500 N of thrust)
df["Thrust_N"] = 4e-11 * (df["RPM"] ** 3.5)

# calculationg the specific fuel consumption telling us the efficiency of the engine 
# Fule flow / Thrust 
df["SFC"] = df["Fuel_Flow_kg_hr"] / df["Thrust_N"]

# We only want when it is actually running as when RPM is 0 it will cause a division by 0 error in the SFC

df_running = df[df["RPM"] > 0 ].copy()

print ("\n __PREFORMANCE DATA (Running)__")
print(df_running[["RPM", "Thrust_N", "SFC", "Vibration_mm_s"]].head(10))

# Plotting the data 

fig, (ax1 , ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Thrust vs RPM graph 

ax1.plot(df_running["RPM"], df_running["Thrust_N"], color="blue", linewidth=2)
ax1.set_title("Thrust Curve")
ax1.set_xlabel("RPM Speed")
ax1.set_ylabel("Thrust (Newtons)")
ax1.grid(True, linestyle="--")

# Vibration Analysis 

ax2.plot(df_running["RPM"], df_running["Vibration_mm_s"], color="orange", linewidth=2)
ax2.axhline(y=4.0, color="red", linestyle="--", label="Danger Threshold (4.0 mm/s)")
ax2.set_title("Vibration Analysis")
ax2.set_xlabel("RPM Speed")
ax2.set_ylabel("Vibration (mm/s)")
ax2.legend()
ax2.grid(True, linestyle="--")


plt.tight_layout()
plt.show()
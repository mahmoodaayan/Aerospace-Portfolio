import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

## Dynamic pressure equation is Q= 1/2 (Rho)*v^2

def sim_MaxQ():

    dt = 1   # chang in time 
    time = np.arange(0, 300, dt)

    # lets asume the acceleration of this rocket is 20m/
    # change made here by changing it from a constant acceleration to the cumulative sum making this more accurate 

    acceleration = 5 + (0.2 * time)

    velocity = np.cumsum(acceleration * dt)
#s = 1/2 at^2

    altitude = np.cumsum(velocity* dt)

# scale hight for earth is 10,000 so with a fraction that is -0.0001 

    
    density = 1.225 * np.exp(-0.0001 * altitude)

    dynamic_pressure = (1/2)*density*velocity**2

    maxq_index = np.argmax(dynamic_pressure)
    maxq_time = time[maxq_index]


    plt.figure(figsize=(10,5))
    plt.plot(time, dynamic_pressure, color="green", linewidth=2)
    plt.axvline(x=maxq_time, color="red", linestyle ="--", label = (f"maxQ (T + {maxq_time} s)"))

    plt.title("Rocket dynamic pressure graph")
    plt.ylabel("Pressure")
    plt.xlabel("Time")
    plt.legend()
    plt.grid(True)
    plt.show()


sim_MaxQ()


"""
results show a 53 second time to reach max q in reality the time to reach max q for a falcon 9 which this is based of
takes around 70 - 80 seconds this is much more accurate than the original copy with constant acceleration which gave us a value
of around 30 seocnds for max q


"""



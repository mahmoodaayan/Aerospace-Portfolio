import matplotlib.pyplot as plt 
import numpy as np 
import mplcursors as mpc

# constants Nitrous Oxide 
pc = 72.51
tc = 309.57
b1 = -6.71893
b2 = 1.35966
b3 = -1.3779
b4 = -4.051


def get_pressure(t_celcius):
    # calculating the pressure using the wegner equation 
    T = t_celcius + 273.5
    Tr = T/tc
    tau = 1 - Tr
    ln_p_pc = (1/Tr) * (b1 * tau + b2 * tau**1.5 + b3 * tau**2.5 + b4 * tau**5)
    p = np.exp(ln_p_pc) * pc
    return p 

temp_range = np.linspace (-20, 36, 200)   #temp range to critical point 
pressure = get_pressure(temp_range)

t_room = 22
p_room = get_pressure(t_room)

t_target_40bar = 10.7  # this is the opperating temp of NOx at 40 bar from the BSI
p_target_40bar = get_pressure(t_target_40bar)


plt.plot(temp_range,pressure, label="N2O pressure", color ="blue", linewidth=3)


plt.scatter([t_room, t_target_40bar], [p_room, p_target_40bar], color="green", s=50, zorder=5)

plt.annotate(f"Room Temp: {t_room}°C\n{p_room:.1f} bar", (t_room, p_room), 
             xytext=(t_room-8, p_room+2), arrowprops=dict(arrowstyle='->'))

plt.annotate(f"Target: {t_target_40bar}°C\n{p_target_40bar:.1f} bar", (t_target_40bar, p_target_40bar), 
             xytext=(t_target_40bar-8, p_target_40bar+5), arrowprops=dict(arrowstyle="->"))

plt.title("N2O self pressure curve", fontsize=15, fontweight="bold")
plt.xlabel("Temp (°C)", fontsize=12)
plt.ylabel("Pressure (Bar)", fontsize=12)
plt.axhline(y=40, color="gray", linestyle="--", alpha=0.5, label="40 Bar Line")
plt.axvline(x=36.4, color="orange", linestyle=":", label="Critical Point (36.4°C)")

plt.grid(True, which="both", linestyle="--", alpha = 0.5)
plt.legend()
plt.tight_layout()
mpc.cursor(hover=True)
plt.show()
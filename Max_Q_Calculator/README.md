# Max-Q Rocket Ascent Simulator

## Overview
This project is a 1D kinematic flight simulator built in Python. It calculates and visualizes the exact moment of **Maximum Dynamic Pressure (Max-Q)** during a rocket's ascent through Earth's atmosphere. 

Instead of relying on constant velocity, this model uses numerical calculus to simulate a rocket's increasing acceleration as it burns fuel and loses mass.

## Technology Stack
* **Python 3**
* **NumPy:** Used for vectorized math, array generation, and numerical integration.
* **Matplotlib:** Used for visualizing the flight telemetry and plotting the Max-Q intersection.

## The Physics & Mathematics
The simulation calculates Max-Q by finding the intersection of two opposing physical forces: a rocket's increasing velocity and the Earth's decaying atmospheric density.

1. **Mass-Loss Acceleration:** Models a rocket lifting off the pad at $5 \text{ m/s}^2$ and gradually increasing acceleration as fuel is consumed.
2. **Numerical Integration:** Uses NumPy's `cumsum()` to integrate acceleration into velocity, and velocity into altitude over time.
3. **Barometric Formula:** Calculates atmospheric density decay based on Earth's scale height ($\approx 10,000 \text{ m}$):
   $$\rho = 1.225 \times e^{-0.0001 \times altitude}$$
4. **Dynamic Pressure:** Applies the standard aerodynamic stress equation:
   $$q = \frac{1}{2} \rho v^2$$

## Assumptions & Limitations
To keep the model lightweight and focused on fundamental kinematics, the following variables were simplified:
* **Throttle Bucket:** The simulation assumes continuous acceleration. Real-world launch vehicles (like the Falcon 9) actively throttle down their engines approaching Max-Q to reduce aerodynamic stress, which pushes their actual Max-Q later in the flight timeline (approx. T+70s).
* **Drag Coefficient:** This is a purely kinematic model and does not account for the aerodynamic shape/drag of the vehicle.
* **Constant Gravity:** The model assumes a constant gravitational pull, rather than decreasing gravity as altitude increases.

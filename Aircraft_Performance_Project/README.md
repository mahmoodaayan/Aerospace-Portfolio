# Aircraft Performance Calculator
**Project Type:** Aerodynamics & Mission Analysis Tool

## Overview
A Python-based engineering tool that calculates key flight metrics based on user inputs and standard aerospace physics formulas. It processes aerodynamic coefficients, fuel data, and weight parameters to generate a comprehensive flight report.

## Key Features
* **Aerodynamics:** Calculates Lift ($L$) and Drag ($D$) using coefficient formulas ($0.5 \cdot \rho \cdot v^2 \cdot S$).
* **Mission Analysis:** Estimates maximum **Range** and **Endurance** based on fuel flow rates.
* **Mass Properties:** Computes Total Weight and Center of Gravity (CG) position.
* **Kinematics:** Calculates acceleration, final velocity, and distance covered over a time interval.
* **Automated Reporting:** Exports all calculated data to an external text file (`aircraft_performance_analysis.txt`) for review.
* **Error Handling:** robust input validation to prevent crashes from non-numeric inputs.

## Usage
Run the script and input the requested flight parameters (Fuel Capacity, Payload, Lift/Drag Coefficients, etc.) when prompted. The tool will print the results to the terminal and save a log file.

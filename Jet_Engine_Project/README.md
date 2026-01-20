# Jet Engine Performance Analysis
**Project Type:** Propulsion Engineering / Data Analysis

## Overview
This project analyzes static fire test data from a prototype turbojet to evaluate thrust efficiency and identify vibration resonance.

## Key Outcomes
* **Thrust Modeling:** Implemented a Power Law ($RPM^{3.5}$) model to estimate thrust based on sensor RPM data.
* **Vibration Analysis:** Detected a critical resonance spike at 12,500 RPM (17% over safety limit) using Matplotlib visualization.
* **Efficiency Metrics:** Calculated Specific Fuel Consumption (SFC) to map engine efficiency curves.

## Technologies Used
* **Pandas:** For cleaning and filtering raw telemetry CSV data.
* **NumPy:** For vectorized physics calculations.
* **Matplotlib:** For generating dual-plot engineering dashboards.

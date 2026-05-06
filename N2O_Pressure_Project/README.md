# N2O Pressure Curve Project

This project models the self-pressurisation behaviour of Nitrous Oxide (N2O) as a function of temperature using the Wagner equation.

## Overview

Nitrous Oxide is commonly used as an oxidiser in hybrid rocket engines. Understanding how its pressure varies with temperature is critical for safe and efficient system design.

This script:
- Computes pressure using thermodynamic relations
- Plots pressure vs temperature
- Highlights key operating points:
  - Room temperature (~22°C)
  - Target condition at 40 bar
  - Critical point (~36.4°C)

## Key Features

- Implements the Wagner equation for N2O
- Generates a smooth pressure curve
- Annotates important operating conditions
- Interactive plot using `mplcursors`

## Requirements

Install the required Python libraries:

```bash
pip install numpy matplotlib mplcursors

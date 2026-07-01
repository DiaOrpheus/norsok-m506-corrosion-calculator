# NORSOK M-506 CO₂ Corrosion Calculator

Web-based calculator for predicting internal CO₂ corrosion rate using the NORSOK M-506 methodology.

## Overview

This application calculates:
- pH of produced water
- CO₂ Fugacity
- Shear Stress
- Internal Corrosion Rate (mm/y)

based on operating conditions and flow parameters commonly used in oil & gas production systems.

The calculator is implemented in Python and provided through a Streamlit web interface for easy use by engineers and researchers.

---

## Features
- NORSOK M-506 corrosion rate calculation
- Automatic pH calculation
- CO₂ fugacity calculation
- Shear stress calculation
- Pressure input in psi or bar
- User-friendly Streamlit interface
- Real-time calculation results

---

## Input Parameters

### Operating Conditions
- Temperature (°C)
- Pressure (bar or psi)
- CO₂ Fraction
- Bicarbonate (mg/L)
- Ionic Strength

### Flow Conditions
- Gas Velocity (m/s)
- Liquid Velocity (m/s)
- Liquid Holdup (%)
- Gas Mass Flow (kg/hr)
- Liquid Mass Flow (kg/hr)
- Gas Volume Flow (m³/hr)
- Liquid Volume Flow (m³/hr)
- Gas Viscosity (cP)
- Liquid Viscosity (cP)
- Pipe Roughness (m)
- Pipe Internal Diameter (m)

---

## Outputs

### Calculated Parameters
- CO₂ Fugacity
- pH
- fpH
- Kt


### Main Results
- Shear Stress (Pa)
- Corrosion Rate (mm/y)

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd norsokm506
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Acknowledgement

This project is derived from the open-source implementation:

https://github.com/dungnguyen2/norsokm506

The original project is licensed under the MIT License.

---

## Modifications

This version has been modified and extended by:

**Gendro Wisnu**

Major enhancements include:
- Streamlit web application
- Improved user interface
- Pressure unit selection
- Input validation
- Enhanced result presentation
- Code maintenance and bug fixes

---

## License

MIT License

Copyright (c) 2019 dungnguyen2

Copyright (c) 2026 Gendro Wisnu

This project remains free to use, modify, and distribute under the MIT License.
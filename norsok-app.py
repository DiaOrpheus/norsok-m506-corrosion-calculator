import streamlit as st
import norsokm506_main as ns

st.set_page_config(
    page_title="NORSOK M-506",
    layout="wide"
)
st.title("NORSOK M-506 CO₂ Corrosion Calculator")

st.write("Source: https://github.com/dungnguyen2/norsokm506")
st.write("Developed by Ari SN & Gendro Wisnu (D&P TEC - PHE)")
st.write("Last Update: 2026-06")

st.header("Operating Conditions")

temp = st.number_input(
    "Temperature (°C)",
    value=65.0,
    help="Typical range: 20 - 150 °C"
)

col1, col2 = st.columns([3,1])
with col1:
    press = st.number_input(
        "Pressure",
        value=37.6,
    )
with col2:
    pressure_unit = st.selectbox(
        "",
        ["bar", "psi"],
        help="Operating pressure"
    )


co2fraction = st.number_input(
    "CO₂ Fraction",
    value=0.2,
    help="0.0 - 1.0"
)

bicarbonate = st.number_input(
    "Bicarbonate (mg/L)",
    value=2003.0,
    help="Produced water analysis"
)

ionstrength = st.number_input(
    "Ionic Strength",
    value=39.66,
    help="Produced water ionic strength"
)

st.header("Flow Conditions")

v_sg = st.number_input(
    "Gas Velocity Vsg (m/s)",
    value=9.0
)

v_sl = st.number_input(
    "Liquid Velocity Vsl (m/s)",
    value=1.0
)

holdup = st.number_input(
    "Liquid Holdup (%)",
    value=10.0
)

st.header("Fluid Properties")

mass_g = st.number_input(
    "Gas Mass Flow (kg/hr)",
    value=234.5,
    help="Example from test case"
)

mass_l = st.number_input(
    "Liquid Mass Flow (kg/hr)",
    value=542.3,
    help="Example from test case"
)

vol_g = st.number_input(
    "Gas Volume Flow (m³/hr)",
    value=14.8,
    help="Example from test case"
)

vol_l = st.number_input(
    "Liquid Volume Flow (m³/hr)",
    value=637.0,
    help="Example from test case"
)

vis_g = st.number_input(
    "Gas Viscosity (cP)",
    value=0.03,
    help="Typical natural gas viscosity"
)

vis_l = st.number_input(
    "Liquid Viscosity (cP)",
    value=1.4,
    help="Produced water viscosity"
)

roughness = st.number_input(
    "Pipe Roughness (m)",
    value=0.00005,
    format="%.5f",
    help="Typical carbon steel pipe"
)

dia = st.number_input(
    "Pipe Internal Diameter (m)",
    value=0.475,
    help="Pipe ID"
)

if pressure_unit == "psi":
    press_bar = press / 14.503774
else:
    press_bar = press

if st.button("Calculate Corrosion Rate"):
    

    ph = ns.pHCalculator(
        temp,
        press,
        co2fraction * press,
        bicarbonate,
        ionstrength,
        2
    )

    shearstress = ns.Shearstress(
        v_sg,
        v_sl,
        mass_g,
        mass_l,
        vol_g,
        vol_l,
        holdup,
        vis_g,
        vis_l,
        roughness,
        dia
    )

    corr = ns.Cal_Norsok(
        co2fraction,
        press,
        temp,
        v_sg,
        v_sl,
        mass_g,
        mass_l,
        vol_g,
        vol_l,
        holdup,
        vis_g,
        vis_l,
        roughness,
        dia,
        bicarbonate,
        ionstrength,
        2
    )

    st.success("Calculation completed")

    st.subheader("Input Summary")
    st.write(f"Temperature : {temp:.2f} °C")
    
    if pressure_unit == "bar":
        pressure_psi = press * 14.503774
    else:
        pressure_psi = press
    st.write(f"Pressure : {pressure_psi:.2f} psi")
    
    st.write(f"CO₂ Fraction : {co2fraction:.2f}")
    
    st.subheader("Calculated Parameters")
    st.write(f"pH : {ph:.2f}")

    st.subheader("Main Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Shear Stress",
            f"{shearstress:.2f} Pa"
        )

    with col2:
        st.metric(
            "Corrosion Rate",
            f"{corr:.2f} mm/y"
        )
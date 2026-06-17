import streamlit as st
import norsokm506_main as ns

st.set_page_config(
    page_title="NORSOK M-506",
    layout="wide",
)

st.markdown("""
<style>
.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.header-title {
    font-size: 70px;
    font-weight: 700;
    color: #2D3142;
    margin: 0;
}

.header-logo {
    max-height: 180px;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([6,1])

with col1:
    st.markdown("""
    <div style="display:flex; align-items:center; height:180px;">
        <h1 class="header-title">
            NORSOK M-506 CO₂ Corrosion Calculator
        </h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("Logo_01.png", width=150)

st.markdown("""
<div style="
border:1px solid #D9D9D9;
border-radius:10px;
padding:15px 20px;
background-color:#FAFAFA;
margin-top:10px;
margin-bottom:25px;
">

<table style="width:100%;">
<tr>
<td style="width:180px;"><b>Source</b></td>
<td>
<a href="https://github.com/dungnguyen2/norsokm506">
https://github.com/dungnguyen2/norsokm506
</a>
</td>
</tr>

<tr>
<td><b>Developed by</b></td>
<td>
Ari SN & Gendro Wisnu
(Drilling & Well D&P TEC - PHE)
</td>
</tr>

<tr>
<td><b>Last Update</b></td>
<td>June 2026</td>
</tr>

</table>

</div>
""", unsafe_allow_html=True)

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
    
if pressure_unit == "psi":
    press_bar = press / 14.503774
else:
    press_bar = press

press = press_bar

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

if st.button("Calculate Corrosion Rate"):
    
    FugCO2 = ns.FugacityofCO2(
    co2fraction,
    press,
    temp
    )
    
    kt = ns.Kt(temp)

    ph = ns.pHCalculator(
        temp,
        press,
        co2fraction * press,
        bicarbonate,
        ionstrength,
        2
    )

    fph = ns.fpH_Cal(temp, float(ph))

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


    if pressure_unit == "bar":
        pressure_psi = press * 14.503774
    else:
        pressure_psi = press

    col_input, col_calc = st.columns(2)
    with col_input:

        st.subheader("📋 Input Summary")

        st.markdown(f"""
| Parameter | Value |
|-----------|--------|
| Temperature | {temp:.2f} °C |
| Pressure | {pressure_psi:.2f} psi |
| CO₂ Fraction | {co2fraction:.2f} |
""")
        
    with col_calc:
        st.subheader("🧮 Calculated Parameters")

        st.markdown(f"""
| Parameter | Value |
|-----------|--------|
| CO₂ Fugacity | {FugCO2:.2f} |
| pH | {ph:.2f} |
| f(pH) | {fph:.3f} |
| Kt | {kt:.4f} |
""")
        

    st.subheader("📈 Main Results")

    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown(
            f"""
<div style="
background-color:white;
border:1px solid #DDDDDD;
border-radius:12px;
padding:20px;
text-align:center;
height:120px;
display:flex;
flex-direction:column;
justify-content:center;
">

<div style="
font-size:20px;
font-weight:600;
">
Shear Stress
</div>

<div style="
font-size:36px;
font-weight:700;
">
{shearstress:.2f} Pa
</div>

</div>
""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
<div style="
background-color:#F4FAF4;
border:2px solid #4CAF50;
border-radius:12px;
padding:20px;
text-align:center;
height:120px;
display:flex;
flex-direction:column;
justify-content:center;
">

<div style="
font-size:20px;
font-weight:600;
color:#2E7D32;
margin-bottom:10px;
">
Corrosion Rate
</div>

<div style="
font-size:36px;
font-weight:700;
color:#2E7D32;
">
{corr:.2f} mm/y
</div>

</div>
""",
            unsafe_allow_html=True
        )
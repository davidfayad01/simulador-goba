
import streamlit as st
from PIL import Image

# Configuración inicial de la página (debe ir primero)
st.set_page_config(page_title="Goba Capital Simulator", layout="centered")

# Mostrar logo principal
logo = Image.open("Goba_Logo-Tagline_CMYK.png")
st.image(logo, width=300)

# Título de la app
st.title("Goba Capital Simulator")

st.markdown("""
Este simulador estima el impacto financiero de tomar un producto de financiamiento de Goba Capital. Según el producto, calcula:
- Ahorros por eficiencia en días operativos (AR, AP, inventario).
- Mejora en flujo de caja.
- ROI y comparativo antes/después.
- Costo financiero trimestral y anual.
""")

# --- Selección de producto ---
st.image("Goba_Icon_CMYK_Med-Green.png", width=25)
st.header("Selección de Producto Financiero")
product = st.selectbox("Select Financial Product", [
    "Factoring",
    "Finance to Suppliers",
    "Inventory Financing",
    "Asset-Based Lending (ABL)",
    "Loan"
])

# --- Datos generales ---
st.image("Goba_Icon_CMYK_Med-Green.png", width=25)
st.header("Input de Datos Financieros")
annual_sales = st.number_input("Annual Sales (USD)", min_value=0.0, value=20000000.0, step=100000.0)
operating_margin = st.number_input("Operating Margin (%)", min_value=0.0, value=12.0, step=0.5) / 100
financing_amount = st.number_input("Financing Amount Requested (USD)", min_value=0.0, value=5000000.0, step=100000.0)
annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=18.0, step=0.5) / 100

# --- Variables específicas por producto ---
st.image("Goba_Icon_CMYK_Med-Green.png", width=25)
st.subheader("Datos Operacionales según el Producto")

if product == "Factoring":
    ar_before = st.number_input("Accounts Receivable Days (Before)", min_value=0, value=75)
    ar_after = st.number_input("Accounts Receivable Days (After)", min_value=0, value=45)
    savings_days = ar_before - ar_after
    cash_type = "AR"
elif product == "Finance to Suppliers":
    ap_before = st.number_input("Accounts Payable Days (Before)", min_value=0, value=30)
    ap_after = st.number_input("Accounts Payable Days (After)", min_value=0, value=60)
    savings_days = ap_after - ap_before
    cash_type = "AP"
elif product == "Inventory Financing":
    inv_before = st.number_input("Inventory Days (Before)", min_value=0, value=90)
    inv_after = st.number_input("Inventory Days (After)", min_value=0, value=60)
    savings_days = inv_before - inv_after
    cash_type = "Inventory"
else:
    savings_days = 0
    cash_type = "N/A"

# --- Cálculos financieros ---
cash_improvement = (annual_sales * savings_days / 365) * operating_margin
financing_cost_annual = financing_amount * annual_interest_rate
financing_cost_quarter = financing_cost_annual / 4
roi = (cash_improvement - financing_cost_annual) / financing_cost_annual if financing_cost_annual != 0 else 0

# --- Resultados ---
st.image("Goba_Icon_CMYK_Med-Green.png", width=25)
st.subheader("Resultados del Simulador")
st.write(f"Ahorro estimado por eficiencia operativa ({cash_type}): **${cash_improvement:,.2f}**")
st.write(f"Costo Financiero Anual: **${financing_cost_annual:,.2f}**")
st.write(f"Costo Financiero Trimestral: **${financing_cost_quarter:,.2f}**")
st.write(f"ROI estimado del financiamiento: **{roi * 100:.2f}%**")

import streamlit as st
import matplotlib.pyplot as plt
from simulaatio import simulate_detailed

st.set_page_config(page_title="Asunto vs vuokra -simulaattori", layout="centered")
st.title("Omistusasuminen vs. vuokra + osakkeet")

# --- SIVUPALKKI: perusparametrit ---
st.sidebar.header("Perusasetukset")
years = st.sidebar.slider("Vuodet", 5, 40, 10)
house_price = st.sidebar.number_input("Asunnon hinta (€)", 100000, 1500000, 650000, step=10000)
down_payment = st.sidebar.number_input("Oma pääoma (€)", 0, 600000, 300000, step=10000)
loan_interest = st.sidebar.slider("Lainan korko %/v", 0.0, 10.0, 3.0, 0.1)
loan_years = st.sidebar.slider("Laina-aika (v)", 5, 40, 25)

# --- PÄÄALUE: kolmessa sarakkeessa tarkemmat kulut ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Omistusasunto – kulut")
    maintenance = st.number_input("Vastike €/kk", 0, 1500, 418, step=10)
    property_tax = st.slider("Kiinteistövero %/v arvosta", 0.0, 1.0, 0.0, 0.05)
    renovation_yearly = st.number_input("Remonttivara €/v", 0, 20000, 3000, step=500)
    owner_other = st.number_input("Omistajan muut kulut €/kk", 0, 300, 40, step=10)
    house_app = st.slider("Asunnon arvonnousu %/v", -5.0, 10.0, 2.0, 0.1)

with col2:
    st.subheader("Vuokra")
    rent_initial = st.number_input("Vuokra €/kk", 0, 3000, 1800, step=50)
    rent_inc = st.slider("Vuokrankorotus %/v", 0.0, 10.0, 3.0, 0.1)
    renter_other = st.number_input("Vuokralaisen muut kulut €/kk", 0, 300, 30, step=10)

with col3:
    st.subheader("Sijoitukset")
    initial_inv = st.number_input("Alkusijoitus osakkeisiin (€)", 0, 600000, 300000, step=10000)
    stock_ret = st.slider("Osaketuotto %/v (netto)", -5.0, 20.0, 6.0, 0.1)
    transfer_tax = st.slider("Varainsiirtovero % kauppahinnasta", 0.0, 4.0, 1.5, 0.1)
    sale_cost = st.slider("Myyntikulut % myyntihinnasta", 0.0, 5.0, 2.0, 0.1)
    allow_neg = st.checkbox("Sallitaanko negatiivinen säästö", value=False)

# --- LASKENTA ---
df = simulate_detailed(
    years=years,
    house_price=house_price,
    down_payment=down_payment,
    loan_interest_annual=loan_interest / 100.0,
    loan_years=loan_years,
    maintenance_fee=maintenance,
    house_appreciation_annual=house_app / 100.0,
    rent_initial=rent_initial,
    rent_increase_annual=rent_inc / 100.0,
    initial_investment=initial_inv,
    stock_return_annual=stock_ret / 100.0,
    transfer_tax_rate=transfer_tax / 100.0,
    sale_cost_rate=sale_cost / 100.0,
    property_tax_rate_annual=property_tax / 100.0,
    renovation_yearly_eur=renovation_yearly,
    owner_other_monthly=owner_other,
    renter_other_monthly=renter_other,
    allow_negative_saving=allow_neg,
)

last = df.iloc[-1]

st.markdown(f"### Yhteenveto {years} vuoden jälkeen")
st.write(f"**Nettovarallisuus A (omistusasunto):** {last['networth_owner']:,.0f} €")
st.write(f"**Nettovarallisuus B (vuokra + osakkeet):** {last['networth_renter']:,.0f} €")

st.markdown("#### Viimeisen kuukauden kulut (suuntaa-antavat)")
st.write(f"Omistaja – kokonaiskulut/kk: {last['owner_total_monthly_cost']:,.0f} €")
st.write(f"Vuokralainen – kokonaiskulut/kk: {last['renter_total_monthly_cost']:,.0f} €")

# --- Kuvaaja ---
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(df["year"], df["networth_owner"], label="Omistusasunto (A)")
ax.plot(df["year"], df["networth_renter"], label="Vuokra + osakkeet (B)")
ax.set_xlabel("Vuosi")
ax.set_ylabel("Nettovarallisuus (€)")
ax.set_title("Nettovarallisuus ajan funktiona (kulut huomioiden)")
ax.grid(True)
ax.legend()
st.pyplot(fig)

st.markdown("#### Viimeiset datarivit")
st.dataframe(df.tail())


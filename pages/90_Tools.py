
import streamlit as st

st.sidebar.title("Benew")
st.sidebar.page_link("app.py", label=t("menu_home"))
st.sidebar.page_link("pages/00_Login.py", label=t("menu_login"))
st.sidebar.page_link("pages/01_Persona.py", label=t("menu_persona"))
st.sidebar.page_link("pages/10_Banking.py", label=t("menu_banking"))
st.sidebar.page_link("pages/20_Insurance.py", label=t("menu_insurance"))
st.sidebar.page_link("pages/30_Healthcare.py", label=t("menu_healthcare"))
st.sidebar.page_link("pages/40_Taxation.py", label=t("menu_taxation"))
st.sidebar.page_link("pages/50_Housing.py", label=t("menu_housing"))
st.sidebar.page_link("pages/60_Transport.py", label=t("menu_transport"))
st.sidebar.page_link("pages/70_Work.py", label=t("menu_work"))
st.sidebar.page_link("pages/80_Life.py", label=t("menu_life"))
st.sidebar.page_link("pages/90_Tools.py", label=t("menu_tools"))

st.title("Outils")
st.header("Crédit conso — mensualité")
A = st.number_input("Montant (€)", min_value=0, value=2000, step=100)
R = st.number_input("Taux annuel (%)", min_value=0.0, value=8.5, step=0.1)
M = st.number_input("Durée (mois)", min_value=1, value=24, step=1)
def monthly(a,rpct,m):
    r = (rpct/100)/12
    if m <= 0: return 0.0
    if r == 0: return a/m
    return (a*r)/(1 - (1+r)**(-m))
p = monthly(A,R,M)
st.metric("Mensualité (€)", round(p,2))
st.write(f"Total remboursé : **{round(p*M,2)} €**")

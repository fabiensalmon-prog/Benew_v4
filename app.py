
import streamlit as st
from data.utils import LANGS, get_lang, set_lang, t, is_authed, get_persona, recommended_path

st.set_page_config(page_title="Benew", page_icon="🌍", layout="wide")

cols = st.columns([2,3,3,3])
with cols[0]:
    st.markdown("### **Benew**")
with cols[-1]:
    lang = get_lang()
    labels = {code:label for code,label in LANGS}
    sel = st.selectbox(t("choose_lang"), options=[c for c,_ in LANGS], format_func=lambda c: labels[c], index=[c for c,_ in LANGS].index(lang))
    if sel != lang:
        set_lang(sel)
        st.rerun()

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

st.divider()

st.markdown(f"#### {t('app_title')}")
if is_authed():
    st.success(f"{t('welcome')}")
    per = get_persona()
    order = recommended_path(per)
    labels = {"banking": t("menu_banking"),"insurance": t("menu_insurance"),"healthcare": t("menu_healthcare"),"taxation": t("menu_taxation"),"housing": t("menu_housing"),"transport": t("menu_transport"),"work": t("menu_work"),"life": t("menu_life")}
    st.subheader(t("recommended_path"))
    cols = st.columns(len(order))
    for i,sec in enumerate(order):
        with cols[i]:
            st.page_link(f"pages/{ {'banking':'10_Banking.py','insurance':'20_Insurance.py','healthcare':'30_Healthcare.py','taxation':'40_Taxation.py','housing':'50_Housing.py','transport':'60_Transport.py','work':'70_Work.py','life':'80_Life.py'}[sec] }", label=labels.get(sec, sec), icon="➡️")
else:
    st.info(t("nav_hint"))
    st.page_link("pages/00_Login.py", label=t("menu_login"), icon="🔐")
    st.page_link("pages/01_Persona.py", label=t("menu_persona"), icon="👤")

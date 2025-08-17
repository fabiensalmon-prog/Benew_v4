
import streamlit as st
from data.utils import t, get_persona, set_persona, recommended_path

st.title(t("persona_title"))
p = get_persona()

c1,c2 = st.columns(2)
with c1:
    profile = st.selectbox(t("profile"), ["student","worker","family","entrepreneur","retiree"], index=["student","worker","family","entrepreneur","retiree"].index(p.get("profile","student")), format_func=lambda x: t(x))
    papers = st.radio(t("papers"), [ "yes","no" ], index=1 if p.get("papers","no")=="no" else 0, horizontal=True, format_func=lambda x: t(x))
    fx = st.radio(t("fx"), [ "yes","no" ], index=1 if p.get("fx","no")=="no" else 0, horizontal=True, format_func=lambda x: t(x))
with c2:
    branch = st.radio(t("branch"), [ "yes","no" ], index=1 if p.get("branch","no")=="no" else 0, horizontal=True, format_func=lambda x: t(x))
    city = st.selectbox(t("city"), ["paris","lyon","other"], index=["paris","lyon","other"].index(p.get("city","paris")), format_func=lambda x: t(x))
    budget = st.number_input(t("budget"), min_value=0, value=int(p.get("budget",800)), step=50)
    duration = st.selectbox(t("duration"), ["short","long"], index=0 if p.get("duration","long")=="short" else 1, format_func=lambda x: t(x))

if st.button(t("save")):
    set_persona({"profile":profile,"papers":papers,"fx":fx,"branch":branch,"city":city,"budget":budget,"duration":duration})
    st.success("✅ Saved")

st.subheader(t("recommended_path"))
order = recommended_path(get_persona())
labels = {"banking": t("menu_banking"),"insurance": t("menu_insurance"),"healthcare": t("menu_healthcare"),"taxation": t("menu_taxation"),"housing": t("menu_housing"),"transport": t("menu_transport"),"work": t("menu_work"),"life": t("menu_life")}
cols = st.columns(len(order))
for i,sec in enumerate(order):
    with cols[i]:
        st.page_link(f"pages/{ {'banking':'10_Banking.py','insurance':'20_Insurance.py','healthcare':'30_Healthcare.py','taxation':'40_Taxation.py','housing':'50_Housing.py','transport':'60_Transport.py','work':'70_Work.py','life':'80_Life.py'}[sec] }", label=labels.get(sec, sec), icon="➡️")

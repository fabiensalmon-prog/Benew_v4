
import streamlit as st
from data.utils import t, is_authed, login, logout

st.title(t("login_title"))

if is_authed():
    st.success("✅ Logged in")
    if st.button(t("logout")):
        logout()
        st.rerun()
else:
    with st.form("login_form"):
        email = st.text_input(t("email"), value="demo@benew.app")
        pwd = st.text_input(t("password"), type="password", value="benew2025")
        ok = st.form_submit_button(t("login"))
    if ok:
        if login(email, pwd):
            st.success("✅ OK")
            st.rerun()
        else:
            st.error(t("bad_login"))
    if st.button(t("skip_login")):
        st.session_state.authed = True
        st.session_state.user_email = "demo@benew.app"
        st.experimental_rerun()


import streamlit as st
from .content import I18N, CONTENT

LANGS = [("fr","Français"),("en","English"),("es","Español"),("uk","Українська"),("zh","中文")]

def get_lang():
    if "lang" not in st.session_state:
        st.session_state.lang = "fr"
    return st.session_state.lang

def set_lang(l):
    st.session_state.lang = l

def t(key):
    lang = get_lang()
    base = I18N.get(lang) or I18N.get("en", {})
    return base.get(key, I18N.get("en", {}).get(key, key))

def section_data(section):
    lang = get_lang()
    sec = CONTENT.get(section, {})
    if not sec: return None
    if lang in sec: return sec[lang]
    return sec.get("en")

def render_section(section_key):
    data = section_data(section_key)
    if not data:
        st.error("Section not found")
        return
    st.title(data.get("title",""))
    intro = data.get("intro", [])
    if intro:
        with st.container(border=True):
            for p in intro:
                st.write(p)
    for s in data.get("sections", []):
        st.subheader(s.get("title",""))
        body = s.get("body")
        if body:
            st.write(body)
        lst = s.get("list")
        if lst:
            st.markdown("\n".join([f"- {x}" for x in lst]))
    cmp = data.get("comparison", {})
    items = (cmp or {}).get("items", [])
    if items:
        st.markdown(f"### {cmp.get('title','')}")
        note = cmp.get("note")
        if note: st.caption(note)
        for it in items:
            name = it.get("name","")
            site = it.get("site","#")
            desc = it.get("desc","")
            st.markdown(f"- [{name}]({site})" + (f" — {desc}" if desc else ""))
    st.caption(t("disclaimer"))

USERS = {"demo@benew.app":"benew2025"}
def is_authed():
    return bool(st.session_state.get("authed", False))
def login(email, password):
    ok = USERS.get(email) == password
    if ok:
        st.session_state.authed = True
        st.session_state.user_email = email
    return ok
def logout():
    st.session_state.authed = False
    st.session_state.user_email = None
def guard():
    if not is_authed():
        st.warning("Please login from the Login page.")
        st.stop()

DEFAULT_PERSONA = {"profile":"student","papers":"no","fx":"no","branch":"no","city":"paris","budget":800,"duration":"long"}
def get_persona():
    if "persona" not in st.session_state:
        st.session_state.persona = DEFAULT_PERSONA.copy()
    return st.session_state.persona
def set_persona(p):
    st.session_state.persona = p
def recommended_path(persona):
    order = ["banking","housing","insurance","healthcare","taxation","transport","work","life"]
    if persona.get("profile") == "entrepreneur":
        order = ["banking","work","taxation","insurance","housing","transport","healthcare","life"]
    if persona.get("profile") == "student":
        order = ["banking","housing","healthcare","transport","insurance","taxation","work","life"]
    if persona.get("fx") == "yes":
        if "banking" in order:
            order.remove("banking")
            order.insert(0,"banking")
    return order

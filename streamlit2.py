import streamlit as st

def page_acceuil():
    st.title("IcAre Insurance")
    st.image("image.webp", use_container_width=True)
    if st.button("lancer le questionnaire", key="image_button"):
        st.session_state.page=2
    if st.button("Quitter"):
        st.stop()

def page2():
    st.title("Questionnaire")
    st.write("le questionnaire du Goat")
    if st.button("retour_acceuil"):
        st.session_state.page = 1


if "page" not in st.session_state:
    st.session_state.page = 1


if st.session_state.page == 1:
    page_acceuil()
else:
    page2()            
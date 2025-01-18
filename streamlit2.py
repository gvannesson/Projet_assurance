import streamlit as st

"""def page_acceuil():
    st.title("IcAre Insurance")
    st.image("image.webp", use_container_width=True)
    if st.button("lancer le questionnaire", on_click=lambda: change_page(2), key="image_button"):
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
    page2()    """




def page_acceuil():
    st.title("IcAre Insurance")
    st.image("image.webp", use_container_width=True)
    st.button("Lancer le questionnaire", on_click=lambda: change_page(2), key="image_button")
    st.button("Quitter", on_click=lambda: st.stop())

def page2():
    st.title("Questionnaire")
    st.write("Le questionnaire du Goat")
    st.button("Retour à l'accueil", on_click=lambda: change_page(1))

def change_page(page):
    st.session_state.page = page

# Initialisation de l'état de la session
if "page" not in st.session_state:
    st.session_state.page = 1

# Logique de navigation des pages
if st.session_state.page == 1:
    page_acceuil()
else:
    page2()

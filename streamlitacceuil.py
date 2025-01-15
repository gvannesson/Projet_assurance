import streamlit as st


def page_acceuil():
    st.title("IcAre Insurance")
    if st.button("", key="image_button"):
        st.session_state.page = 2
    st.markdown(
        """
        <style>
        .stButton button {
            background: url("image.webp") no-repeat center center;
            background-size: contain;
            width: 100%;
            height: 300px;
            border: none;
            cursor: pointer;
        }

        </style>
        """,
        unsafe_allow_html=True

    )    
    
    
    if st.button("quitter"):
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
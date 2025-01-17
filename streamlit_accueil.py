import streamlit as st
import pickle
import pandas as pd
import numpy as np
from classe_p import DropFeatureSelector

def page_acceuil():
    st.title("IcAre Insurance")
    st.image("image.webp", use_container_width=True)
    st.button("Complete the survey,", on_click=lambda: change_page(2), key="image_button")
    st.button("Quit", on_click=lambda: st.stop())

def page2():
    st.write("Welcome to Assur Aimant home page!")

    options = ["Northeast", "Northwest", "Southeast", "Southwest"]

    def remise():
        try : 
            discount = round((1-int(st.session_state.remise)/100)*pred , 1)
            st.write(f"Charges proposal : {discount}, without discount : {pred}")
        except:
            st.write("Please enter valid values")

    def calc():
        if st.session_state.size!="" and st.session_state.weight!="":
            try:
                BMI = round(int(st.session_state.weight)/((int(st.session_state.size)/100)**2),1)
                st.write(f"BMI value is {BMI}")
                return BMI
            except:
                st.write("Please enter valid values")

    

    if 'reset' not in st.session_state:
        st.session_state.reset = False

    if st.session_state.reset:
        st.session_state.age_slider=None
        st.session_state.smoker_radio=None
        st.session_state.sex_radio=None
        st.session_state.age_slider=18
        st.session_state.size=""
        st.session_state.weight=""
        st.session_state.children=0
        st.session_state.region=None
        st.session_state.remise=""
        st.session_state.reset=False

    st.write("Enter the client data")
    slider_val = st.slider("Age",  min_value=18, max_value=100, key="age_slider")
    smoker_radio = st.radio("Smoker",["Yes", "No"],index=None, key="smoker_radio")
    sex_radio = st.radio("Sex",["Male", "Female"],index=None, key="sex_radio")
    c1, c2 = st.columns(2)
    with c1:
        st.text_input('Size (cm)',key="size")
    with c2:
        st.text_input('Weight (kg)',key="weight")
    if st.session_state.size!="" and st.session_state.weight!="":
        BMI=calc()
    st.number_input("Children number", step =1,min_value=0,key='children')
    st.pills("Region", options, selection_mode="single", key='region')
    st.text_input('Exceptional discount (%)',key="remise")
    submitted = st.button("Calculate simulation")
    if submitted:
        if st.session_state.smoker_radio==None or st.session_state.sex_radio==None or st.session_state.region==None:
            st.write("At least a parameter was not filled")
        else: 
            with open('best_model.pkl', 'rb') as f:
                pickle_model = pickle.load(f)
            client=[[st.session_state.age_slider,
                    st.session_state.sex_radio.lower(),
                    st.session_state.children,
                    st.session_state.smoker_radio.lower(),
                    st.session_state.region.lower(),
                    BMI]]
            client_array= pd.DataFrame(client, columns=["age","sex","children","smoker","region","bmi"])
            pred= round(pickle_model.predict(client_array)[0],1)
            if st.session_state.remise != "":
                remise()
            else:
                st.write(f"Charges proposal : {pred}")
    if st.button('Reset values', key='w_reset'):
        st.session_state.reset=True
        st.rerun()

    st.button("Homepage", on_click=lambda: change_page(1))

def change_page(page):
    st.session_state.page = page

if "page" not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    page_acceuil()
else:
    page2()
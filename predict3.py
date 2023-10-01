import pickle as pk
import requests
import streamlit as st
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_chat import message as st_message





#loading diabetics model

#css
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return r.json()

hide_st_style = """
                <style>
                #MainMenu { visibility : hidden;}
                footer { visibility : hidden;}
                header { visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style , unsafe_allow_html = True)
                

# use local css
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")





diabetic_model = pk.load(open('diabetes_model.sav','rb'))

#with menu bar
selected = option_menu(
        menu_title ="",
        options =["Diaognysis"],
        icons = ["house"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal")

if selected == "Diaognysis":
    with st.container():
        def add_bg_from_url():
            st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://akm-img-a-in.tosshub.com/indiatoday/images/story/202206/diabetes.jpg?VersionId=m8MNZaJMHPgAraLrCSxe_hhuC5fFZxYX?size=1200:675");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
            unsafe_allow_html=True)
        add_bg_from_url()
    st.title("Diabetic prediction using Machine learning")
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetic_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

    
    
    
    



    




                                                                                    

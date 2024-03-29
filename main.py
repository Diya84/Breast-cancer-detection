import pickle
import streamlit as st
from PIL import Image
image = Image.open('ribbon.jpg')



breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))

#Judul Web
st.image(image)
st.title('Breast Cancer Predictor')



col1, col2 = st.columns(2)

with col1 :
    meanradius = st.text_input('Clump Thickness', 0, 500)
with col1 :
    mean_texture = st.text_input('Uniform cell size', 0, 500)
with col1 :
    mean_perimeter = st.text_input('Uniform cell shape', 0, 500)
with col2 :
    mean_area = st.text_input('Marginal Adhesion', 0, 500)
with col2 :
    mean_smoothness =st.text_input('Normal Nucleoli', 0 , 500)
    
cancer_diagnosis = ''

if st.button('Predict'):
    cancer_prediction = breast_cancer_model.predict([[meanradius, mean_texture, mean_perimeter, mean_area, mean_smoothness ]])
    
    if(cancer_prediction[0] == 1):
        cancer_diagnosis = 'Breast Cancer Detected, we recommend you to visit a doctor'
    else:
        cancer_diagnosis = 'Breast Cancer not Detected'
    
    st.success(cancer_diagnosis, icon="✅")
  

    

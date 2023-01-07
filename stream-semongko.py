import pickle
import streamlit as st

model = pickle.load(open('semangka.sav', 'rb'))

st.title('PREDIKSI KUALITAS SEMANGKA')

Color = st.number_input ('Input Nilai Color')
Root = st.number_input ('Input Nilai Root')
Sound = st.number_input ('Input Nilai Sound')
Texture = st.number_input ('Input Nilai Texture')
Belly_button = st.number_input ('Input Nilai Belly_button')
Touch = st.number_input ('Input Nilai Touch')
Density = st.number_input ('Input Nilai Density')
sugar_rate = st.number_input ('Input Nilai sugar_rate')

health_diagnosis = ''

if st.button('Test Prediction') :
    prediction = model.predict([[Color, Root, Sound, Texture, Belly_button, Touch, Density, sugar_rate]])

    if (prediction[0] == 0):
        diagnosis = 'Kualitas Buruk'
    else :
        diagnosis = 'Kualitas Bagus'
    
st.success(diagnosis)
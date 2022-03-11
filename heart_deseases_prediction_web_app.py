# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 09:37:44 2022

@author: vraj Thakar


Streamlit’s open-source app framework is the easiest way for data scientists and 
machine learning engineers to create beautiful, performant apps in only a few hours!
 All in pure Python. All for free.


"""

import numpy as np
import pickle
import streamlit as st
#uploaded_file = st.file_uploader("C:/Users/vraj Thakar/Desktop/heart diseases_ml/heart_diseases_prediction_trained_model.sav")


#another person
# write loaded model instead of original name model

#loading the saved model -- rb(reading in binary formate)
loaded_model = pickle.load(open("https://github.com/vraj-thakar/centaral_repo/blob/master/heart_diseases_prediction_trained_model.sav","rb"))

#creating the function for prediction

def heart_diseases_pridiction(input_data):
    
    #change to input data into numpy array
    np_array_ip=np.asarray(input_data)
    # print(np_array_ip)

    #reshape the numpy array as we are predicting for only one instance
    np_array_ip_reshaped = np_array_ip.reshape(1,-1)
    # print(np_array_ip_reshaped )

    prediction = loaded_model.predict(np_array_ip_reshaped)

    if(prediction[0]==1):
        return """The person has heart diseases \ntake care and consult with a heart specialist """
    else:
       return """The person does not have heart diseases \n !!have a good life!!"""
    
#make user interface

def main():
    
    
    #giving a title 
    st.title("Heart Diseases Prediction")
    
    html_temp="""
    <div style="background-color:tomato;padding :10px">
    <h2 style ="color:white;text-align:center;"> Heart diseases predictor ML App </h2>
    </div>
    
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    #age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	
    #getting the input data from the user(create 13 variables)
    
    age = st.text_input("The person’s age in years:")
    sex = st.text_input("The person’s sex (1 = male, 0 = female) :")
    cp = st.text_input(""" chest pain type
— [1]Value = 0: asymptomatic\n
— [2]Value = 1: atypical angina\n
— [3]Value = 2: non-anginal pain\n
— [4]Value = 3: typical angina """)
    trestbps = st.text_input("The person’s resting blood pressure (mm Hg on admission to the hospital):")
    chol = st.text_input("The person’s cholesterol measurement in mg/dl :")
    fbs = st.text_input("The person’s fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false) :")
    restecg = st.text_input("""resting electrocardiographic(ECG) results \n
— [1]Value = 0: showing probable or definite left ventricular hypertrophy by Estes’ criteria\n
— [2]Value = 1: normal\n
— [3]Value = 2: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)""")
    thalach = st.text_input("The person’s maximum heart rate achieved :")
    exang = st.text_input("Exercise induced angina (1 = yes; 0 = no) :")
    oldpeak = st.text_input("ST depression induced by exercise relative to rest (‘ST’ relates to positions on the ECG plot. See more here):")
    slope = st.text_input("""the slope of the peak exercise ST segment — 0: downsloping;\n 1: flat;\n 2: upsloping
0: downsloping; 1: flat; 2: upsloping """)
    ca = st.text_input("The number of major vessels (0–3):")
    thal = st.text_input("""A blood disorder called thalassemia\n[1]Value 0: NO\n
[2]Value = 1: fixed defect (no blood flow in some part of the heart)\n
[3]Value = 2: normal blood flow\n
[4]Value = 3: reversible defect (a blood flow is observed but it is not normal)""")
    
    #the code for prediction
    diagnosis=""   #nidan
    
    #creating the bUtton for the prediction
    if st.button("Heart Diseases Test Results"):
        diagnosis= heart_diseases_pridiction([age, sex,	cp,	trestbps, chol,	fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    
    st.success(diagnosis)


if __name__ == '__main__':
    main()

     
    
    
    

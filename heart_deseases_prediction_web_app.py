# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 09:37:44 2022
@author: vraj Thakar
Streamlit’s open-source app framework is the easiest way for data scientists and 
machine learning engineers to create beautiful, performant apps in only a few hours!
 All in pure Python. All for free.
"""


import streamlit as st

nav=st.sidebar.radio("Navigation",["Prediction","Awareness"],index=0)



if nav=="Prediction":
    import pickle
    import numpy as np 
    
    #another person
    # write loaded model instead of original name model
    
    #loading the saved model -- rb(reading in binary formate)
    loaded_model = pickle.load(open(".\heart_diseases_prediction_trained_model.sav","rb"))
    
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
           return """The person does not have heart diseases \n !!have a good day!!"""
        
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
    



elif nav == "Awareness":
    st.image("hearthealth.jpg",width=800)

    html_temp2="""
    <div style="background-color:grey;padding :10px">
    <h3 style ="color:white;"> Heart disease is a leading cause of death, but it's not inevitable. While you can't change some risk factors — such as family history, sex or age — there are plenty of ways you can reduce your risk of heart disease.

Get started with these seven tips for boosting your heart health:

1. "Don't smoke or use tobacco"
One of the best things you can do for your heart is to stop smoking or using smokeless tobacco. Even if you're not a smoker, be sure to avoid secondhand smoke.

Chemicals in tobacco can damage the heart and blood vessels. Cigarette smoke reduces the oxygen in the blood, which increases blood pressure and heart rate because the heart has to work harder to supply enough oxygen to the body and brain.

There's good news though. The risk of heart disease starts to drop in as little as a day after quitting. After a year without cigarettes, the risk of heart disease drops to about half that of a smoker. No matter how long or how much you smoked, you'll start reaping rewards as soon as you quit.

2. "Get moving: Aim for at least 30 to 60 minutes of activity daily"
Regular, daily physical activity can lower the risk of heart disease. Physical activity helps control your weight. It also reduces the chances of developing other conditions that may put a strain on the heart, such as high blood pressure, high cholesterol and type 2 diabetes.

If you haven't been active for a while, you may need to slowly work your way up to these goals, but in general, you should do aim for at least:

150 minutes a week of moderate aerobic exercise, such as walking at a brisk pace
75 minutes a week of vigorous aerobic activity, such as running
Two or more strength training sessions a week
Even shorter bouts of activity offer heart benefits, so if you can't meet those guidelines, don't give up. Just five minutes of moving can help, and activities such as gardening, housekeeping, taking the stairs and walking the dog all count toward your total. You don't have to exercise strenuously to achieve benefits, but you can see bigger benefits by increasing the intensity, duration and frequency of your workouts.

3. "Eat a heart-healthy diet"
A healthy diet can help protect the heart, improve blood pressure and cholesterol, and reduce the risk of type 2 diabetes. A heart-healthy eating plan includes:

Vegetables and fruits
Beans or other legumes
Lean meats and fish
Low-fat or fat-free dairy foods
Whole grains
Healthy fats, such as olive oil
Two examples of heart-healthy food plans include the Dietary Approaches to Stop Hypertension (DASH) eating plan and the Mediterranean diet.

Limit intake of the following:

Salt
Sugar
Processed carbohydrates
Alcohol
Saturated fat (found in red meat and full-fat dairy products) and trans fat (found in fried fast food, chips, baked goods)
4. "Maintain a healthy weight"
Being overweight — especially around the middle of the body — increases the risk of heart disease. Excess weight can lead to conditions that increase the chances of developing heart disease — including high blood pressure, high cholesterol and type 2 diabetes.

The body mass index (BMI) uses height and weight to determine whether a person is overweight or obese. A BMI of 25 or higher is considered overweight and is generally associated with higher cholesterol, higher blood pressure, and an increased risk of heart disease and stroke.

Waist circumference also can be a useful tool to measure how much belly fat you have. The risk of heart disease is higher if the waist measurement is greater than:

40 inches (101.6 centimeters, or cm) for men
35 inches (88.9 cm) for women
Even a small weight loss can be beneficial. Reducing weight by just 3% to 5% can help decrease certain fats in the blood (triglycerides), lower blood sugar (glucose) and reduce the risk of type 2 diabetes. Losing even more helps lower blood pressure and blood cholesterol level.

5. "Get good quality sleep"
People who don't get enough sleep have a higher risk of obesity, high blood pressure, heart attack, diabetes and depression.

Most adults need at least seven hours of sleep each night. Make sleep a priority in your life. Set a sleep schedule and stick to it by going to bed and waking up at the same times each day. Keep your bedroom dark and quiet, so it's easier to sleep.

If you feel like you've been getting enough sleep but you're still tired throughout the day, ask your health care provider if you need to be evaluated for obstructive sleep apnea, a condition that can increase your risk of heart disease. Signs of obstructive sleep apnea include loud snoring, stopping breathing for short times during sleep and waking up gasping for air. Treatments for obstructive sleep apnea may include losing weight if you're overweight or using a continuous positive airway pressure (CPAP) device that keeps your airway open while you sleep.

6. "Manage stress"
Some people cope with stress in unhealthy ways — such as overeating, drinking or smoking. Finding alternative ways to manage stress — such as physical activity, relaxation exercises or meditation — can help improve your health.

7. "Get regular health screenings"
High blood pressure and high cholesterol can damage the heart and blood vessels. But without testing for them, you probably won't know whether you have these conditions. Regular screening can tell you what your numbers are and whether you need to take action.

Blood pressure. Regular blood pressure screenings usually start in childhood. Starting at age 18, blood pressure should be measured at least once every two years to screen for high blood pressure as a risk factor for heart disease and stroke.

If you're between 18 and 39 and have risk factors for high blood pressure, you'll likely be screened once a year. People age 40 and older also are given a blood pressure test yearly.

Cholesterol levels. Adults generally have their cholesterol measured at least once every four to six years. Cholesterol screening usually starts at age 20, though earlier testing may be recommended if you have other risk factors, such as a family history of early-onset heart disease.
Type 2 diabetes screening. Diabetes is a risk factor for heart disease. If you have risk factors for diabetes, such as being overweight or having a family history of diabetes, your health care provider may recommend early screening. If not, screening is recommended beginning at age 45, with retesting every three years.
If you have a condition such as high cholesterol, high blood pressure or diabetes, your health care provider may prescribe medications and recommend lifestyle changes. Make sure to take your medications as your health care provider prescribes and follow a healthy-lifestyle plan.</h3>
    </div>
    
    """
    st.markdown(html_temp2, unsafe_allow_html=True)
    html_temp3="""
        <div style="background-color:white;padding :10px">
        <h2 style ="color:black;text-align:center;"> Some Other Tipes... </h2>
        </div>
        
        """
    st.markdown(html_temp3, unsafe_allow_html=True)
    st.image("heart-1awer.jpg")
    st.image("heart-2awer.jpg")
    st.image("heart-3awer.jpg")

    html_temp4="""
        <div style="background-color:white;padding :10px">
        <h2 style ="color:blue;text-align:center;"> Have a Nice Day </h2>
       
        </div>
        
        """
    st.markdown(html_temp4, unsafe_allow_html=True)
    html_temp5="""
        <div style="background-color:pink;padding :10px">
        
        <h1 style ="color:red;text-align:center;"> "Stay Safe, Stay Healthy" </h1>
        </div>
        
        """
    st.markdown(html_temp5, unsafe_allow_html=True)
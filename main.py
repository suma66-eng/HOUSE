import streamlit as st
import numpy as np
import joblib
#uploading the model
model= joblib.load("rf.pkl")
st.title("House Price Prediction")
st.markdown("---")
bedroom =st.number_input("Enter the number of bedroom",min_value=0,value=0)
bathroom =st.number_input("Enter the number of bathroom",min_value=0,value=0)
living_area =st.number_input("Enter the number of living_area",min_value=2000,value=2000)
condition_of_house =st.number_input("Enter the condition",min_value=0,value=0)
school =st.number_input("School number",min_value=0,value=0)

x=[[bedroom,bathroom,living_area,condition_of_house,school]]

pred=st.button("Predict")

if pred==True:
    np_array=np.array(x)
    price=int(model.predict(np_array)[0])
    st.write(f"House price={price}")
else:
    st.write(f"please click")

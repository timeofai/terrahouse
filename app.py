import streamlit as st
import pickle
import pandas as pd

pickle_in = open('modelfile.pkl', 'rb')
model = pickle.load(pickle_in)

st.title("Welcome to Crop recommendation engine!")

st.write("Please enter the required parameters\n")

pH = st.number_input("pH")
N = st.number_input("N")
P = st.number_input("P")
K = st.number_input("K")
OC = st.number_input("OC")
Particles = st.number_input("Particles")
Water_holding_content = st.number_input("Water holding content")
soil = st.text_input("Soil type from clay, Sandy, loamy")

Soil_type = 0

if(soil == "clay"):
    Soil_type = 1
elif (soil == "sandy"):
    Soil_type = 2
elif (soil == "loamy"):
    Soil_type = 3


# Create a dataframe to input
input_variables = pd.DataFrame([[pH, N, P, K, OC, Particles, Water_holding_content, Soil_type]],
                                columns=[pH, N, P, K, OC, Particles, Water_holding_content, Soil_type],
                                dtype=float)

prediction = model.predict(input_variables)[0]

if(prediction == 1):
    st.write("Carrot")
elif prediction == 2:
    st.write("Coconut")
elif prediction == 3:
    st.write("Cotton")
elif prediction == 4:
    st.write("Groundnut")
elif prediction == 5:
    st.write("Melon")
elif prediction == 6:
    st.write("Millet")
elif prediction == 7:
    st.write("Potatoes")
elif prediction == 8:
    st.write("Rice")
elif prediction == 9:
    st.write("Vegetable")
elif prediction == 10:
    st.write("Wheat")






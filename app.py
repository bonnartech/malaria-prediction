# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:22:38 2023

@author: Bonn_arts
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Bonn_arts/pred/trained_model.sav', 'rb'))


def malaria_prediction(input_data):
   


    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==1):
        return'outbreak; control measures: vector control, case management and vaccines'
    else:
        return 'medium threat; control measures: antimalaria, IRS, ITN'
    
    
    

def main():
    st.title('Malaria prediction web app')

    r = st.number_input('value of Rainfall',)
    m = st.number_input('value of Min-Temperature')
    mt = st.number_input('value of Max-temprature')
    rel1 = st.number_input('value of Relative humidity 1(0800hrs)' )
    rel2 = st.number_input('value of Relative humidity 2(1400hrs)' )
    mosqp = st.number_input('value of Mosquito population')
    case = st.number_input('number of cases')

    diagnosis = ""

    if st.button('test result'):
        diagnosis = malaria_prediction([r,m,mt,rel1 ,rel2,mosqp,case])
    
        st.success(diagnosis)




if __name__=='__main__':
    main()

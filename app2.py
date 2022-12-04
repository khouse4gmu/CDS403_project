import pickle
import streamlit as st
import pandas as pd

 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Pick_rate, On_fire, Encoded_hero, Win_rate):   
    # Making predictions 
    prediction = classifier.predict( 
        [[Pick_rate, On_fire, Encoded_hero, Win_rate]]) 
    pred = prediction
    return pred
      
  
# this is the main function in which we define our webpage  

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Overwatch Class Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    # following lines create boxes in which user can enter data required to make prediction 
    Pick_rate = st.number_input('What was the pick rate?', key = 1)
    On_fire = st.number_input('The percentage of you on fire', key = 2)
    Encoded_hero = st.slider('What hero are you', 0, 31, 1, key = 3)
    heroes = ['Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'D.Va',
        'Doomfist', 'Echo', 'Genji', 'Hanzo', 'Junkrat', 'Lúcio', 'McCree',
        'Mei', 'Mercy', 'Moira', 'Orisa', 'Pharah', 'Reaper', 'Reinhardt',
        'Roadhog', 'Sigma', 'Soldier: 76', 'Sombra', 'Symmetra',
        'Torbjörn', 'Tracer', 'Widowmaker', 'Winston', 'Wrecking Ball',
        'Zarya', 'Zenyatta']
    st.write("I'm ", heroes[Encoded_hero])
    Win_rate = st.number_input("What was your win rate?", key = 4)
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Pick_rate, On_fire, Encoded_hero, Win_rate) 
        st.success('Your class is is {}'.format(result))

     
if __name__=='__main__': 
    main()
import streamlit as st
from PIL import Image
import random

if 'test' not in st.session_state:
    st.session_state['test']=0
def calling_machine():
    st.write(f"THE ATTEMPTS LEFT FOR THE MACHINE ARE {st.session_state.num_attempt}")
    st.write(f"Is your number {st.session_state.guess}?")
    
    button = st.multiselect("Is the guessed value:", ["None","Correct!", "Too High", "Too Low"], key=f"guess_{st.session_state.n}")
    
    if "None" in button:
        st.session_state['test'] == 3
        
    elif "Correct!" in button:
        st.write("Yay! The machine guessed your number!")
        st.session_state.low = 1
        st.session_state.high = 50
    elif "Too High" in button:
        st.session_state.high = st.session_state.guess - 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        st.experimental_rerun()
    else:
        st.session_state.low = st.session_state.guess + 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

        

def call():
    if st.checkbox("GUESS BY USER"):
        st.session_state['test']=1
        st.write("CLICK ONE MORE TIME")
    elif st.checkbox("GUESS BY MACHINE"):
        st.session_state['test']=2
        st.write("CLICK ONE MORE TIME")
def guessing_game_user():
    if 'num_to_be_guessed' not in st.session_state:
        st.session_state['num_to_be_guessed'] = random.randint(1, 50)
    if 'count' not in st.session_state:
        st.session_state['count'] = 1
    
    st.markdown("<h3 style='text-align:center; color:slateblue; font-weight:bold;'> GUESSING GAME</h3>", unsafe_allow_html=True)

    if st.session_state['count'] < 6:
        guessed_number = st.text_input(label='ENTER YOUR GUESSED NUMBER between 1 to 50:', key='num_input')
        if st.session_state['count'] == 1:
            st.write("YOU HAVE 5 CHANCES")
        else:
            n = 5 - (st.session_state['count'] - 1)
            st.write(f"YOU HAVE {n} CHANCES")

        if guessed_number:
            guessed_number = int(guessed_number)
            if guessed_number > 50 or guessed_number < 1:
                st.write("INVALID INPUT")
            elif guessed_number == st.session_state['num_to_be_guessed']:
                st.write("CONGRATULATIONS, YOU WIN!")
            else:
                st.write(f'ATTEMPT: {st.session_state["count"]}')
                st.write("SORRY, TRY AGAIN")
                st.session_state['count'] += 1
                if guessed_number < st.session_state['num_to_be_guessed']:
                    st.write("THE NUMBER TO BE GUESSED IS GREATER THAN YOUR INPUT NUMBER")
                else:
                    st.write("THE NUMBER TO BE GUESSED IS SMALLER THAN YOUR INPUT NUMBER")
    else:
        st.write("SORRY, YOU FAILED. The number was:", st.session_state['num_to_be_guessed'])
        if st.button("Play Again"):
            guessing_game_user()
def machine_guessing_game():
    st.write("Think of a number between 1 and 50")
    st.write("If you decided click start")
    if 'n' not in st.session_state:
        st.session_state.n=0
    if st.checkbox("start",key=f"starts_{st.session_state.n}"):
        st.session_state.n += 1
        if 'num_attempt' not in st.session_state:
            st.session_state.num_attempt= 6
        if 'low' not in st.session_state:
            st.session_state.low = 1
        if 'high' not in st.session_state:
            st.session_state.high = 50
        if 'guess' not in st.session_state:
            st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
        if st.session_state.num_attempt >0:
            st.session_state.num_attempt-=1
            calling_machine()
              
        else:
            st.write("Yay!you win ")


if st.session_state['test'] == 0:
    
    st.markdown("<h1 style='text-align:center; color:indigo; font-weight:bold;'>PORTFOLIO</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
        
    with col2:
        st.image("C:\Users\aruna\OneDrive\Desktop\python\IMG_20241031_113601_647.webp", caption="This is your image!", use_column_width=True)

    with col1:
        def reuse(a, b):
            title, desc = a, b
            st.markdown(f"<h2 style='text-align:left; color:slateblue; font-weight:bold;'> {title} :- {desc} </h2>", unsafe_allow_html=True)

        reuse("NAME", "ARUNAW RISHE M")
        reuse("PROFESSIONAL", "STUDENT & DEVELOPER")
        reuse("INTEREST", "JAVA DEVELOPER")
        reuse("GITHUB ACCOUNT", "https://github.com/ARUNAWRISHE/new")

    st.markdown("<h3 style='text-align:left; color:slateblue; font-weight:bold;'> DO YOU LIKE TO TRY MY GUESSING GAME</h3>", unsafe_allow_html=True)
    if st.checkbox("YES"):
        st.write(" CHOOSE A WAY YOU'D LIKE TO PLAY MY GUESSING GAME")
        call()
    if st.checkbox("NO"):
        st.write("CLICK  ONE MORE TIME FOR CONFORM")
        st.session_state['test']=3
else:
    st.session_state['test']=int(st.session_state['test'])
    if st.session_state['test'] == 1:
        guessing_game_user()
    elif st.session_state['test']== 2:
        machine_guessing_game()
    elif st.session_state['test'] == 3:
        st.write("THANKS FOR VISITING MY PAGE")
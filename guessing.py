import streamlit as st
from PIL import Image
import random

if 'test' not in st.session_state:
    st.session_state['test']=0
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
            st.stop()
def machine_guessing_game():
    

    low = 1
    high = 50
    attempts = 5

    st.title("Number Guessing Game!")
    st.write("Think of a number between 1 and 50, and I'll try to guess it.")

    if 'attempt' not in st.session_state:
        st.session_state.attempt = 0
        st.session_state.low = low
        st.session_state.high = high

    if st.session_state.attempt < attempts:
        guess = (st.session_state.low + st.session_state.high) // 2
        st.write(f"Is your number {guess}?")
        
        response = st.radio("Please select:", ('Correct', 'High', 'Low'))

        if st.button("Submit"):
            if response == 'Correct':
                st.success(f"Yay! I guessed your number {guess} in {st.session_state.attempt + 1} attempts.")
                st.session_state.attempt = attempts  # End game
            elif response == 'High':
                st.session_state.high = guess - 1
            elif response == 'Low':
                st.session_state.low = guess + 1
            
            st.session_state.attempt += 1
            
    else:
        st.error("I couldn't guess your number within 5 attempts. Better luck next time!")



if st.session_state['test'] == 0:
    
    st.markdown("<h1 style='text-align:center; color:indigo; font-weight:bold;'>PORTFOLIO</h1>", unsafe_allow_html=True)

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
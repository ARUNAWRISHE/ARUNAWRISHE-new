from PIL import Image
import random
import streamlit as st

test=0
def call():
    if st.button("guessing game by you"):
            test= 1
    else:
        st.button("guessing game by machine")
        test = 2
def portfolio_page():
    st.markdown("<h1 style='text-align:center; color:indigo; font-weight:bold;'>PORTFOLIO</h1>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("IMG_20241031_113601_647", type="webp", key="uploader1")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image = image.resize((200, 200))
        col1, col2 = st.columns([3, 1])
        
        with col2:
            st.image(image)

        with col1:
            def reuse(a, b):
                title, desc = a, b
                st.markdown(f"<h2 style='text-align:left; color:slateblue; font-weight:bold;'> {title} :- {desc} </h2>", unsafe_allow_html=True)

            reuse("NAME", "ARUNAW RISHE M")
            reuse("PROFESSIONAL", "STUDENT & DEVELOPER")
            reuse("INTEREST", "JAVA DEVELOPER")
            reuse("GITHUB ACCOUNT", "https://github.com/ARUNAWRISHE/new")

    st.markdown("<h3 style='text-align:left; color:slateblue; font-weight:bold;'> DO YOU LIKE TO TRY MY GUESSING GAME</h3>", unsafe_allow_html=True)
    if st.button("YES"):
        call()
    else:
        st.button("NO")
        test = 3

def guessing_game_user():
    st.markdown("<h3 style='text-align:left; color:slateblue; font-weight:bold;'> CHOOSE A WAY YOU'D LIKE TO PLAY MY GUESSING GAME</h3>", unsafe_allow_html=True)
    if st.button("GUESS BY YOU"):
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
                        st.session_state['count'] = 1
                    else:
                        st.write(f'ATTEMPT: {st.session_state["count"]}')
                        st.write("SORRY, TRY AGAIN BY CLEARING THE PREVIOUS INPUT")
                        st.session_state['count'] += 1
                        if guessed_number < st.session_state['num_to_be_guessed']:
                            st.write("THE NUMBER TO BE GUESSED IS GREATER THAN YOUR INPUT NUMBER")
                        else:
                            st.write("THE NUMBER TO BE GUESSED IS SMALLER THAN YOUR INPUT NUMBER")
                
        else:
            st.write("SORRY, YOU FAILED. The number was:", st.session_state['num_to_be_guessed'])
            if st.button("Play Again"):
                st.session_state['count'] = 1

def machine_guessing_game():
    st.write("THINK OF A NUMBER BETWEEN 1 AND 50")
    if st.button("START"):
        low, high = 1, 50
        num_attempts = 5
        while num_attempts > 0:
            mid = (low + high) // 2
            st.write(f"Is your number {mid}?")
            if st.button("YES"):
                st.write("Yay! The machine guessed your number!")
                return
            elif st.button("NO"):
                num_attempts -= 1
                st.write(f"The machine has {num_attempts} chances left")
                st.write("Is the number greater or smaller?")
                if st.button("GREATER"):
                    low = mid + 1
                elif st.button("SMALLER"):
                    high = mid - 1
        st.write("Out of attempts! You win!")
if test ==0:
    portfolio_page()
else:
    if test == 1:
        guessing_game_user()
    elif test == 2:
        machine_guessing_game()
    else:
        st.write("THANKS FOR VISITING MY PAGE")

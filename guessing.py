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
            guessing_game_user()
def machine_guessing_game():
    st.write("THINK OF A NUMBER BETWEEN 1 AND 50")
    arr=range(1,51)
    low=0
    high=len(arr)
    for i in range(5):
        if st.checkbox("START"):
            num_attempts=5
            mid = (low + high) // 2
            st.write(f"Is  your  number  {mid}?")
            if st.checkbox("YES")==1:
                st.write("Yay! The machine guessed your number!")
            if st.checkbox("NO"):
                num_attempts -= 1
                st.write("The machine has {num_attempts} chances left")
                st.write(f"Whether your guessed number is ")
                if num_attempts > 0:
                    if st.checkbox(f"GREATER THAN {mid}"):
                        low = mid + 1
                    elif st.checkbox(f"SMALLER  THAN {mid}"):
                        high = mid - 1
                else:
                    st.write("Out of attempts! You win!")

if st.session_state['test'] == 0:
    
    st.markdown("<h1 style='text-align:center; color:indigo; font-weight:bold;'>PORTFOLIO</h1>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload an image", type="webp", key="uploader1")
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
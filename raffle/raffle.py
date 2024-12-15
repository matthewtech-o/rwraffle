import streamlit as st
import random
import time
from streamlit_lottie import st_lottie

# Lottie Animation URLs (replace with your desired animation JSONs)
LOTTIE_URL_WINNER = "https://assets9.lottiefiles.com/packages/lf20_touohxv0.json"  # Celebration animation
LOTTIE_URL_LOADING = "https://assets4.lottiefiles.com/private_files/lf30_m6j5igxb.json"  # Rolling animation

# Functions to load Lottie animations
def load_lottieurl(url: str):
    import requests
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animations
lottie_winner = load_lottieurl(LOTTIE_URL_WINNER)
lottie_loading = load_lottieurl(LOTTIE_URL_LOADING)

# Company Branding
COMPANY_LOGO_URL = "/Users/matthewoladiran/Downloads/redwire-logo-color (2).svg"  # Replace with your logo path or URL
PRIMARY_COLOR = "#ff0713"
TEXT_COLOR = "#000000"  # Black for numbers
BG_COLOR = "#FFFFFF"

# Custom CSS for styling
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {BG_COLOR};
        }}
        .title {{
            font-size: 36px;
            font-weight: bold;
            color: {PRIMARY_COLOR};
            text-align: center;
        }}
        .winner {{
            font-size: 28px;
            color: {PRIMARY_COLOR};
            text-align: center;
        }}
        .instructions {{
            font-size: 18px;
            color: {PRIMARY_COLOR};
            text-align: center;
        }}
        .numbers {{
            font-size: 16px;
            color: {TEXT_COLOR};
            text-align: center;
        }}
        .button {{
            background-color: {PRIMARY_COLOR} !important;
            color: white !important;
        }}
    </style>
""", unsafe_allow_html=True)

# Display Company Logo
st.image(COMPANY_LOGO_URL, use_column_width=True)

# App Title
st.markdown('<div class="title">EOYD Raffle Draw</div>', unsafe_allow_html=True)

# Instructions
st.markdown("""
<div class="instructions">
Welcome to the EOYD Raffle Draw! Below are the 30 random numbers participating in this draw. 
Click the button **once per winner** to reveal the lucky winners with a rolling effect!
</div>
""", unsafe_allow_html=True)

# List of numbers (stored in session state to retain across button presses)
if "numbers" not in st.session_state:
    st.session_state.numbers = [
        1, 3, 5, 7, 9, 13, 17, 19, 26, 35, 68, 97, 81, 73, 99, 42, 58, 33,
        180, 365, 208, 537, 791, 112, 850, 972, 623, 425, 379, 777
    ]

if "winners" not in st.session_state:
    st.session_state.winners = []

# Display the numbers in the draw
st.markdown('<div class="instructions">**Numbers in the Draw:**</div>', unsafe_allow_html=True)
st.markdown(f'<div class="numbers">{", ".join(map(str, st.session_state.numbers))}</div>', unsafe_allow_html=True)

# Pick a Winner Button
if st.button("Pick a Winner", key="pick_winner"):
    if st.session_state.numbers:
        # Show rolling animation
        st.markdown('<div class="instructions">Rolling the numbers... 🎲</div>', unsafe_allow_html=True)
        st_lottie(lottie_loading, height=150, key="loading")
        time.sleep(3)  # Delay to simulate rolling
        
        # Select the winner
        winner = random.choice(st.session_state.numbers)
        st.session_state.numbers.remove(winner)
        st.session_state.winners.append(winner)

        # Display winner with celebration animation
        st_lottie(lottie_winner, height=200, key="winner")
        st.markdown(f'<div class="winner">🎉 The winner is: **{winner}** 🎉</div>', unsafe_allow_html=True)
    else:
        st.warning("All numbers have been picked!")

# Display Winners So Far
if st.session_state.winners:
    st.markdown('<div class="instructions">**Winners So Far:**</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="numbers">{", ".join(map(str, st.session_state.winners))}</div>', unsafe_allow_html=True)

# End Message
if len(st.session_state.winners) >= 2:
    st.markdown(f'<div class="instructions">✨ All winners have been selected! ✨</div>', unsafe_allow_html=True)
import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Adds A-Z & a-z

    if use_digits:
        characters += string.digits  # Adds Numbers (0-9)

    if use_special:
        characters += string.punctuation  # Adds Special Characters (!, @, #, etc.)

    return ''.join(random.choice(characters) for _ in range(length))  # Generates Password

# Streamlit UI
st.title("🔑 Password Generator")

length = st.slider(" Select Password Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox(" Include Numbers")
use_special = st.checkbox(" Include Special Characters")

if st.button(" Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f" **Generated Password:** `{password}`")  # Styled output

st.write("---")  # Divider
st.write("Built with ❤️ by [Areesha Nadeem](https://github.com/AreeshaNadeem973)")

import streamlit as st
import random

# List of texts to display
texts = [
    "Hello, World!",
    "Welcome to my Streamlit app!",
    "This is a random text.",
    "Keep clicking to see more!",
    "Have a great day!"
]

# Initialize session state for the selected text
if 'selected_text' not in st.session_state:
    st.session_state.selected_text = random.choice(texts)

# Title of the app
st.title("Regenerate Text Example")

# Display the selected text
st.write(st.session_state.selected_text)

# Button to regenerate text
if st.button("Regenerate"):
    st.session_state.selected_text = random.choice(texts)
    st.success("Text regenerated!")

# Optional: Display the current text for clarity
st.write(f"Current Text: {st.session_state.selected_text}")
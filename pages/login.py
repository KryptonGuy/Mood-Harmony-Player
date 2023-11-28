import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from login.loginBO import *
import spotipy

st.set_page_config(
    page_title="Mood Harmony Player",
    page_icon="🎧",
    initial_sidebar_state="collapsed" 
)

sp_oauth, auth_url = authenticate_spotify()

#If Already Login
if get_spotify_token():
    switch_page("Player")

# Login Button
st.write("<h2 style='text-align:left;'>Login with Spotify</h2>",unsafe_allow_html=True)
loginButton(auth_url)

# Callback 
code = st.experimental_get_query_params().get("code", [None])[0]

if code:
    try:
        token_info = sp_oauth.get_access_token(code, as_dict = True, check_cache=False)
        access_token = token_info['access_token']
    except SpotifyException as e:
        clear_session()
        st.error(f"Error during login: {str(e.reason)}")

    try:
        set_spotify_token(access_token)
        st.success("Login successful!")
        switch_page("Player")

    except SpotifyException as e:
        clear_session()
        st.error(f"Error during login: {str(e.reason)}")




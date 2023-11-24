import streamlit as st
from login.loginBO import *
import spotipy
from streamlit_extras.switch_page_button import switch_page 
import time


st.set_page_config(
    page_title="Mood Harmony Player",
    page_icon="🎧",
    initial_sidebar_state="collapsed" 
)


if get_spotify_token():
    try:
        sp = spotipy.Spotify(auth=get_spotify_token())
        name = sp.current_user()['display_name']
    except SpotifyException as e:
        clear_session()
        st.error(f"Error playing track: {str(e.reason)}")
        time.sleep(2)
        switch_page("login")

    st.write(f"Welcome to Mood Harmony Player! 👋, {name}")

else:
    switch_page("login")
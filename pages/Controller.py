import streamlit as st
import spotipy
from login.loginBO import *
from streamlit_extras.switch_page_button import switch_page 
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mood Harmony Player",
    page_icon="🎧",
    initial_sidebar_state="collapsed" 
)

if not get_spotify_token():
    switch_page("Player")

sp = spotipy.Spotify(auth=get_spotify_token())

search_query = st.text_input("Search for a song:")
if st.button("Search and Play"):
    results = sp.search(q=search_query, type="track", limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        frame = f'<iframe id={track_uri} src="https://open.spotify.com/embed/track/{track_uri[14:]}"  frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'
        try:
            sp.start_playback(uris=[track_uri])
        except SpotifyException as e:
            st.warning(f"Unable to play song: {e.reason}")
        st.write()
        components.html(frame, height=90)
        st.success(f"Playing: {results['tracks']['items'][0]['name']} by {results['tracks']['items'][0]['artists'][0]['name']}")
    else:
        st.warning("No matching songs found.")

# Arrange buttons in a horizontal layout
col1, col2, col3, col4 = st.columns(4)

# Go back to the previous track
if col1.button("⏮️"):
    try:
        sp.previous_track()
    except SpotifyException as e:
        st.warning(f"Unable to perform operation: {e.reason}")

# Pause the playback
if col2.button("⏸️"):
    try:
        sp.pause_playback()
    except SpotifyException as e:
        st.warning(f"Unable to perform operation: {e.reason}")

# Resume playback
if col3.button("▶️"):
    try:
        sp.start_playback()
    except SpotifyException as e:
        st.warning(f"Unable to perform operation: {e.reason}")

# Skip to the next track
if col4.button("⏭️"):
    try:
        sp.next_track()
    except SpotifyException as e:
        st.warning(f"Unable to perform operation: {e.reason}")


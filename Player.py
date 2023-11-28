import streamlit as st
from login.loginBO import *
import spotipy
from streamlit_extras.switch_page_button import switch_page 
import time
from model.modelBO import *
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Mood Harmony Player",
    page_icon="🎧",
    initial_sidebar_state="collapsed" 
)

def play_tracks(tracks, sp):
    try:
        new = []
        for elem in tracks:
            new.append("spotify:track:" +elem)
        sp.start_playback(uris=new)
    except SpotifyException as e:
            st.error(f"Error playing track: {str(e.reason)}")

def populate_tracks(tracks: list) -> None:
    frame = '<iframe id={} src="https://open.spotify.com/embed/track/{}" width="230" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'
    tag = "<h4 style='text-align: center;'>Top Tracks</h4>"
    st.markdown(tag, unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns([3, 3, 3])
        for i, track in enumerate(tracks):
            if i % 3 == 0:
                with col1:
                    components.html(frame.format(track, track), height=400)

            elif i % 3 == 1:
                with col2:
                    components.html(frame.format(track, track), height=400)
            else:
                with col3:
                    components.html(frame.format(track, track), height=400)


if get_spotify_token():
    try:
        sp = spotipy.Spotify(auth=get_spotify_token())
        name = sp.current_user()['display_name']
    except SpotifyException as e:
        clear_session()
        st.error(f"Error playing track: {str(e.reason)}")
        time.sleep(2)
        switch_page("login")

    st.write(f"## Welcome to Mood Harmony Player! 👋, {name}")
    image = st.camera_input("")
    if image:
        emotion = detect_emotion(image)
        if emotion:
            st.write(f"<h3 style='text-align:left;'>You seems to be {emotion}</h3>", unsafe_allow_html=True)
            #st.write(f"### Your emotion is {emotion}") 
            tracks_ids = get_tracks(emotion)
            tracks_li = []
            for i in range(0,100,50):
                tracks_li += sp.tracks(tracks_ids[i:i+50])['tracks']

            
            tracks = k_most_popular(tracks_li,15)
            play_tracks(tracks, sp)
            populate_tracks(tracks)
        else:
            st.write("<h3 style='text-align: center;'>Unable to Detect Face</h3>")

else:
    switch_page("login")
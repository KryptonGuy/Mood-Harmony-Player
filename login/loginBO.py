from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException
import streamlit as st


def authenticate_spotify():

    SPOTIPY_CLIENT_ID = st.secrets["secrets"]['SPOTIPY_CLIENT_ID']
    SPOTIPY_CLIENT_SECRET = st.secrets["secrets"]['SPOTIPY_CLIENT_SECRET']
    SPOTIPY_REDIRECT_URI = st.secrets["secrets"]['SPOTIPY_REDIRECT_URI']
 
    try:
        sp_oauth = SpotifyOAuth(
            SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope='user-library-read user-modify-playback-state'
        )
        auth_url = sp_oauth.get_authorize_url()
        return sp_oauth, auth_url
    
    except SpotifyException as e:
        clear_session()
        st.error(f"Error playing track: {str(e.reason)}")
    

def get_spotify_token():
    return st.session_state.get('spotify_token', None)

def set_spotify_token(token):
    st.session_state.spotify_token = token
    
def loginButton(auth_url):
    auth_url_placeholder = st.empty()
    login_button = f'''
    <a href="{auth_url}" target="_blank" style="display: inline-block; background-color: #1DB954; color: white; padding: 10px; text-decoration: none; border-radius: 5px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Spotify_icon.svg" alt="Spotify Logo" style="vertical-align: middle; width: 20px; height: 20px; margin-right: 5px;">
        Login with Spotify
    </a>
    '''
    auth_url_placeholder.markdown(login_button, unsafe_allow_html=True)
    
def clear_session():
    st.session_state.clear()
# Mood Harmony Player

Welcome to Mood Harmony Player, your personalized music recommendation application! Mood Harmony Player integrates facial emotion detection with Spotify's music catalog to recommend playlists tailored to your emotional state.

## Live Demo

Check out the live demo at [Mood Harmony Player](https://moodharmonyplayer.streamlit.app).

## Overview

Mood Harmony Player leverages cutting-edge technologies and frameworks to deliver a seamless and personalized music recommendation experience. Here's a brief overview of the key components:

- **Frontend Framework:** Streamlit
- **Authentication:** Spotify API
- **Emotion Detection:** FER (Facial Emotion Recognition) Model
- **Clustering Algorithm:** K Means
- **Machine Learning Libraries:** scikit-learn, TensorFlow, Keras
- **Data Manipulation:** NumPy, Pandas
- **Image Processing:** Pillow
- **Websockets:** websockets
- **Deployment:** Docker
- **Web Server:** Nginx (used as a reverse proxy)
- **API Client:** Spotipy (Spotify API wrapper)

## Features

- **Spotify Authentication:** Log in through Spotify to access personalized recommendations.
- **Emotion Detection:** Capture facial expressions through the camera, process the image using the FER model, and determine the user's emotional state.
- **Music Clustering:** Use K Means clustering on the Muse dataset to categorize music based on valence, arousal, and dominance values.
- **Playlist Generation:** Randomly select 150 songs from the identified emotional cluster and query Spotify API to check their popularity.
- **Top 15 Recommendations:** Present the user with the top 15 recommended songs matching their emotional state.
- **Spotify Integration:** Play the recommended songs directly on the user's Spotify account using the Spotify API.

## Usage

1. **Install Dependencies:** Install the required Python packages using `pip install -r requirements.txt`.

2. **Set Up Spotify API:**
   - Create a Spotify Developer account and set up your application.
   - Update the `secrets.toml` file with your Spotify API credentials.

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the Application:**
   Open your web browser and navigate to http://localhost:8501.

## Deployment

The application is deployed using Docker and Nginx for reverse proxy. Follow these steps to deploy the application on a server:

1. **Build Docker Image:**
   ```bash
   docker build -t mood-harmony-player .
   ```

2. **Run Docker Container:**
   ```bash
   docker run -p 80:80 mood-harmony-player
   ```

3. **Access the Deployed Application:**
   Open your web browser and navigate to your server's IP address or domain.


## Acknowledgments

This project is made possible by the contributions of various open-source libraries and frameworks. Special thanks to the developers of Streamlit, Spotipy, scikit-learn, TensorFlow, and others.

## License

This project is licensed under the [GPL-3.0 License](LICENSE).


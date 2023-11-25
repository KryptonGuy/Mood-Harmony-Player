import numpy as np
import pandas as pd
import fer
import PIL
from sklearn.cluster import KMeans
import collections, random
from heapq import nlargest
from operator import itemgetter

model = fer.FER()

emo_cord = {
        "angry": (2.50, 5.93, 5.14),
        "happy": (8.21, 5.55, 7.00),
        "surprise": (7.21, 7.54, 7.25),
        "disgust": (1.69, 3.33, 4.46),
        "fear": (2.97, 5.16, 2.87),
        "sad": (2.40, 2.81, 3.84),
        "neutral": (4.12, 3.38, 4.43),
    }

def detect_emotion(image):
    imagePIL = PIL.Image.open(image)
    img = np.array(imagePIL)
    detected_emotions = model.detect_emotions(img)
    emotion_weights = detected_emotions[0]["emotions"]
    emotion_weights = [(emotion_weights[detected_emotions], detected_emotions) for detected_emotions in emotion_weights]
    emotion_weights.sort()
    return emotion_weights[-1][1]

def distance(
    x1: float,
    y1: float,
    z1: float,
    x2: float,
    y2: float,
    z2: float,
) -> float:
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

def get_centroids() -> tuple:
    coordinates = [(key, value) for key, value in emo_cord.items()]
    centroids = [list(item[1]) for item in coordinates]
    centroids = np.array(centroids)
    labels = [item[0] for item in coordinates]
    return (labels, centroids)


def pre_process_cluster() -> dict:
    data = pd.read_csv("data/musedata.csv")
    data = data[data["spotify_id"].notna()]
    labels, centroids = get_centroids()
    x = data.iloc[:,3:6].values
    k_means_optimum = KMeans(
        n_clusters=7,
        n_init=1,
        init=centroids,
        random_state=50,
        tol=1e-8,
    )
    y = k_means_optimum.fit_predict(x)
    data["cluster"] = y
    tracks = collections.defaultdict(list)
    for i, row in data.iterrows():
        spotify_id = row["spotify_id"]
        cluster = row["cluster"]
        tracks[labels[cluster]].append(spotify_id)

    return tracks

tracks = pre_process_cluster()


def get_tracks(emotion: str, k=150, size=1000) -> list:
    tracks_ls = random.sample(tracks[emotion][:size], k)
    return tracks_ls

def k_most_popular(songs,k):
    track_list = []

    for song in songs:
        track_list.append((song["id"], song["popularity"]))

    top_k = nlargest(k, track_list, key=itemgetter(1))
    
    return [v for v,i in top_k]
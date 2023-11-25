import numpy as np
import pandas as pd
import fer
import PIL

model = fer.FER()

def detect_emotion(image):
    imagePIL = PIL.Image.open(image)
    img = np.array(imagePIL)
    detected_emotions = model.detect_emotions(img)
    emotion_weights = detected_emotions[0]["emotions"]
    emotion_weights = [(emotion_weights[detected_emotions], detected_emotions) for detected_emotions in emotion_weights]
    emotion_weights.sort()
    return emotion_weights[-1][1]

FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip3 install -r requirements.txt

RUN echo -e ${SPOTIFY_SECRETS} >> .streamlit/secrets.toml

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "Player.py", "--server.port=8501"]
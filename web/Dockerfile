FROM python:3.7
WORKDIR /usr/src/app
RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6 -y
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT=5001
CMD gunicorn app:app --timeout 1000 --workers 1 --threads 4 --bind 0.0.0.0:$PORT --reload
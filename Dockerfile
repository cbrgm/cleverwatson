# Not working at the moment! ALSA audio drivers not found! Fixed in new release
FROM python:2.7

WORKDIR /workdir
COPY . /workdir

ENV TTS_USERNAME default-user
ENV TTS_PASSWORD default-password
ENV SELENIUM_URL null

VOLUME /dev/snd:/dev/snd

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y alsa-utils

CMD python main.py

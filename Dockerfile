From continuumio/anaconda3:latest
RUN apt-get update -y
COPY . /app/RandomApi
WORKDIR /app/RandomApi
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "-c","./start.sh"]
EXPOSE 8040

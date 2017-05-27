FROM ubuntu:xenial
MAINTAINER Edward Leoni

# Install dependencies
RUN apt update -y
RUN apt install python-setuptools python-dev build-essential -y
RUN apt install curl -y
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

# Install google cloud SDK
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-xenial main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt update -y
RUN apt install google-cloud-sdk -y
RUN apt install google-cloud-sdk-app-engine-python -y

# Include project files
RUN mkdir /app
WORKDIR /app
ADD . .

# Init google SDK
RUN gcloud auth activate-service-account --key-file matilda.json

# Install project dependencies
RUN pip install -r requirements.txt

# Prepares to run project
RUN echo "export FLASK_APP=/app/app.py; export GOOGLE_APPLICATION_CREDENTIALS=/app/matilda.json; flask run --host=0.0.0.0 --port=5000" > /run.sh

EXPOSE 5000

CMD ["sh", "/run.sh"]
